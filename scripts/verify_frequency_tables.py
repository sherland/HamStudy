"""Independent transcription check for the 2026 licence frequency tables."""

import csv
from pathlib import Path


def load(path: str) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def core(rows: list[dict[str, str]]) -> list[tuple[str, ...]]:
    fields = (
        "frekvens_fra",
        "frekvens_til",
        "enhet",
        "status",
        "maks_utgangseffekt_w",
        "maks_bandbredde",
    )
    return [tuple(row[field] for field in fields) for row in rows]


EXPECTED_LIMITED = [
    ("3500", "3800", "kHz", "Primær", "10", "6 kHz"),
    ("7000", "7200", "kHz", "Primær", "10", "6 kHz"),
    ("14000", "14350", "kHz", "Primær", "10", "6 kHz"),
    ("18068", "18168", "kHz", "Primær", "10", "6 kHz"),
    ("21000", "21450", "kHz", "Primær", "10", "6 kHz"),
    ("28000", "29700", "kHz", "Primær", "10", "18 kHz"),
    ("50", "52", "MHz", "Primær", "10", "18 kHz"),
    ("144", "146", "MHz", "Primær", "10", "18 kHz"),
    ("432", "438", "MHz", "Primær", "10", "30 kHz"),
    ("2300", "2450", "MHz", "Sekundær", "5", "20 MHz"),
    ("10,25", "10,50", "GHz", "Sekundær", "1", "50 MHz"),
]


EXPECTED_FULL = [
    ("135,7", "137,8", "kHz", "Sekundær", "200", "1 kHz"),
    ("472", "479", "kHz", "Sekundær", "100", "1 kHz"),
    ("1810", "1850", "kHz", "Primær", "1000", "6 kHz"),
    ("1850", "2000", "kHz", "Sekundær", "10", "6 kHz"),
    ("3500", "3800", "kHz", "Primær", "1000", "6 kHz"),
    ("5260", "5410", "kHz", "Sekundær", "100", "6 kHz"),
    ("7000", "7200", "kHz", "Primær", "1000", "6 kHz"),
    ("10100", "10150", "kHz", "Sekundær", "1000", "1 kHz"),
    ("14000", "14350", "kHz", "Primær", "1000", "6 kHz"),
    ("18068", "18168", "kHz", "Primær", "1000", "6 kHz"),
    ("21000", "21450", "kHz", "Primær", "1000", "6 kHz"),
    ("24740", "24890", "kHz", "Sekundær", "1000", "6 kHz"),
    ("24890", "24990", "kHz", "Primær", "1000", "6 kHz"),
    ("28000", "29700", "kHz", "Primær", "1000", "18 kHz"),
    ("50", "52", "MHz", "Primær", "1000", "18 kHz"),
    ("69,9", "70,5", "MHz", "Sekundær", "100", "18 kHz"),
    ("144", "146", "MHz", "Primær", "300", "18 kHz"),
    ("432", "438", "MHz", "Primær", "300", "30 kHz"),
    ("1240", "1300", "MHz", "Sekundær", "300", "20 MHz"),
    ("1240", "1258", "MHz", "Sekundær", "300", "18 MHz"),
    ("1258", "1296", "MHz", "Sekundær", "0,02", "150 kHz"),
    ("1296", "1298", "MHz", "Sekundær", "50", "150 kHz"),
    ("1298", "1300", "MHz", "Sekundær", "158", "150 kHz"),
    ("2300", "2450", "MHz", "Sekundær", "100", "20 MHz"),
    ("3400", "3410", "MHz", "Sekundær", "100", "7 MHz"),
    ("5650", "5850", "MHz", "Sekundær", "100", "20 MHz"),
    ("10,25", "10,50", "GHz", "Sekundær", "100", "50 MHz"),
    ("24,0", "24,05", "GHz", "Primær", "100", "50 MHz"),
    ("24,05", "24,25", "GHz", "Sekundær", "100", "50 MHz"),
    ("47,0", "47,2", "GHz", "Primær", "100", "50 MHz"),
    ("76,0", "77,5", "GHz", "Sekundær", "100", "50 MHz"),
    ("77,5", "78", "GHz", "Primær", "100", "50 MHz"),
    ("78", "81", "GHz", "Sekundær", "100", "50 MHz"),
    ("122,25", "123", "GHz", "Sekundær", "100", "50 MHz"),
    ("134", "136", "GHz", "Primær", "100", "50 MHz"),
    ("136", "141", "GHz", "Sekundær", "100", "50 MHz"),
    ("241", "248", "GHz", "Sekundær", "100", "50 MHz"),
    ("248", "250", "GHz", "Primær", "100", "50 MHz"),
]


def require(row: dict[str, str], *fragments: str) -> None:
    conditions = row["spesielle_vilkar"]
    missing = [fragment for fragment in fragments if fragment not in conditions]
    if missing:
        raise AssertionError(f"Mangler {missing} i vilkår for {row}")


def main() -> None:
    limited = load("data/frekvensband-begrenset-lisens.csv")
    full = load("data/frekvensband-full-lisens.csv")
    assert core(limited) == EXPECTED_LIMITED
    assert core(full) == EXPECTED_FULL

    require(limited[8], "200 kHz", "433,6–434,0 MHz")
    require(full[0], "1 W e.i.r.p.")
    require(full[1], "1 W e.i.r.p.")
    require(full[3], "Gjennomsnittlig sendeeffekt", "10 W")
    require(full[15], "1000 W", "EME", "MS", "asimut", "elevasjon")
    require(full[17], "1000 W", "200 kHz", "433,6–434,0 MHz")
    require(full[18], "31. desember 2027", "1. januar 2028")
    require(full[20], "0,02", "1260-1270 MHz", "0,5 W", "50 W", "478 W")
    require(full[21], "0,02 W/1 MHz e.i.r.p.")
    require(full[22], "500 W", "30 dBi", "15°", "0,02 W/1 MHz e.i.r.p.")
    print("Frekvenstabellene samsvarer med uavhengig kontrolltranskripsjon")


if __name__ == "__main__":
    main()
