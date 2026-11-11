#!/usr/bin/env python3
"""Flag duplicate or near-duplicate records (a data-quality and benchmark-leakage guard).

Near-identical records inflate a benchmark (the same text can land in both train
and test) and waste reviewer effort. This checks for:
  - exact duplicate record_id values;
  - exact duplicate synthetic_example text;
  - near-duplicate records by Jaccard token overlap above a threshold.

Deterministic and dependency-free. Exits 1 if any exact duplicate exists or any
pair is at/above --fail-at (default 0.85); pairs at/above --warn-at are listed
but do not fail. Tune thresholds as the dataset grows.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"
_TOKEN = re.compile(r"[a-z0-9]+")


def tokens(record: dict) -> set[str]:
    text = f"{record.get('pattern_summary', '')} {record.get('synthetic_example', '')}"
    text = text.replace("SYNTHETIC EXAMPLE:", " ").lower()
    return set(_TOKEN.findall(text))


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def check(path: Path, warn_at: float, fail_at: float) -> int:
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    failures: list[str] = []
    warnings: list[str] = []

    ids = [r.get("record_id") for r in records]
    for rid in {i for i in ids if ids.count(i) > 1}:
        failures.append(f"duplicate record_id: {rid}")

    seen_text: dict[str, str] = {}
    for r in records:
        example = r.get("synthetic_example", "")
        if example in seen_text:
            failures.append(f"identical synthetic_example in {seen_text[example]} and {r.get('record_id')}")
        else:
            seen_text[example] = r.get("record_id", "?")

    token_sets = {r["record_id"]: tokens(r) for r in records}
    for a, b in combinations(records, 2):
        sim = jaccard(token_sets[a["record_id"]], token_sets[b["record_id"]])
        line = f"{a['record_id']} ~ {b['record_id']}: Jaccard {sim:.2f}"
        if sim >= fail_at:
            failures.append("near-duplicate " + line)
        elif sim >= warn_at:
            warnings.append(line)

    if warnings:
        print(f"Near-duplicate warnings (>= {warn_at}):")
        for w in sorted(warnings, key=lambda s: s.split("Jaccard ")[-1], reverse=True):
            print(f"- {w}")
    if failures:
        print(f"\nDuplicate check FAILED ({len(failures)} issue(s)):")
        for f in failures:
            print(f"- {f}")
        return 1
    print(f"Duplicate check PASSED: {len(records)} records, no exact duplicates, "
          f"none at/above Jaccard {fail_at}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--warn-at", type=float, default=0.70)
    parser.add_argument("--fail-at", type=float, default=0.85)
    args = parser.parse_args()
    return check(args.path.resolve(), args.warn_at, args.fail_at)


if __name__ == "__main__":
    raise SystemExit(main())
