"""A deterministic, dependency-free baseline for scam-family classification.

This is a reproducibility harness, NOT a fraud detector. It measures how well a
simple model separates the twelve synthetic scam families using only the text in
each record. Because the dataset is tiny and synthetic, the scores describe this
dataset and nothing about real-world performance.

Everything here is pure Python and deterministic: the same records always produce
the same model and the same metrics, with no random seed involved.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, NamedTuple

# Small stoplist; kept tiny and transparent rather than importing a corpus.
_STOP = {
    "a", "an", "the", "to", "and", "or", "of", "is", "are", "be", "that", "this",
    "it", "as", "for", "on", "in", "with", "by", "any", "not", "no", "fictional",
    "synthetic", "example", "recipient", "target", "asks", "ask", "claims", "claim",
    "made", "up", "made-up", "message", "notice",
}
_TOKEN = re.compile(r"[a-z0-9]+")


class Record(NamedTuple):
    record_id: str
    text: str
    label: str


def load_records(path: str | Path) -> list[Record]:
    """Load records.jsonl into (id, text, label). Text drops the SYNTHETIC EXAMPLE: marker."""
    records = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        example = obj["synthetic_example"].replace("SYNTHETIC EXAMPLE:", " ")
        text = f"{obj['pattern_summary']} {example}"
        records.append(Record(obj["record_id"], text, obj["scam_family"]))
    return sorted(records, key=lambda r: r.record_id)  # deterministic order


def tokenize(text: str) -> list[str]:
    return [t for t in _TOKEN.findall(text.lower()) if t not in _STOP and len(t) > 2]


class NaiveBayes:
    """Multinomial Naive Bayes with Laplace smoothing. Deterministic."""

    def __init__(self, alpha: float = 1.0):
        self.alpha = alpha
        self.labels: list[str] = []
        self.log_prior: dict[str, float] = {}
        self.log_likelihood: dict[str, dict[str, float]] = {}
        self.vocab: set[str] = set()

    def fit(self, records: Iterable[Record]) -> "NaiveBayes":
        records = list(records)
        label_counts: Counter = Counter(r.label for r in records)
        self.labels = sorted(label_counts)
        token_counts: dict[str, Counter] = {label: Counter() for label in self.labels}
        for r in records:
            token_counts[r.label].update(tokenize(r.text))
        self.vocab = {tok for counts in token_counts.values() for tok in counts}
        v = len(self.vocab)
        total = len(records)
        for label in self.labels:
            self.log_prior[label] = math.log(label_counts[label] / total)
            denom = sum(token_counts[label].values()) + self.alpha * v
            self.log_likelihood[label] = {
                tok: math.log((token_counts[label][tok] + self.alpha) / denom) for tok in self.vocab
            }
            # log-prob for an unseen-in-class token, precomputed:
            self.log_likelihood[label]["<UNK>"] = math.log(self.alpha / denom)
        return self

    def predict(self, text: str) -> str:
        tokens = [t for t in tokenize(text) if t in self.vocab]
        best_label, best_score = self.labels[0], -math.inf
        for label in self.labels:  # sorted → deterministic tie-breaking
            ll = self.log_likelihood[label]
            score = self.log_prior[label] + sum(ll.get(tok, ll["<UNK>"]) for tok in tokens)
            if score > best_score:
                best_label, best_score = label, score
        return best_label


def majority_label(records: list[Record]) -> str:
    counts = Counter(r.label for r in records)
    return sorted(counts, key=lambda k: (-counts[k], k))[0]  # deterministic


def loocv_predictions(records: list[Record], alpha: float = 1.0) -> list[tuple[str, str]]:
    """Leave-one-out cross-validation. Returns (true, predicted) for every record."""
    out = []
    for i, held in enumerate(records):
        train = records[:i] + records[i + 1:]
        model = NaiveBayes(alpha).fit(train)
        out.append((held.label, model.predict(held.text)))
    return out


def confusion_matrix(pairs: list[tuple[str, str]]) -> dict:
    """Return {true_label: {pred_label: count}} over all labels seen, sorted."""
    labels = sorted({t for t, _ in pairs} | {p for _, p in pairs})
    matrix = {t: {p: 0 for p in labels} for t in labels}
    for true, pred in pairs:
        matrix[true][pred] += 1
    return matrix


def metrics(pairs: list[tuple[str, str]]) -> dict:
    """Accuracy, macro-F1, and per-class precision/recall/F1/support."""
    labels = sorted({t for t, _ in pairs} | {p for _, p in pairs})
    tp = defaultdict(int)
    fp = defaultdict(int)
    fn = defaultdict(int)
    support = Counter(t for t, _ in pairs)
    correct = 0
    for true, pred in pairs:
        if true == pred:
            correct += 1
            tp[true] += 1
        else:
            fp[pred] += 1
            fn[true] += 1

    per_class = {}
    f1s = []
    for label in labels:
        prec = tp[label] / (tp[label] + fp[label]) if (tp[label] + fp[label]) else 0.0
        rec = tp[label] / (tp[label] + fn[label]) if (tp[label] + fn[label]) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        per_class[label] = {"precision": round(prec, 4), "recall": round(rec, 4),
                            "f1": round(f1, 4), "support": support[label]}
        if support[label]:  # average F1 over classes actually present in the truth
            f1s.append(f1)
    return {
        "accuracy": round(correct / len(pairs), 4),
        "macro_f1": round(sum(f1s) / len(f1s), 4) if f1s else 0.0,
        "n": len(pairs),
        "per_class": per_class,
    }
