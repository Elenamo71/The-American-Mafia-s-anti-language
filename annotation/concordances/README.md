# Coded concordances

## Files transcribed from the thesis appendices

| File | Appendix | Unit | Columns |
|---|---|---|---|
| `assertives_appendix_H.csv` | H (Table H.1) | example | item, file_id, category (`referential_vagueness` / `agentive_ellipsis`), example |
| `directives_appendix_I.csv` | I (Table I.1) — **sample of 90 of 149** | utterance | appendix_row, file_id, utterance, pragmatic_feature, mitigation, pillar |
| `expressives_commissives_appendix_J.csv` | J (Table J.1) | example | item, file_id, category (`expressive_honor_challenge` / `commissive_honor_defense`), example |
| `modals_deontic_appendix_L.csv` | L (Table L.1) | modal instance | appendix_row, file_id, modal, type, example |
| `modals_epistemic_appendix_M.csv` | M (Table M.1) | modal instance | appendix_row, file_id, modal, type, example |

Every file also has `located_in_corpus` and `found_in_file_instead`, written by
`code/validate_concordances.py` (values explained in `docs/REPRODUCTION.md`).
Text is reproduced exactly as printed in the appendix (curly quotes kept; the
Markdown italics in Appendix L removed; `EDNY_005_` normalised to `EDNY_005`).

These tables are a **bridge**. They document what the thesis printed, but they are
not the analyst's working data.

## Recovered from the working spreadsheets

| File | Content |
|---|---|
| `violence_verbs_inventory.csv` | 31 verb types with token counts and weapon mediation, plus the Table 9.5 semantic field; 28 are in Table 9.5 (*bother*, *die/dying*, *rob* excluded) |
| `violence_verbs_candidates.csv` | Every corpus line matching one of the 31 verbs (113 lines). **To complete:** fill `counted_in_table_9_5` (yes/no) and `weapon_mediated` so the 51 counted tokens are identifiable |

## To deposit (authoritative exports)

| File | Content |
|---|---|
| `speech_acts.csv` | All CATMA speech-act spans: file_id, start, end, text, type, property values, org_context (pass 1 and pass 2) |
| `pronoun_verb.csv` | Concordance lines for *I*/*we* + main verb, with `person`, `predicate` |
| `slurs.csv` | Slur lines with `category`, `sentiment`, `referent_group` |
| `violence_verbs.csv` | Violence-verb lines with `semantic_field`, `weapon_mediation` |
| `resolution_terms.csv` | Violence vs business resolution terms (Table 9.4) |
| `keyword_categories.csv` | Sketch Engine keywords with the ideology / taboo category |
| `pay_concordance.csv` | The PAY/MONEY lines counted for Figure 9.4 |
| `keyword_queries.txt` | The exact queries and search settings used to seed each concordance |
