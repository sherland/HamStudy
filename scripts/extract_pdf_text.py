"""Extract searchable, page-delimited text from a PDF using pypdf."""

from pathlib import Path
import sys

from pypdf import PdfReader


def main() -> None:
    if len(sys.argv) not in (3, 5):
        raise SystemExit(
            "Bruk: extract_pdf_text.py INPUT.pdf OUTPUT.txt [FRA_SIDE TIL_SIDE]"
        )

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    reader = PdfReader(source)
    first = int(sys.argv[3]) if len(sys.argv) == 5 else 1
    last = int(sys.argv[4]) if len(sys.argv) == 5 else len(reader.pages)
    if not 1 <= first <= last <= len(reader.pages):
        raise SystemExit(f"Ugyldig sideintervall {first}–{last}; PDF har {len(reader.pages)} sider")
    pages: list[str] = []
    for number in range(first, last + 1):
        page = reader.pages[number - 1]
        content = (page.extract_text() or "").strip()
        pages.append(f"===== PDF-side {number} =====\n\n{content}\n")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(pages), encoding="utf-8", newline="\n")
    print(f"Ekstraherte PDF-side {first}–{last} fra {source.name}")


if __name__ == "__main__":
    main()
