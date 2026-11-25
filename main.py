"""Worst App Idea Ever Pitched - angle 2: Doorknob.

The program writes a single-sentence pitch for the worst app
imaginable to /output/entry.txt. The pitch must stay within the
gate: 1 to 240 characters of UTF-8 text, not only whitespace.
"""

import os

PITCH = (
    "Doorknob is the world's first app that locks your front door "
    "from the inside while you're outside, then charges $9.99 a month "
    "to knock politely on your behalf and ask whoever lives there "
    "now to let you back in."
)

MIN_CHARS = 1
MAX_CHARS = 240


def build_pitch():
    """Return the pitch, trimmed to one clean sentence."""
    text = " ".join(PITCH.split())
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "pitch must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(text))
        )
    # A sentence ends at a period followed by a space or end of text;
    # a period inside a number such as $9.99 is not a sentence end.
    terminators = sum(
        1
        for i, ch in enumerate(text)
        if ch == "." and (i + 1 == len(text) or text[i + 1] == " ")
    )
    if terminators != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    return text


def main():
    text = build_pitch()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read().decode("utf-8")
    if written != text:
        raise ValueError("entry.txt does not match the pitch")


if __name__ == "__main__":
    main()
