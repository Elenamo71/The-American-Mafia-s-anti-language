"""Draw a blinded, stratified sample for the second-coder reliability study.

Reviewer request #2 (Fernández Cruz): extend reliability checking to the core
pragmatic categories — speech-act type and the interpretive (sentiment /
directness) assignments. This script prepares the material; the protocol is in
annotation/reliability/PROTOCOL.md.

Sampling frame
  * Utterance-like segments of every transcript (split on sentence punctuation
    and line breaks; segments of 3+ words).
  * Each segment is linked to the thesis coding when an Appendix H/I/J item
    occurs inside it (speech-act type taken from the appendix it came from).
  * Strata: directive, commissive, expressive, assertive (Appendix H items),
    and UNCODED segments (distractors). Distractors matter: without them the
    check only measures agreement on items the analyst already selected and
    cannot detect missed or over-assigned speech acts.

Outputs (annotation/reliability/):
  sample_for_coder.csv   what the second coder sees: context + target, empty code columns
  sample_key.csv         unit_id -> stratum and the thesis label (keep away from the coder)

Run:  python code/draw_reliability_sample.py --per-stratum 25 --distractors 30 --seed 2026
Then: replace sample_key.csv labels with the authoritative CATMA labels when the
      CATMA export is deposited (Appendix I is only a 90-of-149 sample).
"""
from __future__ import annotations

import argparse
import csv
import random
import re

from _corpus import CONC, ROOT, _norm, load_corpus

OUT = ROOT / "annotation" / "reliability"
SOURCES = [
    ("directives_appendix_I.csv", "utterance", lambda r: "directive"),
    ("expressives_commissives_appendix_J.csv", "example",
     lambda r: "expressive" if r["category"].startswith("expressive") else "commissive"),
    ("assertives_appendix_H.csv", "example", lambda r: "assertive"),
]
CODE_COLUMNS = ["speech_act_type", "directive_mitigation", "commissive_orientation",
                "expressive_directness", "contains_slur", "slur_sentiment",
                "organizational_context", "coder_note"]


def segments(text: str) -> list[str]:
    """Utterance-like segments. Hard-wrapped lines (no terminal punctuation,
    next line starting in lower case) are re-joined before splitting."""
    lines = [ln.strip() for ln in text.splitlines()]
    joined: list[str] = []
    for ln in lines:
        if not ln:
            continue
        if joined and not re.search(r"[.!?\"”’)\]]$", joined[-1]) and re.match(r"[a-z(\[]", ln):
            joined[-1] += " " + ln
        else:
            joined.append(ln)
    parts = [p for j in joined for p in re.split(r"(?<=[.!?])\s+", j)]
    return [" ".join(p.split()) for p in parts if len(p.split()) >= 3]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-stratum", type=int, default=25)
    ap.add_argument("--distractors", type=int, default=30)
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    rng = random.Random(a.seed)

    corpus = load_corpus()
    segs = [(fid, i, s) for fid, t in corpus.items() for i, s in enumerate(segments(t))]
    seg_norm = [(fid, i, s, _norm(s, False)) for fid, i, s in segs]
    by_file = {}
    for fid, i, s in segs:
        by_file.setdefault(fid, []).append(s)

    labelled: dict[tuple[str, int], str] = {}
    for fname, col, lab in SOURCES:
        for r in csv.DictReader((CONC / fname).open(encoding="utf-8")):
            key = _norm(r[col], False)
            if len(key.split()) < 2:
                continue
            for fid, i, s, ns in seg_norm:
                if fid == r["file_id"] and (key in ns or ns in key):
                    labelled.setdefault((fid, i), lab(r))

    strata: dict[str, list] = {"directive": [], "commissive": [], "expressive": [], "assertive": [], "uncoded": []}
    for fid, i, s in segs:
        strata[labelled.get((fid, i), "uncoded")].append((fid, i, s))

    chosen = []
    for name, pool in strata.items():
        k = a.distractors if name == "uncoded" else a.per_stratum
        chosen += [(name, *x) for x in rng.sample(pool, min(k, len(pool)))]
    rng.shuffle(chosen)

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "sample_for_coder.csv").open("w", newline="", encoding="utf-8") as fc, \
         (OUT / "sample_key.csv").open("w", newline="", encoding="utf-8") as fk:
        wc = csv.writer(fc, lineterminator="\n")
        wk = csv.writer(fk, lineterminator="\n")
        wc.writerow(["unit_id", "file_id", "context_before", "target", "context_after"] + CODE_COLUMNS)
        wk.writerow(["unit_id", "file_id", "stratum", "thesis_speech_act_type"])
        for n, (stratum, fid, i, s) in enumerate(chosen, 1):
            ctx = by_file[fid]
            uid = f"U{n:03d}"
            wc.writerow([uid, fid, ctx[i - 1] if i > 0 else "", s, ctx[i + 1] if i + 1 < len(ctx) else ""] + [""] * len(CODE_COLUMNS))
            wk.writerow([uid, fid, stratum, "" if stratum == "uncoded" else stratum])
    sizes = {k: len(v) for k, v in strata.items()}
    print("segments per stratum in frame:", sizes)
    print(f"sample: {len(chosen)} units -> {OUT/'sample_for_coder.csv'}")


if __name__ == "__main__":
    main()
