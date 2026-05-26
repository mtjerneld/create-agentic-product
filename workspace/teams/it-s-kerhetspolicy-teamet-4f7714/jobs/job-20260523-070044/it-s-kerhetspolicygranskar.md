# IT-säkerhetspolicygranskar

# Teknisk & Strukturell Policygranskning — MissionPoint AB
**Roll:** IT-Säkerhetspolicygranskar
**Fas:** Teknisk & strukturell policygranskning
**Datum:** 2026-02-27 | **Dokument:** MissionPoint IT- och Informationssäkerhetspolicy v1.0

---

## Metodologisk position

Denna granskning bygger vidare på den regulatoriska baseline (Complianceanalytikern) och ISO-mappningen (Standardspecialisten). Uppgiften är att bedöma policyn som **tekniskt och strukturellt dokument** — inte bara lista luckor, utan bedöma om dokumentet *håller som styrdokument* i sin nuvarande form.

Styrande princip: MissionPoint vill ha ett minimalt dokument. Frågan är om minimumet faktiskt är uppnått — eller om policyn i sin nuvarande form skapar mer risk än den undanröjer.

**Antagande som delas med föregående roller:** MissionPoint är inte primär NIS2-aktör. Säkerhetsskyddslagens aktiveringsstatus är oklart och kräver separat klarläggning med kunden — detta påverkar ett kritiskt fynd nedan.

---

## 1. Strukturell helhetsbedömning

### 1.1 Dokumentarkitektur

Policyn är skriven som ett **platt, avsnittslöst dokument** utan hierarki mellan styrande principer och operativa regler. Det finns ingen distinktion mellan:

- Vad MissionPoint åtar sig (ledningspolicy-nivå)
- Vad medarbetare måste göra (regelsnivå)
- Hur det görs (procedusnivå — ska *inte* finnas i en kompakt policy, men gränsen är oklar i nuläget)

**Konsekvens:** Avsnitten 8 (AI), 9 (Incident) och 10 (Distansarbete) är skrivna som miniprocesser inbäddade i policydokumentet. Det är inte nödvändigtvis fel för ett kompakt dokument, men gör det svårt att avgöra vad som är bindande policy och vad som är vägledning.

**Bedömning:** Godkänt för minimal policy — men avsnitt 9 (incidenthantering) har specifika strukturproblem som adresseras nedan.

---

### 1.2 Versionskontroll och livscykel

| Element | Status | Bedömning |
|---|---|---|
| Versionsnummer | v1.0 ✅ | OK |
| Datum | 2026-02-27 ✅ | OK |
| Revisionshistorik (avs. 15) | Tom tabell — inga poster ✅ för v1.0 | Acceptabelt för initialt dokument |
| Revisionsfrekvens | "Minst årligen" (avs. 14) ✅ | Tillräckligt |
| Ägare/ansvarig för uppdatering | **Saknas** ⚠️ | Vem kallar till revision? CIO är informationssäkerhetsansvarig men kopplingen till policydokumentet som sådant är inte explicit |
| Godkännandeprocess | **Saknas** ⚠️ | Inget angivet om vem som fastställer policyn — relevant eftersom den ska godkännas av styrelsen |

**Antagande:** Styrelsebeslutet som är på väg *är* godkännandeprocessen. Men det bör framgå av dokumentet självt att det kräver styrelsenivå för revision.

---

## 2. Täckningsanalys — kritiska krav mot dokumentets faktiska text

Nedan är en avsnitt-för-avsnitt-genomgång mot minimikraven identifierade av föregående roller, med teknisk bedömning av om texten faktiskt *levererar* kravet eller bara *omnämner* det.

### 2.1 Avsnittsvis teknisk bedömning

| Avsnitt | Rubrik | Teknisk status | Kommentar |
|---|---|---|---|
| 1–2 | Inledning / Syfte | ✅ Tillräckligt | CIA-triaden explicit. Proportionalitetsprincipen inkluderad. |
| 3 | Omfattning | ✅ Tillräckligt | Personal, konsulter, system, kundsystem täcks. Geografisk scope saknas men inte kritiskt för kompakt policy. |
| 4–5 | Roll/ansvar + leverantörskedja | ⚠️ Otillräckligt | Se 2.2 nedan. |
| 6 | Principer | ⚠️ Partiellt | CIA täcks. Riskbaserat omnämnt men ingen process. Informationssäkerhetsansvarig definierad — men mandat oklart. |
| 7 | Informationsklassning | 🔴 Kritiskt fynd | Se 2.3 nedan. |
| 7.1 | Personuppgifter / GDPR | ✅ Tillräckligt på policynivå | Hänvisning till Integritetspolicy är korrekt struktur för kompakt dokument. |
| 8 | AI-verktyg | ✅ Styrka | Specifika förbud och tillåtna användningsfall. Bevaras. |
| 9 | Incidenthantering | 🔴 Kritiskt fynd | Se 2.4 nedan. |
| 10 | Distansarbete | ✅ Tillräckligt | Grundregler täckta. Proporterligt för kompakt policy. |
| 11 | Leverantörshantering | ⚠️ Otillräckligt | Se 2.5 nedan. |
| 12 | Ansvar | ⚠️ Otillräckligt | Se 2.6 nedan. |
| 13–15 | Efterlevnad/Uppdatering/Historik | ⚠️ Partiellt | Se 2.7 nedan. |

---

### 2.2 Avsnitt 4–5: Rollgränser och leverantörskedja

**Teknisk bedömning:** Avsnitt 4 etablerar en ansvarsdelning där kunden "normalt" ansvarar för implementering av säkerhetsåtgärder. Avsnitt 5 erkänner NIS2/DORA-leverantörskedjeperspektivet.

**Problem:** Formuleringen "normalt inte har operativt ägarskap" skapar en ansvarsambiguitet. Vad gäller när MissionPoint *faktiskt* har systemåtkomst — vilket policyn själv listar som ett hanterat informationssystem (avs. 3)?

I dessa situationer har MissionPoint reellt ansvar för vad de gör med den åtkomsten, oavsett vem som "äger" systemet. Policyn hanterar inte detta mellanrum.

**Klassificering:** Hög — operationell risk, ej regulatorisk brist i sig, men skapar tvetydighet om ansvar vid incident.

---

### 2.3 Avsnitt 7: "Säkerhetskänslig information" — KRITISKT FYND

**Teknisk bedömning:** Avsnitt 7 listar "säkerhetskänslig information" som en informationskategori MissionPoint hanterar. Termen används utan:

- Definition av vad som avses
- Hanteringsregler specifika för denna kategori
- Hänvisning till externt regelverk

**Regulatorisk exponering:** Termen "säkerhetskänslig information" är ett juridiskt tekniskt begrepp under **Säkerhetsskyddslagen (2018:585)**. Genom att använda termen i en formellt fastställd policy utan definition riskerar MissionPoint att:

1. Oavsiktligt bekräfta att de hanterar information som aktiverar säkerhetsskyddslagens krav
2. Skapa ett policylöfte (konfidentiell hantering, behörighetsbegränsning) utan att ha definierat hur det uppfylls
3. Vid en incident eller tillsyn — ha ett dokument som styrker att de *visste* att de hanterade den typen av information

**Bedömning:** Om MissionPoint **inte** hanterar säkerhetsskyddsklassad information i lagens mening — stryk termen och ersätt med något neutralt ("känslig information"). Om de **faktiskt** hanterar sådan information måste säkerhetsskyddslagen utredas separat och policyn kan inte godkännas utan den utredningen.

**Detta är det enskilt viktigaste tekniska fyndet i dokumentet.**

---

### 2.4 Avsnitt 9: Incidenthantering — KRITISKT FYND

**Teknisk bedömning:** Avsnitt 9 innehåller:
- Hänvisning till GDPR/Integritetspolicyn för personuppgiftsincidenter ✅
- Krav på rapportering till "ledningen" för övriga incidenter
- Incidentexempel

**Vad saknas för att detta ska vara en fungerande minimiprocess:**

| Element | Status | Effekt |
|---|---|---|
| Tidsgräns för intern rapportering | Saknas | Medarbetare vet inte hur snabbt de ska agera |
| Vem i "ledningen" | Saknas | Vid incident vet ingen vem som ska kontaktas |
| Vad som händer efter rapportering | Saknas | Ingen process, ingen eskalationskedja |
| 72-timmarsregeln (GDPR art. 33) | Omnämns *implicit* via hänvisning till Integritetspolicyn | Godkänt på policynivå — förutsätter att Integritetspolicyn faktiskt reglerar detta |

**Bedömning:** Avsnittet skapar en *illusion* av incidentprocess utan att leverera den. En medarbetare som läser dokumentet på natten vid en incident har inte tillräcklig information för att agera rätt. För ett kompakt dokument räcker det med tre meningar: *vem du ringer, när du ringer, vad som händer sedan*. Det saknas.

---

### 2.5 Avsnitt 11: Leverantörshantering

**Teknisk bedömning:** Avsnitt 11 kräver:
- Säkerhetsbedömning före nytt verktyg ✅
- Personuppgiftsbiträdesavtal där tillämpligt ✅
- EU/EES-prioritering ✅

**Vad saknas:**

Krav på **löpande uppföljning** av befintliga leverantörer saknas. Policyn reglerar *onboarding* men inte *livscykel*. En leverantör som godkändes 2020 med god säkerhetsnivå och sedan blivit försvagad faller utanför policyns räckvidd.

För NIS2-leverantörskedjeperspektivet (art. 21.2b) är det rimligt att policyn nämner att befintliga leverantörer med åtkomst till känslig information ska genomgå periodisk bedömning.

**Klassificering:** Medium — men relevant att lyfta som enkel textskärpning.

---

### 2.6 Avsnitt 12: Ansvar

**Teknisk bedömning:**

| Roll | Ansvar i policyn | Bedömning |
|---|---|---|
| Ledningen | "Att denna policy finns och följs" | ⚠️ Tomt åtagande — *hur* ansvarar ledningen? |
| Medarbetare | "Följa policyn, skydda information, rapportera" | ✅ Tillräckligt |
| Informationssäkerhetsansvarig (CIO) | Definieras i avs. 6 men kopplas inte till avs. 12 | ⚠️ Inkonsistens — ansvarig roll borde återfinnas i ansvarsavsnittet |
| Konsulter/uppdragstagare | Omfattas av scope (avs. 3) men saknas i ansvarsavsnittet | ⚠️ Strukturell brist — de som hanterar mest känslig information (systemåtkomst) har inget explicit ansvar formulerat |

**Klassificering:** Hög — ansvarsavsnittet är det styret lider mest av. Det skapar oklarheter vid uppföljning och disciplinärenden.

---

### 2.7 Avsnitt 13–15: Efterlevnad, uppdatering, historik

**Teknisk bedömning:**

Avsnitt 13 ("Brott mot denna policy kan leda till åtgärder beroende på omständigheterna") är juridiskt korrekt men operativt meningslöst. Det signalerar ingen faktisk konsekvens och skapar inte trovärdighet för policyn som styrande dokument.

Avsnitt 14 anger "minst årligen" — tillräckligt.

Avsnitt 15 (Revisionshistorik) är en tom tabell — korrekt för v1.0, men **ägare för revisionen** saknas explicit.

---

## 3. Sammanfattande luckmatris

| # | Fynd | Avsnitt | Typ | Klassificering | Åtgärdshorisont |
|---|---|---|---|---|---|
| F1 | "Säkerhetskänslig information" utan definition — potentiell aktivering av Säkerhetsskyddslagen | 7 | Regulatorisk | **Kritisk** | Omedelbart — blockar styrelsegodkännande |
| F2 | Incidenthantering saknar: vem som kontaktas, när, och vad som sker | 9 | Operationell + Regulatorisk | **Kritisk** | Omedelbart — NIS2-leverantörskedjekrav och GDPR art. 33 |
| F3 | Konsulter/uppdragstagare saknas i ansvarsavsnittet trots att de är i scope | 12 | Strukturell | **Hög** | 90 dagar |
| F4 | Ansvarsambiguitet vid faktisk systemåtkomst ("normalt inte operativt ägarskap") | 4 | Operationell | **Hög** | 90 dagar |
| F5 | Informationssäkerhetsansvarig (CIO) saknas i ansvarsavsnitt — inkonsistens | 6/12 | Strukturell | **Hög** | 90 dagar |
| F6 | Ledningens ansvar är tomt åtagande — ingen mekanism definierad | 12 | Strukturell | **Medium** | 6 månader |
| F7 | Leverantörsuppföljning (löpande) saknas — only onboarding täckt | 11 | Regulatorisk | **Medium** | 6 månader |
| F8 | Policydokumentets ägare och godkännandeprocess framgår ej av dokumentet | 14–15 | Strukturell | **Medium** | 6 månader |
| F9 | Riskhanteringsprocess omnämnd men ej definierad ens på miniminivå | 6 | Best practice | **Medium** | 6 månader |

---

## 4. Styrkor som ska bevaras

Följande delar av policyn är ovanliga och värdefulla — de ska **inte** röras vid revision:

| Element | Varför det är en styrka |
|---|---|
| AI-reglering (avs. 8) | Specifik, med konkreta förbud och tillåtna användningsfall. Ovanligt välformulerat. |
| EU/EES-lagringskrav (avs. 11.1) | Direkt GDPR-relevant, korrekt formulerat med undantagshantering. |
| Hybridarbete (avs. 10) | Grundregler finns. Proporterligt och praktiskt. |
| Leverantörs-scope (avs. 5) | NIS2-leverantörskedjeperspektivet är explicit adresserat — korrekt för MissionPoints profil. |

---

## 5. Bedömning: Kan styrelsen godkänna policyn i nuläget?

**Svar: Nej — inte utan att F1 och F2 är åtgärdade.**

| Scenario | Förutsättning |
|---|---|
| **Godkänn med villkor** | F1 (säkerhetskänslig information) och F2 (incidenthantering) åtgärdas som villkor för godkännande. F3–F5 åtgärdas inom 90 dagar. |
| **Åtgärda först** | Om MissionPoint faktiskt hanterar säkerhetsskyddsklassad information — hela säkerhetsskyddsfrågan måste utredas innan dokumentet fastställs. |

F1 och F2 är **inte** frågor om ambitionsnivå eller "less is more". De är minimikrav som även ett kortfattat dokument måste uppfylla. Resterande fynd (F3–F9) är förbättringar som kan hanteras i ordinarie revision — de blockerar inte styrelsegodkännande men bör loggas som åtgärdsplan.

---

*Nästa steg: Fas 3 — Förbättringsspecialist levererar kirurgiska textförslag för F1 och F2, utan att utöka dokumentets omfång.*
