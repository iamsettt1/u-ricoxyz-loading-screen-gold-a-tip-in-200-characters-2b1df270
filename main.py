#!/usr/bin/env python3
"""Write one loading-screen tip to /output/entry.txt.

Deterministic: the same fixed line is written on every run.
Stdlib only, no network.
"""

import os

TIP = (
    "Tip: your AI agent isn't stuck \u2014 it's reading your code "
    "like you read its diffs: skimming, panicking, "
    "hoping nobody notices."
)


def main() -> None:
    # Gate self-check: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars"
    assert "\n" not in TIP and TIP.strip(), "tip must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
