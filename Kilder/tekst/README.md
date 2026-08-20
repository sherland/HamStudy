# Ekstrahert kildetekst

Denne mappen inneholder søkbare tekstuttrekk fra arkiverte HTML- og
PDF-kilder. Uttrekkene gjør videre analyse reproducerbar og hindrer at samme
kilde må ekstraheres på nytt i hver arbeidsfase.

Regler:

- Originalfilen i `../primar/` er dokumentasjonskilden.
- Tekstuttrekket er et arbeidsformat og kan miste layout, tabellstruktur eller
  symbolplassering.
- Juridiske verdier kontrolleres mot originalen og separat
  kontrolltranskripsjon før de merkes som bekreftet.
- Filnavnet skal gjøre kilde og versjon entydig.

`REG-2026.txt` og `NUMMERFORSKRIFTEN.txt` genereres med
[`../../scripts/extract_lovdata.py`](../../scripts/extract_lovdata.py).

`CEPT_TR_61-02_2024-02-16.txt` og `CEPT_TR_61-01_2024-10-18.txt` genereres
med [`../../scripts/extract_pdf_text.py`](../../scripts/extract_pdf_text.py).

De arkiverte Nkom- og NRRL-nettsidene genereres med
[`../../scripts/extract_html_text.py`](../../scripts/extract_html_text.py).
IARU-PDF-ene genereres med det samme PDF-skriptet. Navigasjonstekst kan følge
med fra nettsidene; original HTML/PDF er fortsatt autoritativ for layout og
struktur.

Tekniske PDF-kilder fra NIST, ITU og MIT er ekstrahert med PDF-skriptet. For
FAA-H-8083-30B er bare det relevante kapittelintervallet, PDF-side 442–615,
bevart i `FAA-H-8083-30B-kap12.txt`; kommandoen bruker skriptets valgfrie
parametere `FRA_SIDE TIL_SIDE`. Original-URL og fullfilens kontrollhash står i
`../TEKNISK-KILDEREGISTER.md`.

For kilder der tabeller, ligninger og figurer er viktige, finnes i tillegg
Marker-uttrekk i `../markdown/`. Ren tekst og strukturert Markdown har ulike
formål og beholdes derfor side om side.
