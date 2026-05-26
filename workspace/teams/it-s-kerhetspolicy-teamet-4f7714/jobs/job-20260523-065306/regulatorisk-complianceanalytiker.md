# Regulatorisk Complianceanalytiker

# Regulatorisk Kartläggning & Granskningsbaseline
## MissionPoint AB — IT- och Informationssäkerhetspolicy v1.0

**Producerad av:** Regulatorisk Complianceanalytiker
**Datum:** 2025 (granskning initierad)
**Status:** Underlag för Fas 1 — Inventering & gap-analys

---

## 1. Organisationsprofil & Regulatoriska Antaganden

### 1.1 Vad vi vet om MissionPoint AB

Baserat på policydokumentet kan följande konstateras om organisationen:

| Parameter | Bedömning | Källa |
|---|---|---|
| Verksamhetstyp | Rådgivande konsultorganisation | Policy §4 |
| Marknad | Sverige | Framgår av adress och kontext |
| Roll mot kunder | Rådgivare — normalt ej operativt systemägarskap | Policy §4 |
| Datatyperna man hanterar | Kunddokument, säkerhetsanalyser, systemåtkomst, personuppgifter, säkerhetskänslig information | Policy §7 |
| IT-modell | Outsourcade IT- och molntjänster används | Policy §11 |
| Arbetsmodell | Hybrid (distansarbete förekommer) | Policy §10 |
| AI-verktygsanvändning | Aktivt (ChatGPT, Copilot, Claude m.fl.) | Policy §8 |

### 1.2 Regulatoriska Antaganden (explicita)

Följande antaganden görs i avsaknad av fullständig organisations­information. Dessa **måste valideras med MissionPoint** innan granskningsmandatet är komplett:

> **Antagande A1:** MissionPoint är *inte* klassificerad som väsentlig eller viktig verksamhet under NIS2 i sin primära roll som konsultbolag. Dock kan bolaget vara indirekt NIS2-berörd som **leverantör till** NIS2-klassificerade kunder (art. 21.2b och art. 21.3 om leverantörskedjor). NIS2 tillämpas därmed på leverantörsnivå, inte som primär aktör.

> **Antagande A2:** MissionPoint hanterar personuppgifter (framgår av §7 och §7.1) och är därmed **personuppgiftsansvarig** under GDPR. Man agerar sannolikt även som **personuppgiftsbiträde** i vissa kunduppdrag — vilket skapar separata GDPR-förpliktelser (art. 28).

> **Antagande A3:** Säkerhetsskyddslagen (2018:585) kan vara aktuell om MissionPoint arbetar med kunder inom försvar, rättsvård eller annan säkerhetsskydds­klassad verksamhet. Policy §7 nämner "säkerhetskänslig information" — detta **kräver omedelbar klarläggning** med kunden.

> **Antagande A4:** MSB:s föreskrifter (MSBFS 2020:6 / 2023:1) bedöms *inte* direkt tvingande för ett privat konsultbolag, men är *de facto* referens­standard vid offentlig upphandling och kundkrav.

> **Antagande A5:** DORA är *inte* primärt tillämpligt. MissionPoint är ingen finansiell aktör. Indirekt relevans uppstår om MissionPoint levererar tjänster till finansiella entiteter (banker, försäkringsbolag) — sådana kunder ställer då DORA-krav nedåt i leverantörskedjan.

---

## 2. Tillämpliga Regulatoriska Ramverk — Normativ Granskningsbaseline

### 2.1 Ramverk med direkt tvingande verkan för MissionPoint

#### GDPR (EU 2016/679) + Dataskyddslagen (2018:218)
**Tillämpningsnivå: OBLIGATORISK**

MissionPoint behandlar personuppgifter och träffas av GDPR i sin helhet. Nedan anges de artiklar som skapar **direkta krav på policynivå**:

| Artikel | Krav | Policykrav |
|---|---|---|
| Art. 5 | Grundläggande principer (ändamålsbegränsning, uppgiftsminimering, lagrings­begränsning) | Ska återspeglas i policy och informationsklassificering |
| Art. 6 | Laglig grund för behandling | Policy eller underliggande riktlinje måste ange lagliga grunder |
| Art. 13–14 | Informationsplikt till registrerade | Hanteras i integritetspolicy (refereras i §7.1) — men policyn måste säkerställa att den integritetspolicyn faktiskt existerar och är uppdaterad |
| Art. 17–21 | Registrerades rättigheter | Process för rättighetshantering saknas i policy |
| Art. 25 | Inbyggd dataskydd & dataskydd som standard | Krav på att dataskydd beaktas vid systemval — berör §11 |
| Art. 28 | Personuppgiftsbiträdesavtal | Explicit krav vid behandling på uppdrag av kund — delvis adresserat i §11 |
| Art. 32 | Lämpliga tekniska och organisatoriska säkerhets­åtgärder | Kräver konkreta kontroller — saknas i nuvarande policy |
| Art. 33–34 | Incidentrapportering (72 h till IMY, info till drabbade) | Delvis adresserat i §9 men utan 72-timmarsregel |
| Art. 35 | Konsekvensbedömning (DPIA) | Krav vid högrisk­behandling — nämns ej i policy |
| Art. 37–39 | Dataskyddsombud (DPO) | Bedömning av DPO-skyldighet saknas |

**Nationell komplettering:** Dataskyddslagen (2018:218) tillåter undantag och tillägg i svensk kontext (t.ex. behandling för journalistiska ändamål, forskning). Inga sådana undantag bedöms relevanta för MissionPoint.

---

#### NIS2 — Indirekt leverantörsperspektiv (EU 2022/2555 / Lag 2024:491)
**Tillämpningsnivå: INDIREKT OBLIGATORISK (leverantörskedja)**

MissionPoint är *inte* direkt NIS2-skyldig (se Antagande A1), men är exponerat via kunds NIS2-krav per art. 21.3:

> *"Väsentliga och viktiga entiteter ska vidta lämpliga och proportionella åtgärder för att hantera de cybersäkerhetsrisker som uppstår i leverantörskedjorna."*

Detta skapar följande **minimikrav som MissionPoint:s kunder kan ställa**:

| NIS2-artikel | Krav som flodar ner till MissionPoint som leverantör |
|---|---|
| Art. 21.2a | Policies för riskanalys och informationssystems­säkerhet |
| Art. 21.2b | Incidenthantering |
| Art. 21.2c | Drifts­kontinuitet och krishantering |
| Art. 21.2e | Säkerhet i leverantörskedjor |
| Art. 21.2h | Grundläggande cyberhygien och utbildning |
| Art. 21.2i | Kryptografi och kryptering |
| Art. 21.2j | HR-säkerhet, åtkomstkontroll, tillgångs­hantering |

**Konsekvens för granskning:** Policyn måste kunna uppvisa efterlevnad mot dessa punkter för att MissionPoint ska vara en godkänd leverantör i NIS2-reglerade kundkedjor.

---

### 2.2 Best Practice-standarder med de facto tvingande verkan

#### ISO/IEC 27001:2022
**Tillämpningsnivå: DE FACTO OBLIGATORISK (offentlig upphandling, kundkrav)**

ISO 27001 är den strukturella referensstandarden för granskningen. Nedan listas de klausuler som direkt genererar krav på policydokumentet:

| Klausul | Krav | Relevans för MissionPoints policy |
|---|---|---|
| 4.1 | Förstå organisationen och dess kontext | Scope-definition och externa krav ska framgå |
| 4.2 | Intressenters krav och förväntningar | Kundkrav, regulatoriska krav — ska kartläggas |
| 4.3 | ISMS-scope | Explicit scope­definition krävs |
| 5.1 | Ledningens åtagande | Ledningspolicy ska signeras och kommuniceras |
| 5.2 | Policy | Separat informationssäkerhetspolicy på ledningsnivå — distinkt från IT-policy |
| 5.3 | Roller och ansvar | CISO/informationssäkerhetsansvarig med tydligt mandat |
| 6.1 | Riskhantering (riskbedömning + riskbehandling) | Formell riskprocess krävs |
| 6.2 | Informationssäkerhetsmål | Mätbara mål och KPI:er |
| 7.2–7.3 | Kompetens och medvetenhet | Utbildnings­krav och säkerhets­medvetenhet |
| 7.4 | Kommunikation | Kommunikationsplan för säkerhetsfrågor |
| 8.1 | Operationell planering | Processer för säkerhets­kontroller |
| 8.2 | Informationssäkerhets­riskbedömning | Periodisk riskbedömning |
| 9.1 | Uppföljning och mätning | Mätmetoder och uppföljning |
| 9.2 | Internrevision | Revisions­program |
| 9.3 | Ledningens genomgång | Formell lednings­genomgång |
| 10.1–10.2 | Ständig förbättring och avvikelsehantering | Dokumenterad förbättrings­process |

**Annex A (ISO 27002:2022 kontroller) — kritiska för policy­granskning:**

| Kontroll-ID | Kontroll | Policynivå-relevans |
|---|---|---|
| A.5.1 | Policies för informationssäkerhet |
