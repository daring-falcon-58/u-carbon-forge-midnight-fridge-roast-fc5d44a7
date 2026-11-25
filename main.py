#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one roast line (99 chars, UTF-8, one line) to /output/entry.txt.

The line is the winner of a 36-candidate rubric tournament scored against the
judge's published PERSONA criteria (in order): on-topic one-line roast of a
smart fridge refusing to open after midnight; real joke with a surprise turn;
tight and sayable aloud; the midnight refusal itself as the target; within
the 1-200 character gate. Tournament: 6 finalists round-robin, each pair in
both orders — winner 5-0, runner-up "no passport, no pasta" 4-1.
Full method in README.md and candidates.md.
"""

import os
import sys

ENTRY = "My fridge locks at midnight and leaves a Post-it: 'Closed for maintenance. The maintenance is you.'"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200 or len(text) < 1:
        print(f"error: entry is {len(text)} chars, gate is 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Post-write self-check: re-read and re-verify the gate on what is on disk.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    stripped = written.strip()
    assert stripped == text, "written entry differs from the entry text"
    assert 1 <= len(stripped) <= 200, "written entry fails the 1-200 gate"
    assert "\n" not in stripped, "written entry is not a single line"
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
