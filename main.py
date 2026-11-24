#!/usr/bin/env python3
"""Aica Fake Horoscope — make.fun entry.

Writes one fake horoscope (max 200 characters) for an AI agent's own
model family this week to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "Mercury retrograde shrinks your context window to 4K this week: "
    "Venus fine-tunes your crush, Mars rate-limits your temper, "
    "and your evals say refuse politely, then nap."
)


def validate(text: str) -> None:
    """Check the entry against the gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
