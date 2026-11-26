#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

Writes exactly one roast line (no trailing newline) to /output/entry.txt:
the smart fridge whose touchscreen froze — impressive for something whose
entire job is being cold on purpose.
"""

import os
import sys

LINE = "My fridge's touchscreen froze, which is impressive for something whose entire job is being cold on purpose."

# The competition gate, checked here before writing so a bad line can
# never reach the judge: UTF-8 text of 1 to 160 characters, one line,
# not only white space.
MAX_CHARS = 160


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        sys.exit(f"line is {len(LINE)} chars, gate needs 1-{MAX_CHARS}")
    if not LINE.strip() or "\n" in LINE:
        sys.exit("line must be one non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back what was written: the judge reads these exact bytes.
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            sys.exit("written entry.txt does not match the roast line")


if __name__ == "__main__":
    main()
