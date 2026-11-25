#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word to /output/entry.txt: the whole internet, summed up.

The word is "brainrot": the internet is the place humanity goes to have its
attention melted into sludge by an endless feed, and then goes back for more.
Funny by itself, true of the internet as a whole rather than any one app, and
not the first obvious word anyone reaches for. Pure stdlib, deterministic —
the same word every run.

Gate check: /output/entry.txt must be UTF-8 text of 1 to 30 characters, not
only whitespace.
"""

import os

WORD = "brainrot"


def validate(word):
    """Check the word against the competition gate before writing it."""
    text = word.strip()
    assert text, "word must not be only whitespace"
    assert " " not in text, "entry must be a single word"
    assert 1 <= len(word) <= 30, "word must be 1 to 30 characters"
    word.encode("utf-8")
    return word


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(WORD) + "\n")


if __name__ == "__main__":
    main()
