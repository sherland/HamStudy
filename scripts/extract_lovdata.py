"""Extract readable paragraphs and tables from archived Lovdata HTML.

Usage:
    python scripts/extract_lovdata.py INPUT.html OUTPUT.txt

The output is a reproducible aid for transcription and review. It does not
replace the archived HTML or the current consolidated text at lovdata.no.
"""

from pathlib import Path
import sys

from bs4 import BeautifulSoup


def clean(element) -> str:
    return " ".join(element.get_text(" ", strip=True).split())


def extract(source: Path) -> str:
    soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
    body = soup.select_one("#documentBody")
    if body is None:
        raise ValueError(f"Fant ikke #documentBody i {source}")

    lines: list[str] = []
    for heading in body.select("h2.paragrafHeader, h3.paragrafHeader"):
        paragraph = heading.find_parent("div", class_="paragraf")
        if paragraph is None:
            continue

        lines.extend((f"## {clean(heading)}", ""))
        for child in paragraph.find_all(recursive=False):
            if child.name in {"h2", "h3"} or "share-paragraf" in child.get("class", []):
                continue
            if child.name == "table":
                rows = child.find_all("tr")
                for row in rows:
                    cells = [clean(cell) for cell in row.find_all(["th", "td"], recursive=False)]
                    if cells:
                        lines.append(" | ".join(cells))
                lines.append("")
            else:
                text = clean(child)
                if text:
                    lines.extend((text, ""))

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Bruk: extract_lovdata.py INPUT.html OUTPUT.txt")
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(extract(source), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
