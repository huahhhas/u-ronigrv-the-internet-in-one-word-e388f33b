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
import sys

WORD = "brainrot"


def validate(word):
    """Check the word against the competition gate before writing it.

    Raises ValueError with a plain message when the word fails the gate,
    so a bad word is reported instead of tripping an assertion.
    """
    text = word.strip()
    if not text:
        raise ValueError("word must not be only whitespace")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word")
    if not 1 <= len(text) <= 30:
        raise ValueError("word must be 1 to 30 characters")
    text.encode("utf-8")
    return text


def main():
    """Write the word, reporting a failed gate or write on stderr."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(validate(WORD) + "\n")
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
