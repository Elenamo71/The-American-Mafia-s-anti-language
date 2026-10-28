# Discrepancies found while building the reproduction package

This file records every point where the deposited materials and the dissertation
text do not yet agree. Each item says how it was detected and what would resolve
it. **None of these items changes a substantive conclusion.** They are the kind
of thing an examiner checks first when a repository is cited as the basis for
reproducibility. Resolve or annotate each one before tagging `v1.0.0`.

Re-run the checks with `python code/run_all.py`.

---

## A. Statistics (Chapter 8)

**A1. The odds-ratio estimator in Table 8.9 is not stated, and it is not the Fisher estimate.**
The thesis gives *"Fisher's exact (two-tailed) – Odds Ratio ≈ 313; 95% CI [91, 1082]"*.
From the Table 8.8 counts (146/3 vs 10/78), `code/stats_contingency.py` gives:

| Estimator | OR | 95% CI |
|---|---|---|
| Haldane–Anscombe (+0.5), Woolf CI | **312.9** | **[90.5, 1081.8]** ← the published values |
| Sample OR (what `scipy.stats.fisher_exact` returns), Woolf CI | 379.6 | [101.5, 1419.8] |
| Conditional MLE with exact CI (the "Fisher" OR proper) | 353.0 | [93.8, 2053.2] |

The p-value (< .001), χ² = 184.5 (no Yates correction) and G² = 212.7 all match exactly.
*Fix:* in Table 8.9 and footnote 56, describe the OR as "Haldane–Anscombe-corrected
OR with Woolf 95% CI; Fisher's exact p". The conclusion is unchanged because the
lower bound is ≥ 90 under every estimator.

**A2. Table 8.13 uses a different estimator.** OR = 3.0, CI [0.14, 64.3] is the
*uncorrected* sample OR with a Woolf CI. With the Table 8.9 method it would be
2.7 [0.21, 35.6]. Fisher p = .505 matches. *Fix:* use one method throughout, or
name the method in each table.

**A3. Figure 8.4 confidence intervals** (55% [40–70], 39% [26–55]) are Wilson
intervals and reproduce exactly. *Fix:* name the method.

**A4. Intra-rater κ.** 72.2% agreement and κ = 0.21 at file level reproduce
exactly from the only confusion matrix the published figures allow
(see `annotation/reliability/PROTOCOL.md`). Additional values: bootstrap 95% CI
for κ is 0.00–0.64; Gwet's AC1 = 0.60; PABAK = 0.44. Consider reporting AC1
alongside κ, because the thesis already invokes the κ paradox.

## B. Corpus files vs Table 1.3

**B1. NJ_002 is ~35% shorter than Table 1.3 states.** The deposited
`NJ_002.txt` has 893 words; Table 1.3 gives 1,372. Every other file is within
±2%. Corpus-wide pronoun counts still match the thesis closely
(*we* = 141 exactly; *I* = 667 vs 673), so this is more likely a Table 1.3 entry
error than a truncated file, but it cannot be settled from the repo alone.
*Fix:* compare `NJ_002.txt` with the PACER source and correct whichever is wrong.

**B2. Per-file word counts depend on tokenisation.** The repo gives 13,666
orthographic words, or 14,393 tokens with clitics split, against 14,072 in the
thesis. Differences per file are small apart from NJ_002. *Fix:* state which tool
produced Table 1.3 (Word, AntConc or Sketch Engine). `corpus_metadata.csv` keeps
the thesis figures and the measured ones side by side.

**B3. File name.** `EDNY_005 .txt` contained a space. It has been renamed to `EDNY_005.txt`.

**B4. Duplicate docket.** EDNY_008 and EDNY_010 both cite 08-cr-00076-JBW.
Confirm that they are distinct filings and add the PACER document numbers.

**B5. Speaker/family attribution of SDNY_001.** Table 1.3 lists Pasquale Parrello
(Genovese). Examples 8.6–8.7 attribute SDNY_001 speech to Harold Thomas (Lucchese).
*Fix:* list every speaker per file in the metadata. The inter-family coding in
Table 8.13 depends on it.

**B6. NJ_001 docket** is printed as `2008ROl468` (letters O and l), which is
probably `2008R01468`. Verify.

## C. Appendix tables vs the deposited transcripts

`code/validate_concordances.py` searches each quoted example in its attributed
file. Overall, **≈ 90% match verbatim**. The full table is in
`data/results/concordance_validation.csv`, and each concordance CSV carries a
`located_in_corpus` column.

**C1. Examples attributed to the wrong file** (found verbatim only in another file):

| Appendix | Row | Attributed | Found in | Text |
|---|---|---|---|---|
| I | 17 | CA2C_001 | EDNY_010 | *Go get your work. No one's giving you nothing.* (also row 55, so a possible **duplicate**) |
| I | 64 | NJ_001 | NJ_002 | *Tell him to remember what happened to these guys.* |
| H | 46 | EDNY_007 | NJ_002 | *this thing is gonna end* (also listed under NJ_002) |
| H | 48 | EDNY_007 | CA2C_001 | *the whole thing with him* |
| H | 49 | EDNY_007 | EDNY_003 | *everything this kid* |
| J | 83 | EDNY_008 | CA2C_001 | *you cocksucker* |

Generic phrases (*the same thing*, *the whole thing*; H 88–89) may legitimately
occur in several files; they are listed in the CSV only for completeness.

**C2. Quotations reworded relative to the transcript.** Thesis § 1.4.2 states
that excerpts are reproduced verbatim without normalisation, but some appendix
quotations differ from the deposited text. Examples:

| Appendix | Row | Appendix text | Transcript has |
|---|---|---|---|
| J | 78 | *I'm gonna beat your fucking ass* | *I'm going to beat your fucking ass* |
| J | 47 | *I'm gonna grab someone* | *We're gonna grab someone* |
| J | 36 | *you're a fuckin' lice* | *your just a fuckin' lice* |
| I | 84 | *Whack and maim this motherfucker—keep the pipes…* | *whack and maim this mother fucker keep the pipes handy and pipe him, pipe him…* |

*Fix:* align the appendix quotations with the transcript text, or note that the
appendices quote in condensed form.

**C3. Appendix text that is not in the deposited transcripts.**
* Appendix M rows 33–34 (NJ_001): *"After speaking to a mortgage broker … DROSSNER
  discussed the income figures…"*; *"Specifically, told DROSSNER, maybe '06…"*.
  These read as the affiant's narrative, not intercepted speech. If they are
  narrative, remove them from the epistemic census (40 → 38); if they are speech,
  the deposited NJ_001 file is incomplete.
* Appendix L row 52 (EDNY_002) *"…they're gonna start telling people you have to take it"*
  and row 73 (EDNY_004) are not located. Check them against the source documents.

**C4. Row counts vs reported totals.**
* Appendix L prints **157** deontic rows; § 9.4 reports **151**. The difference is
  exactly the 6 *supposed to* rows. With those excluded, high-value = 134 and
  median/low = 17, both exactly as in § 9.4. However, § 9.4 *lists* *supposed to*
  among the median/low expressions, and Appendix L's preamble places *better* in
  "median" obligation while § 9.4 counts it as high-value. *Fix:* state the
  counting rule once, and mark the excluded rows in Appendix L.
* Appendix M prints **39** rows; the thesis reports **40**.
* Appendix I is explicitly a 90-row sample of the 149 directives. The other 59
  exist only in the CATMA project, which must be exported for Tables 8.7–8.9 to be
  reproducible at token level.

**C5. Corpus counts vs reported counts** (`code/corpus_frequencies.py`, clitics split):

| Item | Thesis | Repo corpus |
|---|---|---|
| *we* | 141 | 141 |
| *must* | 1 | 1 |
| *I* | 673 | 667 |
| *guy* | 113 | 112 (+ *guys* 29) |
| *thing* | 49 | 46 (+ *things* 12) |

The small gaps are probably tokenisation differences or the B1 issue. State
whether plural forms are included.

## D. Code

**D1. Appendix K does not run as printed** (curly quotes, commas inside string
literals) and it plots hand-entered counts. It has been replaced by
`code/pay_collocation.py`.

**D2. The Figure 9.4 counts cannot be recomputed exactly.** No window or node
definition yields *don't* 7, *fucking* 6, *gonna* 5. With node = *pay* forms and
±5 words: 2 / 6 / 0. With *money* added: 10 / 11 / 8. The business-term zeros
reproduce under every setting. Appendix K says the counts were "aided by manual
count". *Fix:* deposit the PAY/MONEY concordance lines that were counted.

**D3.** § 1.4.4 says "Python 3.1"; that is almost certainly a typo, since
matplotlib and seaborn require Python ≥ 3.8. The repo targets Python ≥ 3.10.

**D4. Scheme narrowing.** The previous README said that the narrowing of the
exploratory CATMA scheme (*Trust* tagset, Conceptual Metaphor layer, finer
speech-act granularity) "is documented in § 1.4.3", but § 1.4.3 does not describe
it. *Fix:* add one sentence to § 1.4.3 or Appendix N. If any of those layers stay
in the CATMA export, list them in `annotation/project/README.md` as *not used in
the thesis*.

## E. Items that cannot be reproduced until material is deposited

| Thesis item | Needed |
|---|---|
| Tables 8.7–8.9 at token level | CATMA export (all 149 directives) and the 88 SBCSAE directive codes |
| Table 9.3 negativity score | Slur / violence / taboo inventories (spreadsheet export) |
| Table 9.4 (13.3:1), Table 9.5 | Violence-verb relexicalisation spreadsheet |
| Ideology : taboo 283 : 241 | Sketch Engine keyword list + manual categorisation |
| Keyness *gotta* G² = 2,590.1 | Sketch Engine export + settings, or an OANC frequency list for `code/keyness.py` |
| 5.7:1 agency-shift ratio | PronounVerb spreadsheet |
| κ = 0.21 per file | `annotation/reliability/pass1_pass2_file_level.csv` |

## F. Findings from the recovered working files (added 28 Oct 2026)

**F1. Table 8.13 is a file-level classification, not a census of 18 tokens.**
The pass-2 coding (`annotation/reliability/intra_rater_pass2_rows.csv`)
reproduces Table 8.13 cell for cell (9/3, 1/1, 2/2), but it has one row per
transcript file, and:

* 10 of the 18 rows are bracketed descriptions of the situation, e.g.
  *[Mediation of "Bazoo" dispute]*, *[Oversight of Capos and Soldiers]*, not
  utterances;
* 4 of the 8 quoted rows are **not found in the deposited transcripts**:
  CA2C_001 *"I'm gonna tell him… he's gonna have to do it"*, EDNY_002 *"They're
  gonna start telling people…"*, EDNY_006 *"I'm gonna cut you in half…"*,
  SDNY_001 *"He should've known better."* Pass 1 adds three more that are not
  found (*"You're a made man, you gotta do what you're told"*, *"I should've
  cracked him"*, *"I'm gonna dissolve you"*);
* the retrospective inter-family row for SDNY_001 is *"He should've known
  better"* (Parrello). The transcript and Chapter 8 instead have *"I should've
  punched his head in then"*.

§ 8.3.2 describes Table 8.13 as "a complete census of the eighteen modal-marked
threat tokens". *Fix (choose one):* (a) re-code Table 8.13 at token level from
the transcripts, with each row quoting an utterance verbatim (candidates can be
drawn from Appendices J and L), and re-run `code/stats_contingency.py`; or
(b) keep the counts and describe the table as a classification of the dominant
threat/directive act per file, replace each quotation that is not in the
transcripts with a verbatim one, and mark the descriptive rows as such. Because
the contrast is already reported as non-significant, either route leaves the
conclusions intact.

**F2. Intra-rater agreement: the unit and the rule.** With the recovered pass
data, 13/18 and κ = 0.211 reproduce exactly (`code/table_8_13_from_passes.py`),
under two rules that the thesis should state:
(i) a file's pass-1 label is the label of its first coded row (EDNY_007 has an
intra-family row (Asaro) before an inter-family row (Di Fiore));
(ii) EDNY_011, left blank in pass 1, is counted as intra-family. If the blank is
treated as missing, agreement is 12/18 and κ = 0.14. Pass 1 and pass 2 also
code *different* representative acts for some files (EDNY_006: Rappa vs Rappa
plus Tantillo; EDNY_007: Asaro vs Di Fiore), so the check compares file
labels, not the same tokens. The five disagreements (EDNY_006, EDNY_007,
EDNY_008, NJ_001, SDNY_001) are all intra → inter, as § 1.4.3 states.

**F3. Table 9.5 reproduces, with one exception.** The violence-verb inventory
gives 51 tokens and 28 types, and every field subtotal and the per-10,000 rates
match. It marks *banged up* as weapon-mediated, so it has 12 weapon-mediated
tokens; Table 9.5 has 11 (corrective field = 0). The inventory records counts but
not which lines were counted: the transcripts contain more forms of most
verbs than were counted (e.g. *straighten\** 7 vs 2; *kill\** 9 vs 2; *stab\** 7
vs 2), presumably because non-violent or reported uses were excluded. § 9.2.2
also says *straighten out* "appears 7 times… in 100% of instances" as a
resolution term, but Table 9.5 counts 2. *Fix:* mark the counted lines in
`annotation/concordances/violence_verbs_candidates.csv`.

**F4. Table 9.9, the *we* column, does not reproduce.** From the transcripts:
*I want* 37 ✓, *I told* 17 ✓, *I know* 22 (23), *I don't* 72 (79); *we are* +
*we're* 27 ✓, *we do* 4 ✓, but *we gotta* = 3 (+ *we got to* 4) against 16, and
*we have/had to* = 2 against 12. The working sheet has placeholders (`[High]`,
`[Med]`), not counts. The "28 instances" of obligation *we* in § 9.3.2 therefore
cannot be recovered. *Fix:* deposit the AntConc collocate output or correct the
counts (*we gotta/got to* 7; *we have/had to* 2).

**F5. The AntConc keyword list was run on 15 files.** Range never exceeds 15,
and *gotta* = 42 equals the count without EDNY_008/010/011. The reference corpus
(≈ 1.02 M tokens) is not named. The *gotta* G² = 2,590.1 in the thesis is not from
this export (AntConc LL = 324.2). See `data/tool_exports/README.md`.

**F6. Superseded analyses in the working files (not deposited).** An earlier
directive comparison used a borrowed business baseline (35% unmitigated / 25%
orders; χ² = 90.82 and 80.62) and earlier counts (123 directives, 5 mitigated;
*I* 835, *we* 163). The thesis replaced these with the purpose-built SBCSAE baseline (§ 8.2.2).
Two versions of a threat-category count (15/8/6 vs 27/11/9) match neither
Table 8.3 nor Table 8.14. **No working data was found for** Table 8.3 (16 veiled
threats), Table 8.14 (5 manipulative / 13 retaliative), Table 9.3 (negativity
score), Table 9.4 (93 : 7), the 5.7 : 1 agency-shift ratio, or the ideology : taboo
283 : 241 ratio.
