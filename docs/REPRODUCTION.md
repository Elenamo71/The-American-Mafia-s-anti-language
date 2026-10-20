# Reproduction guide

```bash
pip install -r requirements.txt
python code/run_all.py      # writes everything below to data/results/
pytest -q                   # fails if any script stops matching the published value
```

**Status key.** ✅ reproduces the published value exactly · 🟡 reproduces, but the
method or the input needs a note in the thesis (see `DISCREPANCIES.md`) ·
⛔ cannot be reproduced until the listed material is deposited.

## Table / figure → script map

| Thesis item | Value(s) | Script | Input | Status |
|---|---|---|---|---|
| Table 1.3 word counts | 14,072 | `corpus_frequencies.py` → `corpus_wordcounts.csv` | `corpus/raw/` | 🟡 NJ_002 differs by ~479 words (B1) |
| Table 8.4 (vagueness/ellipsis) | thing 49, guy 113 | `corpus_frequencies.py` → `key_frequencies.csv` | `corpus/raw/` | 🟡 46 / 112 in repo (C5) |
| Tables 8.7–8.8 (mitigation) | 146/149; 10/88 | `stats_contingency.py` | `data/reported/table_8_7…`, `…8_8…` | 🟡 from published counts; token-level coding ⛔ CATMA export |
| Table 8.9 Fisher / χ² / G² | p < .001; 184.5; 212.7 | `stats_contingency.py` → `table_8_9_reproduced.csv` | as above | ✅ |
| Table 8.9 OR | 313 [91, 1082] | `stats_contingency.py` | as above | 🟡 Haldane–Woolf, not Fisher's OR (A1) |
| Table 8.13 + fn 57 | OR 3.0 [0.14, 64.3]; p = .51 | `stats_contingency.py` → `table_8_13_reproduced.csv` | `data/reported/table_8_13…` | ✅ (method differs from 8.9, A2) |
| Table 8.14 | 5 / 13 | — (descriptive) | `data/reported/table_8_14…` | ✅ |
| Figure 8.4 | 55% [40–70]; 39% [26–55] | `stats_contingency.py` → `expressive_directness_ci.csv` | `data/reported/figure_8_4…` | ✅ Wilson (A3) |
| § 1.4.3 / App. N intra-rater | 72.2%; κ = 0.21 | `reliability.py --demo` | reconstructed matrix | ✅; ⛔ per-file labels |
| § 9.3 *I* : *we* | 673 : 141 | `corpus_frequencies.py` → `modal_census.csv` | `corpus/raw/` | 🟡 667 : 141 |
| § 9.4 deontic : epistemic | 151 : 40 | `corpus_frequencies.py` | `annotation/concordances/modals_*` | 🟡 157 : 39 printed; 151 with *supposed to* excluded (C4) |
| § 9.4 high : low value | 134 : 17 | `corpus_frequencies.py` | `…modals_deontic_appendix_L.csv` | ✅ (excluding *supposed to*) |
| § 9.4 *gotta* / *must* / *better* | 65 / 1 / 10 | `corpus_frequencies.py` | as above | ✅ |
| Figure 9.4 (PAY collocates) | 7 / 6 / 5; 0 / 0 / 0 | `pay_collocation.py [--thesis]` | `corpus/raw/` | 🟡 direction reproduces; exact counts ⛔ PAY concordance (D2) |
| Keyness (*gotta* G² = 2,590.1) | — | `keyness.py --reference …` | OANC Spoken frequency list | ⛔ reference list + settings |
| Table 9.3 negativity score | — | — | slur/violence/taboo inventories | ⛔ |
| Tables 9.4–9.5 (13.3 : 1) | — | — | violence-verb spreadsheet | ⛔ |
| Ideology : taboo 283 : 241 | — | — | keyword list + categories | ⛔ |
| 5.7 : 1 agency shift | — | — | PronounVerb spreadsheet | ⛔ |
| Figures 9.3, 9.5, 9.7, 9.8 | — | — | original figure scripts | ⛔ |

## Appendix data

`code/validate_concordances.py` checks every example in Appendices H, I, J, L and M
against its attributed transcript and writes the result to the
`located_in_corpus` column of each CSV. A summary is written to
`data/results/concordance_validation.csv`:

| Value | Meaning |
|---|---|
| `exact` | found verbatim (punctuation, case and editorial brackets ignored) |
| `segments` | every segment between ellipses/dashes is found, i.e. an elided quotation |
| `partial` | some segments are found |
| `other_file` | not in the attributed file, but found verbatim in another file |
| `not_found` | wording differs from the deposited transcript |

## Tokenisation

`code/_corpus.py` splits clitics (*I'm* → *i* + *'m*), mirroring Sketch Engine
and AntConc for English. This is why the pronoun counts match the thesis.
Orthographic word counts (clitics not split) are reported separately.
