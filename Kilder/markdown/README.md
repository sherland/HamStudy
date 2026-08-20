# Strukturert PDF-uttrekk med Marker

Denne mappen bevarer Markdown, tabeller, ligninger, metadata og ekstraherte
bilder fra utvalgte PDF-kilder. Uttrekkene er laget med `marker_single` 2.0.0
og skal gjenbrukes når lærestoff og senere flashkort bygges.

## Forholdet til originalkilden

- PDF-filen i `../primar/` er dokumentasjonskilden.
- Marker-uttrekket er et arbeidsformat som bevarer mer struktur enn ren tekst,
  men det er ikke autoritativt i seg selv.
- Tabeller, matematiske symboler og figurer som brukes faglig, skal kontrolleres
  mot PDF-en.
- Enkelte PDF-er inneholder dekorative eller tomme bildeobjekter. At Marker har
  eksportert et bilde betyr derfor ikke automatisk at bildet er faglig nyttig.
- `*_meta.json` dokumenterer konverteringen og tabellbehandlingen.

## Reproduserbar kommando

For PDF-er med tekstlag brukes:

```powershell
marker_single INPUT.pdf --output_format markdown --output_dir Kilder/markdown --mode fast --disable_ocr --disable_tqdm
```

Hver kilde får en egen undermappe med Markdown-fil, metadata og eventuelle
bildeuttrekk. Se også `../tekst/` for kompakte, sidenummererte tekstuttrekk som
er bedre egnet til enkel søking.
