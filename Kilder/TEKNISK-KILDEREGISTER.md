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
| FAA-ELEC-2023 | FAA-H-8083-30B, kap. 12, *Fundamentals of Electricity & Electronics* | FAA; myndighetsutgitt lærehåndbok | DC/AC, Ohm/Kirchhoff, komponenter, resonans, transformator, halvledere, filtre og måling | [FAA, full PDF](https://www.faa.gov/sites/faa.gov/files/00_amtg_handbook.pdf) | `primar/FAA-H-8083-30B-kap12-kretser-s442-506.pdf`, `primar/FAA-H-8083-30B-kap12-halvledere-s536-559.pdf`, strukturerte Marker-uttrekk og søketekst for PDF-side 442–615; full PDF er 92,5 MB og er ikke lagt i Git | Full original: `0A39C01BBC454E77A49813CF27E2EF291756FA7111D9308BC290CD0EB71616FD` |
| ITU-AMATEUR-2026 | *Handbook on Amateur and amateur-satellite services*, 2026 | ITU-R; offisiell internasjonal håndbok | Tjenesten, operasjon, nødsamband, systemer, utstyr, antenne-/propagasjonsforsøk og DSP | [ITU](https://www.itu.int/pub/R-HDB-52-2026) | `primar/ITU-R-HDB-52-2026.pdf`, `tekst/ITU-R-HDB-52-2026.txt` | `24A4B1443A39C157D8EBC0C2DCD59FF01E3D44DBCFC2E08406F25085216CC9BC` |
| MIT-CIRCUITS | Chaniotakis og Cory, *Linear Circuits Analysis*, MIT 6.071J, 2006 | MIT OpenCourseWare; universitetskursnotat | Node-/sløyfeanalyse, superposisjon, Thévenin/Norton og maksimal effektoverføring | [MIT OCW](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/resources/linear_crct_ana/) | `primar/MIT-6.071J-linear-circuits.pdf`, `tekst/MIT-6.071J-linear-circuits.txt` | `FEACCE5665083650B0171784D07C15EB465B6CA1EB0B4F92DABE46085FF9FDD9` |
| MIT-THEVENIN-L03 | Agarwal og Lang, MIT 6.002 Lecture 3, 2007 | MIT OpenCourseWare; universitetsforelesning | Nodeanalyse og Thévenin-metoden | [MIT OCW](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l3/) | `primar/MIT-6.002-L03-Thevenin.pdf`, `tekst/MIT-6.002-L03-Thevenin.txt` | `96C22AEDE85777D7B2ED7DE15ED8BDE2CFCD05F0005B97F3843AE1E7FBA851D7` |
| MIT-RC-L09 | Sciolla, MIT 8.022 Lecture 9, 2004 | MIT OpenCourseWare; universitetsforelesning | RC-lading/-utlading, eksponentialforløp og tidskonstant | [MIT OCW](https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture9/) | `primar/MIT-8.022-L09-RC.pdf`, `tekst/MIT-8.022-L09-RC.txt` | `072BC2998B5448A93DBE75A8E0833EB069763B75F26ED40C7B674E88B1959E56` |
| MIT-DB | Roscoe, *The Decibel Unit of Measurement*, MIT 6.101 | MIT OpenCourseWare | Effekt-/spenningsforhold i dB og kaskader | [MIT OCW](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/decibels/) | `primar/MIT-6.101-decibels.pdf`, `tekst/MIT-6.101-decibels.txt` | `53B372A905390827264363C052240AF3BB053E9B09F48BFB105C2D548D821DE7` |
| MIT-FILTERS | Roscoe, *High-Pass/Low-Pass Filter Basics*, MIT 6.101 | MIT OpenCourseWare | Førsteordens RC-filter, knekkfrekvens, fase og helning | [MIT high-pass](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/hpass_filter/), [MIT low-pass](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/lpass_filter/) | `primar/MIT-6.101-highpass.pdf`, `primar/MIT-6.101-lowpass.pdf` og tilsvarende tekstfiler | `17F5B350FA10026FD8497F225015790B45722D01FD6FC0E5A183D31A380296B2`; `D53BC20ABC30CA8A3EFE6BAC418944C6EC9D72C7039854B2E03D77F54CF9F058` |
| MIT-POWER | Roscoe, regulert DC-forsyning og rippel, MIT 6.101 | MIT OpenCourseWare | Likeretter, glatting, regulering og rippelberegning | [MIT regulated supply](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/regulated_ps/), [MIT ripple](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/ripple_volts/) | `primar/MIT-6.101-regulated-power.pdf`, `primar/MIT-6.101-ripple.pdf` og tekstfiler | `D9ECD0FC7C2286ABFD34F20EEF9741D32889EB6D1C9314592931C25C0EDBE199`; `6082ECA885493652264B7523B0138D84B14B823DEB01AEE2C12BFD1EBCD6DD48` |
| MIT-TRANSISTOR | Roscoe, *Transistor Amplifier Configurations*, MIT 6.101 | MIT OpenCourseWare | Felles emitter/base/kollektor og impedans-/forsterkningsegenskaper | [MIT OCW](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/resources/trans_amp_config/) | `primar/MIT-6.101-transistor-config.pdf`, `tekst/MIT-6.101-transistor-config.txt` | `B92E5265EF2B3A5DBE17109A5083DD2E905D5ED758F4B2C5229EC72BF0BD1117` |
| MIT-DSP-SIGNALS | Chaniotakis og Cory, *Signals*, MIT 6.071J, 2006 | MIT OpenCourseWare; universitetskursnotat | Signaltyper, Fourier, sampling, Nyquist, aliasing og ADC/DAC | [MIT OCW](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/resources/02_signals/) | `primar/MIT-6.071J-signals-DSP.pdf`, tekst- og Marker-uttrekk | `65CB92522EC44176009FD39F27C10B4FB4CECE749F921B23E4F7332FDF79C9B5` |
| MIT-DSP-2161 | Rowell, MIT 2.161 forelesning 10, 13 og 18, 2008 | MIT OpenCourseWare; universitetskursnotater | Sampling/DFT, konvolusjon, FIR, FFT-konvolusjon og IIR | [MIT OCW](https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/pages/lecture-notes/) | `primar/MIT-2.161-L10-sampling-DFT.pdf`, `primar/MIT-2.161-L13-convolution.pdf`, `primar/MIT-2.161-L18-FIR-IIR.pdf` med tekst- og Marker-uttrekk | `B349F3370D7BE33592E2084ADC3E1981883F378C53ED05565869153A7AE5DDAA`; `6BEE1B0F85E0354EE08EFE8247ECD70D6DF4F709F2FFD18FFCC8BF619B64ABFF`; `B41A566C20CBAE95D96A3CA17ED2EE4A6C81FC6AA70331E44BE44332FB16E869` |
| IARU-R1-VHF-10.02 | *IARU Region 1 VHF Handbook*, versjon 10.02 | IARU Region 1; veiledende amatørstandard | VHF/UHF-operasjon, båndplan, antenner, polarisasjon, måling og EMC | [IARU R1](https://www.iaru-r1.org/wp-content/uploads/2024/11/VHF_Handbook_V10_02.pdf) | Original, tekst og strukturert Marker-uttrekk er arkivert | `DAD6FCB9CB39D01961124DD19DB76199302233D53477B530D33D005CC1A99B12` |
| USN-NEETS-10 | *Introduction to Wave Propagation, Transmission Lines, and Antennas*, NAVEDTRA 14182 | US Navy; offentlig teknisk opplæringsmodul | Bølgeutbredelse, transmisjonslinjer, SWR, antenner, diagrammer og ionosfære | [NEETS-arkiv](https://maritime.org/doc/neets/mod10.pdf) | `primar/USN-NEETS-mod10-propagation-lines-antennas.pdf` med tekst- og Marker-uttrekk | `2D80C2D8F312748DD1454AE40EF47FA6C17CEB695E3A171AEA3507CAD298ADC0` |
| ITU-P525-5 | Recommendation ITU-R P.525-5, *Calculation of free-space attenuation*, 2024 | ITU-R; gjeldende internasjonal anbefaling | Friluftsfelt, grunnleggende transmisjonstap og linkbudsjett | [ITU-R](https://www.itu.int/rec/R-REC-P.525-5-202411-I/en) | `primar/ITU-R-P.525-5-2024.pdf` med tekst- og Marker-uttrekk | `55FF9BF5BB4534B91863FD84D760FE689E2F969B91DB0EA786717FD078DF1DA5` |
| USN-NEETS-16 | *Introduction to Test Equipment*, NEETS Module 16 | US Navy; offentlig teknisk opplæringsmodul | Multimeter, RF-effekt, signalgenerator, frekvensteller, oscilloskop og spektrumanalysator | [NEETS-arkiv](https://maritime.org/doc/neets/mod16.pdf) | `primar/USN-NEETS-mod16-test-equipment.pdf` med tekst- og Marker-uttrekk | `9399B8C2F6BD68FDB7435D3E218B1B1FED7C1B63494686E77F5044007293BB2C` |
| ADI-DDS-MT085 | Kester, *Fundamentals of Direct Digital Synthesis (DDS)*, MT-085 | Analog Devices; produsentens tekniske veiledning | Faseakkumulator, tuningord, DAC og rekonstruksjonsfilter | [Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/mt-085.pdf) | Direkte PDF-arkivering mislyktes fordi serveren avbrøt forbindelsen 2026-08-20; nettsøkeksemplaret ble kontrollert | Ikke beregnet |
| ADI-SWREG | Zhang, *AN-140: Basic Concepts of Linear Regulator and Switching Mode Power Supplies* | Analog Devices; produsentens applikasjonsnotat | Lineær kontra svitsjet regulering og buck-prinsippet | [Analog Devices](https://www.analog.com/en/resources/app-notes/an-140.html) | Ikke lokalt arkivert: serveren avbrøt begge innhentingsforsøk 2026-08-20 | Ikke beregnet |

## Avledede PDF-utdrag

FAA-utdragene er laget med `scripts/extract_pdf_pages.py` fra den kontrollerte
fullfilen. Sidetallene i filnavnet er PDF-sidetall (1-basert), ikke håndbokas
trykte kapittelsidetall.

| Fil | Sider fra full original | SHA-256 |
|---|---:|---|
| `FAA-H-8083-30B-kap12-kretser-s442-506.pdf` | 442–506 | `789BA3E16E05D0F59246BDB37F16D1BE5D0BB9E0B317F5A3CD470F774741CCD4` |
| `FAA-H-8083-30B-kap12-halvledere-s536-559.pdf` | 536–559 | `8F7D7FE280DA64619BC31400B6A22F53166098FBCA0F6B146A51AE1215B0D7A4` |

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
