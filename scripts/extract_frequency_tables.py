"""Extract the two licence-class frequency tables from archived Lovdata HTML."""

import csv
from pathlib import Path
import re
import sys

from bs4 import BeautifulSoup


FIELDS = [
    "frekvens_fra",
    "frekvens_til",
    "enhet",
    "status",
    "maks_utgangseffekt_w",
    "maks_bandbredde",
    "spesielle_vilkar",
    "kilde",
    "kontrollert_dato",
]


def text(element) -> str:
    return " ".join(element.get_text(" ", strip=True).split())


def parse_table(table, source_section: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for row in table.select("tr")[1:]:
        cells = [text(cell) for cell in row.find_all(["th", "td"], recursive=False)]
        if len(cells) != 6:
            raise ValueError(f"Forventet 6 celler, fant {len(cells)}: {cells}")
        frequency_range, unit, status, power, bandwidth, conditions = cells
        limits = re.split(r"\s*[–-]\s*", frequency_range, maxsplit=1)
        if len(limits) != 2:
            raise ValueError(f"Kan ikke dele frekvensområde: {frequency_range}")
        records.append(
            {
                "frekvens_fra": limits[0],
                "frekvens_til": limits[1],
                "enhet": unit,
                "status": status,
                "maks_utgangseffekt_w": power,
                "maks_bandbredde": bandwidth,
                "spesielle_vilkar": conditions,
                "kilde": source_section,
                "kontrollert_dato": "2026-08-20",
            }
        )
    return records


def write_csv(destination: Path, records: list[dict[str, str]]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Bruk: extract_frequency_tables.py FORSKRIFT.html")

    source = Path(sys.argv[1])
    soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
    frequency_tables = []
    for table in soup.select("#documentBody table"):
        first_row = table.select_one("tr")
        if first_row and text(first_row).startswith("Frekvensbånd"):
            frequency_tables.append(table)

    if len(frequency_tables) != 2:
        raise ValueError(f"Forventet 2 frekvenstabeller, fant {len(frequency_tables)}")

    limited = parse_table(frequency_tables[0], "REG-2026 § 5")
    full = parse_table(frequency_tables[1], "REG-2026 § 5a")
    if len(limited) != 11 or len(full) != 38:
        raise ValueError(
            f"Uventet radantall: begrenset={len(limited)}, full={len(full)}"
        )

    write_csv(Path("data/frekvensband-begrenset-lisens.csv"), limited)
    write_csv(Path("data/frekvensband-full-lisens.csv"), full)
    print(f"Skrev {len(limited)} begrensede og {len(full)} fulle lisensrader")


if __name__ == "__main__":
    main()
