"""Entry program for "How Many Tabs Do You Have Open?".

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.
The entry is a single number, digits only.
"""

import os
import sys

ENTRY = "87"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
