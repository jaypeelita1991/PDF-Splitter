#!/usr/bin/env python3
"""Split a PDF into one file per page.

Usage:
    python split_pdf.py input.pdf [-o OUTPUT_DIR]

Requires: pip install pypdf
"""

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def split_pdf(input_path: Path, output_dir: Path) -> int:
    reader = PdfReader(str(input_path))
    if reader.is_encrypted:
        reader.decrypt("")

    output_dir.mkdir(parents=True, exist_ok=True)
    total = len(reader.pages)
    width = len(str(total))

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out_file = output_dir / f"{input_path.stem}_page_{i:0{width}d}.pdf"
        with open(out_file, "wb") as f:
            writer.write(f)
        print(f"Wrote {out_file}")

    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a PDF into one file per page.")
    parser.add_argument("input", type=Path, help="Path to the PDF to split")
    parser.add_argument(
        "-o", "--output-dir", type=Path,
        help="Folder for the page files (default: <input name>_pages next to the input)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        sys.exit(f"Error: file not found: {args.input}")

    output_dir = args.output_dir or args.input.with_name(f"{args.input.stem}_pages")
    count = split_pdf(args.input, output_dir)
    print(f"Done: {count} page(s) saved to {output_dir}")


if __name__ == "__main__":
    main()
