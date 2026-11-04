# Provenance of deposited files

Which working file each deposited file was derived from. The working files were
spreadsheets kept during the analysis (2024–2026). Unless stated otherwise the
conversion is lossless: same rows, same values, CSV encoding. Columns added
during deposit preparation are named in the last column.

| Deposited file | Working file (sheet) | Thesis item | Added during conversion |
|---|---|---|---|
| `annotation/reliability/intra_rater_pass1_rows.csv` | *Mafia Corpus Linguistic and Statistical Analysis* (identical copy: *… Analysis 1*) | § 1.4.3, App. N | `row`, `verbatim_status` |
| `annotation/reliability/intra_rater_pass2_rows.csv` | *GitHub Intra- Inter family Modal orientation whole Corpus* | Table 8.13; § 1.4.3 | `row`, `verbatim_status` |
| `annotation/reliability/pass1_pass2_file_level.csv` | derived from the two files above (first coded row per file in pass 1) | § 1.4.3, App. N (13/18, κ = 0.21) | whole file |
| `annotation/concordances/violence_verbs_inventory.csv` | *Violent verbs Wepon no weapon* (summary: *Violent verbs count*) | Table 9.5 | `semantic_field_table_9_5` (from Table 9.5), `in_table_9_5` |
| `annotation/concordances/violence_verbs_candidates.csv` | generated from `corpus/raw/` | Table 9.5 | whole file (to be completed) |
| `annotation/scheme/history/catma_pilot_tagset_v0.csv` | *CATMA annotation list for Pragmatics syntax and lexicosemantics* | § 1.4.3 (scheme narrowing) | `level` filled down |
| `data/tool_exports/antconc/keywords_top100_15files.csv` | *AntConc Keywords* (same as *AntConc-Experiment 1*) | § 9.4 background | decimals restored |
| `data/tool_exports/antconc/i_dont_4grams.csv` | *I_We bigrams volition and I donts* (sheet *I dont*) | Table 9.10 | — |
| `data/tool_exports/antconc/thing_L1_R1.csv` | *Bigrams* | § 8.1.2 | — |
| `data/tool_exports/antconc/exploratory/*` | *Experiment on Beef* | not used | — |
| `data/tool_exports/sketchengine/*` | *Keywords _ Sketch Engine*, *Keywords _ Sketch Engine_words* (PDF) | § 1.5 / § 9.4 | rank only |
| `data/tool_exports/voyant/*` | *Topic Analysis features*; Voyant screenshots | not used | — |

Working files not deposited, and the reason for each, are listed in the
deposit-preparation inventory kept by the author.
