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
