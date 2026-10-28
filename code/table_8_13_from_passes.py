"""Rebuild Table 8.13 and the intra-rater agreement (§ 1.4.3) from the deposited coding.

Inputs:
    annotation/reliability/intra_rater_pass2_rows.csv   final (pass-2) coding, one row per file
    annotation/reliability/pass1_pass2_file_level.csv   file-level labels of both passes
Outputs:
    data/results/table_8_13_from_pass2.csv
    data/results/reliability_org_context_file_level.csv

Scope note (see docs/DISCREPANCIES.md, section F1): the pass-2 sheet has ONE row
per transcript file. Ten of the 18 rows describe a situation in brackets instead
of quoting an utterance, and four quotations are not found in the deposited
transcripts. The counts reproduce Table 8.13 exactly, but the unit is a
file-level classification, not a census of 18 utterance tokens.

Run:  python code/table_8_13_from_passes.py
"""
from __future__ import annotations

import csv
from collections import Counter

from _corpus import RESULTS, ROOT
from reliability import cohen_kappa, gwet_ac1, observed, pabak

REL = ROOT / "annotation" / "reliability"
ORIENT = ["Prospective", "Retrospective", "Other"]
CTX = ["Intra-Family", "Inter-Family"]


def table_8_13() -> dict[tuple[str, str], int]:
    rows = list(csv.DictReader((REL / "intra_rater_pass2_rows.csv").open(encoding="utf-8")))
    return Counter((r["modal_orientation"].split(" ")[0], r["org_context"]) for r in rows)


def reliability() -> dict[str, float]:
    rows = list(csv.DictReader((REL / "pass1_pass2_file_level.csv").open(encoding="utf-8")))
    a = [r["pass1_org_context"] for r in rows]
    b = [r["pass2_org_context"] for r in rows]
    return {"n_files": len(a), "agreements": sum(x == y for x, y in zip(a, b)),
            "observed_agreement": observed(a, b), "cohen_kappa": cohen_kappa(a, b),
            "gwet_ac1": gwet_ac1(a, b), "pabak": pabak(a, b)}


def main() -> None:
    t = table_8_13()
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / "table_8_13_from_pass2.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["modal_orientation"] + CTX + ["total"])
        for o in ORIENT:
            w.writerow([o] + [t[(o, c)] for c in CTX] + [sum(t[(o, c)] for c in CTX)])
    print("Table 8.13 (thesis: 9/3, 1/1, 2/2)")
    for o in ORIENT:
        print(f"  {o:14} intra={t[(o, 'Intra-Family')]}  inter={t[(o, 'Inter-Family')]}")

    r = reliability()
    with (RESULTS / "reliability_org_context_file_level.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["measure", "value"])
        for k, v in r.items():
            w.writerow([k, round(v, 4) if isinstance(v, float) else v])
    print(f"Intra-rater, organizational context (thesis: 13/18, kappa = 0.21): "
          f"{r['agreements']}/{r['n_files']}, kappa = {r['cohen_kappa']:.3f}, AC1 = {r['gwet_ac1']:.3f}")


if __name__ == "__main__":
    main()
