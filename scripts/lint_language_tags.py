#!/usr/bin/env python3
"""Lint language tags for a BCP-47-like shape. Advisory by default.

The project keeps language tags flexible and transparent (see
taxonomy/languages.md) rather than enforcing a closed list, so this only warns
about tags that do not look well-formed (likely typos) unless --strict is given.

Accepted shape (a pragmatic subset of BCP-47):
  language (2-3 lowercase letters), optional script (Title-case, 4 letters),
  optional region (2 uppercase letters or 3 digits). Examples: en, en-NG,
  pcm-NG, sw-KE, zh-Hant-HK.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"
BCP47_LIKE = re.compile(r"^[a-z]{2,3}(-[A-Z][a-z]{3})?(-([A-Z]{2}|[0-9]{3}))?$")


def malformed_tags(path: Path) -> dict[str, list[str]]:
    """Return {tag: [record_ids]} for tags that do not match the expected shape."""
    bad: dict[str, list[str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        for tag in record.get("languages", []):
            if not BCP47_LIKE.match(tag):
                bad.setdefault(tag, []).append(record.get("record_id", "?"))
    return bad


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--strict", action="store_true", help="exit 1 if any tag is malformed")
    args = parser.parse_args()
    bad = malformed_tags(args.path.resolve())
    if not bad:
        print("Language-tag lint: all tags look well-formed.")
        return 0
    print("Language-tag lint found tags that do not match the expected shape:")
    for tag, ids in sorted(bad.items()):
        print(f"- {tag!r} in {', '.join(ids)}")
    print("\nThese are warnings; confirm with a language reviewer. Use --strict to fail on them.")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
