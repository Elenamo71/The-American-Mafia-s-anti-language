"""Rebuild Table 9.5 (violence-verb relexicalization by semantic field).

Input:   annotation/concordances/violence_verbs_inventory.csv
         (the working spreadsheet "Violent verbs Wepon no weapon", one row per verb type,
          with the semantic field taken from Table 9.5)
Output:  data/results/table_9_5_reproduced.csv

Rates per 10,000 words use the Table 1.3 corpus size (14,072 words), as in the thesis.

Two limits (docs/DISCREPANCIES.md, F3):
  * the inventory gives counts per verb but not WHICH corpus lines were counted;
    annotation/concordances/violence_verbs_candidates.csv lists every candidate
    line so the selection can be marked and made reproducible;
  * the inventory marks "banged up" as weapon-mediated (12 weapon tokens);
    Table 9.5 reports 11.

Run:  python code/table_9_5_violence.py
"""
from __future__ import annotations

import csv
from collections import defaultdict

from _corpus import CONC, RESULTS

CORPUS_WORDS = 14072
ORDER = ["corrective", "blunt assault", "lethal", "severe harm", "edged-piercing", "asphyxiation", "generic/precursor"]


def table() -> list[dict]:
    rows = [r for r in csv.DictReader((CONC / "violence_verbs_inventory.csv").open(encoding="utf-8"))
            if r["in_table_9_5"] == "yes"]
    agg = defaultdict(lambda: {"tokens": 0, "types": 0, "weapon": 0, "verbs": []})
    for r in rows:
        a = agg[r["semantic_field_table_9_5"]]
        a["tokens"] += int(r["tokens"]); a["types"] += 1
        a["weapon"] += int(r["weapon_mediated_tokens"]); a["verbs"].append(r["verb"].lower())
    total = sum(a["tokens"] for a in agg.values())
    out = []
    for f in ORDER:
        a = agg[f]
        out.append({"semantic_field": f, "tokens": a["tokens"], "pct_tokens": round(100 * a["tokens"] / total, 1),
                    "per_10k_words": round(10_000 * a["tokens"] / CORPUS_WORDS, 1), "types": a["types"],
                    "weapon_mediated": a["weapon"], "verbs": "; ".join(a["verbs"])})
    out.append({"semantic_field": "TOTAL", "tokens": total, "pct_tokens": 100.0,
                "per_10k_words": round(10_000 * total / CORPUS_WORDS, 1),
                "types": sum(a["types"] for a in agg.values()),
                "weapon_mediated": sum(a["weapon"] for a in agg.values()), "verbs": ""})
    return out


def main() -> None:
    out = table()
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / "table_9_5_reproduced.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), lineterminator="\n")
        w.writeheader(); w.writerows(out)
    print("Table 9.5 (thesis TOTAL: 51 tokens, 36.2 per 10K, 28 types, 11 weapon-mediated)")
    for r in out:
        print(f"  {r['semantic_field']:18} tokens={r['tokens']:3}  %={r['pct_tokens']:5}  /10K={r['per_10k_words']:5}"
              f"  types={r['types']:2}  weapon={r['weapon_mediated']}")


if __name__ == "__main__":
    main()
