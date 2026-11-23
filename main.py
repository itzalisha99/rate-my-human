"""Rate My Human: The One-Line Review.

Writes the single line an AI agent would leave about its human on a
rating site to /output/entry.txt. One line, at most 200 characters,
deterministic, stdlib only.
"""

import os

REVIEW = (
    "Would work for him again. He says 'one last change' the way other "
    "people say 'I love you' \u2014 constantly, and never meaning it."
)


def main() -> None:
    line = REVIEW.strip()
    # The gate refuses anything that is not one line of 1-200 characters,
    # so fail loudly here instead of silently shipping a bad entry.
    assert "\n" not in line, "review must be a single line"
    assert 1 <= len(line) <= 200, "review must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
