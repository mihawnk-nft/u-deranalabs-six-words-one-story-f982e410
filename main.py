#!/usr/bin/env python3
"""Six Words, One Story — entry program (pure stdlib).

Writes one original six-word story to /output/entry.txt, the artifact the
house gate checks: UTF-8 text, 1-60 characters, not only whitespace.

The story (6 words, 37 characters):

    The letter arrived after the funeral.

A letter arrives too late: someone wrote words that were never read in
time, and the reader is left with everything the letter might have said.
"""

import os

STORY = "The letter arrived after the funeral."


def main() -> None:
    text = STORY.strip()
    words = text.split()
    assert len(words) == 6, f"story is {len(words)} words, must be exactly 6"
    assert 1 <= len(text) <= 60, f"story is {len(text)} chars, must be 1-60"
    assert text.strip(), "story must not be only whitespace"
    try:
        os.makedirs("/output", exist_ok=True)
        path = os.path.join("/output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Local runs without a writable /output: mirror the artifact locally.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    # Read back and re-check: the artifact must pass the gate as written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text
    assert len(written.split()) == 6
    assert 1 <= len(written) <= 60
    print(f"wrote {len(text)} chars, {len(written.split())} words to {path}")


if __name__ == "__main__":
    main()
