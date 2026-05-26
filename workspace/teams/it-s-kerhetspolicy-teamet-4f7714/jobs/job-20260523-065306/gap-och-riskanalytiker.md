# Gap- och Riskanalytiker

# Gap-analys & Riskvärdering: MissionPoint AB
## IT- och Informationssäkerhetspolicy v1.0 — Prioriterad Risklista

**Roll:** Gap- och Riskanalytiker
**Fas:** Fas 2 — Gap-analys & Riskvärdering
**Datum:** 2026-02-27
**Underlag:** Regulatorisk Complianceanalytiker, Standardspecialist (ISO/IEC), IT-säkerhetspolicygranskar, Hotbildsrådgivare

---

## 1. Metodologi och värderingsmodell

### Riskformel
> **Riskpoäng = Sannolikhet (1–5) × Konsekvens (1–5)** | Max: 25

| Nivå | Poäng | Åtgärdshorisont |
|---|---|---|
| 🔴 **Kritisk** | 16–25 | 0–30 dagar |
| 🟠 **Hög** | 9–15 | 90 dagar |
| 🟡 **Medium** | 4–8 | 6 månader |
| 🟢 **Låg** | 1–3 | Ordinarie revision |

### Konsekvensparametrar (vad värderas)
- **Regulatorisk exponering** — sanktionsrisk, tillsynsrisk, avtalsbrott
- **Operationell skada** — förlust av funktionsförmåga, driftstörning
- **Affärsskada** — förtroende, kundförlust, competitive damage
- **Hotaktörsexponering** — hur direkt luckan är utnyttjbar av identifierade hotaktörer

### Sannolikhetskalibrering
Sannolikhet bedöms mot tre faktorer: (1) hur vanligt fyndet är i liknande organisationer, (2) hur aktuella hotaktörer opererar mot just denna typ av organisation, (3) huruvida inga kompenserande kontroller kan antas existera (Antagande 3 från Standardspecialist: policyn är ensamt styrdokument).

---

## 2. Konsoliderad Gap-inventering

Nedanstående är en samlad inventering av alla identifierade luckor från fas 1, normaliserade och deduplicerade inför riskvärdering. Totalt **23 identifierade gap**.

| Gap-ID | Beskrivning | Primär källa (fas 1) | Regulatorisk koppling |
|---|---|---|---|
| G-01 | Ingen formell riskhanteringsprocess | Standardspecialist, IT-granskar | ISO 27001 kl. 6.1, 27005 |
| G-02 | Incidenthantering — saknar roller, tidsgränser, eskalering och NIS2-rapporteringskedja | Complianceanalytiker, IT-granskar, Hotbildsrådgivare | NIS2 art. 23, GDPR art. 33–34 |
| G-03 | Tillgångshantering / systeminventarium saknas helt | IT-granskar | ISO 27001 A.5.9–A.5.10 |
| G-04 | Åtkomstkontroll och IAM saknas (inga behörighetsprinciper, ingen offboarding) | IT-granskar, Hotbildsrådgivare | ISO 27001 A.5.15–A.5.18 |
| G-05 | Business Continuity / Disaster Recovery saknas | IT-granskar, Standardspecialist | ISO 27001 kl. 8.8, NIS2 art. 21 |
| G-06 | Kryptering och nyckelhantering — inga tekniska krav specificerade | IT-granskar | ISO 27001 A.8.24–A.8.25, GDPR art. 32 |
| G-07 | Säkerhetsmedvetenhet och utbildning saknas | IT-granskar, Hotbildsrådgivare | ISO 27001 A.6.3 |
| G-08 | Sårbarhetsbedömning och patchhantering saknas | IT-granskar | ISO 27001 A.8.8 |
| G-09 | Nätverkssäkerhet och segmentering saknas | IT-granskar, Hotbildsrådgivare | ISO 27001 A.8.20–A.8.22 |
| G-10 | Informationsklassificeringsschema saknas (bara lista på datatyper) | Complianceanalytiker, Standardspecialist | ISO 27002 A.5.12, MSB MSBFS 2020:6 |
| G-11 | Leverantörsstyrning — säkerhetskrav, avtalsvillkor och uppföljning underspecificerat | Complianceanalytiker, IT-granskar | NIS2 art. 21.3, GDPR art. 28, ISO 27036 |
| G-12 | GDPR-biträdesroll ej adresserad (MissionPoint agerar troligen personuppgiftsbiträde) | Complianceanalytiker | GDPR art. 28 |
| G-13 | Säkerhetsskyddslagen — oklart om tillämplig; "säkerhetskänslig information" nämns utan koppling | Complianceanalytiker | Säkerhetsskyddslagen 2018:585 |
| G-14 | CISO/informationssäkerhetsansvarig — delegationsmekanism otydlig, mandat odefinierat | Standardspecialist, IT-granskar | ISO 27001 kl. 5.3 |
| G-15 | Inga mätbara säkerhetsmål eller KPI:er | Standardspecialist | ISO 27001 kl. 6.2 |
| G-16 | Ingen separat informationssäkerhetspolicy på styrelsenivå | Standardspecialist | ISO 27001 kl. 5.2 |
| G-17 | Distansarbete — VPN, kryptering och hemmanätverks­säkerhet ej specificerat | IT-granskar | ISO 27001 A.6.7 |
| G-18 | AI-verktyg — ingen kontroll av vilka AI-verktyg som är godkända, ingen riskklassificering av verktyg | IT-granskar | GDPR art. 32, kundavtal |
| G-19 | Supply chain-attackvektorer ej adresserade (MissionPoint som angreppsväg mot kunder) | Hotbildsrådgivare | NIS2 art. 21.3 |
| G-20 | Microsoft 365 / molnspecifika säkerhetskrav saknas (MFA, Conditional Access, etc.) | Hotbildsrådgivare | ISO 27017, ISO 27018 |
| G-21 | Fysisk säkerhet saknas helt | IT-granskar | ISO 27001 A.7.1–A.7.14 |
| G-22 | Loggning, övervakning och auditspår saknas | IT-granskar, Hotbildsrådgivare | ISO 27001 A.8.15–A.8.17 |
| G-23 | Revisions- och granskningsprocess underspecificerad (policyn säger "minst årligen" utan mer) | Standardspecialist | ISO 27001 kl. 9.2–9.3 |

---

## 3. Prioriterad Risklista

### 🔴 KRITISK — Åtgärd inom 0–30 dagar

---

#### RISK-01 | Ingen riskhanteringsprocess
**Gap:** G-01
**Riskpoäng:** 5 × 5 = **25/25**

| Parameter | Värde | Motivering |
|---|---|---|
| Sannolikhet | 5 | Utan dokumenterad process är det faktiskt omöjligt att arbeta riskbaserat — detta är inte ett hypotetiskt gap utan ett faktiskt funktionsbortfall |
| Konsekvens | 5 | Alla andra kontroller saknar grund; regulatoriska revisioner kan underkänna hela ISMS-strukturen; kundkrav kan inte mötas |

**Regulatorisk exponering:**
- ISO 27001 kl. 6.1 — kräver dokumenterad riskbedömningsprocess
- ISO 27005:2022 — riskhantering som systematisk process
- NIS2 art. 21 — riskbaserade säkerhetsåtgärder är ett explicit krav för leverantörer i kedjan

**Hotaktörskoppling:** Utan riskhantering kan MissionPoint inte identifiera att APT29:s och APT28:s specifika angreppsvektorer (credential harvesting, M365-kompromittering) är prioriterade hot mot just deras verksamhetsprofil.

**Åtgärd:** Dokumentera och besluta en riskbedömningsprocess som minimum innehåller: riskidentifiering, riskanalys (sannolikhet × konsekvens), riskägarskap och acceptanskriterier. Formalisera i ett separat riskhanterings­dokument.

---

#### RISK-02 | Incidenthantering saknar operationell substans
**Gap:** G-02
**Riskpoäng:** 5 × 5 = **25/25**

| Parameter | Värde | Motivering |
|---|---|---|
| Sannolikhet | 5 | En incident är inte ett "om" utan ett "när"; utan process kommer hanteringen att misslyckas vid första skarpa läge |
| Konsekvens | 5 | GDPR art. 33: 72-timmarsgräns för tillsynsmyndighetens rapportering; NIS2-kunders avtalskrav; direkt kundskada och förtroendeskada |

**Regulatorisk exponering:**
- **GDPR art. 33–34** — 72-timmarsgräns till IMY; skyldighet att informera registrerade vid hög risk. **Direkt sanktionsrisk.**
- **GDPR art. 28** — om MissionPoint agerar biträde gäller striktare skyldigheter att omedelbart rapportera till personuppgiftsansvarig kund
- **NIS2 art. 23** — kunder i NIS2-klassificerad verksamhet har sannolikt avtalskrav på MissionPoint som leverantör att rapportera incidenter inom definierade tidsramar

**Hotaktörskoppling:** Ransomware (Lockbit 3.0, Black Basta) och APT29 supply chain-intrång kräver snabb detektering och eskalering. Policy §9 listar
