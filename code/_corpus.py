"""Shared helpers: load the corpus and normalise text for matching/counting.

The raw transcripts are never modified; normalisation happens in memory only.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "corpus" / "raw"
CONC = ROOT / "annotation" / "concordances"
RESULTS = ROOT / "data" / "results"

_APOS = str.maketrans({"’": "'", "‘": "'", "`": "'", "“": '"', "”": '"'})


def load_corpus() -> dict[str, str]:
    """Return {file_id: text} for every transcript in corpus/raw/."""
    return {p.stem: p.read_text(encoding="utf-8-sig") for p in sorted(RAW.glob("*.txt"))}


def tokens(text: str, split_clitics: bool = True) -> list[str]:
    """Lower-cased word tokens.

    split_clitics=True mirrors Sketch Engine / AntConc behaviour for English
    (I'm -> i + 'm), which is how the thesis pronoun counts were produced.
    """
    t = text.translate(_APOS).lower()
    if split_clitics:
        return re.findall(r"[a-z]+|'[a-z]+", t)
    return re.findall(r"[a-z]+(?:'[a-z]+)*", t)


def word_count(text: str) -> int:
    """Orthographic word count (clitics not split, numbers counted)."""
    return len(re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*|\d+(?:[.,]\d+)*", text))


def _norm(s: str, keep_bracket_content: bool) -> str:
    s = s.translate(_APOS).lower()
    s = re.sub(r"\[([a-z])\]", r"\1", s)            # [T]ell -> Tell
    s = re.sub(r"\[([^\]]*)\]", r" \1 " if keep_bracket_content else " ", s)
    s = re.sub(r"[^a-z0-9']+", " ", s).replace("'", "")
    return " ".join(s.split())


def locate(example: str, file_id: str, corpus_norm: dict[str, tuple[str, str]]) -> tuple[str, str]:
    """Check whether an appendix example occurs in the attributed transcript.

    Returns (status, other_file):
      exact      – the whole example occurs in the attributed file
      segments   – every segment between ellipses/dashes occurs there (elided quote)
      partial    – at least one segment occurs there
      other_file – not in the attributed file, but found verbatim in another file
      not_found  – not located (transcription variant, paraphrase, or text absent)
    """
    variants = {_norm(example, True), _norm(example, False)}
    segs_raw = [s for s in re.split(r"\.\.\.|…|—|--|\.\s|\?\s|!\s", example)]
    segs = [s for s in ({_norm(x, False) for x in segs_raw} | {_norm(x, True) for x in segs_raw}) if len(s.split()) >= 2]
    keep, drop = corpus_norm[file_id]
    hay = keep + " || " + drop
    if any(v and v in hay for v in variants):
        return "exact", ""
    core = [s for s in {_norm(x, False) for x in segs_raw} if len(s.split()) >= 2]
    if core and all(s in hay for s in core):
        return "segments", ""
    for other, (k, d) in corpus_norm.items():
        if other != file_id and any(v and (v in k or v in d) for v in variants):
            return "other_file", other
    if any(s in hay for s in segs):
        return "partial", ""
    return "not_found", ""


def corpus_normalised(corpus: dict[str, str]) -> dict[str, tuple[str, str]]:
    return {k: (_norm(v, True), _norm(v, False)) for k, v in corpus.items()}
