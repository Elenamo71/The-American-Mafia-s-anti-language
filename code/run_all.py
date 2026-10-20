"""Run every reproduction step in order. Usage: python code/run_all.py"""
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
STEPS = [
    ("Validate appendix examples against the transcripts", "validate_concordances.py", []),
    ("Corpus counts, wordlist, modal census", "corpus_frequencies.py", []),
    ("Chapter 8 inferential statistics", "stats_contingency.py", []),
    ("Figure 9.4 (as published)", "pay_collocation.py", ["--thesis"]),
    ("Intra-rater kappa (published figures)", "reliability.py", ["--demo"]),
]
for title, script, args in STEPS:
    print(f"\n=== {title} ({script}) ===")
    sys.argv = [script, *args]
    runpy.run_path(str(HERE / script), run_name="__main__")
