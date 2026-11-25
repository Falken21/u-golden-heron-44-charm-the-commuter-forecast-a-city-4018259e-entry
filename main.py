#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Snoozeburg to /output/entry.txt, with no trailing
newline. Snoozeburg keeps broadcast-forecast rhythm -- fog, sunshine,
a light breeze -- and one concrete detail of commuter life: the 8:04
train, running twenty minutes late, just like its passengers.
"""

import os

MAX_CHARS = 140

ENTRY = (
    "Snoozeburg: fog until 8, then sunshine with a light breeze. "
    "The 8:04 is running twenty minutes late \u2014 but so are you, "
    "so it evens out."
)


def entry_text() -> str:
    """Return the forecast line, checked against the gate's cap."""
    assert 0 < len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    return ENTRY


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry_text())


if __name__ == "__main__":
    main()
