# The American Mafia's Anti-Language — Corpus, Annotation Scheme, and Analysis Code

[![DOI](https://img.shields.io/badge/DOI-pending%20via%20Zenodo-blue)](https://zenodo.org)

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
| `annotation/scheme/` | The annotation scheme (tagset) — layers, tags, values, definitions, sources |
| `annotation/project/` | The exported CATMA annotation project (stand-off, TEI/XML) |
| `annotation/concordances/` | Keyword-based concordances, manually annotated, exported to CSV |
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

Annotation followed **two complementary channels**, as described in the dissertation
(§ 1.4.3):

1. **CATMA (qualitative/structural).** Six tagsets applied directly to the 18
   transcripts: *Anti-state anti-language* (the five macro-level ideological pillars),
   *Trust*, *Threats*, *Speech Act Theory* (Searle's taxonomy + Austin's tripartite
   structure + CDA manipulation strategies), *Critical Discourse Analysis*, and
   *Conceptual Metaphor Theory* (Lakoff & Johnson). The raw project export is in
   `annotation/project/`; see `annotation/scheme/CATMA_annotation_guide.md` for the
   full tag inventory and thesis cross-references.
2. **Spreadsheets (quantitative/lexical).** Modal census (deontic/epistemic),
   pronominal agency, lexical nodes and slurs, and violence-verb relexicalization
   were extracted computationally and coded manually in spreadsheets — never in
   CATMA. These live in `annotation/concordances/`.

Reliability was assessed via an **intra-rater** re-annotation pass (Artstein & Poesio,
2008) covering two dimensions only (organizational context, modal orientation); see
the dissertation, § 1.4.3.

---

## Reproducing the analyses

Two levels of reproducibility are distinguished:

1. **Framework reproducibility** — the seven-step analytical decision tree can be applied to
   *any* comparable corpus. It is described in full in the dissertation (§ 1.3.2, Ch. 3).
2. **Analysis reproducibility** — the specific quantitative results can be reproduced from
   the materials here: the corpus (`corpus/`), the keyword lists and annotated concordances
   (`annotation/`), and the scripts (`code/`).

```bash
# 1. clone
git clone https://github.com/Elenamo71/american-mafia-antilanguage.git
cd american-mafia-antilanguage

# 2. environment
pip install -r requirements.txt

# 3. run (see docs/REPRODUCTION.md for per-figure/table instructions)
python code/pay_collocation.py
```

---

## Citation

If you use these materials, please cite both the dissertation and this dataset:

```bibtex
@dataset{morandini_2026_mafia_antilanguage,
  author    = {Morandini, Elena},
  title     = {The American Mafia's Anti-Language:
               Corpus, Annotation Scheme, and Analysis Code},
  year      = {2026},
  publisher = {Zenodo},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.XXXXXXX},
  url       = {https://github.com/Elenamo71/american-mafia-antilanguage}
}
```

*(DOI to be assigned on first Zenodo release — see `docs/DEPOSIT_CHECKLIST.md`.)*

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
