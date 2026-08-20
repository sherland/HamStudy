# Kartlegging av læreboka mot HAREC

Kontrollert: 2026-08-20

## Grunnlag og tolkning

Kartleggingen gjelder *Veien til internasjonal radioamatørlisens*, 8. opplag (2025), og bygger på de tre bildene av innholdsfortegnelsen i `Bok/`. Den sammenholder synlige overskrifter og sidereferanser med de 58 læringsmålene i CEPT T/R 61-02, vedlegg 6.

Selve boksidene er ikke digitalisert eller kontrollert. Derfor betyr ikke «full» at hele bokteksten er verifisert. Dekningskodene i `data/pensummatrise.csv` betyr:

- `FULL_INDIKERT_FRA_TOC`: alle sentrale deltema ser ut til å ha en naturlig plass i de oppførte bokavsnittene.
- `DELVIS_INDIKERT_FRA_TOC`: bare deler av kravet er synlige, eller overskriftene er for generelle til å bekrefte hele kravet.
- `IKKE_INDIKERT_FRA_TOC`: temaet kan finnes i brødteksten, men er ikke synlig i innholdsfortegnelsen.

Resultatet er 45 læringsmål med full indikasjon, 12 med delvis indikasjon og 1 som ikke er uttrykkelig angitt. Den detaljerte, maskinlesbare kartleggingen står i `data/pensummatrise.csv`.

## Hovedkart

| Bokkapittel | Hovedinnhold | HAREC-områder |
|---|---|---|
| 1 Innledning | Radioamatørvirksomhet og grunnlag | Innledende matematikk/enheter, delvis |
| 2 Grunnleggende elektronikk | Strøm, spenning, passive komponenter, AC og resonans | a.1 og a.2; deler av a.3 |
| 3 Halvledere og rør | Dioder, transistorer, forsterkere, strømforsyning | a.2.5–a.2.7 og deler av a.3 |
| 4 Senderen | Modulasjon, oscillatorer, sendertrinn og effekt | a.1.8–a.1.9, a.3.4/a.3.6 og a.5 |
| 5 Senderforstyrrelser | Uønsket utstråling og mottiltak | a.5.4 og a.9 |
| 6 Mottakeren | Mottakertyper, trinn, deteksjon og egenskaper | a.3.5 og a.4 |
| 7 DSP | Sampling, filtre, Fourier og DDS | a.1.10 og a.3.8 |
| 8 Mateledninger og antenner | Transmisjonslinjer, antenner og tilpasning | a.6; deler av a.1.5 og a.7 |
| 9 Bølgeutbredelse | Ionosfære, troposfære, fading og spesialmodi | a.7 |
| 10 EMC | Kobling, skjerming, filtrering og avkobling | a.1.3–a.1.4, a.3.3 og a.9 |
| 11 Måleteknikk | Målemetoder og instrumenter | a.8 og deler av a.1.9 |
| 12 Trafikk og regler | Prosedyrer, kallesignal, internasjonale og norske regler | b.5–b.7 og c.1–c.3 |
| 13 Sikkerhet | Elektrisk, fysisk og RF-relatert sikkerhet | a.10; i tillegg bokstoff utover den korte HAREC-listen |
| 14 CEPT T/R 61-02 vedlegg 6 | Pensumoversikt | Hele HAREC-strukturen som referanse |
| 15 Nettsteder | Videre kilder | Støttemateriale, ikke eget HAREC-punkt |
| 16 Tabeller | Båndplan, Q-koder, RST og fonetisk alfabet | b.1–b.3 og b.6 |

## Punkter som må sidekontrolleres

Disse funnene er ikke konstaterte hull. De er prioriterte steder å kontrollere i den trykte boka før flashkort lages:

1. Symboler (`H-INTRO-B`) er ikke uttrykkelig nevnt i innholdsfortegnelsen.
2. Hele matematikkgrunnlaget, blant annet logaritmer, grafer, binært tallsystem og formelomforming, er ikke eksplisitt listet.
3. Elektriske og magnetiske felt, termisk støy og enkelte digitale feilrettingsbegreper er bare indirekte synlige.
4. Svitsjet strømforsyning med isolasjon/EMC og PLL som egen reguleringssløyfe er ikke tydelig angitt.
5. HARECs komplette linkbudsjett er ikke synlig som egen overskrift i kapittel 9.
6. `SOS`, `MAYDAY`, katastrofesamband og Radio Amateur Code of Conduct er ikke uttrykkelig nevnt.
7. CEPT-reglene i T/R 61-01 må kontrolleres mot gjeldende 2024-utgave, selv om boka har et CEPT-avsnitt.

## Tidskritiske deler

Kapittel 12 ble utgitt før forskrift FOR-2026-03-23-465 trådte i kraft. Bokas norske lisensregler, effektgrenser, bånd, kallesignalregler og eventuelle klasseinndelinger skal derfor ikke brukes som siste autoritet. Bruk `REGELVERK-2026.md` og de arkiverte primærkildene.

Kapittel 14 viser til HAREC-pensumet. Den aktive CEPT T/R 61-02-utgaven er fra 2024, mens vedlegg 6 fortsatt er merket «Edition 9, February 2018». Bokas 2025-opplag kan dermed være godt samsvarende, men dette dokumentet og matrisen bruker den aktive CEPT-filen som fasit.

Båndplanene i kapittel 16 er anbefalt operativ bruk, ikke selve den norske frekvenstillatelsen. De må sammenholdes med gjeldende norsk forskrift og oppdaterte IARU/NRRL-båndplaner.

## Videre bruk

Ved senere produksjon av flashkort bør hvert kort få én eller flere HAREC-ID-er, bokreferanse der den er sidekontrollert, primærkilde og kontrollert dato. Kort basert på et delvis eller ikke indikert bokpunkt bør ikke godkjennes før innholdet er kontrollert mot primærkilden.
