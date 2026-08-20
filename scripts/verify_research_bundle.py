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
    "Kilder/primar/ITU-R-HDB-52-2026.pdf": "24A4B1443A39C157D8EBC0C2DCD59FF01E3D44DBCFC2E08406F25085216CC9BC",
    "Kilder/primar/NIST-SP811-2008.pdf": "788DD8F0BCB0EC06E40C300690266742532A7E760A93BE57764B77ED0EF3482F",
    "Kilder/primar/MIT-6.002-L03-Thevenin.pdf": "96C22AEDE85777D7B2ED7DE15ED8BDE2CFCD05F0005B97F3843AE1E7FBA851D7",
    "Kilder/primar/MIT-6.071J-linear-circuits.pdf": "FEACCE5665083650B0171784D07C15EB465B6CA1EB0B4F92DABE46085FF9FDD9",
    "Kilder/primar/MIT-8.022-L09-RC.pdf": "072BC2998B5448A93DBE75A8E0833EB069763B75F26ED40C7B674E88B1959E56",
    "Kilder/primar/MIT-6.101-decibels.pdf": "53B372A905390827264363C052240AF3BB053E9B09F48BFB105C2D548D821DE7",
    "Kilder/primar/MIT-6.101-highpass.pdf": "17F5B350FA10026FD8497F225015790B45722D01FD6FC0E5A183D31A380296B2",
    "Kilder/primar/MIT-6.101-lowpass.pdf": "D53BC20ABC30CA8A3EFE6BAC418944C6EC9D72C7039854B2E03D77F54CF9F058",
    "Kilder/primar/MIT-6.101-regulated-power.pdf": "D9ECD0FC7C2286ABFD34F20EEF9741D32889EB6D1C9314592931C25C0EDBE199",
    "Kilder/primar/MIT-6.101-ripple.pdf": "6082ECA885493652264B7523B0138D84B14B823DEB01AEE2C12BFD1EBCD6DD48",
    "Kilder/primar/MIT-6.101-transistor-config.pdf": "B92E5265EF2B3A5DBE17109A5083DD2E905D5ED758F4B2C5229EC72BF0BD1117",
    "Kilder/primar/FAA-H-8083-30B-kap12-kretser-s442-506.pdf": "789BA3E16E05D0F59246BDB37F16D1BE5D0BB9E0B317F5A3CD470F774741CCD4",
    "Kilder/primar/FAA-H-8083-30B-kap12-halvledere-s536-559.pdf": "8F7D7FE280DA64619BC31400B6A22F53166098FBCA0F6B146A51AE1215B0D7A4",
    "Kilder/primar/MIT-6.071J-signals-DSP.pdf": "65CB92522EC44176009FD39F27C10B4FB4CECE749F921B23E4F7332FDF79C9B5",
    "Kilder/primar/MIT-2.161-L10-sampling-DFT.pdf": "B349F3370D7BE33592E2084ADC3E1981883F378C53ED05565869153A7AE5DDAA",
    "Kilder/primar/MIT-2.161-L13-convolution.pdf": "6BEE1B0F85E0354EE08EFE8247ECD70D6DF4F709F2FFD18FFCC8BF619B64ABFF",
    "Kilder/primar/MIT-2.161-L18-FIR-IIR.pdf": "B41A566C20CBAE95D96A3CA17ED2EE4A6C81FC6AA70331E44BE44332FB16E869",
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
    "Kilder/tekst/ITU-R-HDB-52-2026.txt",
    "Kilder/tekst/NIST-SP811-2008.txt",
    "Kilder/tekst/MIT-6.002-L03-Thevenin.txt",
    "Kilder/tekst/MIT-6.071J-linear-circuits.txt",
    "Kilder/tekst/MIT-8.022-L09-RC.txt",
    "Kilder/tekst/FAA-H-8083-30B-kap12.txt",
    "Kilder/tekst/MIT-6.101-decibels.txt",
    "Kilder/tekst/MIT-6.101-highpass.txt",
    "Kilder/tekst/MIT-6.101-lowpass.txt",
    "Kilder/tekst/MIT-6.101-regulated-power.txt",
    "Kilder/tekst/MIT-6.101-ripple.txt",
    "Kilder/tekst/MIT-6.101-transistor-config.txt",
    "Kilder/tekst/MIT-6.071J-signals-DSP.txt",
    "Kilder/tekst/MIT-2.161-L10-sampling-DFT.txt",
    "Kilder/tekst/MIT-2.161-L13-convolution.txt",
    "Kilder/tekst/MIT-2.161-L18-FIR-IIR.txt",
}

MARKER_EXTRACTS = {
    "CEPT_TR_61-02_2024-02-16",
    "IARU-R1_HF-bandplan_effective-2016",
    "ITU-R-HDB-52-2026",
    "NIST-SP811-2008",
    "MIT-6.002-L03-Thevenin",
    "MIT-6.071J-linear-circuits",
    "MIT-8.022-L09-RC",
    "MIT-6.101-decibels",
    "MIT-6.101-highpass",
    "MIT-6.101-lowpass",
    "MIT-6.101-regulated-power",
    "MIT-6.101-ripple",
    "MIT-6.101-transistor-config",
    "FAA-H-8083-30B-kap12-kretser-s442-506",
    "FAA-H-8083-30B-kap12-halvledere-s536-559",
    "IARU-R1_VHF-Handbook_v10.02",
    "MIT-6.071J-signals-DSP",
    "MIT-2.161-L10-sampling-DFT",
    "MIT-2.161-L13-convolution",
    "MIT-2.161-L18-FIR-IIR",
}

DOCUMENTS = {
    "PLAN-PENSUM.md", "REGELVERK-2026.md", "HAREC-2024.md",
    "BOKKARTLEGGING.md", "OPERASJON-OG-SIKKERHET.md",
    "GAP-OG-KONFLIKTLOGG.md", "APNE-SPORSMAL.md",
    "GJENNOMFORINGSSTATUS.md", "Kilder/KILDEREGISTER.md",
    "Kilder/TEKNISK-KILDEREGISTER.md", "Materiell/README.md",
    "Materiell/01-grunnleggende-elektronikk.md",
    "Materiell/02-signaler-filtre-halvledere.md",
    "Materiell/03-modulasjon-sendere-mottakere.md",
    "Materiell/04-digital-signalbehandling.md",
}


def main() -> None:
    for filename, expected in ARCHIVES.items():
        path = Path(filename)
        actual = sha256(path.read_bytes()).hexdigest().upper()
        assert actual == expected, f"Hash-avvik: {filename}"

    for filename in TEXT_EXTRACTS:
        path = Path(filename)
        assert path.stat().st_size > 500, f"Tomt eller for lite tekstuttrekk: {filename}"

    for stem in MARKER_EXTRACTS:
        directory = Path("Kilder/markdown") / stem
        markdown = directory / f"{stem}.md"
        metadata = directory / f"{stem}_meta.json"
        # Enkeltsiders diagramkilder kan bestå av én kort bildelenke i Markdown.
        assert markdown.stat().st_size > 50, f"Tomt Marker-uttrekk: {markdown}"
        assert metadata.stat().st_size > 100, f"Manglende Marker-metadata: {metadata}"

    for filename in DOCUMENTS:
        path = Path(filename)
        assert path.stat().st_size > 300, f"Manglende eller for lite dokument: {filename}"

    for verifier in ("scripts/verify_frequency_tables.py", "scripts/verify_harec_matrix.py"):
        subprocess.run([sys.executable, verifier], check=True)

    print(
        f"Forskningspakken er konsistent: {len(ARCHIVES)} originaler, "
        f"{len(TEXT_EXTRACTS)} tekstuttrekk, {len(MARKER_EXTRACTS)} Marker-uttrekk "
        f"og {len(DOCUMENTS)} hoveddokumenter"
    )


if __name__ == "__main__":
    main()
