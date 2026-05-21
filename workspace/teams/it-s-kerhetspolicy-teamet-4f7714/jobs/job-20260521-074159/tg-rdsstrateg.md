# Åtgärdsstrateg

# Åtgärdsplan: Hemsö Fastighets AB IT-policy v4.0
## Konkreta, prioriterade förbättringsförslag — Gap-analys & riskvärdering

**Upprättad av:** Åtgärdsstrateg  
**Datum:** 2025  
**Underlag:** Regulatorisk kartläggning, ISO/IEC-analys, Teknisk policygranskning, Hotbildsanalys  
**Status:** Fas 2 — Gap-analys & riskvärdering med åtgärdsförslag

---

## 1. Sammanfattande bedömning

Hemsös IT-policy v4.0 har tre fundamentala problem som åtgärdsarbetet måste adressera i rätt ordning:

1. **Den är fel typ av dokument** — den blandas ihop med en informationssäkerhetspolicy utan att vara det
2. **Den är fyra år gammal i praktiken** — NIS2, AI-risker, ransomware och OT-hot existerar inte i texten
3. **Den är inte handlingsstyrd** — inga mätbara krav, inga kontroller, ingen incidenthantering

Åtgärdsarbetet struktureras i tre spår som körs parallellt men med tydlig prioritetsordning.

---

## 2. Prioriterad åtgärdsmatris

Varje identifierad brist klassificeras efter:
- **Allvarlighetsgrad:** Kritisk / Hög / Medium / Låg
- **Regulatorisk exponering:** Vilket ramverk som triggas
- **Insats:** Låg (dagar) / Medium (veckor) / Hög (månader)

| # | Brist | Allvarlighet | Ramverk | Insats | Åtgärd |
|---|---|---|---|---|---|
| 1 | Ingen incidenthanteringsprocess | **Kritisk** | NIS2 art. 23, ISO 27001 kl. 6.1 | Medium | Ny sektion + underliggande riktlinje |
| 2 | NIS2-klassificering saknas | **Kritisk** | NIS2 lag 2024:491 | Låg | Juridisk klassificeringsanalys + policytillägg |
| 3 | OT/BMS-säkerhet obehandlad | **Kritisk** | NIS2, ISO 27001 A.5.23 | Hög | Ny sektion, OT-riskanalys |
| 4 | Ingen informationssäkerhetspolicy | **Kritisk** | ISO 27001 kl. 5.2 | Hög | Nytt separat styrdokument |
| 5 | Tredjepartsrisk underreglerad | **Hög** | NIS2 art. 21, GDPR art. 28 | Medium | Utökad leverantörssektion |
| 6 | Inga klassificeringskrav | **Hög** | ISO 27002 A.5.12, MSB | Medium | Klassificeringsmodell + riktlinje |
| 7 | IAM/behörighetsstyrning saknas | **Hög** | ISO 27001 A.5.15–A.5.18 | Medium | Ny sektion + tillhörande riktlinje |
| 8 | BC/DR omnämns inte | **Hög** | ISO 27001 kl. 8.8, NIS2 art. 21 | Medium | Ny sektion, koppling till krishanteringsriktlinje |
| 9 | CISO-roll saknas | **Hög** | ISO 27001 kl. 5.3 | Låg | Rolldefinition i avsnitt 7 |
| 10 | Versionskontroll-inkonsistens | **Medium** | Intern styrning | Låg | Omedelbar korrigering |
| 11 | Inga mätbara säkerhetsmål | **Medium** | ISO 27001 kl. 6.2 | Medium | KPI-bilaga till policy |
| 12 | AI och molntjänster oreglerade | **Medium** | GDPR, kommande AI Act | Medium | Tillägg i strategi-avsnittet |
| 13 | Säkerhetsmedvetandeutbildning | **Medium** | ISO 27002 A.6.3, NIS2 art. 21 | Medium | Krav i policy + utbildningsplan |
| 14 | Sårbarhetshanterings-process | **Medium** | ISO 27002 A.8.8, NIS2 | Medium | Ny sektion |
| 15 | Ansvarig utgivare = CFO | **Låg** | Intern styrning | Låg | Överväg CISO som utgivare |

---

## 3. Kritiska åtgärder — Omedelbar hantering (0–30 dagar)

### 3.1 ⚡ Åtgärd 1: NIS2-klassificeringsanalys

**Brist:** Hemsö har inte fastställt sin NIS2-klassificering. Lagen (2024:491) är i kraft. Om Hemsö är en viktig eller väsentlig verksamhet gäller rapporteringskrav, tekniska minimikrav och tillsynsansvar — utan att policyn adresserar något av detta.

**Konkret åtgärd:**
1. Uppdra åt juridisk rådgivare eller MSB:s vägledning att fastställa om Hemsö klassificeras under NIS2 sektorbilagan (troligen under "digital infrastruktur" eller "offentlig förvaltning"-kopplade sektorer via hyresgästbas)
2. Dokumentera klassificeringen i ett formellt beslutsmemo signerat av CFO
3. Lägg till följande mening i avsnitt 4 (Säkerhet) som interim-åtgärd i befintlig policy:

> *"Hemsö följer tillämpliga krav i NIS2-direktivet (lag 2024:491 om cybersäkerhet) och vidmakthåller en aktuell klassificeringsbedömning. IT-chef ansvarar för att säkerställa att Hemsös säkerhetsåtgärder uppfyller de minimikrav som följer av Hemsös NIS2-klassificering."*

**Insats:** 3–5 dagars juridisk genomlysning + en styrelsedag för beslut  
**Ansvarig:** CFO, stöd från extern juridisk rådgivare

---

### 3.2 ⚡ Åtgärd 2: Åtgärda versionskontroll-inkonsistensen

**Brist:** Dokumentet anger version 4.0 beslutad 2019-04-29 men sidhuvudet anger 2023-04-27. Detta är inte en kosmetisk brist — det skapar legal osäkerhet om vilket dokument som faktiskt är gällande vid en tillsynsinspektion.

**Konkret åtgärd:**
1. IT-chef sammankallar ett möte med CFO denna vecka
2. Fastställ vilket datum som är korrekt beslutsdag
3. Utfärda ett korrigeringsblad (errata) som biläggs den gällande versionen tills nästa full revidering
4. Inför en formell ändringslogg som kräver faktisk styrelsesignatur med datum — inte bara datum i ett sidhuvud

**Insats:** 1 dag  
**Ansvarig:** IT-chef

---

### 3.3 ⚡ Åtgärd 3: Incidenthantering — interimslösning

**Brist:** Policyn saknar helt incidenthantering. NIS2 art. 23 kräver rapportering av allvarliga incidenter till NCSC/MSB inom 24 timmar (tidig varning) och 72 timmar (fullständig anmälan). Utan en process är Hemsö exponerat för sanktioner.

**Konkret åtgärd — tre steg:**

**Steg 1 (denna vecka):** Lägg till följande i avsnitt 4 som interimtext:
> *"Hemsö ska ha dokumenterade rutiner för hantering av IT-säkerhetsincidenter. Alla medarbetare är skyldiga att rapportera misstänkta incidenter till IT-funktionen omedelbart. IT-chef ansvarar för att allvarliga incidenter eskaleras och, där lag så kräver, rapporteras till behörig myndighet inom föreskrivna tidsfrister."*

**Steg 2 (inom 30 dagar):** IT-chef upprättar en **Riktlinje för incidenthantering** som minimum innehåller:
- Definition av vad som utgör en incident (med exempel)
- Klassificeringsmodell: P1 (kritisk) / P2 (allvarlig) / P3 (mindre allvarlig)
- Eskaleringsvägar och kontaktlistor (inkl. NCSC-SE och MSB)
- NIS2-rapporteringsrutin med tidsgränser (24h / 72h / 30 dagar)
- Rollfördelning under incident (IT-chef, CFO, kommunikationsansvarig)
- Krav på incidentlogg och post-mortem

**Steg 3 (inom 60 dagar):** Genomför ett tabletop-övning (skrivbordsövning) med ledningsgruppen baserat på ett ransomware-scenario

**Insats:** Steg 1 = 2 timmar. Steg 2 = 3–5 dagars arbete. Steg 3 = halvdag  
**Ansvarig:** IT-chef, godkänns av VD

---

## 4. Höga åtgärder — Kortsiktig hantering (30–90 dagar)

### 4.1 Åtgärd 4: Skapa separat Informationssäkerhetspolicy

**Brist:** ISO 27001:2022 kl. 5.2 kräver en explicit informationssäkerhetspolicy som ledningsinstrument. Den befintliga IT-policyn är ett strategidokument — inte ett säkerhetsdokument.

**Konkret åtgärd:**
Upprätta ett nytt styrdokument: **Informationssäkerhetspolicy för Hemsö** (styrelsebeslut). Dokumentet ska vara kortfattat (max 2 sidor) men täcka:

| Krav | Innehåll |
|---|---|
| Scope | Vad som ingår i informationssäkerhetsarbetet |
| Mål | Tre till fem mätbara säkerhetsmål
