# Annotation Architecture — American Mafia Anti-Language Corpus

Two distinct, complementary annotation channels were used, as described in § 1.4.3.
This guide replaces earlier drafts that mistakenly modelled a "Modality/Agency" CATMA
tagset — no such tagset exists in the actual project (see `CATMA-Corpus-Export/`,
the real Pass-1 export). Modal, agency, and slur-density coding were always done
in spreadsheets, not in CATMA. What follows reflects the real project structure.

---

## Channel 1 — CATMA (qualitative/structural tagging)

Six tagsets were applied directly to the 18 transcripts in CATMA (Pass 1). The
authoritative source is the raw project export in `annotation/project/`; the
table below is a navigational summary, not a substitute for the exported tagset
definitions.

| Tagset | Representative tags | Function | Thesis reference |
|---|---|---|---|
| **Anti-state anti-language** | Family, Hierarchy, Honor, Omertà, Taxation, Us vs Them, War | The five macro-level ideological pillars | Chapter 5 |
| **Trust** | Individualized, Reputation, System, System of Sanctioning | Meso-level social practice (internal sanctioning) | Chapter 6 |
| **Threats** | Direct, Veiled, Conditional Threat, Futurity, Incentive, Retaliation, Violent verbs | Threat structure and orientation | §§ 8.3–8.4 |
| **Speech Act Theory** | DIRECTIVES, COMMISIVES, ASSERTION, EXPRESSIVES, DECLARATIONS, REPRESENTATIVES; Locutionary/Illocutionary/Perlocutionary; LEGITIMATION, DELEGITIMIZATION, SOCIAL CONTROL, SHAME/SELF-DOUBT, etc. | Composite: Searle's taxonomy + Austin's tripartite structure + CDA manipulation strategies | Ch. 3 (SAT); Chapter 9 |
| **Critical Discourse Analysis** | (manipulation-strategy tags) | Ideological-square annotation layer | § 3.3; Chapter 9 |
| **Conceptual Metaphor Theory** | Ontological, Orientational, Structural | Lakoff & Johnson (1980) metaphor types | § 2.4; Chapter 9 |

**Migration note.** Cleaning this project for deposit means: consolidating the
trilingual labels into English, verifying each tag's property definitions,
and re-exporting — not redesigning the scheme. The tags and their function are
already correct and already support the results reported in the thesis.

---

## Channel 2 — Spreadsheets (quantitative/lexical coding)

Per § 1.4.3, four measures were extracted computationally and coded manually in
spreadsheets — never in CATMA:

| Category | Values | Thesis reference |
|---|---|---|
| Modal census (deontic) | source: subjective/objective; force: absolute/negotiable | § 1.4.3, § 1.3.6; Appendix L |
| Modal census (epistemic) | hypothetical / uncertainty / probability | Appendix M |
| Agency | person (I/we); predicate field (command/violence/speech/other) | § 1.4.3; Appendix J |
| Lexical nodes / slurs | category (institutional/ethnic/pedigree/taboo intensifier); sentiment; referent group | § 1.4.3; § 9.1.2 |
| Relexicalization / violence verbs | semantic field (7 fields); weapon-mediated | § 9.2.2; Table 9.5 |
| Directive mitigation | bald-on-record / mitigated | § 1.3.5; Appendix I |

These live in `annotation/concordances/*.csv` and are migrated using the
tracker (`annotation_tracker.xlsx`), not in CATMA.

---

## Provenance (Pass 1 vs Pass 2)

- **Pass 1** (CATMA, initial period) — established both channels above in full.
- **Pass 2** (spreadsheets only, ~1 year later, independent) — re-classified
  *only* organizational context and modal orientation, as an intra-rater
  reliability check (κ = 0.21, § 1.4.3). These two properties are attached to
  the relevant spreadsheet-channel tokens; they were never part of the CATMA
  tagsets.

## Deposit checklist for this component

- [ ] Export the real CATMA project (Channel 1) cleanly in English → `annotation/project/`
- [ ] Verify each tagset's property definitions against the thesis text
- [ ] Migrate the spreadsheet categories (Channel 2) using `annotation_tracker.xlsx`
- [ ] Do NOT create a "Modal"/"Agency" CATMA tagset — this belongs in Channel 2
