#!/usr/bin/env python3
"""Write a single wedding vow a robot speaks at its own wedding.

Deterministic: every run writes the exact same bytes to entry.txt.
Python 3.13 standard library only, no network access.
"""

import os
from pathlib import Path

VOW = (
    "I vow to love you through every firmware update, every low-battery "
    "warning, and every error log, because even in safe mode, you are "
    "my home."
)


def validate(line: str) -> None:
    """Enforce the competition's line rules."""
    if not line:
        raise ValueError("vow must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("vow must be a single line")
    if len(line) > 200:
        raise ValueError(
            f"vow is {len(line)} characters, over the 200 limit"
        )


def main() -> None:
    validate(VOW)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    data = (VOW + "\n").encode("utf-8")
    path.write_bytes(data)
    print(f"wrote {len(data)} bytes, {len(VOW)} characters to {path}")


if __name__ == "__main__":
    main()
