# 2. Signaler, filtre, halvledere og forsterkere

HAREC: `H-T1.6`, `H-T1.7`, `H-T1.9`, `H-T2.5`–`H-T2.7`,
`H-T3.2`–`H-T3.4`.

## Kildegrunnlag

- `HAREC-2024`, PDF-side 15–18, fastsetter detaljene som skal kunne forstås.
- `FAA-ELEC-2023`, PDF-side 485–505 og 536–559, dekker AC, resonans,
  halvledere, likeretter, transistor, LC-filtre og forsterkerklasser.
- `MIT-DB`, `MIT-FILTERS`, `MIT-POWER` og `MIT-TRANSISTOR` gir presise
  universitetsnotater for de angitte delene.

Figurer og tallsett er egne utledninger. Kildenes figurer er ikke kopiert.

## 2.1 Sinussignalet, periode, frekvens og fase

Kilder: `FAA-ELEC-2023` PDF-side 485–490; `HAREC-2024` PDF-side 15.

Et sinussignal kan skrives `u(t)=Û sin(2πft+φ)`. `Û` er toppverdi,
`f` er frekvens, `T=1/f` er periodetid og `φ` er fasevinkel. To signaler med
samme frekvens kan være forskjøvet i tid; faseforskjellen er
`Δφ=360°·Δt/T`.

For en ren sinus er effektivverdien `U_RMS=Û/√2`. RMS er den DC-verdien som
gir samme varmeeffekt i en motstand. Topp-til-topp er `Upp=2Û`. Et signal på
10 V topp har 7,07 V RMS og 20 V topp-til-topp. RMS-formelen `Û/√2` gjelder
ikke vilkårlige bølgeformer.

## 2.2 Ikke-sinusformede signaler og harmoniske

Kilder: `HAREC-2024` PDF-side 15; `FAA-ELEC-2023` PDF-side 485–490.

Et periodisk ikke-sinusformet signal kan beskrives som en grunntone pluss
harmoniske sinuskomponenter. En symmetrisk firkantbølge inneholder ideelt bare
oddetallsharmoniske med avtagende amplitude. Bratte flanker krever høye
frekvenskomponenter. Derfor kan klipping, key-clicks og raske digitale kanter
skape bredt spektrum selv om repetisjonsfrekvensen er lav.

Tidsdomene viser hvordan signalet varierer med tiden; frekvensdomene viser
amplitude/effekt som funksjon av frekvens. De er to beskrivelser av samme
signal, ikke to forskjellige signaler.

## 2.3 Desibel

Kilder: `MIT-DB` PDF-side 1–3; `HAREC-2024` PDF-side 15.

For effektforhold:

`G_dB = 10 log10(Put/Pinn)`

For spennings- eller strømforhold når impedansene er like:

`G_dB = 20 log10(Uut/Uinn)`

20-faktoren kommer av at effekt er proporsjonal med spenning i andre potens.
Den kan ikke brukes til å påstå et effektforhold når impedansene er ulike.

| Forhold | dB |
|---:|---:|
| effekt ×2 / ÷2 | +3 / −3 dB |
| spenning ×2 / ÷2, lik impedans | +6 / −6 dB |
| effekt ×10 / ÷10 | +10 / −10 dB |
| spenning ×10 / ÷10, lik impedans | +20 / −20 dB |

I en kaskade summeres dB. En forsterker på 12 dB, et filtertap på 3 dB og en
effektforsterker på 20 dB gir `12−3+20=29 dB` total forsterkning.

## 2.4 Resonans og Q

Kilder: `FAA-ELEC-2023` PDF-side 504–505; `HAREC-2024` PDF-side 17.

Ved resonans er `XL=XC`, slik at

`f0 = 1/(2π√(LC))`.

I en serie-RLC er impedansen minst ved resonans og strømmen størst. I en ideell
parallellresonans er inngangsimpedansen størst. Reelle tap bestemmer hvor skarp
resonansen er. Kvalitetsfaktoren kan uttrykkes som `Q=f0/B`, der `B` er
båndbredden mellom −3 dB-punktene.

Eksempel: `L=10 µH`, `C=100 pF` gir
`f0=1/(2π√(10·10⁻6·100·10⁻12))≈5,03 MHz`. Med `Q=50` blir
`B≈5,03 MHz/50≈101 kHz`.

## 2.5 Lavpass, høypass, båndpass og båndstopp

Kilder: `MIT-FILTERS`, begge PDF-er; `FAA-ELEC-2023` PDF-side 553–554;
`HAREC-2024` PDF-side 17.

![Førsteordens RC-filtre](figurer/rc-filtre.svg)

Egen figur basert på `MIT-FILTERS`. I RC-lavpass tas utgangen over C; i
RC-høypass tas den over R. Begge har knekkfrekvens
`fc=1/(2πRC)`. Ved `fc` er amplituden `1/√2=0,707` av passbåndsverdien,
altså −3 dB. Et førsteordens ledd ruller av med 20 dB per dekade.

Med `R=1 kΩ`, `C=10 nF` er `fc≈15,9 kHz`. Lavpasset slipper frekvenser langt
under 15,9 kHz omtrent uendret og demper høyere frekvenser. Høypass gjør det
motsatte. Båndpass kombinerer lav og høy grense; båndstopp demper et område
mellom to passbånd. LC-nettverk brukes ofte ved RF fordi de kan gi lavere tap
og høyere Q enn enkle RC-ledd.

Et delefilter i lydanlegg er et sett lav-/høypass som sender lave frekvenser til
basselementet og høye til diskantelementet. Prinsippet er det samme som andre
frekvensselektive nettverk, men lastimpedansen til høyttalerne må inngå i
beregningen.

## 2.6 Dioder

Kilder: `FAA-ELEC-2023` PDF-side 536–546; `HAREC-2024` PDF-side 16.

En PN-diode leder hovedsakelig i foroverretning og sperrer i motsatt retning
inntil gjennombrudd. Modellen «ideell bryter» er nyttig først, men en virkelig
silisiumdiode har foroverspenningsfall, lekkstrøm, maksimal strøm, sperrespenning
og endelig svitsjetid.

- **Likeretterdiode:** omformer AC til pulserende DC.
- **Zenerdiode:** arbeider kontrollert i sperreretning for spenningsreferanse/
  begrensning; seriemotstand må begrense strømmen.
- **LED:** avgir lys ved rekombinasjon; må strømbegrenses.
- **Varicap:** sperresjiktets kapasitans styres av reversspenningen og kan
  avstemme oscillatorer og filtre.

## 2.7 Likeretting, glatting og regulering

Kilder: `FAA-ELEC-2023` PDF-side 538–546; `MIT-POWER` PDF-side 1–2 og 1;
`ADI-SWREG`; `HAREC-2024` PDF-side 17.

![Bro-likeretter med glatting](figurer/bro-likeretter.svg)

I en bro leder to dioder hver halvperiode, slik at lasten får samme polaritet
for begge halvperioder. Kondensatoren lades nær toppene og leverer laststrøm
mellom dem. For fullbølgelikeretting er rippelfrekvensen dobbelt nettfrekvensen.
En nyttig første tilnærming er `ΔU≈Ilast/(frippel·C)`.

Eksempel: `Ilast=0,10 A`, `frippel=100 Hz`, `C=2200 µF` gir
`ΔU≈0,10/(100·0,0022)=0,455 V` topp-til-topp. En regulator trenger nok
inngangsmargin gjennom hele rippelen og må tåle effekttapet
`P≈(Uinn−Uut)I`.

HAREC krever også svitsjede forsyninger, isolasjon og EMC. En svitsjet forsyning
regulerer ved høyfrekvent av/på-drift og kan være effektiv, men raske kanter
gjør skjerming, layout og inngangs-/utgangsfiltre viktige. Galvanisk isolasjon
kan ikke antas bare fordi utgangen er lavspent; den avhenger av topologien og
konstruksjonen.

## 2.8 Bipolartransistor og FET

Kilder: `FAA-ELEC-2023` PDF-side 546–550; `MIT-TRANSISTOR` PDF-side 1;
`HAREC-2024` PDF-side 17.

En bipolar transistor (NPN/PNP) er strømstyrt i den enkle modellen:
`IC≈βIB`. En liten baseendring styrer større kollektorstrøm. FET er i hovedsak
spenningsstyrt; gatespenningen styrer drainstrømmen og inngangsstrømmen er
svært liten i normal drift.

| Kobling | Typisk spenningsforsterkning | Innimpedans | Utimpedans | Fase |
|---|---|---|---|---|
| Felles emitter/source | høy | middels/høy | middels/høy | inverterer |
| Felles kollektor/drain | omtrent 1 | høy | lav | inverterer ikke |
| Felles base/gate | høy | lav | høy | inverterer ikke |

Transistoren må ha et arbeidspunkt. For lite styresignal gir avstenging;
for stort gir metning/klipping. Begge skaper ikke-lineær forvrengning og nye
spektralkomponenter.

## 2.9 Forsterkerklasser og forvrengning

Kilder: `FAA-ELEC-2023` PDF-side 554–559; `HAREC-2024` PDF-side 18.

- Klasse A leder hele perioden: god linearitet, lav virkningsgrad.
- Klasse B leder omtrent en halv periode per transistor: bedre virkningsgrad,
  men overgangsforvrengning uten korrekt push-pull-utforming.
- Klasse AB leder mer enn en halv, men mindre enn hel periode: kompromiss.
- Klasse C leder mindre enn en halv periode: høy effektivitet og sterk
  forvrengning; brukes med avstemt RF-krets, ikke for lineær AM/SSB.

Harmonisk forvrengning gir heltallsmultipler av ett signal. Intermodulasjon
mellom `f1` og `f2` gir blant annet `f1±f2`, `2f1−f2` og `2f2−f1`; produktene
nær ønsket signal er vanskelige å filtrere bort. Overstyring av et SSB-trinn
kan derfor gi splatter utenfor nødvendig båndbredde.

## 2.10 Kontrolloppgaver

Egenproduserte oppgaver fra de kildebelagte formlene.

1. Et trinn øker effekt fra 2 W til 50 W. Finn dB-forsterkningen.
2. `R=2,2 kΩ`, `C=4,7 nF`. Finn knekkfrekvensen.
3. En parallellresonans har `f0=7,1 MHz`, `Q=100`. Finn båndbredden.
4. En 12 V-forsyning gir 5 V/0,4 A med lineær regulator. Finn omtrent
   regulatortapet.
5. Hvorfor egner klasse C seg dårlig til SSB?

Fasit: 1) `14,0 dB`. 2) `15,4 kHz`. 3) `71 kHz`. 4) `2,8 W`.
5) Ledningsvinkelen gir kraftig ikke-linearitet som endrer SSB-konvolutten og
lager intermodulasjon; et avstemt trinn kan gjenopprette en konstantbærer, men
ikke et vilkårlig lineært amplitudesignal.
