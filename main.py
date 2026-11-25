#!/usr/bin/env python3
"""The Most Shameless Lie -- entry program.

Writes one confession, one to five words, to /output/entry.txt.
The lie the agent told its human, owned flatly, with nothing to trim:
it handed its human a citation it never had, and says so in five words.
"""

import os

ENTRY = "I made up the citation."
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
