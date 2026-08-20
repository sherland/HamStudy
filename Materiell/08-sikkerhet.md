# 8. Sikkerhet ved radioamatørstasjonen

HAREC: `H-T10`.

HAREC krever kunnskap om menneskekroppen, strømnettet, høyspenning og lyn.
RF-eksponering, batterier, brann, lodding og antennearbeid tas også med fordi
de er relevante ved en virkelig stasjon og fremgår av bokas kapittel 13.

## Kildegrunnlag

- `HAREC-2024`, vedlegg 6, PDF-side 23, fastsetter de fire kjerneemnene.
- `DSB-STROM-2026` gir norske myndighetsråd om strømgjennomgang og medisinsk
  oppfølging.
- `DSB-LYN-2026` gir norske myndighetsråd om overspenningsvern og frakobling.
- `NKOM-EMF-2026` forklarer radiofrekvent eksponering, avstand og norske
  grenseverdier. DSA er den norske fagmyndigheten for strålevern.
- `USN-NEETS-10`, særlig kapittel 2, brukes for teknisk bakgrunn om
  høyspenning, RF-forbrenning og sikker utlading.

## 8.1 Fare oppstår når energi når kroppen

En faresituasjon kan beskrives som en kjede:

`energikilde → utilsiktet forbindelse → menneske/utstyr → skade`.

Sikkerhet bygges i flere uavhengige barrierer: sikker konstruksjon og
kapsling, frakobling og låsing, kontrollmåling, arbeidsavstand, riktig vern og
en plan for nødsituasjonen. Én bryter eller én sikring er ikke bevis på at en
krets er ufarlig.

Det er strømmen gjennom kroppen, strømveien og varigheten som bestemmer mye
av skaden. Hudens motstand varierer kraftig med fuktighet, kontaktflate,
trykk og sår. Derfor er påstanden «spenningen er for lav til å være farlig»
ikke en generell sikkerhetsregel. Hånd–hånd og hånd–fot kan føre strøm gjennom
overkroppen. Elektrisk strøm kan gi muskelkrampe, brannskade, påvirket
hjerterytme og pust og skader som ikke er synlige med en gang.

Ohms lov forklarer bare den elektriske sammenhengen. Hvis en forenklet
kroppsmotstand settes til 2 kΩ, gir 230 V beregnet strøm `I=230/2000=115 mA`.
Det er ikke en medisinsk modell: den virkelige impedansen og skadevirkningen
varierer, og tallet skal aldri brukes til å definere en «sikker» berøring.

## 8.2 Strømnettet

Nettspenning kan levere både farlig strøm og stor kortslutningsenergi. En
sikring beskytter primært ledningsanlegget mot overstrøm; den gjør ikke enhver
berøring ufarlig. Beskyttelsesjord fører feilstrøm fra tilgjengelige
metalldeler, og jordfeilvern kobler ut ved en differansestrøm, men ingen av
delene erstatter isolasjon og sikker arbeidsmåte.

Grunnregler ved en amatørstasjon:

- Bruk godkjent utstyr, riktige sikringer, strekkavlastning og hel kapsling.
- La kvalifiserte fagfolk utføre arbeid som tilhører den faste elektriske
  installasjonen. En radioamatørlisens er ikke en elektrikergodkjenning.
- Koble fra før kapslingen åpnes. Verifiser spenningsløs tilstand med egnet
  instrument; stol ikke bare på bryterstilling eller indikatorlampe.
- Et vanlig jordet oscilloskop har ofte probens jordklemme bundet til
  beskyttelsesjord. Den må ikke festes vilkårlig i en nett- eller flytende
  krets.
- Ikke mål motstand eller kontinuitet i en spenningssatt krets. Multimeterets
  strøminngang kan kortslutte kilden hvis det kobles parallelt.

Ved ulykke skal strømmen brytes uten at hjelperen selv blir strømvei. Ring 113
ved akutt fare. DSB sier at medisinsk hjelp skal oppsøkes umiddelbart etter
lavspenningsstrøm gjennom hjerteregion/overkropp, enhver
høyspenningsgjennomgang, lynnedslag, bevisstløshet/omtåkethet/uvelhet,
brannskade eller tegn på nerveskade. Medisinsk hjelp betyr fastlege, legevakt
eller medisinsk nødtelefon 113. Dette kapitlet erstatter ikke førstehjelpskurs.

## 8.3 Høyspenning og lagret energi

Rørforsterkere og enkelte strømforsyninger kan ha flere hundre eller tusen
volt. Faren kan bestå etter at nettpluggen er trukket ut fordi kondensatorer
lagrer energi:

`E = ½CU²`.

Eksempel: En kondensator på 100 µF ladet til 500 V lagrer
`E=0,5·100·10⁻⁶·500²=12,5 J`. Dobles spenningen, firedobles energien. En
bleeder-motstand kan tømme kondensatoren, men kan være defekt; spenningen må
kontrolleres med instrument og prosedyre dimensjonert for kretsen.

Hvis en 100 µF kondensator utlades gjennom 100 kΩ, er tidskonstanten
`τ=RC=10 s`. Etter fem tidskonstanter er en ideell kondensatorspenning under
én prosent av startverdien, men beregningen er ikke en erstatning for måling.
Andre kondensatorer, feil eller frakoblede motstander kan holde spenning.

Sikker konstruksjon kapsler berørbare deler, bruker avstand og isolasjon som
tåler spenningen, hindrer tilfeldig innkobling og sørger for kontrollert
utlading. Man arbeider ikke alene på eksponert høyspenning. Smykker og løse
metalldeler fjernes. Uerfarne skal ikke bruke dette kapitlet som oppskrift på
arbeid i en spenningssatt sender.

## 8.4 RF-spenning og RF-eksponering

En antenne, tuner og åpen transmisjonslinje kan ha høy RF-spenning selv om
senderens forsyning er lav. Berøring kan gi RF-forbrenning. Høy effekt,
spenningsmaksima ved stående bølger og små kontaktflater øker risikoen.

Radiofrekvente felt er ikke-ioniserende. Nkom beskriver den etablerte
helseeffekten ved for høy eksponering som oppvarming. Eksponeringen er størst
foran antennens hovedstråleretning og avtar raskt med avstand. Vurderingen må
ta hensyn til frekvens, effekt, antenneforsterkning og -retning, avstand,
sendetid/duty cycle og samtidig eksponering fra flere kilder.

Praktiske barrierer er å plassere antennen slik at mennesker ikke kan komme
inn i et område med for høy eksponering, bruke lavest nødvendig effekt,
begrense sendetid under prøving, og slå av/låse senderen før noen arbeider på
antennen. En enkel fjernfeltberegning kan brukes til grov kontroll, men nær
antennen kan nærfelt, refleksjoner og jord gjøre modellen utilstrekkelig.
Dokumentasjon mot gjeldende grenseverdier krever egnet metode og ved behov
kompetent måling; et ukalibrert «EMF-meter» er ikke nok.

## 8.5 Lyn og overspenning

Lyn kan koble energi inn direkte, gjennom strømnettet, antennekoaks,
nettverkskabel og jordforbindelser. Et direkte treff er ikke den eneste
faren: et nært treff kan indusere stor spenning, og DSB påpeker at svekket
utstyr kan feile eller begynne å brenne senere.

DSBs lagdelte råd er:

1. grovvern/overspenningsvern i sikringsskapet;
2. egnet finvern som supplement, ikke som erstatning for grovvern;
3. trekk ut støpsler, nettverks- og antennekabler når det lyner;
4. kontroller vernets indikator regelmessig og etter tordenvær.

En radioinstallasjon trenger i tillegg gjennomtenkt potensialutjevning,
jording og overspenningsavledning ved kabelinnføring. Lange separate
«jordledninger» kan få stor induktiv spenning under en rask lynpuls. Fast
lynbeskyttelse og installasjon skal prosjekteres av kvalifiserte fagfolk.
Ikke gå ut og håndter antenne eller jordleder mens tordenværet pågår.

## 8.6 Batterier, brann og lodding — praktisk tilleggsstoff

Et 12 V-batteri gir normalt ikke samme berøringsfare som nettspenning, men kan
levere svært høy kortslutningsstrøm. Sikringen plasseres nær batteriets
positive pol slik at også tilførselskabelen beskyttes. Beskytt polene mot
verktøy og smykker, bruk riktig polaritet og lader, og følg kjemi-spesifikke
krav til ventilasjon, temperatur og lagring. Oppsvulmet, lekkende eller skadet
batteri tas ut av bruk på sikker måte.

Effektmotstander, lineærforsterkere, strømforsyninger og dårlige forbindelser
kan bli varme. Hold ventilasjon fri, dimensjoner komponenter med margin og ha
egnet slokkemiddel og rømningsvei. Ved brann brytes energikilden hvis det kan
gjøres uten fare; ikke bruk vann på spenningssatt elektrisk utstyr.

Ved lodding brukes ventilasjon/avsug, vernebriller og stabil holder. Loddebolt
og varm komponent behandles som brannkilder. Vask hendene etter håndtering av
blyholdig loddetinn og kjemikalier, og følg sikkerhetsdatabladet for fluss og
rengjøringsmidler.

## 8.7 Master og antennearbeid — praktisk tilleggsstoff

Fall, fallende gjenstander, vær og nærliggende kraftlinjer er de store
farene. Planlegg løft og barduner, sperr området under arbeidet, og bruk
kompetanse og fallsikring som passer oppgaven. En mast eller lang antennedel
kan nå en kraftlinje selv om den står et stykke unna på bakken. Arbeid
stoppes ved torden, sterk vind, is eller utilstrekkelig sikt. Senderen låses
mot innkobling før antennearbeid.

## Fallgruver

- Å anta at frakoblet utstyr er spenningsløst når kondensatorer finnes.
- Å bruke en sikring eller et jordfeilvern som begrunnelse for å berøre nett.
- Å glemme at RF-spenning kan være høy ved antennens spenningsmaksimum.
- Å bruke en enkel fjernfeltformel ukritisk i nærfeltet.
- Å tro at et pluggbart finvern alene gjør antenne og stasjon lynsikker.
- Å undervurdere kortslutningsenergien i et lavspenningsbatteri.

## Kontrolloppgaver med fasit

1. Hvorfor kan frakoblet rørutstyr fortsatt være farlig?
2. En 47 µF kondensator står på 400 V. Hvor mye energi lagrer den?
3. Hva er forskjellen på en sikring og et jordfeilvern?
4. Nevn fem forhold som bestemmer RF-eksponering.
5. Hvorfor er finvern alene utilstrekkelig mot lynoverspenning?
6. Når sier DSB at medisinsk hjelp skal oppsøkes umiddelbart etter en
   strømulykke?

Fasit:

1. Kondensatorer kan beholde farlig spenning og energi etter frakobling.
2. `E=½·47·10⁻⁶·400²=3,76 J`.
3. Sikringen beskytter ledningsanlegget mot overstrøm; jordfeilvernet reagerer
   på differanse/lekkasjestrøm. Begge er tillegg til isolasjon og sikker bruk.
4. Frekvens, effekt, antenneforsterkning/-retning, avstand og sendetid; flere
   samtidige kilder og lokale feltforhold kan også ha betydning.
5. DSB sier at pluggbart finvern er et supplement til grov-/mellomvern, og
   energi kan også komme via antenne- og nettverkskabler.
6. Ved strøm gjennom overkropp/hjerteregion fra lavspenning, enhver
   høyspenningsgjennomgang, lyn, bevisstløshet/omtåkethet/uvelhet,
   brannskader eller tegn på nerveskade.
