# Data availability statement: text for the dissertation

Reviewer request #3 (J. Fernández Cruz): *state the format of the corpus to be
deposited and qualify the reproducibility claim in § 1.3.1.* The reviewer also
pointed out that keyword-extracted concordances coded in spreadsheets are not an
annotated corpus with an embedded or stand-off layer, and that keyword retrieval
introduces selection bias.

Below is wording for the corrected dissertation. Replace `[DOI]` after the
Zenodo release and check every item against the repository at that tag.

---

## For § 1.3.1 (replaces the paragraph beginning "Reproducibility operates at two levels")

> Reproducibility operates at two levels. The analytical framework (the decision
> tree, § 1.3.2 and Appendix A) is fully specified and can be applied to any
> comparable corpus. Reproducing the specific results reported in Chapters 8 and 9
> is possible within a narrower scope. The materials are archived in a public
> GitHub repository (https://github.com/Elenamo71/The-American-Mafia-s-anti-language),
> and the version cited here is preserved with a persistent identifier on Zenodo
> (release v1.0.0, [DOI]). The deposit comprises:
> (a) the 18 transcript files as UTF-8 plain text, preserved without normalisation,
> with SHA-256 checksums and file-level metadata (docket, court, date, family, word
> count) in CSV;
> (b) the annotation scheme as a CSV tagset and a coding manual;
> (c) the CATMA 7 annotation project exported as stand-off TEI/XML, containing the
> span-level speech-act, agentive-ellipsis and organizational-context layers;
> (d) the keyword-based concordances with their manual functional coding (pronominal
> agency, slurs, violence-verb relexicalisation, modal census) in CSV; and
> (e) the Python scripts that recompute the reported statistics from these files.
>
> Two limits on this claim should be stated explicitly. First, the
> concordance-based layers are *keyword-seeded*. Only realisations retrieved by the
> keyword queries were coded, so the frequencies are conditional on the keyword
> lists and are not exhaustive counts over the corpus. Second, the speech-act
> typology, expressive directness and slur sentiment rest on the coding of a single
> analyst [*or, if the study is done*: were checked by an independent second coder
> on a stratified sample of 130 units (Cohen's κ = …, Gwet's AC1 = …; see § 1.4.3)].
> The results are therefore reproducible *from the deposited coded material*. They
> are not guaranteed to be re-derivable by an independent re-annotation of the raw
> transcripts.

## For the end of Appendix N (replaces the closing bulleted list)

> The following materials are archived at [DOI] (GitHub mirror:
> https://github.com/Elenamo71/The-American-Mafia-s-anti-language, tag v1.0.0):
>
> | Folder | Content | Format |
> |---|---|---|
> | `corpus/raw/` | 18 transcripts (Table 1.3) | UTF-8 `.txt`, original line breaks, SHA-256 checksums |
> | `corpus/metadata/` | Docket, court, date, family, speakers, word counts | CSV |
> | `annotation/scheme/` | Tagsets, tags, properties, values; coding manual | CSV, Markdown |
> | `annotation/project/` | CATMA 7.2.3 project (speech acts, agentive ellipsis, organizational context) | TEI/XML, stand-off |
> | `annotation/concordances/` | Keyword concordances with manual coding; Appendices H–M in machine-readable form | CSV (UTF-8) |
> | `annotation/reliability/` | Intra-rater pass data; second-coder sample and results | CSV |
> | `code/` | Analysis and figure scripts (Python ≥ 3.10) | `.py` |
>
> Licences: code under MIT. Annotations and derived data under CC BY 4.0. The
> transcript text reproduces public court records; no additional rights are
> claimed in it.

## Note on personal data (decide before release)

The transcripts name defendants, victims, witnesses and uncharged third parties.
The University of Alicante is an EU data controller, so GDPR applies to
publishing these files regardless of the data subjects' nationality. Criminal
conviction data falls under Art. 10 GDPR. Before release, ask the university's
Data Protection Officer (dpd@ua.es) whether to:

* publish the transcripts as they appear in the public record (current approach), or
* pseudonymise individuals who were not convicted in the proceeding, keeping a
  private key so that identities can still be verified against PACER.

Record the decision in `corpus/raw/README.md`.
