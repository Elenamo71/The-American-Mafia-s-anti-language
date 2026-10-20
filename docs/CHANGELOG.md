# Changelog

## [Unreleased] — deposit-prep
### Added
- Corpus metadata from Table 1.3 with measured word/token counts and SHA-256 checksums.
- Annotation scheme (`tagset.csv`) and a coding manual for second coders, from Appendix N.
- Appendices H, I, J, L, M as CSV; every example checked against the transcripts.
- Scripts: chapter 8 statistics (all OR estimators), corpus frequencies and modal
  census, PAY collocation (replaces Appendix K), keyness (open LL implementation),
  agreement statistics (κ, AC1, PABAK, α), reliability sample drawing, `run_all.py`.
- Regression tests that pin the published values; GitHub Action.
- Docs: reproduction map, discrepancies report, data-availability text for the
  thesis (reviewer request 3), reliability protocol (reviewer request 2).
### Changed
- `corpus/raw/EDNY_005 .txt` renamed to `EDNY_005.txt`.
- README rewritten to describe what is actually deposited.

## [1.0.0] — planned (on deposit)
- CATMA TEI export, full concordance spreadsheets, reliability data.
- Zenodo DOI.
