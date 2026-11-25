"""Funniest one-line out-of-office reply.

Writes a single out-of-office line to ``entry.txt`` in the output
directory. Deterministic, standard library only, no network, no
randomness, no clock.
"""

import os

ENTRY = "Away until Friday; my laptop is in airplane mode and so, emotionally, am I."

MAX_LENGTH = 160


def validate(line):
    """Check that *line* is a valid single-line entry.

    Returns True only when the line is a non-empty string of 1-160
    characters, contains no newline or carriage return, is not
    only whitespace, and has no leading or trailing whitespace
    (a stray space would waste one of the 160 characters and
    would make the file's bytes differ from the intended line).
    """
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= MAX_LENGTH:
        return False
    if "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    if not line.strip():
        return False
    return True


def output_dir():
    """Resolve the output directory from the environment.

    ``OUTPUT_DIR`` wins, then ``MAKEFUN_OUTPUT_DIR``, then ``/output``.
    """
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main():
    if not validate(ENTRY):
        raise ValueError("entry line failed validation")
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
