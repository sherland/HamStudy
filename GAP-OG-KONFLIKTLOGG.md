# Gap- og konfliktlogg

Kontrollert: 2026-08-20

Loggen skiller mellom en faktisk konflikt, en tidsrisiko og manglende offentlig bekreftelse. «Uavklart» betyr at opplysningen ikke skal brukes som fakta eller flashkortfasit.

| ID | Sammenligning | Funn | Status | Konsekvens |
|---|---|---|---|---|
| G-01 | Bok 2025 mot forskrift 2026 | Bokas regelkapittel er eldre enn FOR-2026-03-23-465. Selve boksidene er ikke kontrollert, så konkrete tekstkonflikter er ikke fastslått. | `TIDSRISIKO` | Alle norske regler i kap. 12 og tabeller i kap. 16 må erstattes eller bekreftes mot `REGELVERK-2026.md`. |
| G-02 | Bokkapittel 14 mot HAREC-2024 | Aktiv T/R 61-02 er datert 2024, men vedlegg 6 heter fortsatt vedlegg 6 og er merket Edition 9, February 2018. | `INGEN_PÅVIST_KONFLIKT` | Matrisen bruker den aktive CEPT-filen; bokteksten bør fortsatt sidekontrolleres. |
| G-03 | Eldre norsk pensumliste mot HAREC | Ingen autoritativ eldre norsk pensumliste ble samlet inn som gjeldende kilde. | `UAVKLART` | Eldre kursplaner skal ikke definere dagens pensum. |
| G-04 | Nkom-nettside mot Lovdata | Nkom-siden bekrefter prøve/administrasjon og viser videre til forskriften. Ingen motstridende tallverdier ble funnet. Siden bruker enkelte steder den eldre formuleringen «forskriften om radioamatørlisens». | `TERMINOLOGI` | Juridiske vilkår og tall hentes fra Lovdata. |
| G-05 | NRRL/IARU-båndplan mot forskrift | Kildene har ulik funksjon: forskriften gir tillatelse, båndplanen anbefaler bruk. Den arkiverte IARU HF-planen er effektiv fra 2016 og kan være eldre enn senere operative revisjoner. | `IKKE_JURIDISK_KONFLIKT` | Ikke bruk båndplan som hjemmel eller eldre plan som automatisk gjeldende praksis. |
| G-06 | Effektbegreper | PEP/senderens utgangseffekt, gjennomsnittseffekt og e.i.r.p. er ikke synonymer. Forskriften definerer utgangseffekt som PEP og bruker e.i.r.p. i enkelte særvilkår. | `BEGREPSRISIKO` | Hvert spørsmål må angi målepunkt og effektbegrep; antennegevinst og linjetap inngår ved e.i.r.p. |
| G-07 | Full mot begrenset lisens | Full lisens er HAREC klasse A og har egne bånd/vilkår. Begrenset lisens gjelder bare i Norge og har egen frekvenstabell og utstyrsvilkår. | `BEKREFTET_FORSKJELL` | Hold kortstokker og tabeller tydelig merket; dette prosjektet retter seg mot full lisens. |
| G-08 | Gammel og ny norsk terminologi | Den bindende tittelen er «forskrift om radioamatørvirksomhet». Begrepene full lisens (HAREC klasse A) og begrenset lisens er sentrale fra 2026. | `TERMINOLOGI` | Normaliser nye kort til forskriftens ordlyd og behold eldre ord bare som søkealias. |
| G-09 | HAREC mot bokas innholdsfortegnelse | 45 av 58 mål er fullt indikert, 12 delvis og 1 ikke eksplisitt. Dette er ikke fulltekstkontroll. | `SIDEKONTROLL_NØDVENDIG` | Prioriter punktene i `BOKKARTLEGGING.md` før kortproduksjon. |
| G-10 | Offisiell eksamensinformasjon | Nkom bekrefter at NRRL arrangerer og Nkom lager spørsmål. Format, varighet, beståttgrense, hjelpemidler, utdelt formelsamling og overgangsdato for 2026-regler ble ikke funnet offentlig. | `UAVKLART` | Ikke bygg studietaktikk eller kortfasit på lokale eller eldre opplysninger uten skriftlig bekreftelse. |
| G-11 | Øvingsoppgaver/oppgavebank | Ingen offentlig, versjonsmerket oppgavebank eller gammelt eksamenssett ble funnet i de kontrollerte offisielle kildene. | `UAVKLART` | Matrisen er ikke stikkprøvekontrollert mot faktiske oppgavetyper. |
| G-12 | Sikkerhetsomfang | HAREC a.10 nevner kropp, strømnett, høyspenning og lyn. Bokas innholdsfortegnelse viser mer sikkerhetsstoff, blant annet EMF. | `TILLEGG_ELLER_NASJONALT` | Skill eksplisitt HAREC-minimum fra nyttig sikkerhetsopplæring og eventuelle nasjonale krav. |

## Prioritet før flashkort

1. Få skriftlig svar på G-10 og om hele vedlegg 6 er norsk eksamenspensum.
2. Sidekontroller G-01 og G-09 i brukerens trykte bok.
3. Kontroller en aktuell enkeltbåndplan før operative frekvensanbefalinger lages.
4. Bruk en eventuell offentlig, datert oppgavebank til stikkprøver uten å la eldre spørsmål overstyre nyere regelverk.
