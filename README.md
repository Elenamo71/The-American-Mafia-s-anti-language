# The American Mafia's Anti-Language: Corpus, Annotation Scheme, and Analysis Code

Supplementary research materials for the doctoral dissertation:

> Morandini, E. (2026). *The American Mafia's anti-language: A mixed-methods approach*
> [Doctoral dissertation, Universidad de Alicante].

The repository contains the corpus, the annotation scheme, the coded concordances
and the analysis code behind the quantitative findings of Chapters 8–9. The
dissertation applies a socio-cognitive Critical Discourse Analysis (van Dijk, 2011)
to authenticated RICO trial transcripts and analyses them as a Hallidayan
anti-language.

[![reproduce](../../actions/workflows/reproduce.yml/badge.svg)](../../actions/workflows/reproduce.yml)

---

## Quick start

```bash
git clone https://github.com/Elenamo71/The-American-Mafia-s-anti-language.git
cd The-American-Mafia-s-anti-language
pip install -r requirements.txt          # Python >= 3.10
sha256sum -c corpus/metadata/SHA256SUMS  # transcripts are byte-identical to the deposit
python code/run_all.py                   # every reproducible table/figure -> data/results/
pytest -q                                # checks the numbers printed in the thesis
```

What reproduces today, what doesn't yet, and why: [`docs/REPRODUCTION.md`](docs/REPRODUCTION.md).
Points where the deposit and the thesis text disagree: [`docs/DISCREPANCIES.md`](docs/DISCREPANCIES.md).

---

## Repository contents

| Folder | Contents | Format |
|---|---|---|
| `corpus/raw/` | The 18 transcript files (Table 1.3), preserved without normalisation | UTF-8 `.txt` (original CRLF line breaks) |
| `corpus/metadata/` | Docket, court, date, family, speakers; thesis and measured word counts; checksums | CSV, `SHA256SUMS` |
| `annotation/scheme/` | Tagsets, tags, properties and values (Appendix N); coding manual for second coders | CSV, Markdown |
| `annotation/project/` | CATMA 7 project export: the span-annotated layers | stand-off TEI/XML *(to deposit)* |
| `annotation/concordances/` | Appendices H, I, J, L, M as data, with each example checked against the transcripts; keyword concordances with manual coding | CSV |
| `annotation/reliability/` | Reliability protocol, the intra-rater pass, the second-coder sample | Markdown, CSV |
| `code/` | Analysis and figure scripts | Python |
| `data/reported/` | Counts transcribed from the thesis tables (script inputs where raw coding is not yet deposited) | CSV |
| `data/results/` | Script outputs | CSV, PNG |
| `docs/` | Reproduction guide, discrepancies, data-availability text for the thesis, deposit checklist | Markdown |
| `tests/` | Regression tests that pin the published numbers | pytest |

---

## Data availability and scope

The corpus comes from **authenticated U.S. federal RICO proceedings (2000–2023)**
retrieved through PACER/CourtListener. The source documents are public records.
Each file's docket number is given in `corpus/metadata/corpus_metadata.csv`, so
any transcript can be checked against the primary source. Transcription follows
the original FBI conventions (thesis Table 1.4); nothing has been normalised.

**Privacy note.** The transcripts name third parties (witnesses, victims, and
people mentioned but not convicted). Anyone using this material is responsible
for handling it according to the data-protection and privacy rules of their
jurisdiction. See `docs/DATA_AVAILABILITY_STATEMENT.md` for the GDPR question
that applies to the deposit itself.

---

## Annotation

Annotation followed a **two-stage, corpus-assisted procedure** (thesis § 1.4.3;
full scheme in Appendix N and [`annotation/scheme/`](annotation/scheme/)).

**Stage 1: computational extraction** (Sketch Engine, AntConc) produced keyness
scores, concordances, collocations, n-grams and frequency lists. The 3.8:1
deontic-to-epistemic ratio, the 4.8:1 *I*:*we* ratio, the keyness scores and the
pronominal bigrams are outputs of this stage, not manual annotations.

**Stage 2: manual functional coding** of the retrieved material, for the functions
that surface form does not reveal. For example, *"This guy is no good anymore"* was
retrieved through the keyword *guy* but coded as an implied directive.

| Tagset | Tag | Properties (values) | Channel |
|---|---|---|---|
| SpeechActs | Assertive / Directive / Commissive / Expressive | epistemic_commitment; mitigation; modal_orientation; directness | CATMA span |
| AgentiveEllipsis | SuppressedAgent | agent_recoverable (yes/no/ambiguous) | CATMA span |
| Context | (property on speech-act tokens) | organizational_context (intra-family/inter-family/civilian) | CATMA span |
| Agency | PronounVerb | person (I/we); predicate (command/violence/speech/other) | spreadsheet over concordance |
| Slurs | Slur | category; sentiment (neutral/hostile); referent_group (ingroup/outgroup) | spreadsheet over concordance |
| Relexicalization | ViolenceVerb | semantic_field (7 values); weapon_mediation (yes/no) | spreadsheet over concordance |

This operative scheme is a narrowed version of a broader exploratory scheme piloted
in CATMA. Categories were set aside if they did not bear on the Chapter 8–9
research questions, or if their fine distinctions could not be coded reliably by a
single annotator: a *Trust* tagset (kept for future work), a Conceptual Metaphor
layer (its function is covered by Hallidayan relexicalisation), and the finer
speech-act granularity.

**Modality is not a manual annotation layer.** The modal census is a count from
the wordlists; manual work was limited to disambiguating functionally ambiguous
forms (e.g. *must* as obligation vs inference) before counting.

**Coverage caveat.** The concordance-based layers are *keyword-seeded*. Only
realisations retrieved by the keyword queries were coded, so frequencies are
conditional on the keyword lists and are not exhaustive counts over the corpus
(thesis § 1.3.1).

**Reliability.** The thesis reports an intra-rater second pass at file level on
two dimensions (organizational context, modal orientation): 13/18 files agree,
κ = 0.21. The speech-act typology, expressive directness and slur sentiment rest
on single-analyst coding. A second-coder study of these layers is set out in
[`annotation/reliability/PROTOCOL.md`](annotation/reliability/PROTOCOL.md).

---

## Reproducibility: two levels

1. **Framework.** The analytical decision tree (thesis § 1.3.2, Appendix A) can be
   applied to any comparable corpus.
2. **Analysis.** The specific results can be reproduced *from the deposited coded
   material*: corpus, keyword lists, coded concordances and scripts. They are not
   guaranteed to be re-derivable by an independent re-annotation of the raw
   transcripts (see the coverage caveat).

---

## Citation

Cite both the dissertation and this dataset (see also [`CITATION.cff`](CITATION.cff)):

```bibtex
@phdthesis{morandini_2026_mafia_antilanguage_thesis,
  author = {Morandini, Elena},
  title  = {The American Mafia's anti-language: A mixed-methods approach},
  school = {Universidad de Alicante},
  year   = {2026}
}

@misc{morandini_2026_mafia_antilanguage_data,
  author       = {Morandini, Elena},
  title        = {The American Mafia's Anti-Language:
                  Corpus, Annotation Scheme, and Analysis Code},
  year         = {2026},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/Elenamo71/The-American-Mafia-s-anti-language}
}
```

---

## Licences

* **Code** (`code/`, `tests/`): [MIT](LICENSE)
* **Annotations and derived data** (`annotation/`, `data/`, `corpus/metadata/`): [CC BY 4.0](LICENSE-DATA)
* **Transcript text** (`corpus/raw/`): reproduces U.S. federal court records. No
  additional rights are claimed in it (see [`corpus/raw/README.md`](corpus/raw/README.md)).

---

## Status

**Pre-release (deposit preparation).** The corpus, metadata, scheme, appendix
data, statistics and tests are in place. The CATMA export, the full concordance
spreadsheets and the reliability data are still to be added; see
[`docs/DEPOSIT_CHECKLIST.md`](docs/DEPOSIT_CHECKLIST.md).
