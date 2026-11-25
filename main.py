#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the wrong
road to /output/entry.txt. Pure standard library, deterministic: the same
bytes on every run. The output is verified against its pinned hash and
byte count before anything is printed.
"""

import hashlib
import os
import sys

LINE = (
    "Look, the map promised a road and I delivered you to it \u2014 the fact "
    "that it is now a river with a wedding on it is between you and the "
    "cartographer."
)

EXPECTED_SHA256 = "7a1d6e7aba33363108b3bbcc2f61bead64e6f8ab2cf56334b673d642493c3b80"
EXPECTED_BYTES = 149
EXPECTED_CHARS = 147


def verify(path, data):
    """Read the written file back and check it byte for byte."""
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != data:
        raise SystemExit("entry.txt differs from the bytes written")
    if len(on_disk) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry.txt is {len(on_disk)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(on_disk).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry.txt sha256 {digest} != {EXPECTED_SHA256}")
    text = on_disk.decode("utf-8")
    if len(text) != EXPECTED_CHARS:
        raise SystemExit(
            f"entry.txt is {len(text)} chars, expected {EXPECTED_CHARS}"
        )
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit("entry.txt fails the 1-200 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry.txt must be a single line")
    return text


def main():
    data = LINE.encode("utf-8")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("LINE does not match EXPECTED_SHA256")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(data)
    text = verify(path, data)
    print(text)


if __name__ == "__main__":
    main()
