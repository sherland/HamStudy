# Teknisk kilderegister

Kontrollert: 2026-08-20

Dette registeret dokumenterer kildene til forklaringene i `Materiell/`.
HAREC-2024 bestemmer omfanget, men er normalt ikke en lærebok. Derfor brukes
offentlige standarder, myndighetshåndbøker, ITU-publikasjoner og andre
identifiserbare tekniske primær-/institusjonskilder til selve faginnholdet.

## Kvalitetskrav

Et fagavsnitt er ikke ferdig før det har:

1. én eller flere kilde-ID-er med eksakt del-/sidereferanse;
2. HAREC-ID som viser hvorfor innholdet hører til pensumet;
3. merking av egen utledning, regneeksempel eller figur;
4. kontroll mot annen kilde ved definisjoner eller formler der notasjon varierer;
5. en registrert usikkerhet dersom kildene ikke dekker hele forklaringen.

## Registrerte kilder

| ID | Dokument | Utgiver/status | Dekning | Original | Lokal kopi/uttrekk | SHA-256 av original |
|---|---|---|---|---|---|---|
| HAREC-2024 | CEPT T/R 61-02, 2024-02-16, vedlegg 6 | CEPT; normgivende pensum | Alle 58 læringsmål | [CEPT](https://docdb.cept.org/document/926) | `primar/CEPT_TR_61-02_2024-02-16.pdf`, `tekst/CEPT_TR_61-02_2024-02-16.txt` | `9250EC6FD7FA302321A80ADC244C15305C77075F99B9BF799223F27422571999` |
| NIST-SI-811 | *Guide for the Use of the International System of Units (SI)*, SP 811, 2008 | NIST; offentlig måleteknisk veiledning | SI-enheter, prefikser, symboler og tallskriving | [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e2008.pdf) | `primar/NIST-SP811-2008.pdf`, `tekst/NIST-SP811-2008.txt` | `788DD8F0BCB0EC06E40C300690266742532A7E760A93BE57764B77ED0EF3482F` |
| FAA-ELEC-2023 | FAA-H-8083-30B, kap. 12, *Fundamentals of Electricity & Electronics* | FAA; myndighetsutgitt lærehåndbok | DC/AC, Ohm/Kirchhoff, komponenter, resonans, transformator, halvledere, filtre og måling | [FAA, full PDF](https://www.faa.gov/sites/faa.gov/files/00_amtg_handbook.pdf) | Relevant søketekst, PDF-side 442–615: `tekst/FAA-H-8083-30B-kap12.txt`; full PDF er 92,5 MB og er ikke lagt i Git | `0A39C01BBC454E77A49813CF27E2EF291756FA7111D9308BC290CD0EB71616FD` |
| ITU-AMATEUR-2026 | *Handbook on Amateur and amateur-satellite services*, 2026 | ITU-R; offisiell internasjonal håndbok | Tjenesten, operasjon, nødsamband, systemer, utstyr, antenne-/propagasjonsforsøk og DSP | [ITU](https://www.itu.int/pub/R-HDB-52-2026) | `primar/ITU-R-HDB-52-2026.pdf`, `tekst/ITU-R-HDB-52-2026.txt` | `24A4B1443A39C157D8EBC0C2DCD59FF01E3D44DBCFC2E08406F25085216CC9BC` |
| MIT-CIRCUITS | Chaniotakis og Cory, *Linear Circuits Analysis*, MIT 6.071J, 2006 | MIT OpenCourseWare; universitetskursnotat | Node-/sløyfeanalyse, superposisjon, Thévenin/Norton og maksimal effektoverføring | [MIT OCW](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/resources/linear_crct_ana/) | `primar/MIT-6.071J-linear-circuits.pdf`, `tekst/MIT-6.071J-linear-circuits.txt` | `FEACCE5665083650B0171784D07C15EB465B6CA1EB0B4F92DABE46085FF9FDD9` |
| MIT-THEVENIN-L03 | Agarwal og Lang, MIT 6.002 Lecture 3, 2007 | MIT OpenCourseWare; universitetsforelesning | Nodeanalyse og Thévenin-metoden | [MIT OCW](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l3/) | `primar/MIT-6.002-L03-Thevenin.pdf`, `tekst/MIT-6.002-L03-Thevenin.txt` | `96C22AEDE85777D7B2ED7DE15ED8BDE2CFCD05F0005B97F3843AE1E7FBA851D7` |
| MIT-RC-L09 | Sciolla, MIT 8.022 Lecture 9, 2004 | MIT OpenCourseWare; universitetsforelesning | RC-lading/-utlading, eksponentialforløp og tidskonstant | [MIT OCW](https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture9/) | `primar/MIT-8.022-L09-RC.pdf`, `tekst/MIT-8.022-L09-RC.txt` | `072BC2998B5448A93DBE75A8E0833EB069763B75F26ED40C7B674E88B1959E56` |

## Kildebruk i regneeksempler og figurer

Et regneeksempel kan ha andre tall enn kilden. Da merkes det «egen utledning»
og viser til de kildebelagte lovene/formlene det bruker. Egne SVG-figurer skal
ikke fremstilles som faksimiler; bildeteksten skal angi hvilke kildebegreper
figuren visualiserer. På den måten kan et senere flashkort spores både til
pensumkravet og til det tekniske grunnlaget for svaret.

## Videre kildebehov

FAA-kilden dekker mye grunnleggende elektronikk, men ikke hele HAREC på
radioingeniørnivå. Før de senere kapitlene ferdigstilles må registeret utvides
med autoritative kilder for minst:

- modulasjon, spektrum, sendere og mottakere;
- DSP, sampling, FIR/IIR, Fourier og DDS;
- transmisjonslinjer, antenner, ERP/e.i.r.p. og linkbudsjett;
- ionosfærisk/troposfærisk utbredelse og radiostøy;
- EMC, uønsket utstråling og standardiserte målinger;
- elektrisk sikkerhet, RF-eksponering og lynvern.

Ingen av disse kapitlene skal få status «ferdig» bare fordi HAREC-punktet står
i pensummatrisen.
