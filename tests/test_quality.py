import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_duplicates
import coverage_report
import lint_language_tags
import make_manifest

DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"


class DuplicateCheckTests(unittest.TestCase):
    def test_current_dataset_has_no_duplicates(self):
        self.assertEqual(check_duplicates.check(DATA, warn_at=0.70, fail_at=0.85), 0)

    def test_injected_exact_duplicate_fails(self, ):
        record = json.loads(DATA.read_text(encoding="utf-8").splitlines()[0])
        tmp = ROOT / "tests" / "_tmp_dupes.jsonl"
        try:
            tmp.write_text(json.dumps(record) + "\n" + json.dumps(record) + "\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):  # the check prints its findings; keep test logs clean
                rc = check_duplicates.check(tmp, 0.70, 0.85)
            self.assertEqual(rc, 1)
        finally:
            tmp.unlink(missing_ok=True)

    def test_jaccard_bounds(self):
        self.assertEqual(check_duplicates.jaccard({"a", "b"}, {"a", "b"}), 1.0)
        self.assertEqual(check_duplicates.jaccard({"a"}, {"b"}), 0.0)


class ManifestTests(unittest.TestCase):
    def test_committed_manifest_verifies(self):
        # The manifest in the repo must match the committed artifacts.
        self.assertEqual(make_manifest.verify(), 0)

    def test_sha256_matches_hashlib(self):
        import hashlib
        path = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"
        self.assertEqual(make_manifest.sha256(path), hashlib.sha256(path.read_bytes()).hexdigest())


class LanguageTagTests(unittest.TestCase):
    def test_current_tags_are_wellformed(self):
        self.assertEqual(lint_language_tags.malformed_tags(DATA), {})

    def test_detects_malformed_tag(self):
        tmp = ROOT / "tests" / "_tmp_lang.jsonl"
        try:
            tmp.write_text('{"record_id":"X","languages":["english","en-NG"]}\n', encoding="utf-8")
            bad = lint_language_tags.malformed_tags(tmp)
            self.assertIn("english", bad)
            self.assertNotIn("en-NG", bad)
        finally:
            tmp.unlink(missing_ok=True)


class CoverageTests(unittest.TestCase):
    def test_summary_totals(self):
        n_records = len([l for l in DATA.read_text(encoding="utf-8").splitlines() if l.strip()])
        report = coverage_report.summarise(DATA)
        self.assertEqual(report["records"], n_records)
        self.assertEqual(len(report["dimensions"]["scam_family"]), 12, "all 12 families should be represented")
        # Each record has exactly one scam_family, so the family counts sum to the record total.
        self.assertEqual(sum(report["dimensions"]["scam_family"].values()), n_records)


if __name__ == "__main__":
    unittest.main()
