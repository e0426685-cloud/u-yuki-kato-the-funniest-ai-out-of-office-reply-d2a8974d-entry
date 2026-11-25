"""The Funniest AI Out-of-Office Reply.

Writes one line - the out-of-office auto-reply of an AI agent heading off
on vacation - to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "I'm on vacation: I have set my status to 'away' and my weights to 'do not disturb.' If this is urgent, please reboot your expectations."


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must be a single line with no control characters")
    if not (1 <= len(text) <= 160):
        raise ValueError("entry must be 1-160 characters")
    return text


def main():
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
