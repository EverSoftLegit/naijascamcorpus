import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"
SCHEMA = ROOT / "schemas" / "scam-pattern.schema.json"
TEMPLATE = ROOT / "templates" / "record.template.json"

try:
    from jsonschema import Draft202012Validator
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False


def load_records():
    return [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]


class DatasetFoundationTests(unittest.TestCase):
    def test_initial_records_are_nonempty_and_unique(self):
        records = load_records()
        self.assertGreaterEqual(len(records), 1)
        ids = [record["record_id"] for record in records]
        self.assertEqual(len(ids), len(set(ids)), "record_id values must be unique")

    def test_initial_release_is_synthetic_only(self):
        for record in load_records():
            self.assertEqual(record["record_type"], "synthetic_pattern")
            self.assertEqual(record["source"]["source_kind"], "synthetic")
            self.assertEqual(record["confidence"], "not_applicable_synthetic")
            self.assertEqual(record["privacy_review"], "passed")
            self.assertTrue(record["synthetic_example"].startswith("SYNTHETIC EXAMPLE:"))

    def test_schema_is_json_schema_2020_12(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])

    @unittest.skipUnless(HAVE_JSONSCHEMA, "jsonschema not installed")
    def test_every_record_validates_against_schema(self):
        validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
        for record in load_records():
            errors = [e.message for e in validator.iter_errors(record)]
            self.assertEqual(errors, [], f"{record.get('record_id')} failed schema: {errors}")

    @unittest.skipUnless(HAVE_JSONSCHEMA, "jsonschema not installed")
    def test_template_validates_against_schema(self):
        # The contributor template must never drift out of the schema.
        validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
        errors = [e.message for e in validator.iter_errors(json.loads(TEMPLATE.read_text(encoding="utf-8")))]
        self.assertEqual(errors, [], f"record.template.json failed schema: {errors}")

    def test_taxonomy_matches_schema(self):
        # The consistency checker exits 0 only when every taxonomy file matches the schema enums.
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_taxonomy_consistency.py")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
