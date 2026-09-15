# The American Mafia's Anti-Language — Corpus, Annotation Scheme, and Analysis Code

Supplementary research materials for the doctoral dissertation:

> Morandini, E. (2026). *The American Mafia's anti-language: A mixed-methods approach*
> [Doctoral dissertation, Universidad de Alicante].

This repository provides the corpus, the annotation scheme, the annotated concordances,
and the analysis code required to reproduce the quantitative findings reported in the
dissertation. It operationalizes a socio-cognitive Critical Discourse Analysis (van Dijk)
of authenticated RICO trial transcripts, analyzed as a Hallidayan anti-language.

---

## Repository contents

| Folder | Contents |
|--------|----------|
| `corpus/raw/` | The 18 transcript files (14,072 words) constituting the American Mafia corpus |
| `corpus/metadata/` | File-level metadata: PACER/CourtListener docket numbers, dates, jurisdictions |
| `annotation/scheme/` | The annotation scheme: the five operative tagsets (CATMA TEI/XML), plus a guide giving layers, tags, values, definitions, and thesis cross-references |
| `annotation/project/` | The exported CATMA annotation project (stand-off TEI/XML): the span-annotated layers |
| `annotation/concordances/` | Keyword-based concordances, manually coded, exported to CSV |
| `code/` | Python analysis and visualization scripts (keyness, collocation, statistics) |
| `data/results/` | Derived tables and figures underlying the dissertation's quantitative claims |
| `docs/` | Extended documentation, reproduction guide, changelog |

---

## Data availability & scope

The corpus derives from **authenticated U.S. federal RICO proceedings (2000–2023)**,
sourced from PACER/CourtListener. Source documents are matters of public record; each
file's docket number is provided in `corpus/metadata/` so that any transcript can be
independently verified against the primary source.

**Privacy note.** These transcripts name third parties (witnesses, victims, and individuals
mentioned but not convicted). Users of this material are responsible for handling it in
accordance with applicable data-protection and privacy obligations in their jurisdiction.

---

## Annotation

Annotation followed a **two-stage, corpus-assisted procedure** (dissertation § 1.4.3;
full scheme in Appendix N). Candidate spans were first retrieved computationally; the
retrieved material was then coded manually for the pragmatic, agentive, and lexicosemantic
functions that surface form alone does not disclose. For example, *"This guy is no good
anymore"* was retrieved through the keyword *guy* but manually coded as an implied
directive, not a description.

**Stage 1 — computational extraction (Sketch Engine, AntConc).** Keyness, concordances,
collocations, n-grams, and frequency lists. All ratios and counts reported in the
dissertation — the 3.8:1 deontic-to-epistemic ratio, the 4.8:1 *I*:*we* ratio, keyness
scores, and the pronominal bigrams — are outputs of this stage, not manual annotations.

**Stage 2 — manual functional coding.** Recorded against the scheme in
`annotation/scheme/`, which comprises five operative tagsets:

| Tagset | Tag | Properties (values) |
|--------|-----|---------------------|
| SpeechActs | Assertive / Directive / Commissive / Expressive | epistemic_commitment; mitigation; modal_orientation; subtype; org_context |
| AgentiveEllipsis | SuppressedAgent | agent_recoverable (yes/no/ambiguous) |
| Agency | PronounVerb | person (I/we); predicate (command/violence/speech/other) |
| Slurs | Slur | category; sentiment (neutral/hostile); referent_group (ingroup/outgroup) |
| Relexicalization | ViolenceVerb | semantic_field (7 values); weapon_mediation (yes/no) |

Speech-act type, expressive subtype, agentive ellipsis, and organizational context were
annotated as spans in **CATMA** (stand-off TEI; `annotation/project/`). Pronominal agency,
slurs, violence-verb relexicalization, and the deontic/epistemic modal census were coded
over **keyword concordances** in spreadsheets (`annotation/concordances/`). **Modality is
not a manual annotation layer:** the modal census is a wordlist-derived count, with manual
work limited to disambiguating functionally ambiguous forms before tallying.

This operative scheme is the result of narrowing a broader exploratory scheme piloted in
CATMA. Categories that did not bear on the Chapter 8–9 research questions, or whose
fine-grained distinctions could not be coded reliably by a single annotator, were set aside
(a *Trust* tagset, reserved for future work; a Conceptual Metaphor layer, whose function is
handled through Hallidayan relexicalization; and the finer speech-act granularity). The
narrowing is documented in § 1.4.3.

**Coverage & reproducibility caveat.** The annotated material consists of keyword-extracted
concordances with manual functional coding, **not** an exhaustive annotation layer over the
full corpus. Realizations not recovered by the keyword queries are not surfaced or counted;
frequencies are therefore conditioned on the keyword lists. This is stated in § 1.3.1 and
scopes the analysis-reproducibility claim below.

**Reliability** was assessed via an **intra-rater** re-annotation pass (Artstein & Poesio,
2008) covering two dimensions only — organizational context and modal orientation — with the
remaining interpretive layers resting on single-annotator coding (dissertation § 1.4.3).

---

## Reproducing the analyses

Two levels of reproducibility are distinguished:

1. **Framework reproducibility** — the analytical decision tree can be applied to *any*
   comparable corpus. It is described in full in the dissertation (§ 1.3.2, Ch. 3).
2. **Analysis reproducibility** — the specific quantitative results can be reproduced from
   the materials here: the corpus (`corpus/`), the keyword lists and annotated concordances
   (`annotation/`), and the scripts (`code/`), subject to the coverage caveat above (results
   are reproducible from the deposited keyword-seeded concordances, not re-derivable by
   exhaustive re-annotation of the raw corpus).

```bash
# 1. clone
git clone https://github.com/Elenamo71/The-American-Mafia-s-anti-language.git
cd The-American-Mafia-s-anti-language

# 2. environment
pip install -r requirements.txt

# 3. run (see docs/REPRODUCTION.md for per-figure/table instructions)
python code/pay_collocation.py
```

---

## Citation

If you use these materials, please cite both the dissertation and this dataset:

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
  howpublished = {GitHub repository},
  url          = {https://github.com/Elenamo71/The-American-Mafia-s-anti-language}
}
```

---

## Licences

- **Code** (`code/`): [MIT License](LICENSE-CODE)
- **Corpus, annotations, and derived data** (`corpus/`, `annotation/`, `data/`):
  [Creative Commons Attribution 4.0 International (CC-BY-4.0)](LICENSE-DATA)

---

## Status

🚧 **Skeleton / placeholder release.** Structure and documentation are in place; corpus,
annotation project, and code will be populated on deposit (post-viva). See
`docs/DEPOSIT_CHECKLIST.md` for what remains to be uploaded.
