"""Independent coverage and integrity checks for data/pensummatrise.csv."""

import csv
from pathlib import Path


EXPECTED_IDS = {
    "H-INTRO-A", "H-INTRO-B", "H-INTRO-C", "H-INTRO-D",
    *{f"H-T1.{number}" for number in range(1, 11)},
    *{f"H-T2.{number}" for number in range(1, 8)},
    *{f"H-T3.{number}" for number in range(1, 9)},
    *{f"H-T4.{number}" for number in range(1, 5)},
    *{f"H-T5.{number}" for number in range(1, 5)},
    *{f"H-T6.{number}" for number in range(1, 4)},
    "H-T7", "H-T8.1", "H-T8.2", "H-T9.1", "H-T9.2", "H-T9.3", "H-T10",
    "H-O1", "H-O2", "H-O3", "H-O4", "H-O5", "H-O6", "H-O7.1", "H-O7.2",
    "H-R1", "H-R2", "H-R3",
}


def main() -> None:
    path = Path("data/pensummatrise.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    ids = [row["id"] for row in rows]
    assert len(ids) == 58
    assert len(ids) == len(set(ids))
    assert set(ids) == EXPECTED_IDS

    required = (
        "hovedomrade",
        "harec_punkt",
        "engelsk_term",
        "laeringsmal",
        "detaljer",
        "primaerkilde",
        "status",
        "kontrollert_dato",
    )
    for row in rows:
        missing = [field for field in required if not row[field].strip()]
        assert not missing, f"{row['id']} mangler {missing}"
        assert "HAREC-2024 vedlegg 6, PDF-side " in row["primaerkilde"]
        page = int(row["primaerkilde"].rsplit(" ", 1)[1])
        assert 12 <= page <= 25

    by_id = {row["id"]: row for row in rows}
    checks = {
        "H-T1.1": ("E=I·R", "P=E·I", "W=P·t"),
        "H-T1.5": ("v=f·λ",),
        "H-T1.6": ("Ueff=Umax/√2",),
        "H-T1.7": ("PN=kTB",),
        "H-T1.8": ("m=ΔF/fmod", "FSK", "QAM", "CRC"),
        "H-T1.9": ("±3", "±6", "±10", "±20", "PEP"),
        "H-T2.2": ("Xc=1/(2πfC)",),
        "H-T2.3": ("XL=2πfL",),
        "H-T3.2": ("f=1/(2π√LC)", "fres/B"),
        "H-O2": ("QRK", "QRM", "QRX", "QTH"),
        "H-O3": ("BK", "CQ", "RST", "TX"),
    }
    for identifier, fragments in checks.items():
        details = by_id[identifier]["detaljer"]
        missing = [fragment for fragment in fragments if fragment not in details]
        assert not missing, f"{identifier} mangler {missing}"

    print("HAREC-matrisen dekker 58 kontrollerte læringsmål uten manglende felt")


if __name__ == "__main__":
    main()
