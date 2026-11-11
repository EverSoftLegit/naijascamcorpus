#!/usr/bin/env python3
"""Fail if the taxonomy/*.json controlled vocabularies drift from the schema enums.

The schema is the single source of truth for every controlled field. The
taxonomy files add human-readable labels and definitions for reviewers, but
their id sets must match the schema exactly. This guard makes a mismatch a CI
failure instead of a silent inconsistency.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# field in schema -> (taxonomy file, key holding the list, how to read an id)
CHECKS = {
    "channel": ("channels.json", "channels", lambda x: x),
    "scam_family": ("scam-families.json", "families", lambda x: x["id"]),
    "persuasion_tactics": ("tactics.json", "tactics", lambda x: x),
    "impersonated_sector": ("sectors.json", "sectors", lambda x: x["id"]),
    "requested_actions": ("requested-actions.json", "requested_actions", lambda x: x["id"]),
}


def schema_enum(props: dict, field: str) -> set[str]:
    node = props[field]
    if node.get("type") == "array":
        node = node["items"]
    return set(node["enum"])


def main() -> int:
    props = json.loads((ROOT / "schemas" / "scam-pattern.schema.json").read_text(encoding="utf-8"))["properties"]
    problems: list[str] = []
    for field, (filename, key, read_id) in CHECKS.items():
        path = ROOT / "taxonomy" / filename
        if not path.is_file():
            problems.append(f"{field}: missing taxonomy file {filename}")
            continue
        tax_ids = {read_id(item) for item in json.loads(path.read_text(encoding="utf-8"))[key]}
        enum_ids = schema_enum(props, field)
        if tax_ids != enum_ids:
            missing = enum_ids - tax_ids
            extra = tax_ids - enum_ids
            detail = []
            if missing:
                detail.append(f"in schema but not {filename}: {sorted(missing)}")
            if extra:
                detail.append(f"in {filename} but not schema: {sorted(extra)}")
            problems.append(f"{field}: " + "; ".join(detail))

    if problems:
        print("Taxonomy/schema consistency FAILED:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print(f"Taxonomy/schema consistency PASSED: {len(CHECKS)} controlled fields match the schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
