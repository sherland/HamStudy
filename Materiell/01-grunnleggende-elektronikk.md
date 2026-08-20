# 1. Grunnleggende elektronikk og kretsregning

HAREC: `H-INTRO-A`–`H-INTRO-D`, `H-T1.1`, `H-T1.2`, `H-T1.6`,
`H-T1.9`, `H-T2.1`–`H-T2.4` og deler av `H-T3.1`.

## Kildegrunnlag

- `HAREC-2024`, vedlegg 6, PDF-side 12 og 14–18, fastsetter omfanget.
- `NIST-SI-811`, PDF-side 16–20 og 24–25, støtter enheter, prefikser og
  skriveregler.
- `FAA-ELEC-2023`, kapittel 12, PDF-side 458–506, støtter grunnstørrelser,
  Ohms lov, effekt, serie/parallell, Kirchhoff, AC, C, L, resonans og
  transformatorer.
- `MIT-CIRCUITS`, særlig PDF-side 3–23, støtter den systematiske
  kretsanalysen, Thévenin/Norton og maksimal effektoverføring.
- `MIT-RC-L09`, PDF-side 2–7, støtter RC-kretsenes eksponentialforløp og
  tidskonstant.

Alle fire kilde-ID-er er registrert med original-URL, lokalt uttrekk og hash i
`Kilder/TEKNISK-KILDEREGISTER.md`. Regnetallene og SVG-figurene nedenfor er
egne pedagogiske utledninger fra de kildebelagte lovene; de er ikke kopierte
oppgaver eller figurer.

## 1.1 Størrelser, enheter og prefikser

Kilder: `HAREC-2024` PDF-side 12 og 14; `NIST-SI-811` PDF-side 16–20.

Elektrisk ladning måles i coulomb (C). Strøm er hvor raskt ladning passerer et
tverrsnitt:

`I = Q/t`

Én ampere betyr én coulomb per sekund. Spenning er energi per ladning:

`U = W/Q`

Én volt betyr én joule per coulomb. Motstand beskriver hvor sterkt en komponent
motsetter seg strøm. For en ohmsk motstand gjelder:

`U = I·R`, `I = U/R`, `R = U/I`

Vanlige prefikser må kunne brukes begge veier:

| Prefiks | Symbol | Faktor | Eksempel |
|---|---:|---:|---:|
| giga | G | 10⁹ | 1 GHz = 1 000 000 000 Hz |
| mega | M | 10⁶ | 3,5 MHz = 3 500 000 Hz |
| kilo | k | 10³ | 4,7 kΩ = 4700 Ω |
| milli | m | 10⁻³ | 25 mA = 0,025 A |
| mikro | µ | 10⁻⁶ | 100 µF = 0,0001 F |
| nano | n | 10⁻⁹ | 10 nF = 0,000000010 F |
| piko | p | 10⁻¹² | 47 pF = 0,000000000047 F |

Store og små bokstaver betyr ulike ting: `mW` er milliwatt, mens `MW` er
megawatt. Regn helst om til grunnenheter før innsetting, eller velg prefikser
som kansellerer på en kontrollert måte.

## 1.2 Ohms lov, effekt og energi

Kilder: `FAA-ELEC-2023` PDF-side 458–463; `HAREC-2024` PDF-side 14–15.

Når strøm går gjennom en motstand, omdannes elektrisk energi hovedsakelig til
varme. De viktigste effektformlene er:

`P = U·I = I²R = U²/R`

Energi er effekt ganger tid:

`W = P·t`

### Eksempel: seriemotstand for en last

Egen utledning fra Ohms lov og effektformlene i kildene over.

En 12 V-kilde skal drive en last som kan modelleres som 240 Ω.

1. Strøm: `I = 12 V / 240 Ω = 0,050 A = 50 mA`.
2. Effekt i lasten: `P = 12 V · 0,050 A = 0,60 W`.
3. På 10 minutter (`600 s`) brukes `W = 0,60 W · 600 s = 360 J`.

En motstand merket 0,5 W er for liten her. I praktisk konstruksjon velges en
effektklasse med margin, for eksempel 1 W, og temperatur/ventilasjon vurderes.

## 1.3 Kirchhoffs lover

Kilder: `FAA-ELEC-2023` PDF-side 477–484; `MIT-CIRCUITS` PDF-side 3–10.

Ohms lov beskriver én komponent. Kirchhoffs lover binder hele kretsen sammen:

1. **Strømloven (KCL):** summen av strømmer inn i et knutepunkt er lik summen
   ut. Ladning forsvinner ikke.
2. **Spenningsloven (KVL):** den algebraiske summen av spenningene rundt en
   lukket sløyfe er null. Energi per ladning bevares.

Velg selv strømretninger. Får du negativt svar, går den virkelige strømmen
motsatt av pilen du valgte; regningen er ikke dermed feil.

## 1.4 Serie- og parallellkobling

Kilder: `FAA-ELEC-2023` PDF-side 474–484; `HAREC-2024` PDF-side 17.

![Serie- og parallellkobling](figurer/serie-parallell.svg)

Egen figur basert på serie-/parallellreglene i `FAA-ELEC-2023`.

### Seriekobling

Samme strøm går gjennom alle motstandene. Spenningene summeres:

`R_total = R1 + R2 + …`

For 100 Ω, 220 Ω og 680 Ω i serie blir `R_total = 1000 Ω = 1,0 kΩ`.
Med 10 V blir strømmen `10 V / 1000 Ω = 10 mA`.

### Parallellkobling

Samme spenning ligger over hver gren. Strømmene summeres:

`1/R_total = 1/R1 + 1/R2 + …`

For to motstander kan dette skrives:

`R_total = R1·R2/(R1+R2)`

To kontroller er nyttige:

- totalmotstanden må være mindre enn den minste grenmotstanden;
- to like motstander `R` i parallell gir `R/2`.

### Eksempel: blandet serie-/parallellkrets

Egen utledning fra serie-/parallellreglene, Ohms lov og KCL.

I figuren er `R1 = 100 Ω`, `R2 = 330 Ω`, `R3 = 220 Ω` og kilden 12 V.
`R2` og `R3` står parallelt; denne kombinasjonen står i serie med `R1`.

1. Parallellkombinasjonen:
   `R23 = 330·220/(330+220) = 132 Ω`.
2. Totalmotstand: `R_total = 100 + 132 = 232 Ω`.
3. Kildestrøm: `I = 12/232 = 0,0517 A = 51,7 mA`.
4. Spenning over R1: `U1 = 0,0517·100 = 5,17 V`.
5. Spenning over parallellgrenene: `U23 = 12−5,17 = 6,83 V`.
6. Grenstrømmer: `I2 = 6,83/330 = 20,7 mA` og
   `I3 = 6,83/220 = 31,0 mA`.
7. KCL-kontroll: `20,7 + 31,0 = 51,7 mA`.

## 1.5 Spenningsdeler og belastning

Kilder: `FAA-ELEC-2023` PDF-side 481–484; `MIT-CIRCUITS` PDF-side 3–10.

![Belastet spenningsdeler](figurer/spenningsdeler.svg)

Egen figur og utledning fra node-/spenningsdelerreglene i kildene over.

Uten last er utgangen fra to seriemotstander:

`U_ut = U_inn · R2/(R1+R2)`

Dette er ikke en ideell spenningsforsyning. Når en last `RL` kobles til, står
`RL` parallelt med `R2`. Bruk først `R_ned = R2 || RL`, deretter:

`U_ut = U_inn · R_ned/(R1+R_ned)`

### Eksempel: hvorfor et voltmeter påvirker kretsen

La `U_inn = 10 V`, `R1 = R2 = 1 MΩ`.

- Uten last: `U_ut = 5,0 V`.
- Med et 10 MΩ-voltmeter:
  `R_ned = 1 MΩ || 10 MΩ = 0,909 MΩ`.
- Målt spenning:
  `U_ut = 10·0,909/(1+0,909) = 4,76 V`.

Måleinstrumentets inngangsmotstand har altså gitt omtrent 4,8 % målefeil.

## 1.6 Knutepunktsanalyse for en mer sammensatt krets

Kilder: `MIT-CIRCUITS` PDF-side 3–10; `MIT-THEVENIN-L03` PDF-side 2–8.

![Knutepunktskrets](figurer/knutepunkt.svg)

Egen figur og eget tallsett. Ligningsmetoden følger MIT-kildene.

Knutepunktsanalyse er en systematisk bruk av KCL. Sett jord til 0 V. I figuren
er node A koblet til 12 V gjennom 1 kΩ, til jord gjennom 2 kΩ og til node B
gjennom 3 kΩ. Node B går til jord gjennom 1 kΩ.

KCL i A:

`(VA−12)/1000 + VA/2000 + (VA−VB)/3000 = 0`

KCL i B:

`(VB−VA)/3000 + VB/1000 = 0`

Multipliser den første med 6000 og den andre med 3000:

`6(VA−12) + 3VA + 2(VA−VB) = 0`  →  `11VA−2VB=72`

`VB−VA + 3VB = 0`  →  `VA=4VB`

Sett `VA=4VB` inn i første ligning:

`44VB−2VB=72`, derfor `VB=1,714 V` og `VA=6,857 V`.

Kontroll i node B: strømmen fra A er
`(6,857−1,714)/3 kΩ = 1,714 mA`, lik strømmen fra B til jord
`1,714 V/1 kΩ = 1,714 mA`.

Dette er en generell metode også når kretsen ikke kan reduseres med enkel
serie-/parallellregning.

## 1.7 Reell spenningskilde og Thévenin-modell

Kilder: `HAREC-2024` PDF-side 14; `MIT-CIRCUITS` PDF-side 11–23;
`MIT-THEVENIN-L03` PDF-side 9–18. Eksemplene er egne utledninger.

En praktisk kilde kan modelleres som en ideell spenning `U0` i serie med en
indre motstand `Ri`:

`U_klemme = U0 − I·Ri`

Kortslutningsstrømmen i modellen er `I_kort = U0/Ri`; en virkelig kilde kan ha
ytterligere strømbegrensning og må aldri kortsluttes som målemetode uten at det
er uttrykkelig sikkert.

Enhver lineær resistiv toklemmekrets kan erstattes av en Thévenin-spenning
`UTh` i serie med `RTh`. `UTh` er tomgangsspenningen. `RTh` finnes ved å slå av
uavhengige kilder (ideell spenningskilde kortsluttes, ideell strømkilde brytes)
og se motstanden inn i terminalene.

For spenningsdeleren med 10 V og `R1=R2=1 kΩ`:

- `UTh = 5 V`;
- `RTh = R1 || R2 = 500 Ω`.

Med `RL=500 Ω` blir lastspenningen
`5 V · 500/(500+500) = 2,5 V`.

Maksimal effekt overføres til en rent resistiv last når `RL=RTh`. Da er bare
halvparten av kildens tilgjengelige spenning over lasten, og virkningsgraden er
50 %. Dette er nyttig ved signaltilpasning, men sjelden ønskelig i en
kraftforsyning.

## 1.8 Kondensatoren

Kilder: `FAA-ELEC-2023` PDF-side 491–496; `HAREC-2024` PDF-side 16;
`MIT-RC-L09` PDF-side 2–7 for RC-eksponentialene og `τ=RC`.

![Kondensatorens likestrømsforløp](figurer/rc-lading.svg)

Egen figur basert på de kildebelagte lade-/utladningsforløpene.

En kondensator lagrer energi i et elektrisk felt mellom to ledende flater.
Kapasitansen er:

`C = Q/U`

Strømmen bestemmes av hvor raskt spenningen endres:

`i = C·du/dt`

Konsekvenser:

- kondensatorspenningen kan ikke hoppe momentant uten uendelig strøm;
- ved stabil likespenning er en ideell kondensator åpen krets;
- ved rask endring kan den føre betydelig strøm;
- energi: `W = ½CU²`.

I en RC-ladekrets er tidskonstanten `τ = RC`. Ved lading fra 0 mot `U0`:

`uC(t) = U0(1−e^(−t/RC))`

Etter 1τ er spenningen 63,2 % av sluttverdien, etter 3τ omtrent 95 %, og etter
5τ over 99 %. Ved utlading fra `Ustart`:

`uC(t) = Ustart·e^(−t/RC)`

### Eksempel: avkoblingskondensator

`R=10 kΩ`, `C=100 µF` gir `τ = 10 000·0,0001 = 1 s`. Ved lading mot 12 V er
spenningen etter 2 s:

`uC = 12(1−e^(−2)) = 10,38 V`.

Kondensatorer i parallell summeres: `C_total=C1+C2+…`. I serie summeres de
inverse, på samme måte som parallellmotstander:

`1/C_total = 1/C1 + 1/C2 + …`

For sinusformet vekselspenning er kapasitiv reaktans:

`XC = 1/(2πfC)`

Strømmen ligger 90° foran spenningen i en ideell kondensator. Når frekvensen
øker, blir `XC` mindre. Derfor kan en kondensator brukes til å slippe høyfrekvent
støy til jord, koble AC mellom trinn mens DC sperres, eller inngå i filtre og
resonanskretser.

### Eksempel: reaktans

For `C=100 nF` ved `f=1 kHz`:

`XC = 1/(2π·1000·100·10⁻9) = 1592 Ω ≈ 1,59 kΩ`.

Ved 10 kHz blir reaktansen 159 Ω, altså en tidel. Praktiske kondensatorer har
også seriemotstand (ESR), lekkasje og parasittisk induktans; over egen
selvresonans oppfører de seg ikke lenger primært kapasitivt.

## 1.9 Spolen

Kilder: `FAA-ELEC-2023` PDF-side 497–503; `HAREC-2024` PDF-side 16.

En spole lagrer energi i et magnetfelt. For en ideell spole:

`u = L·di/dt`, `W = ½LI²`, `XL = 2πfL`

Strømmen kan ikke hoppe momentant uten uendelig spenning. Ved stabil DC er en
ideell spole en kortslutning; en virkelig vikling har resistans. Ved sinusformet
AC ligger strømmen 90° etter spenningen. Reaktansen øker med frekvensen.

En 10 mH-spole ved 1 kHz har:

`XL = 2π·1000·0,010 = 62,8 Ω`.

Spoler i serie summeres når gjensidig kobling kan neglisjeres. For ukoblede
spoler i parallell brukes inversformelen. Jern- og ferrittkjerner øker
induktansen, men kan mettes og har frekvensavhengige tap.

## 1.10 Transformatoren

Kilder: `FAA-ELEC-2023` PDF-side 506–510; `HAREC-2024` PDF-side 16.

En transformator bruker gjensidig magnetisk kobling. For en ideell
transformator med viklingstall `N1` og `N2`:

`U2/U1 = N2/N1`, `I2/I1 = N1/N2`, `P1=P2`

En impedans på sekundærsiden reflekteres til primærsiden med kvadratet av
viklingsforholdet:

`Z_inn = (N1/N2)²·Z_last`

### Eksempel: impedanstransformasjon

En 50 Ω-last skal ses som 200 Ω. Da må
`N1/N2 = √(200/50) = 2`. Primærviklingen trenger altså dobbelt så mange
vindinger som sekundærviklingen i idealmodellen.

Virkelige transformatorer har kobbertap, kjernetap, lekkinduktans og begrenset
båndbredde. En vanlig transformator gir galvanisk isolasjon; en autotransformator
gjør ikke det.

## 1.11 Vekselstrøm som kompleks impedans

Kilder: `FAA-ELEC-2023` PDF-side 496–505; `MIT-CIRCUITS` PDF-side 2–10;
`HAREC-2024` PDF-side 15–18. Kompleksnotasjonen er en matematisk
representasjon av fase- og reaktansforholdene i kildene.

Motstand og reaktans samles i impedansen `Z`:

- motstand: `ZR = R`;
- spole: `ZL = jωL`;
- kondensator: `ZC = 1/(jωC) = −j/(ωC)`.

Serieimpedanser summeres direkte. Parallellimpedanser summeres via
admittans `Y=1/Z`. For en serie-RL-krets er:

`Z = R + jXL`, `|Z| = √(R²+XL²)`, `φ = arctan(XL/R)`.

### Eksempel: serie-RL

`R=100 Ω`, `L=10 mH`, `f=1 kHz` gir `XL=62,8 Ω`.

`Z = 100+j62,8 Ω`, `|Z|=118,1 Ω`, `φ=32,1°`.

Med 10 V RMS blir strømmen `10/118,1=84,7 mA RMS`, og strømmen ligger 32,1°
etter spenningen. Bare motstanden bruker middel-effekt:
`P=I²R=(0,0847)²·100=0,718 W`.

## 1.12 Fallgruver

Egen pedagogisk oppsummering av feil som kan oppdages med kontrollreglene og
formlene i dette kapitlets kilder.

- Å summere parallellmotstander som om de stod i serie.
- Å glemme at total parallellmotstand må være mindre enn minste gren.
- Å bruke mA direkte i en formel sammen med Ω og tro at svaret blir volt uten
  å kontrollere prefiksene.
- Å anta at en spenningsdeler beholder samme utgang når den belastes.
- Å kalle reaktans for energitap. Ideelle L og C lagrer og returnerer energi;
  reelle komponenter har separate tap.
- Å bruke toppverdi og RMS-verdi om hverandre.
- Å slå av en spenningskilde i Thévenin-analyse ved å åpne den; en ideell
  spenningskilde erstattes med kortslutning.

## 1.13 Kontrolloppgaver

Egenproduserte oppgaver og fasit, avledet fra de kildebelagte lovene over.

1. Tre motstander på 470 Ω, 1 kΩ og 2,2 kΩ står i serie over 12 V. Finn strømmen
   og spenningen over 1 kΩ.
2. Finn totalmotstanden for 1 kΩ, 1,5 kΩ og 3 kΩ i parallell.
3. En 9 V-kilde har indre motstand 2 Ω og belastes med 16 Ω. Finn strøm,
   klemmespenning og effekt i lasten.
4. En 1 µF-kondensator står i serie med 1 kΩ. Finn tidskonstanten og omtrent
   hvor lang tid lading til over 99 % tar.
5. Finn `XC` for 220 pF ved 14 MHz.
6. En transformator har 500 vindinger på primæren og 50 på sekundæren. Primæren
   får 230 V RMS. Finn ideell sekundærspenning og strømforholdet `I2/I1`.

### Fasit

1. `R=3,67 kΩ`, `I=3,27 mA`, `U_1k=3,27 V`.
2. `R_total=500 Ω`.
3. `I=0,5 A`, `U_klemme=8 V`, `P_last=4 W`.
4. `τ=1 ms`, over 99 % etter omtrent `5 ms`.
5. `XC≈51,7 Ω`.
6. `U2=23 V RMS`, `I2/I1=10`.
