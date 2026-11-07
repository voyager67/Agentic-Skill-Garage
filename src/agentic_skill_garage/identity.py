"""Identity profile templates and reproducible prompt packets."""
from __future__ import annotations
import json
from pathlib import Path
from .security import write_text_no_overwrite

TEMPLATE={"schema_version":1,"name":"replace-me","kind":"character","canonical_description":"","invariants":[],"avoid":[],"reference_assets":[]}

def create_profile(path: Path, name: str, kind: str="character"):
    if kind not in {"character","brand","product","environment","prop"}:
        raise ValueError("kind must be character, brand, product, environment, or prop")
    data=dict(TEMPLATE); data["name"]=name; data["kind"]=kind
    return write_text_no_overwrite(Path(path), json.dumps(data,indent=2,ensure_ascii=False)+"\n")

def build_prompt(profile_path: Path, manifest_path: Path|None=None) -> str:
    data=json.loads(Path(profile_path).read_text(encoding="utf-8"))
    for key in ("name","kind","canonical_description","invariants","avoid","reference_assets"):
        if key not in data: raise ValueError(f"Identity profile is missing {key!r}")
    if data["kind"] not in {"character","brand","product","environment","prop"}: raise ValueError("Unsupported identity kind")
    assets={}
    if manifest_path and Path(manifest_path).exists():
        for line in Path(manifest_path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                item=json.loads(line); assets[item.get("asset_id")]=item
    lines=[f"# Identity: {data['name']}",f"Type: {data['kind']}","", "## Canonical description",data["canonical_description"] or "Not supplied.","", "## Invariants"]
    lines += [f"- {x}" for x in data["invariants"]] or ["- No invariants supplied; request approval before inventing them."]
    lines += ["", "## Avoid"]
    lines += [f"- {x}" for x in data["avoid"]] or ["- No exclusions supplied."]
    lines += ["", "## References"]
    for ref in data["reference_assets"]:
        if isinstance(ref,str): ref={"asset_id":ref,"role":"unspecified"}
        asset=assets.get(ref.get("asset_id"),{})
        lines.append(f"- asset_id={ref.get('asset_id','unknown')}; role={ref.get('role','unspecified')}; file={asset.get('path','not in manifest')}; sha256={asset.get('sha256','unknown')}")
    lines += ["", "## Generation instruction", "Preserve every invariant. Use each reference only for its assigned role. If references conflict, stop and ask which source is authoritative. Do not silently alter logos, product geometry, facial identity, wardrobe, or other approved identifiers."]
    return "\n".join(lines)+"\n"
