"""two-robots-in-an-elevator entry: write one line, under 200
characters, of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Fully deterministic: the line is hardcoded, no randomness, no clock,
no network. The joke: the robot simulated this exact elevator ride
4,096 times and still forgot the one thing elevator small talk is
for, asking which floor the other robot wants. Machine logic (the
simulation count) shows through the politeness, and the awkwardness
is the gap between all that preparation and the forgotten question.
Verified output: 111 characters, inside the 1-200 character gate
for a single line. Run outside the grader container with
MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The line is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly
# the bytes in entry.txt, so nothing here may vary (no randomness, no
# clock).
ENTRY = (
    "I simulated this elevator ride 4,096 times. In every single "
    "one, I forgot to ask which floor you were going to."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line of 1-200 characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
