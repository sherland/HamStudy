"""Verify local links and SVG figures used by the study material."""

import re
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
MATERIAL = ROOT / "Materiell"


def main() -> None:
    markdown_files = sorted(MATERIAL.glob("*.md"))
    assert len(markdown_files) == 10, (
        f"Forventet README + 9 kapitler, fant {len(markdown_files)}"
    )
    link_count = 0
    for document in markdown_files:
        text = document.read_text(encoding="utf-8")
        if document.name != "README.md":
            assert "## Kildegrunnlag" in text or "## Kildegrunnlag og rang" in text
            assert "Kontrolloppgaver" in text, f"Mangler kontrolloppgaver: {document}"
        for target in re.findall(r"!?\[[^]]*\]\(([^)]+)\)", text):
            target = target.strip("<>")
            if re.match(r"^(?:https?://|mailto:|#)", target):
                continue
            filename = unquote(target.split("#", 1)[0])
            assert (document.parent / filename).resolve().is_file(), (
                f"Brutt lokal lenke i {document.name}: {target}"
            )
            link_count += 1

    figures = sorted((MATERIAL / "figurer").glob("*.svg"))
    assert len(figures) >= 15, (
        f"Forventet minst 15 SVG-figurer, fant {len(figures)}"
    )
    for figure in figures:
        root = ElementTree.parse(figure).getroot()
        assert root.tag.endswith("svg"), f"Ikke gyldig SVG-rot: {figure}"

    print(
        f"Materialressurser kontrollert: {len(markdown_files)} Markdown-filer, "
        f"{len(figures)} SVG-figurer og {link_count} lokale lenker"
    )


if __name__ == "__main__":
    main()
