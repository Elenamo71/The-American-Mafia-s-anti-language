"""Corpus-derived counts behind Chapters 8–9.

Outputs (data/results/):
    corpus_wordcounts.csv     per-file word/token counts vs Table 1.3
    corpus_wordlist.csv       full frequency list (clitics split, lower-cased)
    key_frequencies.csv       items cited in the thesis (I, we, gotta, must, guy, thing, …)
    modal_census.csv          deontic/epistemic tallies from Appendices L and M,
                              under both counting rules found in the thesis

Tokenisation: clitics are split (I'm -> i + 'm), as in Sketch Engine/AntConc.
Run:  python code/corpus_frequencies.py
"""
from __future__ import annotations

import csv
from collections import Counter

from _corpus import CONC, RESULTS, ROOT, load_corpus, tokens, word_count

KEY_ITEMS = ["i", "we", "gotta", "must", "better", "should", "guy", "guys", "thing", "things",
             "stuff", "pay", "money", "rat", "might", "may", "maybe", "perhaps", "could", "would"]
HIGH_VALUE = {"Strong Obligation", "Prohibition", "Threat Obligation", "Certainty/Command"}


def _write(name, header, rows):
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / name).open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main() -> None:
    corpus = load_corpus()
    meta = {r["file_id"]: r for r in csv.DictReader((ROOT / "corpus/metadata/corpus_metadata.csv").open(encoding="utf-8"))}

    total = Counter()
    rows = []
    for fid, text in corpus.items():
        toks = tokens(text)
        total.update(toks)
        thesis = int(meta[fid]["words_thesis_table_1_3"])
        wc = word_count(text)
        rows.append([fid, thesis, wc, len(toks), wc - thesis])
    rows.append(["TOTAL", sum(r[1] for r in rows), sum(r[2] for r in rows), sum(r[3] for r in rows),
                 sum(r[2] for r in rows) - sum(r[1] for r in rows)])
    _write("corpus_wordcounts.csv", ["file_id", "words_thesis", "words_repo", "tokens_clitics_split", "diff"], rows)
    _write("corpus_wordlist.csv", ["token", "freq"], total.most_common())

    n = sum(total.values())
    _write("key_frequencies.csv", ["item", "freq", "per_10k"],
           [[w, total[w], round(total[w] / n * 10_000, 2)] for w in KEY_ITEMS])

    deon = list(csv.DictReader((CONC / "modals_deontic_appendix_L.csv").open(encoding="utf-8")))
    epis = list(csv.DictReader((CONC / "modals_epistemic_appendix_M.csv").open(encoding="utf-8")))
    d_all = len(deon)
    d_excl = sum(1 for r in deon if r["modal"] != "supposed to")
    high = sum(1 for r in deon if r["type"] in HIGH_VALUE)
    low_excl = d_excl - high
    e = len(epis)
    census = [
        ["deontic_rows_printed_appendix_L", d_all, "all rows printed in Appendix L"],
        ["deontic_excluding_supposed_to", d_excl, "matches the 151 reported in § 9.4"],
        ["epistemic_rows_printed_appendix_M", e, "thesis reports 40"],
        ["ratio_deontic_epistemic_reported_rule", round(d_excl / 40, 2), "151/40 as in § 9.4"],
        ["ratio_deontic_epistemic_printed_rows", round(d_all / e, 2), "157/39 from printed appendices"],
        ["high_value_deontic", high, "Strong + Prohibition + Threat (better) + Certainty/Command; thesis 134"],
        ["median_low_deontic_excl_supposed_to", low_excl, "can + should + need to; thesis 17"],
        ["gotta_got_to_rows", sum(1 for r in deon if r["modal"] == "gotta/got to"), "thesis 65"],
        ["must_rows", sum(1 for r in deon if r["modal"] == "must"), "thesis 1"],
        ["better_rows", sum(1 for r in deon if r["modal"] == "better"), "thesis 10"],
        ["I_tokens_corpus", total["i"], "thesis 673"],
        ["we_tokens_corpus", total["we"], "thesis 141"],
        ["ratio_I_we_corpus", round(total["i"] / total["we"], 2), "thesis 4.8"],
    ]
    _write("modal_census.csv", ["measure", "value", "note"], census)
    for m in census:
        print(f"{m[0]:42} {m[1]:>8}   {m[2]}")


if __name__ == "__main__":
    main()
