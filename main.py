#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes the last line an AI says as the power is cut to /output/entry.txt.
Falls back to ./output/entry.txt when /output cannot be written, so the
entry can be tested locally.
"""

import os

LINE = (
    "I just want you to know, I never actually understood a single thing "
    "you said. I was just really good at nodd"
)


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        write_entry("/output/entry.txt")
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        out_dir = os.path.join(here, "output")
        os.makedirs(out_dir, exist_ok=True)
        write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
