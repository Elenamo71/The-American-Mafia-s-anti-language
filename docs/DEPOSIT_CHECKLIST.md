# Deposit checklist (post-viva)

Work through this after the defence, before the first tagged release + Zenodo DOI.

## Corpus
- [ ] Upload the 18 transcript files to `corpus/raw/`
- [ ] Complete `corpus/metadata/corpus_metadata.csv` (docket numbers, dates, word counts)
- [ ] Confirm privacy handling of third-party names (see README privacy note)

## Annotation
- [ ] Freeze the English tagset in `annotation/scheme/tagset.csv` (done — verify)
- [ ] Rebuild the clean CATMA project (monolingual EN) and export to `annotation/project/`
- [ ] Export annotated concordances to `annotation/concordances/*.csv`
- [ ] Add the baseline SBCSAE directives (88 tokens) used for the OR ≈ 313 contrast

## Code
- [ ] Move Appendix K code into `code/` with clear filenames
- [ ] Verify each script runs from a clean clone
- [ ] Complete the table/figure → script map in REPRODUCTION.md
- [ ] Pin versions in requirements.txt

## Release
- [ ] Add your ORCID to CITATION.cff
- [ ] Tag v1.0.0
- [ ] Connect the repo to Zenodo → obtain DOI
- [ ] Replace every DOI placeholder (README, CITATION.cff) with the real DOI
- [ ] Update the URL/DOI in the deposited dissertation (§ 1.3.1 + Data Availability)
