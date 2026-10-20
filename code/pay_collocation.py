"""Collocates of the node PAY (Figure 9.4; replaces the code printed in Appendix K).

Appendix K plotted hand-entered counts and, as printed, does not run (Word
converted the quotation marks). This script does two things:

1. `--thesis`  redraws Figure 9.4 from the counts published in the thesis
               (don't 7, fucking 6, gonna 5; bank/invoice/contract 0).
2. default     recomputes collocates of pay/pays/paid/paying within a ±W token
               window directly from corpus/raw/, so the published counts can be
               checked. Window size and node forms are arguments because the
               thesis does not state them.

Reproducibility note: no window/node combination reproduces 7/6/5 exactly
(Appendix K says the counts were "aided by manual count"). The business-term
zeros reproduce under every setting. To close the gap, deposit the PAY
concordance lines that were counted (annotation/concordances/pay_concordance.csv).

Outputs: data/results/pay_collocates.csv, data/results/figure_9_4_pay_collocates.png
Run:     python code/pay_collocation.py [--window 5] [--thesis]
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from _corpus import RESULTS, load_corpus, tokens  # noqa: E402

NODE = {"pay", "pays", "paid", "paying"}
HOSTILE = ["don't", "fucking", "gonna"]
BUSINESS = ["bank", "invoice", "contract"]
THESIS_COUNTS = {"don't": 7, "fucking": 6, "gonna": 5, "bank": 0, "invoice": 0, "contract": 0}


def collocates(window: int, nodes: set[str] = NODE) -> Counter:
    c = Counter()
    for text in load_corpus().values():
        # keep clitics attached here so that "don't" is one collocate, as in the figure
        toks = tokens(text, split_clitics=False)
        for i, t in enumerate(toks):
            if t in nodes:
                c.update(toks[max(0, i - window): i] + toks[i + 1: i + 1 + window])
    return c


def plot(counts: dict[str, int], subtitle: str) -> None:
    terms = HOSTILE + BUSINESS
    colors = ["#b23a48"] * len(HOSTILE) + ["#8a8f98"] * len(BUSINESS)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(terms, [counts.get(t, 0) for t in terms], color=colors)
    ax.set_title(f"Collocates of the node PAY\n{subtitle}", fontsize=13)
    ax.set_ylabel("Co-occurrence frequency")
    ax.set_xlabel("Collocate")
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color="#b23a48"), plt.Rectangle((0, 0), 1, 1, color="#8a8f98")],
              labels=["Hostile/coercive", "Standard business"], title="Semantic field", frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    RESULTS.mkdir(parents=True, exist_ok=True)
    fig.savefig(RESULTS / "figure_9_4_pay_collocates.png", dpi=200)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", type=int, default=5)
    ap.add_argument("--thesis", action="store_true", help="plot the counts published in the thesis")
    ap.add_argument("--with-money", action="store_true", help="add MONEY to the node set (the thesis text cites collocates 'near pay and money')")
    a = ap.parse_args()
    c = collocates(a.window, NODE | {"money"} if a.with_money else NODE)
    with (RESULTS / "pay_collocates.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["collocate", f"freq_window_{a.window}", "thesis_figure_9_4"])
        for t, f in c.most_common():
            w.writerow([t, f, THESIS_COUNTS.get(t, "")])
    for t in HOSTILE + BUSINESS:
        print(f"{t:10} corpus(±{a.window})={c[t]:3}   thesis={THESIS_COUNTS[t]}")
    if a.thesis:
        plot(THESIS_COUNTS, "counts as published (Figure 9.4)")
    else:
        plot(c, f"recomputed from corpus, window ±{a.window}")


if __name__ == "__main__":
    main()
