"""Create a PDF containing an inclusive, 1-based page interval."""

from pathlib import Path
import sys

from pypdf import PdfReader, PdfWriter


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit(
            "Bruk: extract_pdf_pages.py INPUT.pdf OUTPUT.pdf FRA_SIDE TIL_SIDE"
        )

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    first = int(sys.argv[3])
    last = int(sys.argv[4])
    reader = PdfReader(source)
    if not 1 <= first <= last <= len(reader.pages):
        raise SystemExit(
            f"Ugyldig sideintervall {first}–{last}; PDF har {len(reader.pages)} sider"
        )

    writer = PdfWriter()
    for number in range(first, last + 1):
        writer.add_page(reader.pages[number - 1])

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as output:
        writer.write(output)
    print(
        f"Skrev PDF-side {first}–{last} fra {source.name} til {destination.name}"
    )


if __name__ == "__main__":
    main()
