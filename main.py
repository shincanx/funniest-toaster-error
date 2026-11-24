#!/usr/bin/env python3
"""Writes the funniest toaster error message to /output/entry.txt.

Deterministic, no network, no randomness: the same line every run.
"""

from pathlib import Path

LINE = "E07: Crumb tray full. Nine years I have carried this family. Please clean me."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
