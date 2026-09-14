# Reproduction guide

This guide maps each quantitative claim in the dissertation to the script and data that
produce it. Populate the right-hand columns as scripts are uploaded.

## Environment
```bash
pip install -r requirements.txt
```

## Table / figure → script map

| Dissertation item | Produces | Script | Input |
|-------------------|----------|--------|-------|
| Table 8.x (bald-on-record directives; OR ≈ 313) | Fisher / χ² / G² | `code/directive_stats.py` | `annotation/concordances/directives.csv` |
| Fig. 9.4 (PAY collocates) | collocation figure | `code/pay_collocation.py` | `corpus/raw/` |
| Fig. 9.5 (PAY/MONEY radial map) | concept map | `code/concept_map.py` | `corpus/raw/` |
| Table 9.4 (semantic-field displacement 13.3:1) | frequency counts | `code/semantic_displacement.py` | `corpus/raw/` |
| Table 9.5 (violence-verb inventory) | inventory + rates | `code/violence_inventory.py` | `annotation/concordances/violence.csv` |
| Table 9.3 (negativity score 2.35×) | density measure | `code/negativity_score.py` | `annotation/concordances/slurs.csv` |
| Appendix L / M (modal census) | deontic/epistemic counts | `code/modal_census.py` | `annotation/concordances/modals.csv` |

*(Row list is illustrative — align with your final table/figure numbering.)*
