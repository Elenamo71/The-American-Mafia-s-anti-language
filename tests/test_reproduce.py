"""Regression tests: the scripts must keep reproducing the numbers printed in the thesis.

Run: pytest -q
"""
import csv
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import corpus_frequencies  # noqa: E402
import reliability  # noqa: E402
import stats_contingency as sc  # noqa: E402
from _corpus import load_corpus  # noqa: E402


def test_corpus_has_18_files_matching_metadata():
    corpus = load_corpus()
    meta = [r["file_id"] for r in csv.DictReader((ROOT / "corpus/metadata/corpus_metadata.csv").open(encoding="utf-8"))]
    assert sorted(corpus) == sorted(meta) and len(meta) == 18


def test_table_1_3_total_preserved():
    meta = csv.DictReader((ROOT / "corpus/metadata/corpus_metadata.csv").open(encoding="utf-8"))
    assert sum(int(r["words_thesis_table_1_3"]) for r in meta) == 14072


def test_table_8_9():
    r = sc.table_8_9()
    assert (r["a"], r["b"], r["c"], r["d"]) == (146, 3, 10, 78)
    assert r["chi2_pearson"] == pytest.approx(184.5, abs=0.05)
    assert r["G2_loglik"] == pytest.approx(212.7, abs=0.05)
    assert r["fisher_p_two_sided"] < 0.001
    # published OR ≈ 313 [91, 1082] = Haldane-Anscombe + Woolf
    assert round(r["OR_haldane"]) == 313
    assert round(r["OR_haldane_woolf_low"]) == 91
    assert round(r["OR_haldane_woolf_high"]) == 1082


def test_table_8_13():
    r = sc.table_8_13()
    assert r["OR_sample"] == pytest.approx(3.0)
    assert r["OR_sample_woolf_low"] == pytest.approx(0.14, abs=0.005)
    assert r["OR_sample_woolf_high"] == pytest.approx(64.3, abs=0.05)
    assert round(r["fisher_p_two_sided"], 2) == 0.51


def test_figure_8_4_wilson_intervals():
    ci = {e["degree"]: e for e in sc.expressive_ci()}
    assert (round(ci["D1"]["wilson_low"], 2), round(ci["D1"]["wilson_high"], 2)) == (0.40, 0.70)
    assert (round(ci["D3"]["wilson_low"], 2), round(ci["D3"]["wilson_high"], 2)) == (0.26, 0.55)


def test_intra_rater_kappa_published():
    a = ["intra"] * 12 + ["inter"] + ["intra"] * 5
    b = ["intra"] * 12 + ["inter"] + ["inter"] * 5
    assert reliability.observed(a, b) == pytest.approx(13 / 18)
    assert round(reliability.cohen_kappa(a, b), 2) == 0.21


def test_modal_census_section_9_4():
    corpus_frequencies.main()
    m = {r["measure"]: r["value"] for r in csv.DictReader((ROOT / "data/results/modal_census.csv").open(encoding="utf-8"))}
    assert int(m["deontic_excluding_supposed_to"]) == 151
    assert int(m["high_value_deontic"]) == 134
    assert int(m["median_low_deontic_excl_supposed_to"]) == 17
    assert int(m["gotta_got_to_rows"]) == 65
    assert int(m["must_rows"]) == 1
    assert int(m["we_tokens_corpus"]) == 141


# ---- working-file data recovered on 2026-10-28 -------------------------------

def test_reliability_from_deposited_passes():
    import table_8_13_from_passes as t
    r = t.reliability()
    assert (r["agreements"], r["n_files"]) == (13, 18)
    assert round(r["cohen_kappa"], 2) == 0.21


def test_table_8_13_from_pass2_matches_published():
    import table_8_13_from_passes as t
    got = t.table_8_13()
    pub = {r["modal_orientation"]: r for r in csv.DictReader((ROOT / "data/reported/table_8_13_modal_orientation.csv").open(encoding="utf-8"))}
    for o, key in [("Prospective", "prospective"), ("Retrospective", "retrospective"), ("Other", "other")]:
        assert got[(o, "Intra-Family")] == int(pub[key]["intra_family"])
        assert got[(o, "Inter-Family")] == int(pub[key]["inter_family"])


def test_table_9_5_from_inventory():
    import table_9_5_violence as t
    rows = {r["semantic_field"]: r for r in t.table()}
    assert rows["TOTAL"]["tokens"] == 51 and rows["TOTAL"]["types"] == 28
    assert rows["TOTAL"]["per_10k_words"] == 36.2
    assert [rows[f]["tokens"] for f in t.ORDER] == [15, 12, 8, 5, 5, 3, 3]
    # inventory marks "banged up" as weapon-mediated; thesis reports 11 (DISCREPANCIES F3)
    assert rows["TOTAL"]["weapon_mediated"] == 12


def test_table_9_10_i_dont_4grams_match_corpus():
    import collections
    exp = {r["Type"]: int(float(r["Freq"])) for r in csv.DictReader((ROOT / "data/tool_exports/antconc/i_dont_4grams.csv").open(encoding="utf-8"))}
    from _corpus import tokens
    c = collections.Counter()
    for text in load_corpus().values():
        tk = tokens(text, split_clitics=False)
        for a, b, d in zip(tk, tk[1:], tk[2:]):
            if a == "i" and b == "don't":
                c[d] += 1
    for w in ("want", "know", "care", "need", "give"):
        assert c[w] == exp[f"i don t {w}"]
