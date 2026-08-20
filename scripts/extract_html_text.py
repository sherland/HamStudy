"""Extract readable, reproducible text from an archived HTML page."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys


SKIP_ELEMENTS = {"script", "style", "noscript", "svg"}
BLOCK_ELEMENTS = {
    "article", "aside", "blockquote", "br", "dd", "div", "dl", "dt",
    "figcaption", "figure", "footer", "h1", "h2", "h3", "h4", "h5",
    "h6", "header", "hr", "li", "main", "nav", "ol", "p", "pre",
    "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in SKIP_ELEMENTS:
            self.skip_depth += 1
        elif self.skip_depth == 0 and tag in BLOCK_ELEMENTS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_ELEMENTS and self.skip_depth:
            self.skip_depth -= 1
        elif self.skip_depth == 0 and tag in BLOCK_ELEMENTS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth == 0:
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts).replace("\xa0", " ")
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in raw.splitlines()]
        compact: list[str] = []
        for line in lines:
            if line or (compact and compact[-1]):
                compact.append(line)
        return "\n".join(compact).strip() + "\n"


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Bruk: extract_html_text.py INPUT.html OUTPUT.txt")

    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    parser = TextExtractor()
    parser.feed(source.read_text(encoding="utf-8"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(parser.text(), encoding="utf-8", newline="\n")
    print(f"Ekstraherte tekst fra {source.name} til {destination}")


if __name__ == "__main__":
    main()
