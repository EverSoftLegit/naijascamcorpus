# Benchmark: scam-family classification baseline

A **reproducibility harness**, not a fraud detector and not a performance claim.
It measures how well a simple text model separates the twelve synthetic scam
families in `data/v0.1/synthetic/records.jsonl`, so that future tooling has a
deterministic reference point to beat.

## What it does

- **Task:** given a record's `pattern_summary` + `synthetic_example` text, predict its `scam_family` (12 classes).
- **Models:** a majority-class reference, and a multinomial Naive Bayes baseline.
- **Protocol:** leave-one-out cross-validation (train on all records but one, predict the held-out record, repeat).
- **Metrics:** accuracy, macro-F1, per-class precision / recall / F1 / support, and a confusion matrix (which families get mistaken for which).

## Run it

```bash
python benchmark/run_benchmark.py
```

Writes `benchmark/results/baseline-metrics.json` and prints a table. No arguments
needed; `--data` and `--output` override the defaults.

## Reproducibility

Pure Python standard library, no dependencies, and **no randomness** — no seed is
involved. The same records always produce the same model and the same numbers,
on any machine, so a change in the score means a real change in the data or the
code, never run-to-run noise.

## How to read the results (important)

- The dataset is **27 synthetic records**. Scores describe *this dataset*; they say
  nothing about detecting real scams, and must never be cited as real-world accuracy.
- With 12 classes, a majority-class guess scores about 0.11 accuracy. The baseline
  clearing that bar only shows the text carries class signal in this small set.
- Per-class F1 of 0.0 for a family usually means too few examples of it for a
  bag-of-words model under leave-one-out, not that the family is undetectable.

## Intended use

- A reference other contributors can try to beat with better features or models.
- A regression signal: if a data or schema change unexpectedly moves the baseline, that is worth a look.
- A teaching example of a clean, dependency-free, fully reproducible evaluation.

It is explicitly **out of scope** to use these numbers to claim a model can detect
real-world fraud, or to deploy anything trained on this data for operational decisions.
