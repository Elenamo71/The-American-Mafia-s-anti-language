# Tool exports

These files are outputs of the corpus tools, kept as they came from the tool
apart from the conversion to CSV. Each section below states the corpus version
the tool was run on. **Several exports predate the final 18-file corpus.**

## AntConc (`antconc/`)

| File | Content | Corpus version | Used in thesis |
|---|---|---|---|
| `keywords_top100_15files.csv` | Keyword list, top 100 by log-likelihood | 15 files, 13,527 tokens (no EDNY_008, EDNY_010, EDNY_011) | background to § 9.4. The thesis's keyness values come from Sketch Engine |
| `i_dont_4grams.csv` | 4-grams beginning *I don't* | 14,518 tokens (implied by NormFreq) | **Table 9.10**, identical |
| `thing_L1_R1.csv` | Word immediately left and right of *thing* | full corpus (43 tokens) | § 8.1.2 / Appendix H (vague reference) |
| `exploratory/beef_*`, `exploratory/violated_*` | KWIC, keyword row, collocates and 5-grams for *beef* and *violated* | 15 files | exploratory, not reported |

**Keyword list, how it was checked.** The export was written with a Spanish
locale, which dropped the decimal point in the normalised and keyness columns
(e.g. `34745324` for 34,745.324 per million). The CSV restores three decimals;
this was confirmed against the values quoted in the working notes (*beat*:
NormFreq 665.336). Recomputing log-likelihood with `code/keyness.py` formulas
reproduces the column (e.g. *gotta* 324.0 vs 324.2 exported). The implied
reference corpus has **≈ 1,017,879 tokens and at least 497 files**. *Its identity
is not recorded in the export; state which corpus it was.* The Range column
(max 15) shows the run used the 15-file corpus version.

The AntConc *gotta* log-likelihood (324.2) is not the *gotta* G² = 2,590.1
reported in § 10.1.2 / Resumen § 7. That figure comes from a different run (Sketch
Engine vs OANC Spoken, per § 1.5), which still has to be exported (see `sketchengine/`).

## Sketch Engine (`sketchengine/`)

| File | Content |
|---|---|
| `keywords_single_lemmas_top50_2024-09-11.csv` | Top 50 single-word keywords (lemmas), user corpus `american_mobsters`, 11 Sep 2024 |
| `keywords_multiword_terms_top50_2024-09-11.csv` | Top 50 multi-word terms, same run |

These are transcribed from two PDF printouts of the Sketch Engine screen, which
show **rank only, with no scores, frequencies or reference-corpus name**. To make the
keyness results reproducible, re-run *Keywords* and use *Download → CSV*. That
export includes the score, the frequencies, the reference corpus, the attribute
(word/lemma), the minimum frequency and the score type (simple maths with N, or
log-likelihood).

Working notes ("Comparison across Corpus") also record a Sketch Engine
*Compare corpora* run: American Mobsters vs OANC spoken = 4.74; vs enTenTen21 = 4.11;
OANC spoken vs enTenTen21 = 3.95 (1.00 = identical; higher = more different).
Export that matrix as well if the comparison is cited.

## Voyant Tools (`voyant/`)

| File | Content |
|---|---|
| `topic_model_terms_10x10.csv` | 10 topics × 10 terms (LDA) |
| `topic_model_document_weights.csv` | Topic weights per document (15 documents) |
| `screenshots/` | Cirrus word cloud (Jun 2024), summary panel (Nov 2024: **15 documents, 12,535 words**), topic panel (Dec 2024) and other views |

Exploratory, and not reported in the thesis. Voyant's topic model is not deterministic, so
the December 2024 screenshot and the CSV come from different runs and their topics
differ. The November 2024 summary also documents that NJ_002 was already about 900
words long at that date (see `docs/DISCREPANCIES.md`, B1).
