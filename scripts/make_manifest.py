#!/usr/bin/env python3
"""Generate or verify a SHA-256 manifest for release artifacts.

The release checklist requires checksums for every dataset release so a
published artifact is tamper-evident and a consumer can confirm they have the
exact bytes. This writes an `sha256sum`-compatible manifest and can verify it.

  python scripts/make_manifest.py            # write the manifest
  python scripts/make_manifest.py --check    # verify files match the manifest (exit 1 on mismatch)
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "v0.1" / "MANIFEST.sha256"

# Files whose bytes are covered by the release manifest, as repo-relative paths.
ARTIFACTS = [
    "data/v0.1/synthetic/records.jsonl",
    "data/v0.1/DATASET_CARD.md",
    "schemas/scam-pattern.schema.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def generate() -> int:
    lines = [f"{sha256(ROOT / rel)}  {rel}" for rel in ARTIFACTS]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST.relative_to(ROOT)} covering {len(ARTIFACTS)} artifact(s).")
    return 0


def verify() -> int:
    if not MANIFEST.is_file():
        print(f"Manifest missing: {MANIFEST.relative_to(ROOT)} (run without --check to create it)")
        return 1
    expected = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            expected[rel] = digest
    problems = []
    for rel in ARTIFACTS:
        if rel not in expected:
            problems.append(f"{rel}: not listed in manifest")
        elif sha256(ROOT / rel) != expected[rel]:
            problems.append(f"{rel}: checksum mismatch (file changed since the manifest was written)")
    for rel in expected:
        if rel not in ARTIFACTS:
            problems.append(f"{rel}: in manifest but no longer a tracked artifact")
    if problems:
        print("Manifest verification FAILED:")
        for p in problems:
            print(f"- {p}")
        return 1
    print(f"Manifest verification PASSED: {len(ARTIFACTS)} artifact(s) match.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify instead of writing")
    args = parser.parse_args()
    return verify() if args.check else generate()


if __name__ == "__main__":
    raise SystemExit(main())
