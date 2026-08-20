"""Build the traceable HAREC syllabus matrix from CEPT T/R 61-02 Annex 6."""

import csv
from pathlib import Path


FIELDS = [
    "id",
    "hovedomrade",
    "harec_punkt",
    "engelsk_term",
    "laeringsmal",
    "detaljer",
    "norsk_saerregel",
    "primaerkilde",
    "bokreferanse",
    "dekning",
    "status",
    "kontrollert_dato",
]


ROWS: list[dict[str, str]] = []


def add(
    identifier: str,
    area: str,
    point: str,
    english: str,
    objective: str,
    details: str,
    page: int,
    norwegian_rule: str = "",
) -> None:
    ROWS.append(
        {
            "id": identifier,
            "hovedomrade": area,
            "harec_punkt": point,
            "engelsk_term": english,
            "laeringsmal": objective,
            "detaljer": details,
            "norsk_saerregel": norwegian_rule,
            "primaerkilde": f"HAREC-2024 vedlegg 6, PDF-side {page}",
            "bokreferanse": "",
            "dekning": "IKKE_KARTLAGT",
            "status": "HAREC_BEKREFTET",
            "kontrollert_dato": "2026-08-20",
        }
    )


# Innledende krav
add("H-INTRO-A", "Forutsetninger", "Innledning a", "Units, multiples and sub-multiples", "Kunne bruke enheter og prefikser for alle størrelser i pensumet.", "Kjenne måleenhetene og vanlige multipler og submultipler.", 12)
add("H-INTRO-B", "Forutsetninger", "Innledning b", "Symbols", "Kunne kjenne igjen og bruke symbolene som inngår i pensumet.", "Kretssymboler og andre faglige symboler som brukes i pensumet.", 12)
add("H-INTRO-C", "Forutsetninger", "Innledning c", "Mathematical concepts and operations", "Kunne utføre matematikken som kreves i HAREC-oppgaver.", "Addisjon; subtraksjon; multiplikasjon; divisjon; brøker; tierpotenser; eksponentialer; logaritmer; kvadrering; kvadratrot; inverse verdier; lineære og ikke-lineære grafer; binært tallsystem.", 12)
add("H-INTRO-D", "Forutsetninger", "Innledning d", "Formulae and transposition", "Kunne bruke og omforme formlene som står i pensumet.", "Sette inn verdier med korrekte enheter og transponere en formel for å finne ønsket ukjent.", 12)

# a) Teknisk innhold, kapittel 1
add("H-T1.1", "Teknikk", "a.1.1", "Conductivity", "Forstå grunnleggende elektriske størrelser, ledningsevne og energiberegning.", "Leder, halvleder og isolator; strøm, spenning og motstand; ampere, volt og ohm; Ohms lov E=I·R; Kirchhoffs lover; effekt P=E·I og watt; energi W=P·t; batterikapasitet i amperetimer.", 14)
add("H-T1.2", "Teknikk", "a.1.2", "Sources of electricity", "Forstå reelle spenningskilder og kobling av kilder.", "Spenningskilde; elektromotorisk spenning (EMF); kortslutningsstrøm; indre motstand; klemmespenning; serie- og parallellkobling av spenningskilder.", 14)
add("H-T1.3", "Teknikk", "a.1.3", "Electric field", "Forstå elektrisk felt og elektrisk skjerming.", "Elektrisk feltstyrke; enheten volt per meter; skjerming av elektriske felt.", 14)
add("H-T1.4", "Teknikk", "a.1.4", "Magnetic field", "Forstå magnetfelt rundt strømførende ledere og magnetisk skjerming.", "Magnetfelt rundt strømførende leder; skjerming av magnetiske felt.", 14)
add("H-T1.5", "Teknikk", "a.1.5", "Electromagnetic field", "Forstå radiobølger som elektromagnetiske bølger.", "Radiobølger; utbredelseshastighet; sammenhengen v=f·λ; polarisasjon.", 14)
add("H-T1.6", "Teknikk", "a.1.6", "Sinusoidal signals", "Kunne beskrive og beregne egenskaper ved sinusformede signaler.", "Tidsdiagram; momentanverdi; amplitude Umax; effektivverdi/RMS Ueff=Umax/√2; middelverdi; periode og periodetid; frekvens og hertz; faseforskjell.", 15)
add("H-T1.7", "Teknikk", "a.1.7", "Non-sinusoidal signals and noise", "Forstå ikke-sinusformede signaler, harmoniske og støy.", "Lydsignal; firkantbølge; tidsdiagram; likespenningskomponent, grunntone og overharmoniske; termisk mottakerstøy PN=kTB; båndstøy; støytetthet; støyeffekt i mottakerens båndbredde.", 15)
add("H-T1.8", "Teknikk", "a.1.8", "Modulated signals", "Forstå analoge og digitale modulasjonsformer og deres spektrum.", "CW; AM; PM; FM; SSB; frekvensdeviasjon og modulasjonsindeks m=ΔF/fmod; bærebølge, sidebånd og båndbredde; tidsformer for CW, AM, SSB og FM; spektrum for CW, AM og SSB; FSK, 2-PSK, 4-PSK og QAM; bit- og symbolrate (baud) og båndbredde; CRC og retransmisjon; fremoverrettet feilkorreksjon.", 15)
add("H-T1.9", "Teknikk", "a.1.9", "Power and energy", "Kunne beregne effekt, dB-forhold, tilpasning og virkningsgrad.", "Sinuseffekt P=i²R=P=u²/R=u_eff·i_eff; effektforholdene 0, ±3, ±6, ±10 og ±20 dB; samlet dB for kaskader av forsterkere og dempeledd; maksimal effektoverføring; virkningsgrad η=Pout/Pin·100 %; Peak Envelope Power (PEP).", 15, "REG-2026 § 3 bokstav i definerer senderens utgangseffekt som PEP")
add("H-T1.10", "Teknikk", "a.1.10", "Digital Signal Processing (DSP)", "Forstå grunnprinsippene i digital signalbehandling.", "Sampling og kvantisering; minste samplingsrate/Nyquist-frekvens; konvolusjon i tids- og frekvensdomene, grafisk; anti-aliasfilter og rekonstruksjonsfilter; ADC og DAC.", 15)

# Kapittel 2
add("H-T2.1", "Teknikk", "a.2.1", "Resistor", "Forstå motstandens egenskaper og belastning.", "Ohm; resistans; strøm-/spenningskarakteristikk; effekttap.", 16)
add("H-T2.2", "Teknikk", "a.2.2", "Capacitor", "Forstå kondensatorens egenskaper i likestrøm- og vekselstrømkretser.", "Kapasitans og farad; kvalitativ sammenheng mellom kapasitans, dimensjoner og dielektrikum; kapasitiv reaktans Xc=1/(2πfC); faseforhold mellom spenning og strøm.", 16)
add("H-T2.3", "Teknikk", "a.2.3", "Coil", "Forstå spolens egenskaper og induktive reaktans.", "Selvinduktans og henry; kvalitativ virkning av vindingstall, diameter, lengde og kjernemateriale; induktiv reaktans XL=2πfL; faseforhold; Q-faktor.", 16)
add("H-T2.4", "Teknikk", "a.2.4", "Transformers application and use", "Forstå ideelle transformatorer og transformasjon av spenning, strøm og impedans.", "Ideell transformator Pprim=Psek; sammenheng mellom viklingsforhold og spenningsforhold; motsatt sammenheng for strømforhold; kvalitativ impedanstransformasjon; praktisk bruk av transformatorer.", 16)
add("H-T2.5", "Teknikk", "a.2.5", "Diode", "Kjenne virkemåte og bruk av sentrale diodetyper.", "Likeretterdiode; zenerdiode; LED; varicap; sperrespenning; lekkstrøm.", 16)
add("H-T2.6", "Teknikk", "a.2.6", "Transistor", "Forstå grunnleggende bipolar- og felteffekttransistorkoblinger.", "PNP og NPN; forsterkningsfaktor; FET kontra bipolar transistor, spennings- kontra strømstyrt; felles emitter/source, base/gate og kollektor/drain; inn- og utgangsimpedans for koblingene.", 17)
add("H-T2.7", "Teknikk", "a.2.7", "Miscellaneous components", "Kjenne andre komponenter som er relevante i radioamatørutstyr.", "Enkelt elektronrør; spenninger og impedanser i høyeffekts rørtrinn; impedanstransformasjon; enkle integrerte kretser, inkludert operasjonsforsterkere.", 17)

# Kapittel 3
add("H-T3.1", "Teknikk", "a.3.1", "Combination of components", "Kunne analysere grunnleggende komponentkombinasjoner.", "Serie- og parallellkobling av motstander, spoler, kondensatorer, transformatorer og dioder; strøm og spenning; reelle, ikke-ideelle komponenters oppførsel ved høy frekvens.", 17)
add("H-T3.2", "Teknikk", "a.3.2", "Filter", "Forstå resonanskretser og analoge og digitale filtre.", "Serie- og parallellresonans; impedans og frekvenskarakteristikk; resonans f=1/(2π√LC); Q=2πfL/Rs=Rp/(2πfL)=fres/B; båndbredde; båndpass; lavpass, høypass og båndstopp; frekvensrespons; pi- og T-filter; kvartskrystall; ikke-ideelle komponenter; digitale filtre.", 17)
add("H-T3.3", "Teknikk", "a.3.3", "Power supply", "Forstå oppbygning og EMC-forhold i strømforsyninger.", "Halv- og helbølgelikeretting; brokobling; glatting; stabilisering av lavspenningsforsyninger; svitsjede strømforsyninger; isolasjon og EMC.", 17)
add("H-T3.4", "Teknikk", "a.3.4", "Amplifier", "Forstå LF-/HF-forsterkere og forvrengning.", "LF- og HF-forsterkere; forsterkning; amplitude-/frekvenskarakteristikk og båndbredde; bredbånd kontra avstemt trinn; klasse A, AB, B og C; harmonisk og intermodulasjonsforvrengning; overstyring.", 18)
add("H-T3.5", "Teknikk", "a.3.5", "Detector", "Forstå deteksjon og demodulasjon av AM, SSB/CW og FM.", "AM-konvoluttdetektor; diodedetektor; produktdetektor og beat-oscillator; FM-detektor.", 18)
add("H-T3.6", "Teknikk", "a.3.6", "Oscillator", "Forstå oscillatorprinsipper og frekvensstabilitet.", "Tilbakekobling og tilsiktet/utilsiktet oscillasjon; faktorer for frekvens og stabilitet; oscillasjonsvilkår; LC-, krystall- og overtoneoscillator; VCO; fasestøy.", 18)
add("H-T3.7", "Teknikk", "a.3.7", "Phase Locked Loop (PLL)", "Forstå en faselåst sløyfe og PLL-basert frekvenssyntese.", "Reguleringssløyfe med fasekomparator; frekvenssyntese med programmerbar deler i tilbakekoblingssløyfen.", 18)
add("H-T3.8", "Teknikk", "a.3.8", "Digital signal processing systems", "Forstå sentrale DSP-systemstrukturer.", "FIR- og IIR-filtertopologier; Fourier-transformasjon, DFT og FFT med grafisk forståelse; Direct Digital Synthesis (DDS).", 18)

# Kapittel 4
add("H-T4.1", "Teknikk", "a.4.1", "Receiver types", "Kjenne hovedtypene radiomottakere.", "Enkel og dobbel superheterodynmottaker; direktkonverterende mottaker.", 18)
add("H-T4.2", "Teknikk", "a.4.2", "Receiver block diagrams", "Kunne lese blokkdiagrammer for vanlige mottakere.", "CW-mottaker A1A; AM-mottaker A3E; SSB-mottaker J3E; FM-mottaker F3E.", 18)
add("H-T4.3", "Teknikk", "a.4.3", "Receiver stages", "Forstå funksjonen til hvert hovedtrinn i en mottaker på blokknivå.", "HF-forsterker med avstemt eller fast båndpass; fast og variabel oscillator; blander; mellomfrekvensforsterker; limiter; detektor og produktdetektor; lydforsterker; AGC; S-meter; squelch.", 19)
add("H-T4.4", "Teknikk", "a.4.4", "Receiver characteristics", "Kunne beskrive mottakerens viktigste ytelsesegenskaper.", "Nabokanal; selektivitet; følsomhet; mottakerstøy og støytall; stabilitet; speilfrekvens; desensitivisering/blokkering; intermodulasjon og kryssmodulasjon; reciprocal mixing/fasestøy.", 19)

# Kapittel 5
add("H-T5.1", "Teknikk", "a.5.1", "Transmitter types", "Forstå sendere med og uten frekvenstransponering.", "Senderarkitektur med eller uten frekvensomforming.", 19)
add("H-T5.2", "Teknikk", "a.5.2", "Transmitter block diagrams", "Kunne lese blokkdiagrammer for vanlige sendere.", "CW-sender A1A; SSB-sender J3E; FM-sender der lydsignalet modulerer VCO-en i en PLL, F3E.", 19)
add("H-T5.3", "Teknikk", "a.5.3", "Transmitter stages", "Forstå funksjonen til hvert hovedtrinn i en sender på blokknivå.", "Blander; oscillator; buffer; driver; frekvensmultiplikator; effektforsterker; utgangstilpasning; utgangsfilter; FM-, SSB- og fasemodulator; krystallfilter.", 19)
add("H-T5.4", "Teknikk", "a.5.4", "Transmitter characteristics", "Kunne beskrive senderens viktigste ytelses- og renhetsegenskaper.", "Frekvensstabilitet; RF-båndbredde; sidebånd; audiofrekvensområde; ikke-linearitet, harmonisk og intermodulasjon; utgangsimpedans, effekt og virkningsgrad; frekvensdeviasjon og modulasjonsindeks; CW-key clicks og chirp; SSB-overmodulasjon og splatter; spuriøs RF; kabinettstråling; fasestøy.", 20)

# Kapittel 6
add("H-T6.1", "Teknikk", "a.6.1", "Antenna types", "Kjenne virkemåte og form for sentrale antennetyper.", "Senterfødet og endefødet halvbølge; foldet dipol; kvartbølge vertikal/ground plane; Yagi med parasittelementer; apertureantenner, parabol og horn; trap-dipol.", 20)
add("H-T6.2", "Teknikk", "a.6.2", "Antenna characteristics", "Forstå antenners elektriske egenskaper og stråling.", "Strøm- og spenningsfordeling; matepunktimpedans; kapasitiv/induktiv impedans for ikke-resonant antenne; polarisasjon; direktivitet, virkningsgrad og gain; effektivt areal; ERP og EIRP; front/back-forhold; horisontalt og vertikalt strålingsdiagram.", 20, "REG-2026 § 3 bokstav h og særvilkår i § 5a bruker e.i.r.p.")
add("H-T6.3", "Teknikk", "a.6.3", "Transmission lines", "Forstå transmisjonslinjer, tilpasning og tap.", "Parallell leder; koaksialkabel; bølgeleder; karakteristisk impedans Z0; hastighetsfaktor; SWR; tap; balun; antennetuner i pi- og T-konfigurasjon.", 21)

# Kapittel 7–10
add("H-T7", "Teknikk", "a.7", "Propagation", "Forstå radiobølgers utbredelse og kunne gjøre en grunnleggende linkbudsjettvurdering.", "Signaldemping og S/N; frirom og invers-kvadratlov; ionosfærelag, kritisk frekvens, solpåvirkning og MUF; bakke- og rombølge, strålingsvinkel og skipavstand; flervei og fading; troposfærisk ducting/spredning; antennehøyde og radiohorisont; temperaturinversjon; sporadisk E; aurora; meteor og måne; atmosfærisk, galaktisk og termisk bakkestøy; linkbudsjett med dominerende støykilde, minimum S/N og mottatt effekt, path loss, antennegevinst, linjetap og minimum sendereffekt.", 21)
add("H-T8.1", "Teknikk", "a.8.1", "Making measurements", "Kunne velge og tolke sentrale målinger på radio- og elektronikkutstyr.", "DC- og AC-spenning og strøm; målefeil fra frekvens, bølgeform og instrumentets indre motstand; resistans; DC- og RF-effekt, middel og PEP; SWR; RF-konvolutt; frekvens; resonansfrekvens.", 22)
add("H-T8.2", "Teknikk", "a.8.2", "Measuring instruments", "Kunne bruke og forstå sentrale måleinstrumenter.", "Digitalt og analogt multimeter; RF-effektmeter; reflektometer/SWR-meter; signalgenerator; frekvensteller; oscilloskop; spektrumanalysator.", 22)
add("H-T9.1", "Teknikk", "a.9.1", "Interference in electronic equipment", "Kjenne vanlige former for interferens i elektronisk utstyr.", "Blokkering; interferens med ønsket signal; intermodulasjon; deteksjon i lydkretser.", 22)
add("H-T9.2", "Teknikk", "a.9.2", "Causes of interference", "Forstå hvordan senderfelt og uønskede signaler kobles inn i annet utstyr.", "Senderens feltstyrke; spuriøs stråling, parasittisk stråling og harmoniske; påvirkning via antenneinngang, andre tilkoblede ledninger eller direkte innstråling.", 22, "REG-2026 § 9 viser til ITU-R SM.329 for uønsket utstrålt effekt")
add("H-T9.3", "Teknikk", "a.9.3", "Measures against interference", "Kunne foreslå tiltak for å forebygge og fjerne interferens.", "Filtrering; avkobling; skjerming.", 22)
add("H-T10", "Sikkerhet", "a.10", "Safety", "Forstå grunnleggende elektrisk og fysisk sikkerhet ved en radioamatørstasjon.", "Menneskekroppen; strømnettet; høyspenning; lyn.", 23)

# b) Operative regler og prosedyrer
add("H-O1", "Operasjon", "b.1", "Phonetic alphabet", "Kunne ITUs fonetiske alfabet og bruke det korrekt.", "Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu.", 23)
add("H-O2", "Operasjon", "b.2", "Q-code", "Forstå spørsmål- og svarbetydningen til Q-kodene i HAREC-listen.", "QRK, QRM, QRN, QRO, QRP, QRT, QRZ, QRV, QSB, QSL, QSO, QSY, QRX og QTH.", 23)
add("H-O3", "Operasjon", "b.3", "Operational abbreviations", "Forstå og bruke de operative forkortelsene i HAREC-listen.", "BK, CQ, CW, DE, K, MSG, PSE, RST, R, RX, TX og UR.", 24)
add("H-O4", "Operasjon", "b.4", "International distress signs, emergency traffic and natural disaster communication", "Kjenne internasjonale nødsignaler og radioamatørens rolle ved katastrofer.", "SOS i radiotelegrafi; MAYDAY i radiotelefoni; internasjonal bruk av amatørstasjoner ved nasjonale katastrofer; bånd allokert til amatørtjenesten og amatørsatellittjenesten.", 24)
add("H-O5", "Operasjon", "b.5", "Call signs", "Forstå identifikasjon og oppbygning av kallesignaler.", "Identifikasjon av amatørstasjon; bruk og sammensetning av kallesignal; nasjonale prefikser.", 24, "REG-2026 §§ 4 og 7; nummerforskriften § 35b")
add("H-O6", "Operasjon", "b.6", "IARU band plans", "Forstå IARU-båndplaner og formålet med dem.", "Båndplanenes oppbygning og formål; skille anbefalt bruk fra nasjonal frekvenstillatelse.", 24, "REG-2026 § 7 sier at sendinger bør følge relevante båndplaner")
add("H-O7.1", "Operasjon", "b.7.1", "Social responsibility of radio amateur operation", "Forstå radioamatørens sosiale ansvar og selvregulering.", "Radio Amateur Code of Conduct; selvregulering og selvdisiplin.", 24)
add("H-O7.2", "Operasjon", "b.7.2", "Operating procedures", "Kunne gjennomføre en korrekt kontakt og kontrollere sendekvaliteten.", "Starte, gjennomføre og avslutte kontakt; korrekt kallesignal og forkortelser; tillatt innhold; kontroll av sendekvalitet.", 25, "REG-2026 § 7")

# c) Regler
add("H-R1", "Regelverk", "c.1", "ITU Radio Regulations", "Kjenne ITU-reglene som rammer inn amatørtjenesten.", "Definisjon av Amateur Service, Amateur Satellite Service og Amateur station; artikkel 25; tjenestenes status; ITUs radioregioner.", 25)
add("H-R2", "Regelverk", "c.2", "CEPT regulations", "Forstå CEPT-ordningen for midlertidig internasjonal bruk.", "T/R 61-01; midlertidig bruk i CEPT-land; midlertidig bruk i ikke-CEPT-land som deltar i T/R 61-01-systemet.", 25)
add("H-R3", "Regelverk", "c.3", "National laws, regulations and licence conditions", "Kjenne norske lover, forskrifter og lisensvilkår og forstå loggføring.", "Nasjonale lover; forskrifter og lisensvilkår; føre logg; formålet med loggen; hvilke data som registreres.", 25, "REG-2026; nummerforskriften § 35b")


def main() -> None:
    identifiers = [row["id"] for row in ROWS]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Dupliserte pensum-ID-er")
    if len(ROWS) != 58:
        raise ValueError(f"Forventet 58 læringsmål, fant {len(ROWS)}")

    destination = Path("data/pensummatrise.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ROWS)
    print(f"Skrev {len(ROWS)} HAREC-læringsmål til {destination}")


if __name__ == "__main__":
    main()
