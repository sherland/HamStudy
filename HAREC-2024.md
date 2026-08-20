# HAREC-pensum 2024

Kontrollert: 2026-08-20  
Kilde: CEPT Recommendation T/R 61-02, utgave 2024-02-16, vedlegg 6

## Versjon og avgrensning

Den aktive T/R 61-02-utgaven er datert 16. februar 2024. Forsiden opplyser at
vedlegg 2 og 4 ble oppdatert i 2024, mens vedlegg 6 – eksamenspensumet – sist
ble oppdatert i februar 2018. Lærebokens henvisning til vedlegg 6 er derfor
fortsatt riktig.

CEPT beskriver vedlegg 6 som veiledning til nasjonale myndigheter når de lager
HAREC-eksamen. Formålet er et rimelig kunnskapsnivå for bruk, forsøk og
eksperimenter med amatørstasjoner. Integrerte og diskrete komponenter kan
inngå i kretsoppgaver.

## Innledende ferdighetskrav

Før fagkapitlene forutsetter HAREC at kandidaten kan:

- bruke enheter, multipler og submultipler
- kjenne symbolene som brukes i pensumet
- regne med de fire regneartene, brøker, tierpotenser, eksponentialer,
  logaritmer, kvadrering, kvadratrot og inverse verdier
- tolke lineære og ikke-lineære grafer
- forstå binære tall
- bruke og omforme pensumformlene

Disse kravene er egne læringsmål i pensummatrisen og skal ikke behandles som
frivillige forkunnskaper.

## Struktur

Den maskinlesbare matrisen ligger i
[`data/pensummatrise.csv`](data/pensummatrise.csv).

| Del | Område | Læringsmål i matrisen |
|---|---|---:|
| Innledning | Regning, enheter, symboler og formler | 4 |
| a | Elektrisk, elektromagnetisk og radioteknisk teori | 10 |
| a | Komponenter | 7 |
| a | Kretser | 8 |
| a | Mottakere | 4 |
| a | Sendere | 4 |
| a | Antenner og transmisjonslinjer | 3 |
| a | Bølgeutbredelse | 1 |
| a | Måleteknikk | 2 |
| a | Interferens og immunitet | 3 |
| a | Sikkerhet | 1 |
| b | Operative regler og prosedyrer | 8 |
| c | ITU-, CEPT- og nasjonalt regelverk | 3 |
| | **Totalt** | **58** |

Hvert læringsmål inneholder:

- stabil ID
- HAREC-punkt og engelsk originalterm
- norsk læringsmål og detaljavgrensning
- PDF-side i T/R 61-02
- eventuell norsk særregel
- plass for bokreferanse og dekningsstatus

## Formeloversikt

Formlene er visuelt kontrollert mot PDF-side 14–17 fordi vanlig
tekstuttrekking forvrenger flere av formeloppsettene.

| Tema | Formel eller forhold |
|---|---|
| Ohms lov | `E = I · R` |
| Elektrisk effekt | `P = E · I` |
| Elektrisk energi | `W = P · t` |
| Bølgehastighet | `v = f · λ` |
| Sinus, effektivverdi | `Ueff = Umax / √2` |
| Termisk støy | `PN = k · T · B` |
| FM-modulasjonsindeks | `m = ΔF / fmod` |
| Sinuseffekt | `P = i²R = u²/R = ueff · ieff` |
| Virkningsgrad | `η = Pout/Pin · 100 %` |
| Kapasitiv reaktans | `XC = 1/(2πfC)` |
| Induktiv reaktans | `XL = 2πfL` |
| Resonansfrekvens | `f = 1/(2π√LC)` |
| Q for resonanskrets | `Q = 2πfL/Rs = Rp/(2πfL) = fres/B` |

Transformatorforholdene inngår også: ideelt er primær- og sekundæreffekt
like, spenningsforholdet følger viklingsforholdet, strømforholdet er omvendt,
og impedansforholdet behandles kvalitativt.

## Omfang som lett kan bli oversett

Pensumet er bredere enn klassisk grunnleggende elektronikk. Matrisen tar
uttrykkelig med:

- digitale modulasjoner, CRC, retransmisjon og feilkorreksjon
- sampling, konvolusjon, FIR/IIR, DFT/FFT og DDS
- fasestøy og reciprocal mixing
- svitsjede strømforsyninger og EMC
- direktkonverterende mottaker
- apertureantenner, bølgeledere og linkbudsjett
- spektrumanalysator
- sosialt ansvar og selvregulering
- nødtrafikk og naturkatastrofer
- loggføring som del av nasjonalt regelverk

## Kontrollspor

- Original PDF:
  [`Kilder/primar/CEPT_TR_61-02_2024-02-16.pdf`](Kilder/primar/CEPT_TR_61-02_2024-02-16.pdf)
- Lagret tekstuttrekk:
  [`Kilder/tekst/CEPT_TR_61-02_2024-02-16.txt`](Kilder/tekst/CEPT_TR_61-02_2024-02-16.txt)
- Ekstraksjon:
  [`scripts/extract_pdf_text.py`](scripts/extract_pdf_text.py)
- Matrisebygging:
  [`scripts/build_harec_matrix.py`](scripts/build_harec_matrix.py)
- Uavhengig dekningskontroll:
  [`scripts/verify_harec_matrix.py`](scripts/verify_harec_matrix.py)

Den ekstraherte teksten er et søkbart arbeidsformat. PDF-en forblir
originalkilden, særlig for formler, tabeller og visuell struktur.
