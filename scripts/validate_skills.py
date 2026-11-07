#!/usr/bin/env python3
"""Validate Agentic Skill Garage's standalone Agent Skills catalogue."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_LICENSES = {"Apache-2.0", "MIT"}
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str):
    match = FRONTMATTER.match(text)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        if key in fields:
            return None
        fields[key] = value.strip().strip('"\'')
    return fields


def main() -> int:
    skill_root = ROOT / "skills"
    if skill_root.is_symlink() or not skill_root.is_dir():
        print(f"ERROR: skills directory missing or symlinked: {skill_root}", file=sys.stderr)
        return 2
    errors = []
    actual = set()
    license_counts = {}
    directories = sorted(p for p in skill_root.iterdir() if p.is_dir() or p.is_symlink())
    for folder in directories:
        if folder.is_symlink() or not folder.is_dir():
            errors.append(f"{folder}: skill directories must not be symlinks")
            continue
        manifest = folder / "SKILL.md"
        if not NAME.fullmatch(folder.name):
            errors.append(f"{manifest}: invalid skill directory name")
            continue
        if not manifest.is_file() or manifest.is_symlink():
            errors.append(f"{manifest}: SKILL.md missing or symlinked")
            continue
        text = manifest.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)
        if fields is None:
            errors.append(f"{manifest}: invalid or duplicate frontmatter")
            continue
        if fields.get("name") != folder.name:
            errors.append(f"{manifest}: name does not match directory")
        description = fields.get("description", "")
        if not description:
            errors.append(f"{manifest}: description is required")
        elif len(description) > 1024:
            errors.append(f"{manifest}: description exceeds 1024 characters")
        license_name = fields.get("license")
        if license_name not in ALLOWED_LICENSES:
            errors.append(f"{manifest}: license must be one of {sorted(ALLOWED_LICENSES)}")
        else:
            license_counts[license_name] = license_counts.get(license_name, 0) + 1
        body = FRONTMATTER.sub("", text, count=1)
        if len(body.splitlines()) < 18:
            errors.append(f"{manifest}: skill instructions are too short")
        if len(body.split()) < 100:
            errors.append(f"{manifest}: skill needs more actionable detail")
        actual.add(folder.name)

    try:
        index = json.loads((ROOT / "skills-index.json").read_text(encoding="utf-8"))
        records = index["skills"]
        indexed = [item["name"] for item in records]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(f"skills-index.json: cannot parse catalogue ({exc})")
        records, indexed, index = [], [], {}

    if len(indexed) != len(set(indexed)):
        errors.append("skills-index.json contains duplicate names")
    if index.get("name") != "Agentic Skill Garage":
        errors.append("skills-index.json project name is incorrect")
    if index.get("skill_count") != len(indexed):
        errors.append("skills-index.json count does not match its records")
    if set(indexed) != actual:
        errors.append(f"catalogue mismatch: missing={sorted(actual-set(indexed))}; extra={sorted(set(indexed)-actual)}")

    if errors:
        print(f"Validation failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    declared = ", ".join(f"{name}: {count}" for name, count in sorted(license_counts.items()))
    print(f"Validated {len(actual)} Agent Skills ({declared}) and {len(indexed)} catalogue entries.")
    print("Checks cover directory safety, names, frontmatter, descriptions, declared license identifiers, body depth, and index consistency.")
    print("License metadata validation does not establish copyright ownership or resolve upstream provenance; see NOTICE.md.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
