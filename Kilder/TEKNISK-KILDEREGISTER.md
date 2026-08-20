# Teknisk kilderegister

Kontrollert: 2026-08-20

Dette registeret dokumenterer kildene til forklaringene i `Materiell/`.
HAREC-2024 bestemmer omfanget, men er normalt ikke en lærebok. Derfor brukes
offentlige standarder, myndighetshåndbøker, ITU-publikasjoner og andre
identifiserbare tekniske primær-/institusjonskilder til selve faginnholdet.

Der tabeller, ligninger eller figurer inngår, er det også lagret strukturerte
Marker-uttrekk under `markdown/`. Uttrekkene er avledede arbeidskopier; den
registrerte original-PDF-en og dens kontrollsum er fortsatt fasit.

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
| MIT-DB | Roscoe, *The Decibel Unit of Measurement*, MIT 6.101 | MIT OpenCourseWare | Effekt-/spenningsforhold i dB og kaskader | [MIT OCW](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/decibels/) | `primar/MIT-6.101-decibels.pdf`, `tekst/MIT-6.101-decibels.txt` | `53B372A905390827264363C052240AF3BB053E9B09F48BFB105C2D548D821DE7` |
| MIT-FILTERS | Roscoe, *High-Pass/Low-Pass Filter Basics*, MIT 6.101 | MIT OpenCourseWare | Førsteordens RC-filter, knekkfrekvens, fase og helning | [MIT high-pass](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/hpass_filter/), [MIT low-pass](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/lpass_filter/) | `primar/MIT-6.101-highpass.pdf`, `primar/MIT-6.101-lowpass.pdf` og tilsvarende tekstfiler | `17F5B350FA10026FD8497F225015790B45722D01FD6FC0E5A183D31A380296B2`; `D53BC20ABC30CA8A3EFE6BAC418944C6EC9D72C7039854B2E03D77F54CF9F058` |
| MIT-POWER | Roscoe, regulert DC-forsyning og rippel, MIT 6.101 | MIT OpenCourseWare | Likeretter, glatting, regulering og rippelberegning | [MIT regulated supply](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/regulated_ps/), [MIT ripple](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/ripple_volts/) | `primar/MIT-6.101-regulated-power.pdf`, `primar/MIT-6.101-ripple.pdf` og tekstfiler | `D9ECD0FC7C2286ABFD34F20EEF9741D32889EB6D1C9314592931C25C0EDBE199`; `6082ECA885493652264B7523B0138D84B14B823DEB01AEE2C12BFD1EBCD6DD48` |
| MIT-TRANSISTOR | Roscoe, *Transistor Amplifier Configurations*, MIT 6.101 | MIT OpenCourseWare | Felles emitter/base/kollektor og impedans-/forsterkningsegenskaper | [MIT OCW](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/trans_amp_config/) | `primar/MIT-6.101-transistor-config.pdf`, `tekst/MIT-6.101-transistor-config.txt` | `B92E5265EF2B3A5DBE17109A5083DD2E905D5ED758F4B2C5229EC72BF0BD1117` |
| ADI-SWREG | Zhang, *AN-140: Basic Concepts of Linear Regulator and Switching Mode Power Supplies* | Analog Devices; produsentens applikasjonsnotat | Lineær kontra svitsjet regulering og buck-prinsippet | [Analog Devices](https://www.analog.com/en/resources/app-notes/an-140.html) | Ikke lokalt arkivert: serveren avbrøt begge innhentingsforsøk 2026-08-20 | Ikke beregnet |

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
