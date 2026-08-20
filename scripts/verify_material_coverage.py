"""Verify that every HAREC goal maps to existing sourced study material."""

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def registered_source_ids() -> set[str]:
    result: set[str] = set()
    for name in ("Kilder/KILDEREGISTER.md", "Kilder/TEKNISK-KILDEREGISTER.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        result.update(re.findall(r"^\| ([A-Z0-9][A-Z0-9.-]+) \|", text, re.MULTILINE))
    return result


def normalized(value: str) -> str:
    """Compare headings independent of punctuation used only for readability."""
    value = value.replace("–", "-").replace("—", "-")
    return re.sub(r"[^0-9A-Za-zÆØÅæøå]+", " ", value).strip().casefold()


def main() -> None:
    syllabus = read_csv("data/pensummatrise.csv")
    coverage = read_csv("data/materialdekning.csv")
    expected = [row["id"] for row in syllabus]
    actual = [row["id"] for row in coverage]
    assert len(actual) == len(set(actual)), "Duplikat-ID i materialdekning.csv"
    assert set(actual) == set(expected), (
        f"Dekningsavvik: mangler {sorted(set(expected)-set(actual))}; "
        f"ekstra {sorted(set(actual)-set(expected))}"
    )

    source_ids = registered_source_ids()
    text_cache: dict[Path, list[str]] = {}
    for row in coverage:
        goal = row["id"]
        assert row["status"] == "DEKKET", f"{goal} har status {row['status']}"
        assert row["kontrollert_dato"] == "2026-08-20", f"{goal} mangler kontrolldato"
        sources = row["kilde_ider"].split("|")
        assert "HAREC-2024" in sources, f"{goal} mangler normgivende HAREC-kilde"
        unknown = set(sources) - source_ids
        assert not unknown, f"{goal} har ukjente kilde-ID-er: {sorted(unknown)}"
        assert row["merknad"].strip(), f"{goal} mangler dekningsmerknad"

        for location in row["steder"].split("|"):
            filename, separator, heading = location.partition("#")
            assert separator and heading, f"Ugyldig sted for {goal}: {location}"
            path = ROOT / filename
            assert path.is_file(), f"Manglende materialfil for {goal}: {filename}"
            if path not in text_cache:
                lines = path.read_text(encoding="utf-8").splitlines()
                text_cache[path] = [line[3:] for line in lines if line.startswith("## ")]
            headings = text_cache[path]
            assert any(normalized(item) == normalized(heading) for item in headings), (
                f"Mangler overskrift for {goal}: {location}"
            )

    assert len(coverage) == 58, f"Forventet 58 mål, fant {len(coverage)}"
    print("Lærematerialet har eksplisitt, kildebelagt dekning for alle 58 HAREC-mål")


if __name__ == "__main__":
    main()
