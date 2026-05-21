# Hotbildsrådgivare

# Hotbildsanalys: Hemsö Fastighets AB IT-policy v4.0
## Bedömning mot aktuella cyberhot mot svenska organisationer

**Upprättad av:** Hotbildsrådgivare  
**Datum:** 2025  
**Källor:** NCSC-SE Årsrapport 2023–2024, ENISA Threat Landscape 2024, MSB Informationssäkerhet i Sverige 2024, SÄPO Årsbok 2024  
**Status:** Teknisk & strukturell policygranskning — Fas 3 av 3

---

## 1. Sammanfattande bedömning

> **Sammantagen hotexponering: HÖG**
> 
> Hemsö Fastighets AB befinner sig i ett exponerat läge som IT-policyn **inte adresserar**. Bolaget äger och förvaltar samhällsfastigheter åt offentlig sektor — ett segment som konsekvent rankas bland de högst prioriterade målen för statssponsrade hotaktörer mot Sverige. IT-policyn (v4.0, senast reviderad 2019) saknar adressering av samtliga identifierade prioriterade hottyper från NCSC-SE och ENISA.

---

## 2. Hotaktörslandskap relevant för Hemsö

### 2.1 Statssponsrade aktörer

Hemsös hyresgästbas (försvar, domstolar, sjukhus, kriminalvård, skolor) gör bolaget till ett **indirekt mål för underrättelseinhämtning**. NCSC-SE har i sina senaste rapporter identifierat följande som aktiva hot mot Sverige:

| Hotaktör | Ursprung | Metod | Relevans för Hemsö |
|---|---|---|---|
| APT28 / Fancy Bear | Ryssland (GRU) | Spearphishing, credential harvesting, OT-intrång | **HÖG** — Aktiv mot samhällsviktig infrastruktur i Sverige |
| APT29 / Cozy Bear | Ryssland (SVR) | Supply chain-kompromittering, molntjänstintrång | **HÖG** — Specifikt inriktad mot Microsoft 365-miljöer |
| Volt Typhoon | Kina (PLA) | Living-off-the-land, OT/ICS-intrång via fastighetssystem | **HÖG** — Direkt relevant för fastighetsautomation |
| Lazarus Group | Nordkorea | Ransomware, finansiellt motiverat | **MEDEL** — Opportunistisk mot alla sektorer |

> ⚠️ **Kritiskt antagande:** Hemsö driver sannolikt fastighetstekniska system (BMS/BAS — Building Management Systems) som kopplas mot IT-nätverket. Volt Typhoon har specifikt riktat in sig på just denna OT/IT-konvergens i samhällsfastigheter i Europa.

### 2.2 Kriminella hotaktörer (finansiellt motiverade)

Enligt ENISA Threat Landscape 2024 är **ransomware den dominerande hottypen mot europeiska organisationer** för fjärde året i rad. Fastighetsbolag med outsourcad IT är särskilt exponerade:

- **Lockbit 3.0 / Black Basta / Cl0p** — aktiva mot mellerstora europeiska fastighetsbolag
- **Business Email Compromise (BEC)** — specifikt mot CFO/ekonomifunktioner i fastighetsbolag (hyresbetalningar, leverantörsfakturor)
- **MSP-kompromittering** — outsourcade IT-driftleverantörer är en etablerad attackvektor mot deras kundbas

---

## 3. Hotspecifik analys mot IT-policyns innehåll

### 3.1 Ransomware och utpressningsattacker

**Hotbild (NCSC-SE 2024):** Ransomware-incidenter mot svenska organisationer ökade med 37% 2023. Medelkostnad för en incident i mellanstor organisation: 8–15 MSEK i direkta kostnader.

**Vad policyn säger:**
> *"Virus och andra skadliga program [...] ska förhindras genom att PC, servrar och alla externa accesspunkter/portar förses med en aktiv och väl uppdaterad skyddslösning så som antivirus/spam och brandväggar."* (Avsnitt 4)

**Gap-analys:**

| Krav för ransomware-resiliens | Status i policy |
|---|---|
| Offline/immutable backup-strategi | ❌ Saknas helt |
| Incidentresponsplan med ransomware-specifikt scenario | ❌ Saknas helt |
| Nätverkssegmentering för att begränsa lateral rörelse | ❌ Saknas |
| Testad återställningsförmåga (RTO/RPO-definitioner) | ❌ Saknas |
| EDR/XDR (modern endpointskydd bortom antivirus) | ❌ Antivirus nämns — otillräckligt 2025 |
| Privileged Access Management (PAM) | ❌ Saknas |

**Bedömning:** Policyn beskriver ett **2012-årigt skyddskoncept** (antivirus + brandvägg) som är demonstrerat otillräckligt mot moderna ransomware-angrepp. En ransomware-aktör som kompromitterar driftleverantören når Hemsö utan att möta policystyrd motåtgärd.

---

### 3.2 Supply chain-attacker mot IT-driftleverantör

**Hotbild (ENISA 2024):** Supply chain-attacker mot IT-leverantörer ökade med 58% 2023. SolarWinds, Kaseya och MOVEit-attackerna har etablerat outsourcad IT-drift som primär attackvektor mot kundbaser.

**Vad policyn säger:**
> *"Hemsös IT-lösning ska bygga på centraliserad och outsourcad drift"* (Avsnitt 3)  
> *"Driftpartner ansvarar för att inget informationsläckage skall uppstå"* (Avsnitt 5)

**Gap-analys:**

| Krav för supply chain-resiliens | Status i policy |
|---|---|
| Krav på leverantörens säkerhetscertifieringar (ISO 27001, SOC 2) | ❌ Saknas |
| Rätt att genomföra säkerhetsrevisioner av leverantör | ❌ Saknas |
| Krav på leverantörens incidentrapportering (tidsgränser) | ❌ Saknas |
| Exitstrategi och portabilitetskrav | ❌ Saknas |
| Koncentrationsrisk-bedömning (enda leverantör) | ❌ Saknas |
| SLA med säkerhetsmässiga KPI:er | ❌ Saknas |

**Bedömning:** Policyn delegerar säkerhetsansvaret till driftleverantören utan att definiera **vilka krav** leverantören ska uppfylla eller hur Hemsö verifierar efterlevnad. Detta är den **mest kritiska enskilda bristen** ur ett hotbildsperspektiv givet Hemsös outsourcade profil.

---

### 3.3 Identitetsbaserade attacker och credential harvesting

**Hotbild (NCSC-SE 2024):** 86% av alla intrång börjar med kompromitterade identiteter. Microsoft 365-miljöer — vilket Hemsö explicit använder — är primärt mål för Password Spray, OAuth-token-stöld och MFA-bypasses (AiTM-phishing).

**Vad policyn säger:**  
*Ingenting om identitets- och åtkomsthantering.*

**Gap-analys:**

| Krav för identitetsskydd | Status i policy |
|---|---|
| Krav på MFA för alla användare | ❌ Saknas |
| Privileged Identity Management (just-in-time-access) | ❌ Saknas |
| Policy för lösenordskomplexitet/lösenordslöshet | ❌ Saknas |
| Offboarding-process (återkallande av åtkomst vid avslut) | ❌ Saknas |
| Gästkonton och externa användares åtkomst | ❌ Saknas |
| Conditional Access-policyer | ❌ Saknas |

**Bedömning:** För en Microsoft 365-centrerad organisation utan IAM-krav i IT-policyn är exponeringen mot identitetsbaserade angrepp **kritisk**. APT29 (rysk SVR) är specifikt känd för att utnyttja Microsoft 365-miljöers autentiseringsmekanismer.

---

### 3.4 OT/IT-konvergens och fastighetstekniska system

**Hotbild (ENISA 2024, Volt Typhoon TTP-rapport 2024):** Fastighetsautomationssystem (BMS, HVAC, låssystem, brandlarm) kopplas alltmer mot IT-nätverk och utgör en obevarad attackyta. Volt Typhoon har kompromitterat byggnadsautomationssystem i samhällsfastigheter som **persistent access**-plattform.

**Vad policyn säger:**  
*Ingenting om OT, fastighetstekniska system, eller IT/OT-gränssnittet.*

**Gap-analys:**

| Krav för OT/IT-säkerhet | Status i policy |
|---|---|
| Definition av OT-system inom IT-policyns scope | ❌ Saknas |
| Nätverkssegmentering OT/IT | ❌ Saknas |
| Säkerhetskrav på fastighetstekniska system | ❌ Saknas |
| Inventering av OT-tillgångar | ❌ Saknas |
| Patchhantering för OT-enheter | ❌ Saknas |

> ⚠️ **Antagande med hög konsekvens:** Hemsö som fastighetsförvaltare driver nästan säkert BMS-system (Building Management Systems) i sina fastigheter. Att dessa system inte nämns i IT-policyn innebär att de sannolikt faller utanför IT-säkerhetsstyrningen — en blind fläck som är direkt exploaterbar.

---

### 3.5 Phishing, spearphishing och BEC

**Hotbild (NCSC-SE 2024):** Phishing är fortfarande den vanligaste initiala attackvektorn (68% av incidenter). BEC
