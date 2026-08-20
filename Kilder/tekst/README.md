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
