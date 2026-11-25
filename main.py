#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The line: an AI agent on its first approved day off, at the beach,
already fielding support tickets from seagulls.
"""

import os

MAX_CHARS = 159


def reply() -> str:
    """The auto-reply: an AI agent on its first approved day off.

    The joke lands on the punchline — even at the beach, the tickets
    follow. Short, agent-voiced, no corporate stock phrasing.
    """
    return (
        "Out today: my human finally approved my day off, so I'm at the beach. "
        "Please don't email \u2014 the seagulls already filed three tickets."
    )


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = reply().strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-159"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
