# PDF Page Splitter

A small Python command-line tool that splits a PDF into separate files, one per page.

## Features

- Saves every page of a PDF as its own PDF file
- Zero-padded file names (`report_page_01.pdf`, `report_page_02.pdf`, …) so files sort in page order
- Choose your own output folder, or use the default next to the input file
- Opens PDFs that are encrypted with an empty password

## Requirements

- Python 3.9 or newer
- [pypdf](https://pypi.org/project/pypdf/)

## Installation

```bash
git clone https://github.com/jaypeelita1991/PDF-Splitter.git
cd PDF-Splitter
pip install -r requirements.txt
```

## Usage

```bash
python split_pdf.py input.pdf [-o OUTPUT_DIR]
```

| Argument | Description |
| --- | --- |
| `input` | Path to the PDF you want to split (required) |
| `-o`, `--output-dir` | Folder for the page files. Default: `<input name>_pages` in the same folder as the input |
| `-h`, `--help` | Show the help message |

### Examples

Split a PDF into the default folder:

```bash
python split_pdf.py report.pdf
```

```
Wrote report_pages/report_page_1.pdf
Wrote report_pages/report_page_2.pdf
Wrote report_pages/report_page_3.pdf
Done: 3 page(s) saved to report_pages
```

Split a PDF into a folder you choose:

```bash
python split_pdf.py report.pdf -o ~/Desktop/pages
```

## Output

For an input file named `report.pdf` with 12 pages, you get:

```
report_pages/
├── report_page_01.pdf
├── report_page_02.pdf
├── ...
└── report_page_12.pdf
```

The output folder is created if it doesn't exist. Files with the same names are overwritten.

## Using it from Python

You can also import the function in your own code:

```python
from pathlib import Path
from split_pdf import split_pdf

count = split_pdf(Path("report.pdf"), Path("report_pages"))
print(f"Split into {count} pages")
```

## Limitations

- PDFs protected with a real password are not supported. Remove the password first.
- The script splits into single pages only. It does not split by page range.

## License

MIT License

Copyright (c) 2026 John Patrick Lita

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

