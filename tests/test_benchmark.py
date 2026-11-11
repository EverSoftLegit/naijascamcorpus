import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "benchmark"))

from baseline import (NaiveBayes, Record, confusion_matrix, load_records, loocv_predictions,
                      majority_label, metrics, tokenize)
import run_benchmark

DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"


class BaselineTests(unittest.TestCase):
    def test_tokenize_lowercases_drops_marker_and_stopwords(self):
        toks = tokenize("SYNTHETIC EXAMPLE: A fictional URGENT message")
        self.assertIn("urgent", toks)
        self.assertNotIn("the", toks)
        self.assertNotIn("a", toks)

    def test_naive_bayes_is_deterministic(self):
        records = load_records(DATA)
        m1 = NaiveBayes().fit(records)
        m2 = NaiveBayes().fit(records)
        preds1 = [m1.predict(r.text) for r in records]
        preds2 = [m2.predict(r.text) for r in records]
        self.assertEqual(preds1, preds2)

    def test_model_learns_training_signal(self):
        # Trained and tested on the same tiny set, it should fit most of it.
        records = load_records(DATA)
        model = NaiveBayes().fit(records)
        correct = sum(model.predict(r.text) == r.label for r in records)
        self.assertGreater(correct / len(records), 0.6)

    def test_loocv_beats_majority_baseline(self):
        records = load_records(DATA)
        nb = metrics(loocv_predictions(records))
        top = majority_label(records)
        maj = metrics([(r.label, top) for r in records])
        self.assertGreater(nb["accuracy"], maj["accuracy"])

    def test_metrics_shapes_and_ranges(self):
        pairs = [("a", "a"), ("a", "b"), ("b", "b")]
        m = metrics(pairs)
        self.assertAlmostEqual(m["accuracy"], 2 / 3, places=4)
        self.assertEqual(m["per_class"]["a"]["support"], 2)
        self.assertTrue(0.0 <= m["macro_f1"] <= 1.0)

    def test_confusion_matrix_rows_sum_to_support(self):
        records = load_records(DATA)
        pairs = loocv_predictions(records)
        matrix = confusion_matrix(pairs)
        m = metrics(pairs)
        for label, row in matrix.items():
            self.assertEqual(sum(row.values()), m["per_class"][label]["support"])

    def test_evaluate_output_is_reproducible(self):
        a = run_benchmark.evaluate(DATA)
        b = run_benchmark.evaluate(DATA)
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))
        self.assertEqual(a["records"], len(load_records(DATA)))
        self.assertEqual(a["models"]["naive_bayes"]["n"], a["records"])


if __name__ == "__main__":
    unittest.main()
