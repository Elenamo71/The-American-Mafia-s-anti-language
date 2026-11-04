"""Open re-implementation of the keyness analysis (§ 9.4; Sketch Engine in the thesis).

Computes, for every word in the study corpus against a reference frequency list:
    log-likelihood G² (Dunning, 1993; Rayson & Garside, 2000 formulation),
    Log Ratio effect size (Hardie, 2014), and %DIFF (Gabrielatos & Marchi, 2012).

The reference list is NOT distributed here (licence). To reproduce the thesis:
  1. Download OANC (spoken portion) from https://anc.org/data/oanc/
  2. Build a frequency list with the same tokeniser:
         python code/keyness.py --build-reference /path/to/oanc/spoken \
             --out data/reference/oanc_spoken_freq.csv
  3. Run:
         python code/keyness.py --reference data/reference/oanc_spoken_freq.csv

Note: Sketch Engine's *default* keyword score is "simple maths" (Kilgarriff, 2009),
not log-likelihood. Record which score and which OANC version the thesis used,
and the minimum-frequency threshold, in docs/REPRODUCTION.md; results will
differ from Sketch Engine output if tokenisation or lemmatisation differ.

Output: data/results/keyness_vs_reference.csv
"""
from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from pathlib import Path

from _corpus import RESULTS, load_corpus, tokens


def g2(a: int, b: int, c: int, d: int) -> float:
    """a = freq in study, b = freq in reference, c = study size, d = reference size."""
    e1 = c * (a + b) / (c + d)
    e2 = d * (a + b) / (c + d)
    s = 0.0
    if a:
        s += a * math.log(a / e1)
    if b:
        s += b * math.log(b / e2)
    return 2 * s


def log_ratio(a, b, c, d, floor=0.5):
    return math.log2(((a or floor) / c) / ((b or floor) / d))


def build_reference(folder: Path, out: Path) -> None:
    cnt = Counter()
    for p in folder.rglob("*.txt"):
        cnt.update(tokens(p.read_text(encoding="utf-8", errors="ignore")))
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["token", "freq"])
        w.writerows(cnt.most_common())
    print(f"reference: {sum(cnt.values()):,} tokens, {len(cnt):,} types -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reference", type=Path)
    ap.add_argument("--build-reference", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--min-freq", type=int, default=3)
    a = ap.parse_args()
    if a.build_reference:
        build_reference(a.build_reference, a.out or Path("data/reference/oanc_spoken_freq.csv"))
        return
    if not a.reference:
        ap.error("--reference is required (see module docstring)")

    study = Counter()
    for t in load_corpus().values():
        study.update(tokens(t))
    ref = {r["token"]: int(r["freq"]) for r in csv.DictReader(a.reference.open(encoding="utf-8"))}
    c, d = sum(study.values()), sum(ref.values())
    rows = []
    for w, f in study.items():
        if f < a.min_freq:
            continue
        b = ref.get(w, 0)
        rows.append([w, f, b, round(g2(f, b, c, d), 2), round(log_ratio(f, b, c, d), 3),
                     round(((f / c) - (b / d)) / (b / d) * 100, 1) if b else ""])
    rows.sort(key=lambda r: -r[3])
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / "keyness_vs_reference.csv").open("w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh, lineterminator="\n")
        wr.writerow(["token", "freq_study", "freq_reference", "G2", "log_ratio", "pct_diff"])
        wr.writerows(rows)
    for r in rows[:20]:
        print(f"{r[0]:15} {r[1]:5} {r[2]:9} G2={r[3]:9.1f} LR={r[4]:6.2f}")


if __name__ == "__main__":
    main()
