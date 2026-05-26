# Projektledare & Granskningskoordinator · Slutleverans

# Fullständig granskning: MissionPoints IT- och Informationssäkerhetspolicy v1.0

Detta dokument är IT-säkerhetsteamets slutleverans: en komplett granskning av MissionPoint ABs IT- och Informationssäkerhetspolicy v1.0, med gap-analys, riskvärdering, konkreta åtgärdsförslag och färdig ersättningspolicytext för kritiska avsnitt. Leveransen är direkt handlingsbar för IT-chef och informationssäkerhetsansvarig.

---

## Del 1 — Vad är bra i policyn

Policyn är ett välskrivet och välintentionerat grunddokument. Följande delar fungerar och ska bevaras i nästa version:

| Styrka | Varför det håller |
|---|---|
| **Scopet är väldefinierat (§3)** | Täcker anställda, konsulter och uppdragstagare — ingen gråzon kring vem som omfattas |
| **AI-reglering är proaktiv (§8)** | Konkret förbud mot att dela känslig information med AI-verktyg; tydliga exempel på tillåtet och förbjudet — långt framme jämfört med branschnorm |
| **Rollen mot kunder är tydlig (§4–5)** | Policyn erkänner leverantörsrollen och NIS2-indirektheten utan att överdriva eget ansvar |
| **Datageografi adresseras (§11.1)** | EU/EES-prioritering för molntjänster är explicit och direkt relevant för GDPR-efterlevnad |
| **Personuppgifter hanteras separat (§7.1)** | GDPR-hänvisning och koppling till Integritetspolicyn är korrekt strukturerat |
| **Hybridarbete är reglerat (§10)** | Grundläggande regler för distansarbete finns — ovanligare än man tror i policydokument av denna typ |

---

## Del 2 — Gap-matris: 23 identifierade luckor

Nedan samtliga identifierade gap mot GDPR, NIS2, ISO 27001:2022, ISO 27005 och MSB-föreskrifter, rangordnade efter prioritet.

| Gap-ID | Beskrivning | Regulatorisk koppling | Prioritet |
|---|---|---|---|
| G-01 | Ingen formell riskhanteringsprocess | ISO 27001 kl. 6.1, ISO 27005 | 🔴 Kritisk |
| G-02 | Incidenthantering saknar roller, tidsgränser, eskalering och rapporteringsplikt | GDPR art. 33–34, NIS2 art. 23 | 🔴 Kritisk |
| G-03 | Tillgångshantering och systeminventarium saknas helt | ISO 27001 A.5.9–A.5.10 | 🔴 Kritisk |
| G-04 | Åtkomstkontroll och IAM saknas (inga behörighetsprinciper, ingen offboarding) | ISO 27001 A.5.15–A.5.18, GDPR art. 25 | 🔴 Kritisk |
| G-05 | Säkerhetsskyddslagen — "säkerhetskänslig information" nämns utan definition eller hanteringsregler | Säkerhetsskyddslagen 2018:585 | 🔴 Kritisk |
| G-06 | Business Continuity / Disaster Recovery saknas | ISO 27001 kl. 8.8, NIS2 art. 21 | 🟠 Hög |
| G-07 | Kryptering och nyckelhantering — inga tekniska krav | ISO 27001 A.8.24–A.8.25, GDPR art. 32 | 🟠 Hög |
| G-08 | Säkerhetsmedvetenhet och utbildning saknas | ISO 27001 A.6.3 | 🟠 Hög |
| G-09 | Sårbarhetsbedömning och patchhantering saknas | ISO 27001 A.8.8 | 🟠 Hög |
| G-10 | CISO/informationssäkerhetsansvarigs mandat och rapporteringsväg otydlig | ISO 27001 kl. 5.3 | 🟠 Hög |
| G-11 | Inga mätbara säkerhetsmål eller KPI:er | ISO 27001 kl. 6.2 | 🟠 Hög |
| G-12 | Leverantörsstyrning — säkerhetskrav, avtalsvillkor och uppföljning underspecificerat | NIS2 art. 21.3, GDPR art. 28, ISO 27036 | 🟠 Hög |
| G-13 | Loggning, övervakning och auditspår saknas | ISO 27001 A.8.15–A.8.17 | 🟠 Hög |
| G-14 | Supply chain-attackvektorer ej adresserade (MissionPoint som angreppsväg mot kunder) | NIS2 art. 21.3 | 🟠 Hög |
| G-15 | Microsoft 365 och molnspecifika säkerhetskrav saknas (MFA, Conditional Access) | ISO 27017, ISO 27018 | 🟠 Hög |
| G-16 | GDPR-biträdesroll ej adresserad — MissionPoint agerar troligen personuppgiftsbiträde i kunduppdrag | GDPR art. 28 | 🟠 Hög |
| G-17 | Informationsklassificeringsschema saknas — bara lista på datatyper, inga nivåer | ISO 27002 A.5.12, MSB MSBFS 2020:6 | 🟡 Medium |
| G-18 | Distansarbete — VPN, diskkryptering och hemmanätverkssäkerhet ej specificerat | ISO 27001 A.6.7 | 🟡 Medium |
| G-19 | AI-verktyg — ingen godkännandeprocess, ingen riskklassificering av verktyg, ingen distinktion enterprise vs. consumer | GDPR art. 32, kundavtal | 🟡 Medium |
| G-20 | Fysisk säkerhet saknas helt | ISO 27001 A.7.1–A.7.14 | 🟡 Medium |
| G-21 | Ingen separat informationssäkerhetspolicy på styrelsenivå — IT-policy och ISMS-policy blandas | ISO 27001 kl. 5.2 | 🟡 Medium |
| G-22 | Säker systemutveckling och integrationssäkerhet saknas | ISO 27001 A.8.25–A.8.31 | 🟡 Medium |
| G-23 | Revisionshistorik (§15) är tom; revisions- och granskningsprocess underspecificerad | ISO 27001 kl. 9.2–9.3 | 🟢 Låg |

---

## Del 3 — Prioriterad risklista

### Riskvärderingsmodell
**Riskpoäng = Sannolikhet (1–5) × Konsekvens (1–5)**

| Nivå | Poäng | Åtgärdshorisont |
|---|---|---|
| 🔴 Kritisk | 16–25 | 0–30 dagar |
| 🟠 Hög | 9–15 | 90 dagar |
| 🟡 Medium | 4–8 | 6 månader |
| 🟢 Låg | 1–3 | Ordinarie revision |

---

### 🔴 RISK-01 — Ingen riskhanteringsprocess
**Gap:** G-01 | **Riskpoäng: 5 × 5 = 25/25**

Policyn deklarerar att MissionPoint "arbetar riskbaserat" men definierar ingen process för hur risker identifieras, värderas, beslutas eller följs upp. Utan dokumenterad process kan MissionPoint inte förklara för kunder, revisorer eller tillsynsmyndigheter hur säkerhetsbeslut fattas. Alla andra kontroller saknar grund.

**Regulatorisk exponering:** ISO 27001 kl. 6.1 kräver dokumenterad riskbedömningsprocess. NIS2-bundna kunder kan avtalsrättsligt kräva att deras leverantörer uppvisar en sådan. ISO 27005:2022 kräver att processen är reproducerbar och producerar jämförbara resultat.

---

### 🔴 RISK-02 — Incidenthantering saknar operationell substans
**Gap:** G-02 | **Riskpoäng: 5 × 5 = 25/25**

§9 är ett embryo, inte en process. Det finns inga tidsgränser, inga roller, ingen eskalationskedja och ingen koppling till GDPR:s 72-timmarskrav. Om en incident inträffar i morgon vet ingen exakt vad som ska göras.

**Regulatorisk exponering:** GDPR art. 33: anmälan till IMY inom 72 timmar — ett av de vanligaste grunderna för sanktionsavgifter i Sverige. GDPR art. 28: om MissionPoint agerar personuppgiftsbiträde gäller striktare omedelbar rapporteringsskyldighet till den personuppgiftsansvarige kunden. NIS2 art. 23: kunder i NIS2-klassificerad verksamhet ställer avtalskrav på leverantörer.

---

### 🔴 RISK-03 — Åtkomstkontroll och IAM saknas
**Gap:** G-04 | **Riskpoäng: 4 × 5 = 20/25**

Policyn hanterar konfidentialitet som princip men innehåller inga krav på hur åtkomst faktiskt styrs. Principen om minsta privilegium nämns inte. Det finns inga krav på MFA, behörighetsgenomgångar eller offboarding-process.

**Hotaktörskoppling:** §7 konstaterar att MissionPoint hanterar systemåtkomst till kundsystem. APT29 (Cozy Bear) är dokumenterat specialiserad på credential theft mot konsult- och rådgivningsfirmor för att nå slutkunderna via supply chain. En komprometterad MissionPoint-medarbetares credentials kan ge åtkomst till flera kunders produktionsmiljöer.

**Scenariorisk:** En konsult med aktiv systemåtkomst till tre kundmiljöer har sin laptop kompromitterad via spearphishing. Angriparen använder lagrade sessionstoken för att röra sig lateralt in i samtliga kundmiljöer. Policyn saknar krav på sessionshantering, MFA-enforcement eller segmentering. Sannolikhet 4 × Konsekvens 5 = **20 — Kritisk**.

---

### 🔴 RISK-04 — Säkerhetsskyddslagen oklarad
**Gap:** G-05 | **Riskpoäng: 4 × 5 = 20/25**

Policyn nämner "säkerhetskänslig information" i §7 utan att definiera begreppet, etablera hanteringsregler eller avgöra om Säkerhetsskyddslagen (2018:585) är tillämplig. Om MissionPoint hanterar säkerhetsskyddsklassad information utan att ha identifierat det är bolaget i potentiellt allvarligt lagbrott med straffrättsliga konsekvenser.

---

### 🔴 RISK-05 — Tillgångshantering och systeminventarium saknas
**Gap:** G-03 | **Riskpoäng: 4 × 4 = 16/25**

Det finns ingen förteckning över vilka system, enheter och informationstillgångar som MissionPoint äger och ansvarar för. En policy utan inventarium är som ett larm utan lista på vad som ska bevakas. Utan inventarium är det omöjligt att genomföra meningsfulla riskbedömningar, säkerställa att patchar når alla system, eller avgöra vad som ingår i scope vid en incident.

---

### 🟠 RISK-06 — M365-exponering och avsaknad av molnsäkerhetskrav
**Gap:** G-15 | **Riskpoäng: 4 × 4 = 16/25**

Microsoft Copilot nämns i §8, vilket indikerar M365-miljö. Det finns inga krav på Conditional Access, MFA, adminskyddsstyrning eller appregistreringsstyrning. NCSC-SE och Microsoft MSTIC har dokumenterat att APT29 systematiskt angriper M365-miljöer via OAuth app-registreringar, kompromitterade servicekonton och MFA fatigue-attacker.

---

### 🟠 RISK-07 — Ransomware-beredskap strukturellt otillräcklig
**Gap:** G-06 (delvis G-02) | **Riskpoäng: 4 × 5 = 20/25**

Policyn saknar backup-strategi, RTO/RPO-krav, kommunikationsplan vid datapubliceringshot och betalningspolicy. Ransomware är den dominerande hottypen mot europeiska organisationer (ENISA Threat Landscape 2024, fjärde året i rad). Konsultfirmor med kunddata är attraktiva för dubbel utpressning: kryptering av egna system + hot om publicering av kundkontrakt och säkerhetsanalyser.

---

### 🟠 RISK-08 — Business Email Compromise (BEC)
**Gap:** G-14 (delvis) | **Riskpoäng: 3 × 4 = 12/25**

Rådgivare med direktkontakt mot kundernas ledning och ekonomifunktion är primära BEC-mål. En komprometterad MissionPoint-medarbetares e-postkonto kan användas för att kommunicera med kunder i medarbetarens namn. Policyn saknar krav på e-postsäkerhet (SPF/DKIM/DMARC) och social engineering-utbildning.

---

### 🟠 RISK-09 — Leverantörsstyrning underspecificerad
**Gap:** G-12 | **Riskpoäng: 3 × 4 = 12/25**

§11 nämner säkerhetsbedömning men definierar inte vad "rimlig" innebär. Det finns inga minimikrav, inga avtalsklausuler, ingen revisionsrätt och ingen kontinuerlig uppföljning. GDPR art. 28 kräver personuppgiftsbiträdesavtal — partiellt adresserat men utan konkreta krav.

---

### 🟠 RISK-10 — GDPR-biträdesroll ej adresserad
**Gap:** G-16 | **Riskpoäng: 3 × 4 = 12/25**

MissionPoint agerar sannolikt personuppgiftsbiträde i de flesta kunduppdrag. Biträdesrollen medför separata GDPR-förpliktelser (art. 28) som inte adresseras i policyn: skyldighet att ingå biträdesavtal, krav på att inte anlita underbiträden utan godkännande, och skyldighet att omedelbart rapportera incidenter till den personuppgiftsansvarige
