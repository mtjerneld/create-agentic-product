# Standardspecialist (ISO/IEC)

# ISO/IEC-analys: Hemsö Fastighets AB IT-policy v4.0
## Regulatorisk kartläggning & granskningsbaseline

**Upprättad av:** Standardspecialist (ISO/IEC)
**Datum:** 2025-01-27
**Tillämpliga standarder:** ISO/IEC 27001:2022, ISO/IEC 27002:2022

---

## 1. Metodologisk ansats och antaganden

### Antaganden
- Hemsö Fastighets AB klassificeras som ett **fastighetsbolag med samhällsviktig infrastruktur** (skolor, vård, omsorg) vilket sannolikt innebär exponering mot NIS2-relaterade sektorskrav.
- Bolaget driver outsourcad IT-drift mot extern leverantör (bekräftat i policy avsnitt 5), vilket aktiverar ISO 27001 Annex A kontroller för leverantörsrelationer (A.5.19–A.5.22 i 2022 års version).
- Policyn daterar senaste beslut till **2019-04-29** (version 4.0), trots att dokumentet anger datum 2023-04-27 — detta är en intern inkonsistens. Antagande: policyn är i praktiken **oförändrad sedan 2019** och återspeglar inte ISO 27001:2022-uppdateringen.
- Organisationsstorlek: Mellanstor organisation, styrs av styrelse med CFO som IT-ägare.

---

## 2. Tillämpliga ISO/IEC-standarder — Översikt och relevansbedömning

| Standard | Version | Relevans för Hemsö | Applicerbarhetsnivå |
|---|---|---|---|
| ISO/IEC 27001 | 2022 | Ledningssystem för informationssäkerhet (ISMS) | **Hög** — Ger strukturkrav för hela policyhierarkin |
| ISO/IEC 27002 | 2022 | Implementeringsvägledning för kontroller | **Hög** — Operationell baseline för säkerhetsåtgärder |
| ISO/IEC 27005 | 2022 | Riskhantering informationssäkerhet | **Hög** — Policyn saknar riskprocess helt |
| ISO/IEC 27017 | 2015 | Molntjänstsäkerhet | **Medium** — Outsourcad drift aktiverar dessa krav |
| ISO/IEC 27018 | 2019 | Personuppgifter i molntjänster | **Medium** — Direkt koppling till GDPR-avsnittet |
| ISO/IEC 27036 | 2021 | Leverantörssäkerhet | **Medium** — Tredjepartsrisk underbehandlad i policy |

---

## 3. ISO 27001:2022 — Kravstrukturanalys mot policyn

ISO 27001:2022 ställer krav inom **10 klausuler** (kap. 4–10) för ISMS-etablering. Nedan analyseras varje klausul mot vad Hemsös IT-policy adresserar respektive saknar.

### 3.1 Klausul 4 — Organisationens kontext

**ISO 27001:2022 krav:**
- 4.1: Förstå organisationen och dess sammanhang
- 4.2: Förstå intressenters behov och förväntningar
- 4.3: Definiera ISMS-scope
- 4.4: Etablera ISMS

**Vad policyn gör:** Identifierar IT som verktyg för affärsidén och nämner att IT ska stödja strategin.

**Gap:**
- ❌ Ingen **scope-definition** för informationssäkerheten finns (vilka system, processer, platser ingår i ISMS)
- ❌ Inga **intressenter** identifierade (hyresgäster, myndigheter, finansiärer, leverantörer)
- ❌ Ingen **kontextanalys** (interna/externa faktorer som påverkar informationssäkerheten)
- ❌ ISMS som ledningssystemkoncept saknas helt — policyn är en IT-styrningspolicy, inte en ISMS-policy

**Åtgärd (ISO-specifik):** Lägg till ett avsnitt "Tillämpningsområde och kontext" som explicit definierar vad informationssäkerhetspolicyn omfattar och vilka intressenter som berörs. Skilj tydligt på *IT Policy* och *Informationssäkerhetspolicy* — ISO 27001 kräver den senare.

---

### 3.2 Klausul 5 — Ledarskap

**ISO 27001:2022 krav:**
- 5.1: Ledningens åtagande
- 5.2: Policy (informationssäkerhetspolicy med specifika krav)
- 5.3: Roller, ansvar och befogenheter

**Vad policyn gör:** Avsnitt 7 definierar roller för Styrelse, VD och CFO. Avsnitt 8 beskriver underhåll och implementering.

**Gap:**
- ❌ Ingen **informationssäkerhetspolicy** per ISO 27001 kl. 5.2 — standarden kräver explicit:
  - Policyn ska vara lämplig för organisationens syfte
  - Inkludera mål eller ge ram för informationssäkerhetsmål
  - Inkludera åtagande att uppfylla tillämpliga krav
  - Inkludera åtagande till kontinuerlig förbättring
- ❌ **CISO/Informationssäkerhetsansvarig** är helt frånvarande i rollförteckningen — ISO 27001 kl. 5.3 kräver att ansvar och befogenheter för informationssäkerhetsrollen är tydligt definierat
- ⚠️ IT-chef nämns som upprättare men saknar definierat mandat i säkerhetsfrågor
- ❌ **Ledningens åtagande** (management commitment) är inte explicit formulerat

**Åtgärd (ISO-specifik):**
1. Tillföra ett stycke om ledningens åtagande med de fyra punkterna ovan
2. Definiera och tillsätta en CISO-funktion eller tydlig informationssäkerhetsroll med mandat
3. Säkerställa att policyn uppfyller ISO 27001 kl. 5.2-kraven explicit

---

### 3.3 Klausul 6 — Planering

**ISO 27001:2022 krav:**
- 6.1: Åtgärder för att hantera risker och möjligheter (inkl. riskbedömning och riskbehandlingsplan)
- 6.2: Informationssäkerhetsmål
- 6.3: Planering av förändringar

**Vad policyn gör:** Nämner i avsnitt 4 att krishanteringsriktlinjen "syftar till att minimera risker". Avsnitt 2 anger övergripande IT-mål.

**Gap:**
- ❌ **Ingen riskprocess** definierad eller refererad (ISO 27001 kräver dokumenterad riskbedömningsmetodik per kl. 6.1.2)
- ❌ **Inga mätbara informationssäkerhetsmål** — policymålen är enbart kvalitativa affärsmål, inte säkerhetsmål per kl. 6.2
- ❌ Ingen referens till **riskägare** eller riskregister
- ❌ Förändringsstyrning (6.3) helt frånvarande
- ⚠️ Hänvisning till "krishanteringsriktlinje" är otillräcklig ersättning för systematisk riskhantering

**Åtgärd (ISO-specifik):**
1. Lägg till policykrav på att en **riskbedömning ska genomföras** minst årligen enligt definierad metodik (referera ISO 27005)
2. Formulera **minst 3–5 mätbara informationssäkerhetsmål** (t.ex. max antal kritiska incidenter per år, RTO/RPO-nivåer, utbildningstäckning)
3. Kräv att en **Statement of Applicability (SoA)** upprättas och underhålls

---

### 3.4 Klausul 7 — Stöd

**ISO 27001:2022 krav:**
- 7.1–7.2: Resurser och kompetens
- 7.3: Medvetenhet
- 7.4: Kommunikation
- 7.5: Dokumenterad information

**Vad policyn gör:** Avsnitt 3 nämner att alla anställda ska ha tillräcklig IT-kunskap. Avsnitt 8 adresserar implementering och kommunikation delvis.

**Gap:**
- ❌ **Informationssäkerhetsutbildning och -medvetenhet** (security awareness) saknas som krav — ISO 27001 kl. 7.2–7.3 kräver kompetenshantering och medvetenhetsprogram specifikt för säkerhet
- ❌ Ingen kravbeskrivning för **dokumenthantering av ISMS-dokumentation** (versionskontroll, tillgänglighet, skydd)
- ⚠️ "Tillräcklig kunskap om IT" är för vagt — ISO 27001 kräver rollspecifik säkerhetskompetens
- ❌ Ingen kommunikationsplan för säkerhetsfrågor internt/externt

**Åtgärd (ISO-specifik):**
1. Lägg till krav på **annual security awareness-program** med mätbar effekt
2. Lägg till krav på rollspecifik säkerhetskompetens (t.ex. utökad utbildning för IT-personal, systemägare, ledning)
3. Definiera krav på dokumenthantering med koppling till ISMS-dokumentstruktur

---

### 3.5 Klausul 8 — Verksamhet

**ISO 27001:2022 krav:**
- 8.1: Operationell planering och kontroll
- 8.2: Riskbedömning (genomförande)
- 8.3: Riskbehandling (genomförande)

**Vad policyn gör:** Avsnitt 4 nämner antivirus, brandväggar och krishantering. Avsnitt 5 adresserar GDPR-hantering operationellt.

**Gap:**
-
