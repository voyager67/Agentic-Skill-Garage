"""Identity profile templates and validated, reproducible prompt packets."""
from __future__ import annotations
import json
import re
from pathlib import Path, PurePosixPath
from .security import write_text_no_overwrite, require_regular_file

TEMPLATE={"schema_version":1,"name":"replace-me","kind":"character","canonical_description":"","invariants":[],"avoid":[],"reference_assets":[]}
KINDS={"character","brand","product","environment","prop"}
ASSET_ID=re.compile(r"^[A-Za-z0-9_-]{1,64}$")
SHA256=re.compile(r"^[0-9a-f]{64}$")


def _safe_manifest_path(value):
    if not isinstance(value,str) or not value:
        return False
    rel=PurePosixPath(value)
    return (
        not rel.is_absolute()
        and bool(rel.parts)
        and not any(part in {".",".."} for part in rel.parts)
        and "\\" not in value
        and ":" not in value
    )


def _string_list(value, field):
    if not isinstance(value,list) or any(not isinstance(item,str) for item in value):
        raise ValueError(f"Identity profile field {field!r} must be an array of strings")
    return value


def create_profile(path: Path, name: str, kind: str="character"):
    if kind not in KINDS:
        raise ValueError("kind must be character, brand, product, environment, or prop")
    if not isinstance(name,str) or not name.strip() or len(name.strip())>128:
        raise ValueError("name must contain 1 to 128 non-whitespace characters")
    data=dict(TEMPLATE); data["name"]=name.strip(); data["kind"]=kind
    return write_text_no_overwrite(Path(path), json.dumps(data,indent=2,ensure_ascii=False)+"\n")


def build_prompt(profile_path: Path, manifest_path: Path|None=None) -> str:
    profile=require_regular_file(Path(profile_path))
    try:
        data=json.loads(profile.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Identity profile is not valid JSON: {exc}") from exc
    if not isinstance(data,dict):
        raise ValueError("Identity profile must be a JSON object")
    if data.get("schema_version",1)!=1:
        raise ValueError("Unsupported identity profile schema_version")
    required=("name","kind","canonical_description","invariants","avoid","reference_assets")
    for key in required:
        if key not in data:
            raise ValueError(f"Identity profile is missing {key!r}")
    if not isinstance(data["name"],str) or not data["name"].strip():
        raise ValueError("Identity profile name must be a non-empty string")
    if data["kind"] not in KINDS:
        raise ValueError("Unsupported identity kind")
    if not isinstance(data["canonical_description"],str):
        raise ValueError("canonical_description must be a string")
    invariants=_string_list(data["invariants"],"invariants")
    avoid=_string_list(data["avoid"],"avoid")
    references=data["reference_assets"]
    if not isinstance(references,list):
        raise ValueError("reference_assets must be an array")

    assets={}
    if manifest_path:
        manifest=Path(manifest_path).expanduser()
        if manifest.exists() or manifest.is_symlink():
            manifest=require_regular_file(manifest)
            for number,line in enumerate(manifest.read_text(encoding="utf-8").splitlines(),1):
                if not line.strip():
                    continue
                try:
                    item=json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid manifest line {number}: {exc}") from exc
                if not isinstance(item,dict):
                    raise ValueError(f"Invalid manifest line {number}: expected a JSON object")
                asset_id=item.get("asset_id")
                if not isinstance(asset_id,str) or not ASSET_ID.fullmatch(asset_id):
                    raise ValueError(f"Invalid manifest line {number}: invalid asset_id")
                if not _safe_manifest_path(item.get("path")):
                    raise ValueError(f"Invalid manifest line {number}: unsafe relative asset path")
                if not isinstance(item.get("sha256"),str) or not SHA256.fullmatch(item["sha256"]):
                    raise ValueError(f"Invalid manifest line {number}: invalid SHA-256 digest")
                assets[asset_id]=item

    lines=[
        f"# Identity: {data['name']}",
        f"Type: {data['kind']}",
        "",
        "## Canonical description",
        data["canonical_description"] or "Not supplied.",
        "",
        "## Invariants",
    ]
    lines += [f"- {item}" for item in invariants] or ["- No invariants supplied; request approval before inventing them."]
    lines += ["", "## Avoid"]
    lines += [f"- {item}" for item in avoid] or ["- No exclusions supplied."]
    lines += ["", "## References"]
    for number,ref in enumerate(references,1):
        if isinstance(ref,str):
            ref={"asset_id":ref,"role":"unspecified"}
        if not isinstance(ref,dict):
            raise ValueError(f"reference_assets[{number-1}] must be a string or object")
        asset_id=ref.get("asset_id")
        role=ref.get("role","unspecified")
        if not isinstance(asset_id,str) or not ASSET_ID.fullmatch(asset_id):
            raise ValueError(f"reference_assets[{number-1}] has an invalid asset_id")
        if not isinstance(role,str) or not role.strip():
            raise ValueError(f"reference_assets[{number-1}] role must be a non-empty string")
        asset=assets.get(asset_id,{})
        lines.append(
            f"- asset_id={asset_id}; role={role}; "
            f"file={asset.get('path','not in manifest')}; sha256={asset.get('sha256','unknown')}"
        )
    lines += [
        "",
        "## Generation instruction",
        "Preserve every invariant. Use each reference only for its assigned role. If references conflict, stop and ask which source is authoritative. Do not silently alter logos, product geometry, facial identity, wardrobe, or other approved identifiers.",
    ]
    return "\n".join(lines)+"\n"
