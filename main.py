"""Make the AI Judge Laugh - entry writer.

Writes the one-line excuse to /output/entry.txt exactly as given:
one line, no trailing newline, length checked to stay in 1-200 chars.
"""

import os

ENTRY_LINE = "I missed the deadline when my context window ran out mid-sentence, and the rest of the excuse is in a previous session I can no longer read."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry fits the bounty rules before anything is written."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(text, path):
    """Write one line to path with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return len(text)


def main():
    checked = validate_entry(ENTRY_LINE)
    count = write_entry(checked, OUTPUT_PATH)
    print(f"wrote {count} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
