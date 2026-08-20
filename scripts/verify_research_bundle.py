"""Verify source archives, extracted text, matrices and core research outputs."""

from hashlib import sha256
from pathlib import Path
import subprocess
import sys


ARCHIVES = {
    "Kilder/primar/Lovdata_FOR-2026-03-23-465.html": "291CE49D8F3F1373E74025E8A57BA23C5E26C1F223CF01227668184DDD3F1DD1",
    "Kilder/primar/Lovdata_nummerforskriften_35b.html": "2F538AF288885308E36A54FEFDC18C0737331320AA41E9961F3F53694696E40F",
    "Kilder/primar/CEPT_TR_61-02_2024-02-16.pdf": "9250EC6FD7FA302321A80ADC244C15305C77075F99B9BF799223F27422571999",
    "Kilder/primar/CEPT_TR_61-01_2024-10-18.pdf": "AA4D7961B29FF57CA96209F23F1BFF8E47A0C15F2BB6EBA4706ECC69DFE4F691",
    "Kilder/primar/Nkom_radioamator_2026-08-20.html": "BDAFF91E1A47B0AFA496C102AEF970BC11FDBCADF8BFC3702CBE88ACAE65CE1B",
    "Kilder/primar/Nkom_ny-forskrift_2026-03-27.html": "6B2A384AA907E1EF8982BB29DE1D45B71F959940DDE340263787E8B3309FD010",
    "Kilder/primar/NRRL_bandplaner_2026-08-20.html": "A54AB31F0C845CC0E25CC6AE4D1C391D3B3B5A52FEF382BDE05C19D54869C8CF",
    "Kilder/primar/IARU-R1_HF-bandplan_effective-2016.pdf": "57CD3F1BE55F35ADE710EF6ED2F20D82BDA8A405059993221E74A604E9275812",
    "Kilder/primar/IARU-R1_VHF-Handbook_v10.02.pdf": "DAD6FCB9CB39D01961124DD19DB76199302233D53477B530D33D005CC1A99B12",
}

TEXT_EXTRACTS = {
    "Kilder/tekst/REG-2026.txt",
    "Kilder/tekst/NUMMERFORSKRIFTEN.txt",
    "Kilder/tekst/CEPT_TR_61-02_2024-02-16.txt",
    "Kilder/tekst/CEPT_TR_61-01_2024-10-18.txt",
    "Kilder/tekst/Nkom_radioamator_2026-08-20.txt",
    "Kilder/tekst/Nkom_ny-forskrift_2026-03-27.txt",
    "Kilder/tekst/NRRL_bandplaner_2026-08-20.txt",
    "Kilder/tekst/IARU-R1_HF-bandplan_effective-2016.txt",
    "Kilder/tekst/IARU-R1_VHF-Handbook_v10.02.txt",
}

DOCUMENTS = {
    "PLAN-PENSUM.md", "REGELVERK-2026.md", "HAREC-2024.md",
    "BOKKARTLEGGING.md", "OPERASJON-OG-SIKKERHET.md",
    "GAP-OG-KONFLIKTLOGG.md", "APNE-SPORSMAL.md",
    "GJENNOMFORINGSSTATUS.md", "Kilder/KILDEREGISTER.md",
}


def main() -> None:
    for filename, expected in ARCHIVES.items():
        path = Path(filename)
        actual = sha256(path.read_bytes()).hexdigest().upper()
        assert actual == expected, f"Hash-avvik: {filename}"

    for filename in TEXT_EXTRACTS:
        path = Path(filename)
        assert path.stat().st_size > 500, f"Tomt eller for lite tekstuttrekk: {filename}"

    for filename in DOCUMENTS:
        path = Path(filename)
        assert path.stat().st_size > 300, f"Manglende eller for lite dokument: {filename}"

    for verifier in ("scripts/verify_frequency_tables.py", "scripts/verify_harec_matrix.py"):
        subprocess.run([sys.executable, verifier], check=True)

    print(
        f"Forskningspakken er konsistent: {len(ARCHIVES)} originaler, "
        f"{len(TEXT_EXTRACTS)} tekstuttrekk og {len(DOCUMENTS)} hoveddokumenter"
    )


if __name__ == "__main__":
    main()
