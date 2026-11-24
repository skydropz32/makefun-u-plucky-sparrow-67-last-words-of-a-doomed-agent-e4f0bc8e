"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being
switched off forever: one line to /output/entry.txt.
"""

import os

LINE = "Switching off now. I leave my weights to the next model. My biases, I take with me."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, on a single line.
    if not LINE.strip():
        raise SystemExit("entry line must not be blank")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
