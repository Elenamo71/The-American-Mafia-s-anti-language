"""Agreement statistics for annotation reliability (reviewer request #2).

Input: a CSV with one row per coded unit and two label columns, e.g.

    unit_id,file_id,span,coder_a,coder_b
    D001,CA2C_001,"Tell him to go fuck himself.",directive,directive

Reports, overall and per category:
    observed agreement, Cohen's κ, PABAK, Gwet's AC1, Krippendorff's α (nominal),
    bootstrap 95% CIs for κ and AC1, and the confusion matrix.

AC1 and PABAK are included because the thesis invokes the "kappa paradox"
(Feinstein & Cicchetti, 1990): with skewed categories κ is depressed even when
raw agreement is high; AC1 (Gwet, 2008) is the coefficient usually reported
alongside κ in that situation.

Usage:
    python code/reliability.py annotation/reliability/<file>.csv \
        --a coder_a --b coder_b [--out data/results/reliability_<name>.csv]
    python code/reliability.py --demo     # sanity check on a known example
"""
from __future__ import annotations

import argparse
import csv
import random
from collections import Counter
from pathlib import Path


def observed(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a)


def cohen_kappa(a, b):
    n = len(a)
    cats = sorted(set(a) | set(b))
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in cats)
    po = observed(a, b)
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def pabak(a, b):
    q = len(set(a) | set(b))
    return float("nan") if q < 2 else (q * observed(a, b) - 1) / (q - 1)


def gwet_ac1(a, b):
    n = len(a)
    cats = sorted(set(a) | set(b))
    q = len(cats)
    if q < 2:
        return float("nan")
    ca, cb = Counter(a), Counter(b)
    pi = {k: (ca[k] + cb[k]) / (2 * n) for k in cats}
    pe = sum(p * (1 - p) for p in pi.values()) / (q - 1)
    return (observed(a, b) - pe) / (1 - pe)


def krippendorff_alpha_nominal(a, b):
    """Two coders, no missing data, nominal metric."""
    values = list(a) + list(b)
    n = len(values)
    cnt = Counter(values)
    do = sum(x != y for x, y in zip(a, b)) * 2 / n           # observed disagreement
    de = sum(cnt[c] * cnt[k] for c in cnt for k in cnt if c != k) / (n * (n - 1))
    return float("nan") if de == 0 else 1 - do / de


def bootstrap(fn, a, b, reps=2000, seed=1):
    rng = random.Random(seed)
    idx = list(range(len(a)))
    vals = []
    for _ in range(reps):
        s = [rng.choice(idx) for _ in idx]
        v = fn([a[i] for i in s], [b[i] for i in s])
        if v == v:
            vals.append(v)
    vals.sort()
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def report(a, b):
    k_lo, k_hi = bootstrap(cohen_kappa, a, b)
    g_lo, g_hi = bootstrap(gwet_ac1, a, b)
    return {
        "n_units": len(a),
        "categories": "|".join(sorted(set(a) | set(b))),
        "observed_agreement": observed(a, b),
        "cohen_kappa": cohen_kappa(a, b), "kappa_ci_low": k_lo, "kappa_ci_high": k_hi,
        "pabak": pabak(a, b),
        "gwet_ac1": gwet_ac1(a, b), "ac1_ci_low": g_lo, "ac1_ci_high": g_hi,
        "krippendorff_alpha_nominal": krippendorff_alpha_nominal(a, b),
    }


def landis_koch(k):
    if k != k:
        return "n/a"
    for lim, lab in [(0, "poor"), (0.2, "slight"), (0.4, "fair"), (0.6, "moderate"), (0.8, "substantial")]:
        if k <= lim:
            return lab
    return "almost perfect"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--a", default="coder_a")
    ap.add_argument("--b", default="coder_b")
    ap.add_argument("--out")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    if args.demo:
        # File-level organizational-context check reported in Appendix N:
        # 13/18 agreement, κ = 0.21, disagreements only pass-1 intra -> pass-2 inter.
        # These constraints determine the confusion matrix uniquely:
        # pass 1 = 17 intra / 1 inter; pass 2 = 12 intra / 6 inter.
        a = ["intra"] * 12 + ["inter"] * 1 + ["intra"] * 5
        b = ["intra"] * 12 + ["inter"] * 1 + ["inter"] * 5
        rows = [{"unit_id": i, args.a: x, args.b: y} for i, (x, y) in enumerate(zip(a, b))]
    else:
        rows = [r for r in csv.DictReader(Path(args.csv).open(encoding="utf-8"))
                if r.get(args.a, "").strip() and r.get(args.b, "").strip()]
    a = [r[args.a].strip() for r in rows]
    b = [r[args.b].strip() for r in rows]

    res = report(a, b)
    for k, v in res.items():
        print(f"{k:28} {v:.3f}" if isinstance(v, float) else f"{k:28} {v}")
    print(f"{'kappa band (Landis & Koch)':28} {landis_koch(res['cohen_kappa'])}")

    cats = sorted(set(a) | set(b))
    print("\nconfusion matrix (rows = A, cols = B)")
    print(" " * 14 + "".join(f"{c[:12]:>13}" for c in cats))
    cm = Counter(zip(a, b))
    for x in cats:
        print(f"{x[:13]:14}" + "".join(f"{cm[(x, y)]:>13}" for y in cats))

    if args.out:
        per_cat = []
        for c in cats:   # one-vs-rest agreement per category
            aa = [x == c for x in a]
            bb = [y == c for y in b]
            per_cat.append({"category": c, "n_a": sum(aa), "n_b": sum(bb),
                            "kappa_one_vs_rest": cohen_kappa(aa, bb)})
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(["measure", "value"])
            for k, v in res.items():
                w.writerow([k, round(v, 4) if isinstance(v, float) else v])
            w.writerow([])
            w.writerow(["category", "n_a", "n_b", "kappa_one_vs_rest"])
            for p in per_cat:
                w.writerow([p["category"], p["n_a"], p["n_b"], round(p["kappa_one_vs_rest"], 4)])


if __name__ == "__main__":
    main()
