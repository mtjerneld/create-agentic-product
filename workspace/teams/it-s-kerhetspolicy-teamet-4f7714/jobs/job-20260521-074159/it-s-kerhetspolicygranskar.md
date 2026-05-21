# IT-säkerhetspolicygranskar

# Teknisk & Strukturell Policygranskning
## Hemsö Fastighets AB — IT-policy v4.0

**Utfärdad av:** IT-säkerhetspolicygranskar  
**Datum:** 2025  
**Underlag:** IT Policy v4.0, Regulatorisk kartläggning (Complianceanalytiker), ISO/IEC-analys (Standardspecialist)  
**Status:** Granskningsleverans — Fas 3

---

## Sammanfattande bedömning

Hemsös IT-policy v4.0 är ett **strategiskt intentionsdokument** som fungerar acceptabelt som ägarformulerande styrning på styrelsesnivå. Den är dock **otillräcklig som operationellt säkerhetsdokument** och uppfyller inte de krav som 2025 års regulatoriska landskap ställer. Policyn är i realiteten oförändrad sedan 2019 trots formella datum som antyder 2023 — en direkt trovärdighetsbrist.

**Övergripande betyg per dimension:**

| Dimension | Betyg (1–5) | Kommentar |
|---|---|---|
| Täckning | 2/5 | Stora vita fläckar: incident response, BC/DR, IAM, tredjepartsrisk |
| Tydlighet | 2/5 | Vaga formuleringar, inga mätbara krav |
| Aktualitet | 1/5 | NIS2, AI-risker, Zero Trust — inget finns med |
| Ansvarsfördelning | 2/5 | Fragmenterad, IT-chef underspecificerad, CISO saknas |
| Implementerbarhet | 2/5 | Policyn är inte handlingsstyrd — saknar koppling till kontroller |

---

## 1. Strukturell analys

### 1.1 Dokumenthierarki och styrningslogik

Policyn refererar till tre styrdokument:
- IT Policy (detta dokument — styrelsebeslut)
- Riktlinje för IT (VD-beslut)
- Instruktion för IT (ledningsbeslut)

**Brist:** Hierarkin är otydlig och ofullständig. En funktionsduglig policyhierarki för informationssäkerhet bör följa en väldefinierad struktur. Nedanstående struktur saknas helt i Hemsös dokumentation:

```
Styrelsenivå:    IT-policy (denna) + Informationssäkerhetspolicy (SAKNAS)
       ↓
VD-nivå:         Riktlinjer per domän (IT-användning, klassificering, 
                 incidenthantering, tredjepartshantering)
       ↓
Operationell:    Instruktioner, processbeskrivningar, tekniska krav
       ↓
Kontrollnivå:    Tekniska säkerhetskrav, konfigurationsstandarder
```

**Kritisk brist:** Det finns ingen separat **Informationssäkerhetspolicy** — IT-policyn försöker täcka båda domänerna men misslyckas med båda. ISO 27001:2022 kl. 5.2 kräver explicit en informationssäkerhetspolicy som ledningsinstrument.

### 1.2 Versionskontroll och datuminkonsistens

Dokumentet uppvisar en direkt inkonsistens:

| Fält | Värde i dokumentet |
|---|---|
| Senaste version | 4.0 |
| Beslutsdatum version 4.0 | 2019-04-29 |
| Beslutsdatum i sidhuvud | 2023-04-27 |
| Giltigt fr.o.m. | 2023-04-27 |

**Slutsats:** Dokumentet uppger 2023 som ikraftträdandedatum men versionsförteckningen visar ingen revidering efter 2019. Antingen saknas en version 5.0 i förteckningen, eller har datumet uppdaterats utan att innehållet reviderats — vilket i sig är en styrningsbrist. Detta undergräver dokumentets rättsliga och regulatoriska trovärdighet.

**Åtgärd:** Korrigera omedelbart. Lägg till en version 5.0 med korrekt beslutsdatum och ändringslogg, eller återställ datumen till 2019.

---

## 2. Täckningsanalys — Avsnitt för avsnitt

### 2.1 Avsnitt 1 — Introduktion

**Vad fungerar:** Definierar IT-begreppet, placerar policyn i dokumenthierarkin.

**Brister:**
- ❌ Definitionen av "IT" exkluderar OT (Operational Technology) — kritiskt för ett fastighetsbolag med fastighetsautomation (BMS, SCADA, hissar, passersystem)
- ❌ Scope är inte definierat: gäller policyn dotterbolag, joint ventures, inhyrda konsulter?
- ❌ Ingen koppling till informationsklassificering — "information är en viktig tillgång" är en tom formulering utan klassificeringsschema

**Åtgärdsförslag:**
> Lägg till en explicit scope-paragraf: *"Denna policy gäller Hemsö Fastighets AB och dess helägda dotterbolag, samtliga anställda, konsulter och tredjepartsaktörer med åtkomst till Hemsös IT-miljö och information, inklusive operativa styrsystem (OT) i fastighetsbestånd."*

---

### 2.2 Avsnitt 2 — Övergripande mål

**Vad fungerar:** Mål är välformulerade på affärsnivå, kopplar IT till affärsstrategi.

**Brister:**
- ❌ Målen är **mätbara på noll punkter** — ingen KPI, inget målvärde, ingen uppföljningsmekanism
- ❌ Säkerhet nämns i förbifarten ("på ett säkert sätt") men är inte ett explicit övergripande mål
- ❌ Resiliens och kontinuitet saknas som mål

**Åtgärdsförslag:**
> Lägg till explicit säkerhetsmål: *"Hemsös IT-miljö ska upprätthålla konfidentialitet, integritet och tillgänglighet för affärskritisk information. Säkerhetsincidenter ska minimeras genom riskbaserade kontroller och kontinuerlig utvärdering."*

> Lägg till mätbarhetskrav: *"IT-avdelningen ska årligen rapportera utfall mot definierade säkerhetsmål till CFO och styrelsen."*

---

### 2.3 Avsnitt 3 — Strategi

**Vad fungerar:** Tydlig strategisk inriktning mot standardisering, centraliserad upphandling, Microsoft-plattform.

**Brister:**
- ❌ **Systemägare och Systemansvarig** definieras inte — roller nämns men ansvarsinnehåll saknas helt
- ❌ **"Beprövad kunskap/metodik"** är odefinierat — vad innebär det i praktiken? Inga referensstandarder anges
- ❌ Ingen hantering av **skugg-IT** (Shadow IT) — ett reellt hot i en Microsoft 365-miljö
- ❌ Ingen styrning av **molntjänster och SaaS** — "outsourcad drift" beskrivs men cloud governance saknas
- ❌ Ingen styrning av **AI-verktyg** (Copilot, ChatGPT, etc.) som aktivt används i alla organisationer 2025
- ❌ Mobilitetsaspekten nämns ("arbeta obehindrat oavsett geografi") utan säkerhetskrav för mobila enheter, BYOD eller VPN

**Åtgärdsförslag:**
> Tillägg för systemägarskap: *"Systemägare ansvarar för informationssäkerheten i sitt system, inklusive behörighetshantering, klassificering av systemets information och godkännande av systemförändringar. Systemansvarig ansvarar för den tekniska förvaltningen."*

> Tillägg för molntjänster: *"Molntjänster och SaaS-lösningar ska genomgå IT-avdelningens säkerhetsgodkännande innan driftsättning. Databehandlingsavtal ska upprättas för alla leverantörer som behandlar Hemsös data."*

> Tillägg för AI-verktyg: *"Användning av AI-baserade verktyg och tjänster regleras separat i Riktlinje för IT. Ingen affärskritisk eller konfidentiell information får matas in i externa AI-tjänster utan föregående säkerhetsgranskning."*

---

### 2.4 Avsnitt 4 — Säkerhet

**Detta är den mest kritiskt underpresterade delen av policyn.**

**Nuvarande innehåll (i fulltext):**
Avsnittet hänvisar till krishanteringsriktlinje, nämner antivirus/spam/brandväggar och refererar till "kontrollstruktur för låga operationella risker."

**Strukturella brister:**

| Säkerhetsdomän | Status i policy | Regulatorisk relevans |
|---|---|---|
| Riskhantering (riskbedömning, riskbehandling) | ❌ Saknas | ISO 27001 kl. 6.1, NIS2 art. 21 |
| Incidenthantering och rapportering | ❌ Saknas | NIS2 art. 23, MSB-föreskrifter |
| Business continuity / katastrofåterställning | ❌ Saknas | ISO 27001 kl. A.5.29-5.30, NIS2 |
| Identitets- och åtkomsthantering (IAM/PAM) | ❌ Saknas | ISO 27002 A.5.15-5.18 |
| Säkerhetsklassificering av information | ❌ Saknas | ISO 27001 A.5.12-5.13 |
| Kryptering | ❌ Saknas | GDPR art. 32, ISO 27002 A.8.24 |
| Sårbarhetsshantering och patchning | ❌ Saknas | NIS2 art. 21, ISO 27002 A.8.8 |
| Nätverkssegmentering | ❌ Saknas | ISO 27002 A.8.20-8.22 |
| Säkerhetsloggning och övervakning | ❌
