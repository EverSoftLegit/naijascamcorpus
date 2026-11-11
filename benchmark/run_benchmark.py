#!/usr/bin/env python3
"""Run the scam-family classification baseline and write reproducible metrics.

Usage: python benchmark/run_benchmark.py [--data PATH] [--output PATH]

Reports a majority-class reference and a Naive Bayes baseline under leave-one-out
cross-validation. Deterministic: re-running on the same data yields identical
numbers. This measures the synthetic dataset only and is not a real-world claim.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baseline import NaiveBayes, confusion_matrix, load_records, loocv_predictions, majority_label, metrics

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "v0.1" / "synthetic" / "records.jsonl"
DEFAULT_OUT = ROOT / "benchmark" / "results" / "baseline-metrics.json"


def evaluate(data_path: Path) -> dict:
    records = load_records(data_path)
    # Majority-class reference (what accuracy you get by always guessing the top class).
    top = majority_label(records)
    majority_pairs = [(r.label, top) for r in records]
    nb_pairs = loocv_predictions(records)
    nb = metrics(nb_pairs)
    nb["confusion"] = confusion_matrix(nb_pairs)
    maj = metrics(majority_pairs)
    return {
        "dataset": str(data_path.relative_to(ROOT) if data_path.is_relative_to(ROOT) else data_path),
        "records": len(records),
        "classes": len({r.label for r in records}),
        "protocol": "leave-one-out cross-validation",
        "deterministic": True,
        "models": {
            "majority_class": {"accuracy": maj["accuracy"], "macro_f1": maj["macro_f1"], "predicts": top},
            "naive_bayes": nb,
        },
        "caveat": "Synthetic data only. Scores characterise this dataset and do not indicate real-world detection accuracy.",
    }


def print_report(result: dict) -> None:
    nb = result["models"]["naive_bayes"]
    maj = result["models"]["majority_class"]
    print(f"Dataset: {result['dataset']}  ({result['records']} records, {result['classes']} classes)")
    print(f"Protocol: {result['protocol']}\n")
    print(f"{'model':<16}{'accuracy':>10}{'macro_f1':>10}")
    print(f"{'majority_class':<16}{maj['accuracy']:>10.4f}{maj['macro_f1']:>10.4f}")
    print(f"{'naive_bayes':<16}{nb['accuracy']:>10.4f}{nb['macro_f1']:>10.4f}\n")
    print(f"{'scam_family':<22}{'prec':>8}{'rec':>8}{'f1':>8}{'n':>5}")
    for label, m in sorted(nb["per_class"].items()):
        print(f"{label:<22}{m['precision']:>8.3f}{m['recall']:>8.3f}{m['f1']:>8.3f}{m['support']:>5}")

    matrix = nb.get("confusion")
    if matrix:
        labels = sorted(matrix)
        abbr = {label: f"{i:02d}" for i, label in enumerate(labels)}
        print("\nConfusion matrix (rows = true, columns = predicted):")
        print(" " * 24 + " ".join(abbr[c] for c in labels))
        for true in labels:
            cells = " ".join(f"{matrix[true][p] or '.':>2}" for p in labels)
            print(f"{true:<22}{abbr[true]}  {cells}")
        print("legend: " + ", ".join(f"{abbr[l]}={l}" for l in labels))
    print(f"\n{result['caveat']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    result = evaluate(args.data.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print_report(result)
    print(f"\nWrote {args.output.relative_to(ROOT) if args.output.is_relative_to(ROOT) else args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
