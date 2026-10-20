# Deposit checklist

Status as of branch `deposit-prep`. Work from top to bottom. Items marked **(R2)**
and **(R3)** answer Fernández Cruz's recommendations 2 and 3.

## Corpus
- [x] 18 transcripts in `corpus/raw/` (EDNY_005 filename fixed)
- [x] `corpus_metadata.csv` filled from Table 1.3, plus measured counts and SHA-256
- [ ] Resolve NJ_002 length vs Table 1.3 (DISCREPANCIES B1)
- [ ] Confirm EDNY_008/EDNY_010 docket, NJ_001 docket, SDNY_001 speakers (B4–B6)
- [ ] Add PACER document numbers (ECF No.) per file in the `notes` column
- [ ] Ask the UA Data Protection Officer about third-party names; record the decision in `corpus/raw/README.md` **(R3)**

## Annotation
- [x] Appendix N → `annotation/scheme/tagset.csv` + `codebook.md`
- [x] Appendices H, I, J, L, M → `annotation/concordances/*_appendix_*.csv`, validated against the transcripts
- [ ] Export the CATMA 7 project as TEI/XML → `annotation/project/` **(R3)**
- [ ] Export the full concordance spreadsheets (all 149 directives, PronounVerb, Slur, ViolenceVerb, keyword categories, PAY lines) → `annotation/concordances/` **(R3)**
- [ ] Add the 88 SBCSAE directive codes (transcript + line references if the SBCSAE licence does not allow excerpts)
- [ ] Fix the appendix rows flagged in DISCREPANCIES C1–C4, or annotate them

## Reliability **(R2)**
- [ ] Settle the **⚑ decide** rules in `annotation/scheme/codebook.md`
- [ ] Fill `annotation/reliability/pass1_pass2_file_level.csv` with the real per-file labels
- [ ] Recruit a second coder; run the calibration round; code `sample_for_coder.csv` blind
- [ ] `python code/reliability.py …` for each layer; report κ, AC1, PABAK and the confusion matrix in § 1.4.3

## Code
- [x] Appendix K replaced by `code/pay_collocation.py`
- [x] `stats_contingency.py`, `corpus_frequencies.py`, `reliability.py`, `keyness.py`, `validate_concordances.py`, `run_all.py`
- [x] Regression tests + GitHub Action
- [ ] Add the original figure scripts (Figures 9.3, 9.5, 9.7, 9.8)
- [ ] Keyness: add the Sketch Engine export and settings, or build the OANC list with `keyness.py --build-reference`

## Thesis text **(R3)**
- [ ] Replace § 1.3.1 and the end of Appendix N with the text in `docs/DATA_AVAILABILITY_STATEMENT.md`
- [ ] Footnote 56 / Table 8.9: name the OR estimator (A1); align Table 8.13 (A2); name Wilson CIs (A3)
- [ ] § 9.4 / Appendix L: state the counting rule for *supposed to* and *better* (C4)

## Release
- [ ] Add your ORCID to `CITATION.cff`
- [ ] Merge `deposit-prep`; tag `v1.0.0`
- [ ] Enable the Zenodo–GitHub integration **before** tagging, so the tag triggers the DOI
- [ ] Replace `10.5281/zenodo.XXXXXXX` in README, CITATION.cff and the thesis
