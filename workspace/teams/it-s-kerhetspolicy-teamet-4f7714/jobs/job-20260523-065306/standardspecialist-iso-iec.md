# Standardspecialist (ISO/IEC)

# ISO/IEC-analys: MissionPoints IT- och Informationssäkerhetspolicy v1.0

**Roll:** Standardspecialist ISO/IEC | **Fas:** Regulatorisk kartläggning & analys
**Datum:** 2026-02-27 | **Granskad policy:** MissionPoint AB, IT- och Informationssäkerhetspolicy v1.0

---

## 1. Analysens scope och antaganden

### Tillämpliga standarder i denna analys
| Standard | Motivering för tillämpning |
|---|---|
| **ISO/IEC 27001:2022** | Primär strukturstandard; de facto krav vid offentlig upphandling i Sverige. MissionPoint är konsultorganisation med kunder i reglerade sektorer — NIS2-kundernas leverantörskrav aktiverar indirekt. |
| **ISO/IEC 27002:2022** | Kontrollkatalog för operationell implementation — används för att bedöma täckning av specifika kontroller. |
| **ISO/IEC 27005:2022** | Riskhanteringsstandard — bedömer om policyns riskbaserade ansats är tillräckligt operationaliserad. |
| **ISO/IEC 27036-1/-2** | Leverantörssäkerhet — aktiveras av kap. 11 i policyn. |
| **ISO/IEC 27018:2019** | Personuppgifter i molntjänster — aktiveras av kap. 7.1 + kap. 11.1 (EU/EES-lagring). |

### Explicita antaganden
> ⚠️ **Antagande 1:** MissionPoint är inte NIS2-klassificerat som viktig eller väsentlig verksamhet i egen rätt, men agerar leverantör till sådana organisationer. Leverantörskedjeartikeln (NIS2 art. 21.3) aktiverar därmed indirekta krav på MissionPoints egna säkerhetsnivå.
>
> ⚠️ **Antagande 2:** MissionPoint saknar formell ISO 27001-certifiering idag. Analysen görs mot standarden som best-practice-referens och marknadskrav, inte som certifieringsrevision.
>
> ⚠️ **Antagande 3:** Policyn v1.0 är organisationens primära (och enda kända) styrdokument för informationssäkerhet. Inga underliggande riktlinjer, instruktioner eller processbeskrivningar antas existera.

---

## 2. Mappning: ISO 27001:2022 klausuler vs. policyinnehåll

### Klausul 4 — Organisationens kontext

| Krav (ISO 27001 kl. 4) | Status i policyn | Fynd |
|---|---|---|
| **4.1** Förstå organisationen och dess kontext (interna/externa faktorer) | ❌ Saknas | Ingen analys av affärskontext, marknad, konkurrenter, lagkrav som driver ISMS-behovet |
| **4.2** Förstå intressenters behov och förväntningar | ⚠️ Partiell | Kap. 5 nämner att kunder kan ställa krav, men ingen systematisk intressentanalys |
| **4.3** Fastställa ISMS-scope | ⚠️ Partiell | Kap. 3 definierar scope men saknar geografiska gränser, systeminventarium och explicit undantag |
| **4.4** Etablera, implementera, underhålla och kontinuerligt förbättra ISMS | ❌ Saknas | Policyn beskriver inte ett ISMS som system — ingen Plan-Do-Check-Act-struktur omnämns |

**Gap-bedömning kl. 4:** Kritisk brist. Utan kontextanalys och definierat ISMS-scope kan ingen av de efterföljande klausulerna implementeras korrekt. En policy utan scope-definition kan inte revideras, certifieras eller kommuniceras meningsfullt.

---

### Klausul 5 — Ledarskap

| Krav (ISO 27001 kl. 5) | Status i policyn | Fynd |
|---|---|---|
| **5.1** Ledningens engagemang och ansvar | ⚠️ Partiell | Kap. 12 nämner att "ledningen ansvarar för att denna policy finns och följs" — extremt generellt, saknar konkret ledningsåtagande |
| **5.2** Informationssäkerhetspolicy (ledningsnivå, kommuniceras, upprätthålls) | ⚠️ Partiell | Policyn existerar men saknar: (a) explicit koppling till verksamhetsmål, (b) mätbara åtaganden, (c) dokumenterad ledningsgodkännande med namngiven befattningshavare |
| **5.3** Organisatoriska roller, ansvar och befogenheter | ⚠️ Partiell | Kap. 6 utnämner CIO som informationssäkerhetsansvarig — men saknar: befogenheter, rapporteringsväg till ledning, delegationsstruktur, och skillnad mot ISO 27001:s krav på att rollen *rapporterar om ISMS-prestanda till högsta ledning* |

**Specifikt fynd kl. 5.2 — ISO 27001 krav på ledningspolicyn:**
ISO 27001:2022 kl. 5.2 kräver att policyn explicit:
- (a) Är lämplig för organisationens syfte ✅
- (b) Innehåller informationssäkerhetsmål *eller* ett ramverk för att fastställa dessa ❌
- (c) Inkluderar ett åtagande om att uppfylla tillämpliga krav ❌ (GDPR nämns men NIS2, ISO 27001 och MSB-föreskrifter saknas)
- (d) Inkluderar ett åtagande om kontinuerlig förbättring ❌

---

### Klausul 6 — Planering

| Krav (ISO 27001 kl. 6) | Status i policyn | Fynd |
|---|---|---|
| **6.1.1** Åtgärder för att hantera risker och möjligheter (allmänt) | ❌ Saknas | Ingen process för att identifiera och hantera risker som hotar ISMS-mål |
| **6.1.2** Riskbedömningsprocess | ❌ Saknas | Kap. 6 nämner "riskbaserat arbete" men definierar ingen process, inga kriterier, ingen metod, ingen frekvens |
| **6.1.3** Riskbehandlingsplan | ❌ Saknas | Inget omnämnande av hur identifierade risker behandlas, accepteras, eller överförs |
| **6.2** Informationssäkerhetsmål och planering | ❌ Saknas | Inga mätbara mål, inga KPI:er, ingen plan för hur mål ska uppnås |

**Gap-bedömning kl. 6:** Kritisk brist. "Riskbaserat arbete" utan en definierad riskprocess är en deklaration utan substans. ISO 27001 kräver att riskbedömningsprocessen är *dokumenterad*, *reproducerbar* och producerar *jämförbara resultat*.

---

### Klausul 7 — Stöd

| Krav (ISO 27001 kl. 7) | Status i policyn | Fynd |
|---|---|---|
| **7.1** Resurser | ❌ Saknas | Inga resurstilldelningar för säkerhetsarbetet |
| **7.2** Kompetens | ❌ Saknas | Inga kompetenskriterier för säkerhetsroller |
| **7.3** Medvetenhet | ❌ Saknas | Ingen policy för säkerhetsmedvetenhet, utbildning eller kommunikation |
| **7.4** Kommunikation | ❌ Saknas | Hur, när och till vem kommuniceras säkerhetsinformation? |
| **7.5** Dokumenterad information | ⚠️ Partiell | Kap. 14–15 nämner revision och revisionshistorik, men saknar dokumenthierarkibeskrivning, klassificering av dokument, och versionskontrollkrav |

---

### Klausul 8 — Drift

| Krav (ISO 27001 kl. 8) | Status i policyn | Fynd |
|---|---|---|
| **8.1** Driftplanering och styrning | ❌ Saknas | Ingen styrning av hur säkerhetsprocesser operationaliseras i det dagliga arbetet |
| **8.2** Informationssäkerhetsriskbedömning | ❌ Saknas | Se kl. 6.1.2 — processen saknas genomgående |
| **8.3** Informationssäkerhetsriskbehandling | ❌ Saknas | Se kl. 6.1.3 |

---

### Klausul 9 — Utvärdering av prestanda

| Krav (ISO 27001 kl. 9) | Status i policyn | Fynd |
|---|---|---|
| **9.1** Övervakning, mätning, analys och utvärdering | ❌ Saknas | Inga mätpunkter, inga mätmetoder, ingen frekvens |
| **9.2** Internrevision | ❌ Saknas | Kap. 14 nämner "ses över minst årligen" — men ingen internrevision, ingen revisionsplan, inga kriterier |
| **9.3** Ledningens genomgång | ❌ Saknas | Ingen ledningsgenomgångsprocess definierad |

---

### Klausul 10 — Förbättring

| Krav (ISO 27001 kl. 10) | Status i policyn | Fynd |
|---|---|---|
| **10.1** Kontinuerlig förbättring | ❌ Saknas | Ingen förbättringsprocess, ingen koppling till incidenter → förbättring |
| **10.2** Avvikelse och korrigerande åtgärder | ⚠️ Partiell | Kap. 9 nämner "rotorsak och förebyggande åtgärder" vid incidenter — men ingen formell avvikelsehanteringsprocess |

---

## 3. Mappning: ISO 27002:2022
