"""Reproduce the inferential statistics of Chapter 8 (Tables 8.9 and 8.13, § 8.4.2).

Inputs  (counts transcribed from the dissertation):
    data/reported/table_8_7_directives_by_file.csv
    data/reported/table_8_8_sbcsae_baseline.csv
    data/reported/table_8_13_modal_orientation.csv
    data/reported/figure_8_4_expressive_directness.csv
Outputs:
    data/results/table_8_9_reproduced.csv
    data/results/table_8_13_reproduced.csv
    data/results/expressive_directness_ci.csv

Every odds-ratio estimator is reported side by side, because the published
values depend on the estimator:
  * Table 8.9  (OR ≈ 313, 95% CI [91, 1082]) = Haldane–Anscombe (+0.5) OR, Woolf CI
  * Table 8.13 (OR = 3.0, 95% CI [0.14, 64.3]) = uncorrected sample OR, Woolf CI
  * scipy.stats.fisher_exact returns the *sample* OR (379.6 for Table 8.9);
    the exact conditional-MLE OR with exact CI is a third option (≈353 [94, 2053]).
The p-values (Fisher two-sided), Pearson χ² (no Yates) and G² match the thesis.

Run:  python code/stats_contingency.py
"""
from __future__ import annotations

import csv
import math

from scipy.stats import binomtest, chi2_contingency, fisher_exact
from scipy.stats.contingency import odds_ratio

from _corpus import RESULTS, ROOT

REPORTED = ROOT / "data" / "reported"
Z = 1.959963984540054


def _read(name: str) -> list[dict]:
    return list(csv.DictReader((REPORTED / name).open(encoding="utf-8")))


def woolf(a: float, b: float, c: float, d: float, add: float = 0.0) -> tuple[float, float, float]:
    a, b, c, d = (x + add for x in (a, b, c, d))
    o = (a * d) / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return o, math.exp(math.log(o) - Z * se), math.exp(math.log(o) + Z * se)


def analyse_2x2(table: list[list[int]]) -> dict:
    """All statistics for a 2×2 table [[a, b], [c, d]]."""
    (a, b), (c, d) = table
    _, p_fisher = fisher_exact(table, alternative="two-sided")
    cond = odds_ratio(table, kind="conditional")
    cond_ci = cond.confidence_interval(confidence_level=0.95)
    chi2, p_chi2, _, _ = chi2_contingency(table, correction=False)
    chi2_y, p_chi2_y, _, _ = chi2_contingency(table, correction=True)
    g2, p_g2, _, _ = chi2_contingency(table, correction=False, lambda_="log-likelihood")
    out = {
        "a": a, "b": b, "c": c, "d": d,
        "fisher_p_two_sided": p_fisher,
        "chi2_pearson": chi2, "chi2_p": p_chi2,
        "chi2_yates": chi2_y, "chi2_yates_p": p_chi2_y,
        "G2_loglik": g2, "G2_p": p_g2,
        "OR_conditional_mle": cond.statistic,
        "OR_conditional_ci_low": cond_ci.low, "OR_conditional_ci_high": cond_ci.high,
    }
    if min(a, b, c, d) > 0:
        o, lo, hi = woolf(a, b, c, d)
        out.update(OR_sample=o, OR_sample_woolf_low=lo, OR_sample_woolf_high=hi)
    o, lo, hi = woolf(a, b, c, d, add=0.5)
    out.update(OR_haldane=o, OR_haldane_woolf_low=lo, OR_haldane_woolf_high=hi)
    return out


def _write(name: str, rows: list[dict]) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / name).open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()})


def table_8_9() -> dict:
    mafia = _read("table_8_7_directives_by_file.csv")
    sbc = _read("table_8_8_sbcsae_baseline.csv")
    m_u = sum(int(r["unmitigated"]) for r in mafia)
    m_m = sum(int(r["mitigated"]) for r in mafia)
    s_u = sum(int(r["unmitigated"]) for r in sbc)
    s_m = sum(int(r["mitigated"]) for r in sbc)
    res = {"comparison": "Mafia vs SBCSAE: unmitigated/mitigated directives"}
    res.update(analyse_2x2([[m_u, m_m], [s_u, s_m]]))
    _write("table_8_9_reproduced.csv", [res])
    return res


def table_8_13() -> dict:
    rows = {r["modal_orientation"]: r for r in _read("table_8_13_modal_orientation.csv")}
    t = [[int(rows["prospective"]["intra_family"]), int(rows["prospective"]["inter_family"])],
         [int(rows["retrospective"]["intra_family"]), int(rows["retrospective"]["inter_family"])]]
    res = {"comparison": "Prospective/Retrospective x Intra/Inter-family (2x2 sub-table)"}
    res.update(analyse_2x2(t))
    _write("table_8_13_reproduced.csv", [res])
    return res


def expressive_ci() -> list[dict]:
    rows = _read("figure_8_4_expressive_directness.csv")
    n = sum(int(r["n"]) for r in rows if r["degree"] != "E0")
    out = []
    for r in rows:
        if r["degree"] == "E0":
            continue
        k = int(r["n"])
        bt = binomtest(k, n)
        wil = bt.proportion_ci(0.95, method="wilson")
        exa = bt.proportion_ci(0.95, method="exact")
        out.append({"degree": r["degree"], "k": k, "n": n, "prop": k / n,
                    "wilson_low": wil.low, "wilson_high": wil.high,
                    "clopper_pearson_low": exa.low, "clopper_pearson_high": exa.high})
    _write("expressive_directness_ci.csv", out)
    return out


def main() -> None:
    r = table_8_9()
    print("Table 8.9  (thesis: OR≈313 [91,1082]; χ²=184.5; G²=212.7; p<.001)")
    print(f"  Fisher p = {r['fisher_p_two_sided']:.3g}   χ² = {r['chi2_pearson']:.1f}   G² = {r['G2_loglik']:.1f}")
    print(f"  OR Haldane+Woolf   = {r['OR_haldane']:.1f} [{r['OR_haldane_woolf_low']:.1f}, {r['OR_haldane_woolf_high']:.1f}]  <- matches thesis")
    print(f"  OR sample+Woolf    = {r['OR_sample']:.1f} [{r['OR_sample_woolf_low']:.1f}, {r['OR_sample_woolf_high']:.1f}]")
    print(f"  OR conditional MLE = {r['OR_conditional_mle']:.1f} [{r['OR_conditional_ci_low']:.1f}, {r['OR_conditional_ci_high']:.1f}]")
    r = table_8_13()
    print("Table 8.13 (thesis: OR=3.0 [0.14,64.3]; Fisher p=.51)")
    print(f"  Fisher p = {r['fisher_p_two_sided']:.3f}")
    print(f"  OR sample+Woolf    = {r['OR_sample']:.2f} [{r['OR_sample_woolf_low']:.2f}, {r['OR_sample_woolf_high']:.1f}]  <- matches thesis")
    print(f"  OR Haldane+Woolf   = {r['OR_haldane']:.2f} [{r['OR_haldane_woolf_low']:.2f}, {r['OR_haldane_woolf_high']:.1f}]")
    print("Expressive directness (thesis: D1 55% [40-70]; D3 39% [26-55])")
    for e in expressive_ci():
        print(f"  {e['degree']}: {e['prop']:.0%}  Wilson [{e['wilson_low']:.0%}, {e['wilson_high']:.0%}]"
              f"  exact [{e['clopper_pearson_low']:.0%}, {e['clopper_pearson_high']:.0%}]")


if __name__ == "__main__":
    main()
