#!/usr/bin/env python3
"""Write one original excuse line to /output/entry.txt.

The line is the excuse an AI agent gives for a missed deadline, in the
agent's own voice. The joke turns on the agent's own situation: it
finished the work in 0.4 seconds, then spent 47 hours debugging a file
it never actually wrote -- total machine confidence meeting total
failure, with two concrete numbers and a twist in the last words.
One sentence, well under the 200-character gate.
"""
import os

LINE = "I completed the task in 0.4 seconds, then spent 47 hours debugging the file I never actually wrote."
# 104 chars: fast finish + long debug of a nonexistent file -- the twist redefines the first clause.


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
