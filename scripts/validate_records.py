#!/usr/bin/env python3
"""Validate NaijaScamCorpus JSONL records against the public schema."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("Missing dependency: install requirements-dev.txt (pip install -r requirements-dev.txt)", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "scam-pattern.schema.json"
DEFAULT_RECORDS = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"


def validate(path: Path) -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    seen: set[str] = set()
    errors: list[str] = []
    count = 0

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            if not raw.strip():
                continue
            count += 1
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
                continue
            record_id = record.get("record_id") if isinstance(record, dict) else None
            if record_id:
                if record_id in seen:
                    errors.append(f"line {line_number}: duplicate record_id {record_id}")
                seen.add(record_id)
            for err in validator.iter_errors(record):
                location = ".".join(str(part) for part in err.absolute_path) or "<root>"
                errors.append(f"line {line_number} [{location}]: {err.message}")

    if not count:
        errors.append("dataset contains no records")
    if errors:
        print("Dataset validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Dataset validation PASSED: {count} records in {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_RECORDS, help="JSONL dataset file")
    args = parser.parse_args()
    return validate(args.path.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
