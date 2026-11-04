# Reliability study protocol (reviewer request #2)

**Request** (J. Fernández Cruz, external report, recommendation 2): extend the
reliability check of the annotation to the core pragmatic categories, i.e. the
interpretive speech-act and sentiment assignments, *or* hedge the claims that
depend on them.

**Current state** (thesis § 1.4.3, Appendix N): only *organizational context*
and *modal orientation* were re-checked. That check was an intra-rater second pass
at **file level**: 13 of 18 files agree (72.2%), κ = 0.21. The actual pass data
are now deposited (`intra_rater_pass1_rows.csv`, `intra_rater_pass2_rows.csv`,
`pass1_pass2_file_level.csv`), and `python code/table_8_13_from_passes.py`
reproduces the published figures from them. The confusion matrix is:

| | Pass 2 intra | Pass 2 inter |
|---|---|---|
| **Pass 1 intra** | 12 | 5 |
| **Pass 1 inter** | 0 | 1 |

Re-analysed: κ = 0.211 (bootstrap 95% CI 0.00–0.64), PABAK = 0.44, Gwet's
AC1 = 0.60, Krippendorff's α = 0.14. With n = 18 files the estimate is too
imprecise to carry much weight, which is a further reason to move to token-level units.

## What to test

| Layer | Categories | Claims that depend on it |
|---|---|---|
| Speech-act type | assertive / directive / commissive / expressive / none | Tables 8.15–8.17; pillar mapping; "forensic pragmatics" proposals |
| Directive mitigation | bald-on-record / mitigated | 98% unmitigated; OR ≈ 313 (the only strongly significant result) |
| Expressive directness | D3 / D2 / D1 / E0 | Figure 8.4 (55% / 39%) |
| Slur sentiment | neutral / hostile (+ referent group) | Negativity score, Table 9.3 |
| Organizational context | intra / inter / civilian, **per token** | Table 8.13 (already hedged) |

## Design (recommended: inter-rater)

1. **Second coder.** An independent linguist who did not take part in the
   analysis, for example a fellow doctoral candidate who has used the
   van Dijk / Guillén-Nieto framework. The coder works only from
   `annotation/scheme/codebook.md` and the transcripts. They do not see the
   thesis chapters, the appendices or `sample_key.csv`.
2. **Training.** One calibration round on 15 units that are **not** in the
   test sample, followed by a discussion of the codebook only. Do not adjust any
   labels during calibration.
3. **Sample.** `python code/draw_reliability_sample.py --per-stratum 25 --distractors 30 --seed 2026`
   draws 130 units: 25 each of directive, commissive, expressive and assertive
   (as coded in the thesis), plus 30 uncoded segments as distractors. The
   distractors are what make speech-act *assignment* testable rather than only
   agreement on pre-selected items. Commit the seed and the sample file before
   coding starts.
4. **SBCSAE baseline.** The second coder should also code the 88 SBCSAE
   directives (mitigation only). The OR ≈ 313 contrast depends equally on how
   the baseline was coded.
5. **Coding.** The coder fills the code columns of `sample_for_coder.csv`, working blind.
6. **Analysis.** For each layer:
   `python code/reliability.py annotation/reliability/<layer>.csv --a thesis --b coder2 --out data/results/reliability_<layer>.csv`
   Report observed agreement, Cohen's κ with bootstrap CI, Gwet's AC1 and PABAK
   (needed because the categories are skewed), and the confusion matrix. The
   script also gives per-category one-vs-rest κ.
7. **Adjudication.** Disagreements may be discussed after the coefficients are
   computed, but the coefficients must be reported **before** adjudication.

### Fallback (if no second coder is available)

Run a token-level intra-rater pass on the same 130-unit sample after a cooling
interval of at least four weeks, coding blind from the codebook. Report it as
intra-rater agreement, which is weaker evidence, and hedge the dependent claims
as the reviewer allows. An LLM coder can be reported as a *supplementary* check
but not as a substitute for an independent human coder.

## Reporting thresholds (decide before coding)

| κ / AC1 | Wording in the thesis |
|---|---|
| ≥ .80 | "reliably coded" |
| .61–.80 | "substantial agreement"; claims stand with a note |
| .41–.60 | "moderate"; dependent claims reworded as interpretive |
| ≤ .40 | category treated as single-analyst interpretation (as now) |

## Files

| File | Content |
|---|---|
| `sample_for_coder.csv` | Blinded units (context + target) with empty code columns |
| `sample_key.csv` | Thesis label per unit. **Not committed until coding is finished** (listed in `.gitignore`); regenerate it locally with the same seed. Replace it with the CATMA labels once those are exported. |
| `intra_rater_pass1_rows.csv`, `intra_rater_pass2_rows.csv` | The two passes as coded, one row per coded act, with `verbatim_status` checked against the transcripts |
| `pass1_pass2_file_level.csv` | File-level labels behind the 72.2% / κ = 0.21 (rules in `docs/DISCREPANCIES.md`, F2) |
| `<layer>.csv` | One per layer: `unit_id,thesis,coder2` |
