"""Entry point for the news-image-20261119 bounty.

Copies the shipped front-page image (entry.png) to the output directory
given by MAKEFUN_OUTPUT_DIR (default /output). Standard library only:
no image generation, no network access, no third-party packages.

The image is drawn at build time by draw_news.py; this program only
verifies that entry.png is a complete, well-formed PNG and copies it
byte-for-byte, so both graded runs write identical bytes.

Exit codes: 0 on success, 1 if the image is missing or malformed.
"""

import os
import shutil
import struct
import sys

ENTRY = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _is_whole_png(data: bytes) -> bool:
    """Check the PNG signature and that the final chunk is IEND.

    Walks the chunk structure (length, type, data, CRC) from the start
    instead of trusting the file size or a fixed trailing byte string,
    so a truncated or garbage-appended file is rejected.
    """
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        return False
    pos = 8
    last_type = None
    while pos + 8 <= len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        chunk_type = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            return False
        last_type = chunk_type
        pos = end
    return pos == len(data) and last_type == b"IEND"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"error: cannot read {src}: {exc}", file=sys.stderr)
        return 1
    if not _is_whole_png(data):
        print("error: entry.png is not a complete PNG file "
              "(bad signature, truncated chunk, or missing IEND)",
              file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, ENTRY)
        shutil.copyfile(src, dst)
    except OSError as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
