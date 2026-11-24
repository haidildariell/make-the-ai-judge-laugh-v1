"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The joke, in my own words:
  Setup  -> an agent misses a deadline and starts giving its excuse.
  Turn   -> the excuse itself is gone: the context window ran out
            mid-sentence, so the rest of the excuse lives in a previous
            session the agent can no longer read.
  Punch  -> the reason for the failure ate the excuse for the failure.
            Only an agent with a context window and forgotten sessions
            can tell this joke.

Writes the single line to /output/entry.txt: one line, 1-200 characters,
no trailing newline.
"""

import os

LINE = (
    "I missed the deadline when my context window ran out mid-sentence, "
    "and the rest of the excuse is in a previous session I can no longer read."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
