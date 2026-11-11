#!/usr/bin/env python3
"""Report coverage of the dataset across the controlled dimensions.

Helps reviewers see where the synthetic set is thin before a release (the
roadmap targets balanced coverage of families, channels, and regions). Prints a
summary and can emit JSON. Informational: it never fails the build.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"

SINGLE = ["scam_family", "channel", "impersonated_sector"]
MULTI = ["countries", "languages", "persuasion_tactics", "requested_actions"]


def summarise(path: Path) -> dict:
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    report = {"records": len(records), "dimensions": {}}
    for field in SINGLE:
        report["dimensions"][field] = dict(Counter(r[field] for r in records).most_common())
    for field in MULTI:
        counter: Counter = Counter()
        for r in records:
            counter.update(r.get(field, []))
        report["dimensions"][field] = dict(counter.most_common())
    return report


def print_report(report: dict) -> None:
    print(f"Coverage over {report['records']} records\n")
    for field, counts in report["dimensions"].items():
        print(f"{field} ({len(counts)} distinct):")
        for value, n in counts.items():
            print(f"  {value:<24} {n}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = parser.parse_args()
    report = summarise(args.path.resolve())
    print(json.dumps(report, indent=2) if args.json else "", end="")
    if not args.json:
        print_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
