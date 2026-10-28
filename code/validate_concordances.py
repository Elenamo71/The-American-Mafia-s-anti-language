"""Re-check every appendix example against the deposited transcripts.

Updates the `located_in_corpus` / `found_in_file_instead` columns of the
annotation/concordances/*_appendix_*.csv files and writes a summary to
data/results/concordance_validation.csv.

Run:  python code/validate_concordances.py
"""
import csv
from collections import Counter

from _corpus import CONC, RESULTS, corpus_normalised, load_corpus, locate

TEXT_COL = {"directives_appendix_I.csv": "utterance"}


def main() -> None:
    cn = corpus_normalised(load_corpus())
    summary = []
    for path in sorted(CONC.glob("*_appendix_*.csv")):
        rows = list(csv.DictReader(path.open(encoding="utf-8")))
        col = TEXT_COL.get(path.name, "example")
        counts = Counter()
        for r in rows:
            status, other = locate(r[col], r["file_id"], cn)
            r["located_in_corpus"], r["found_in_file_instead"] = status, other
            counts[status] += 1
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator="\n")
            w.writeheader(); w.writerows(rows)
        for status in ("exact", "segments", "partial", "other_file", "not_found"):
            summary.append({"file": path.name, "status": status, "n": counts[status], "of": len(rows)})
        print(f"{path.name:45} " + "  ".join(f"{k}={counts[k]}" for k in ("exact", "segments", "partial", "other_file", "not_found")))
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / "concordance_validation.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "status", "n", "of"], lineterminator="\n")
        w.writeheader(); w.writerows(summary)


if __name__ == "__main__":
    main()
