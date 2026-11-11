#!/usr/bin/env python3
"""Run every non-interactive check in order. One command for contributors and CI.

Runs: taxonomy/schema consistency, schema validation of the dataset, the
duplicate/leakage check, and manifest verification. Exits non-zero if any fail.
Unit tests and the benchmark are run separately (see the README).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# (step name, argv, fails_build). The language lint is advisory: it surfaces
# warnings but does not fail the build unless run with --strict directly.
STEPS = [
    ("taxonomy/schema consistency", ["check_taxonomy_consistency.py"], True),
    ("schema validation", ["validate_records.py"], True),
    ("duplicate / leakage check", ["check_duplicates.py"], True),
    ("manifest verification", ["make_manifest.py", "--check"], True),
    ("language-tag lint (advisory)", ["lint_language_tags.py"], False),
]


def main() -> int:
    failed = []
    for name, argv, fails_build in STEPS:
        print(f"\n=== {name} ===")
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / argv[0]), *argv[1:]])
        if result.returncode != 0 and fails_build:
            failed.append(name)
    print("\n" + ("All checks passed." if not failed else f"FAILED: {', '.join(failed)}"))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
