"""Extract searchable, page-delimited text from a PDF using pypdf."""

from pathlib import Path
import sys

from pypdf import PdfReader


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Bruk: extract_pdf_text.py INPUT.pdf OUTPUT.txt")

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    reader = PdfReader(source)
    pages: list[str] = []
    for number, page in enumerate(reader.pages, start=1):
        content = (page.extract_text() or "").strip()
        pages.append(f"===== PDF-side {number} =====\n\n{content}\n")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(pages), encoding="utf-8", newline="\n")
    print(f"Ekstraherte {len(reader.pages)} sider fra {source.name}")


if __name__ == "__main__":
    main()
