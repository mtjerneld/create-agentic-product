# Kvalitetssäkrare

# Kvalitetssäkringsgranskning — MissionPoint IT- & Informationssäkerhetspolicy v1.0
**Roll:** Kvalitetssäkrare | **Fas:** Rapportering & rekommendationer
**Datum:** 2026-02-27 | **Leverans:** Slutligt granskningsresultat inför styrelsebeslut

---

## Inledning och granskningsmandat

Detta dokument är teamets sista kontrollstation innan leverans till MissionPoints styrelse. Granskningen verifierar att teamets samlade arbete är:

1. **Internt konsistent** — inga motstridiga bedömningar eller riskpoäng mellan roller
2. **Korrekt kalibrerat** — "less is more"-principen har faktiskt hållits; inga onödiga krav har smugit sig in
3. **Fullständigt på miniminivå** — inga kritiska fynd har fallit mellan stolarna
4. **Handlingsbart för styrelsen** — beslutsunderlaget är tydligt och inte längre än nödvändigt

**Antaganden som ärvs och bekräftas:** MissionPoint är inte primär NIS2-aktör. Säkerhetsskyddslagens aktiveringsstatus är oklar. Policyn är ensamt styrande dokument. Styrelsebeslutet som avses är godkännandeprocessen.

---

## 1. Internkonsistensverifiering

Granskning av om teamets roller är överens om fynd, risknivåer och prioriteringar.

| Fynd | Compliance | Standard | Granskar | Hotbild | Gap/Risk | Åtgärd | Utfall |
|---|---|---|---|---|---|---|---|
| F1 — Säkerhetskänslig info utan definition | ⚠️ Kritisk | — | ⚠️ Kritisk | ⚠️ Kritisk | 🔴 20p | Klarläggning + text | ✅ Konsistent |
| F2 — Incidenthantering utan tidsgränser/roller | ⚠️ Kritisk | ⚠️ Kritisk | ⚠️ Kritisk | ⚠️ Kritisk | 🔴 16p | Textändring | ✅ Konsistent |
| F3 — MFA/autentisering saknas | — | ⚠️ Kritisk | ⚠️ Kritisk | ⚠️ Kritisk | 🔴 16p | Textändring | ✅ Konsistent |
| F4 — Åtkomstkontroll/offboarding saknas | ⚠️ Hög | ⚠️ Hög | ⚠️ Hög | ⚠️ Hög | 🟠 15p | Textändring | ✅ Konsistent |
| F5 — Riskhanteringsprocess ej beskriven | ⚠️ Hög | ⚠️ Hög | ⚠️ Hög | — | 🟠 12p | Textändring | ✅ Konsistent |
| F6 — Förbättringsåtagande saknas | — | ⚠️ Medium | — | — | 🟡 8p | En mening | ✅ Konsistent |
| F7 — Utbildning/medvetenhet saknas | — | ⚠️ Medium | — | ⚠️ Medium | 🟡 8p | En mening | ✅ Konsistent |

**Utfall:** Inga motstridiga bedömningar identifierade. Risknivåer är enhetliga mellan rollerna.

**En notering:** Åtgärdsstrategen hanterar F6 och F7 trots att de klassas som Medium (8 poäng), vilket formellt faller utanför den uttalade prioriteringen "endast Kritisk och Hög". Åtgärderna är motiverade — de är vardera en mening och kostar ingenting — men det bör noteras att detta är en avvikelse från minimumorientering. Styrelsen bör informeras om att dessa är frivilliga förstärkningar, inte regulatoriska krav.

---

## 2. Kalibreringskontroll — "less is more"-principen

Granskning av om något av teamets förslag adderar onödig bulk.

| Kontrollpunkt | Bedömning |
|---|---|
| Inga nya avsnitt föreslagna | ✅ Bekräftat — alla ändringar är textskärpningar inom befintliga avsnitt |
| Inga ISO-certifieringskrav smugna in | ✅ Bekräftat — standarden tillämpas som baseline, ej certifieringsrevision |
| AI-reglering och EU/EES-lagring orörd | ✅ Bekräftat — identifierade som styrkor och lämnades intakta av samtliga roller |
| Inga "nice to have"-krav lyfta till kritisk/hög | ✅ Bekräftat — loggning, fysisk säkerhet, informationsklassningsschema m.m. är korrekt nedprioriterade |
| Hotbildsanalysen håller sig till MissionPoints faktiska profil | ✅ Bekräftat — analysen är kalibrerad mot konsultbolag med systemåtkomst, inte generisk |

**En avvikelse noterad och bedömd som acceptabel:** Åtgärdsstrategen föreslår att godkännandeprocessen dokumenteras i revisionshistoriken (F8, implicit). Detta är korrekt och minimalt — det handlar om att fylla i ett fält som redan finns i dokumentet, inte om att lägga till nytt innehåll.

---

## 3. Fullständighetskontroll — har något kritiskt missats?

Kontroll mot teamets kunskapsbas och regulatoriska ramverk.

### 3.1 Fynd som inte lyfts — motivering granskas

| Potentiellt fynd | Teamets hantering | QA-bedömning |
|---|---|---|
| Loggning och övervakning saknas | Nedprioriterat — Medium/Låg för konsultprofil | ✅ Korrekt för minimum |
| Fysisk säkerhet ej adresserad | Nedprioriterat — inte primärt för konsultbolag utan egna serverhallar | ✅ Korrekt |
| Informationsklassningsschema saknas | Nedprioriterat — kan hanteras i underliggande riktlinje | ✅ Korrekt |
| Business Continuity/DR saknas | Nedprioriterat — inte aktiverat för icke-primär NIS2-aktör på denna nivå | ✅ Acceptabelt, men se not nedan |
| DORA-exponering (leverantörsled) | Nämnd som villkorlig — inte bedömd vidare | ✅ Korrekt att parkera utan kundbekräftelse |
| Krypteringskrav ej specificerade | Inte explicit adresserat av något team | ⚠️ **Se avsnitt 3.2** |

### 3.2 Ett fynd som saknas i teamets leverans

**Kryptering och nyckelhantering (GDPR art. 32, ISO 27001 A.8.24)**

Teamet har inte explicit adresserat att policyn saknar varje krav på kryptering — varken för data i vila eller data i transit. För en organisation som hanterar systemåtkomst, konfidentiella dokument och personuppgifter hos kunder är detta en reell lucka.

**QA-bedömning av allvarlighetsgrad:**

Åtgärdsstrategen täckte MFA under F3 (autentisering), vilket är det mest akuta. Krypteringskrav är av liknande karaktär men något lägre prioritet eftersom:
- GDPR art. 32 kräver "lämpliga tekniska åtgärder" men specificerar inte kryptering som absolut krav
- Policyn hänvisar till "godkända system" (avs. 7) vilket indirekt kan täcka detta i praktiken

**Klassificering:** Hög (Sannolikhet 3 × Konsekvens 4 = 12). Bör adresseras men blockerar inte styrelsebeslut.

**Föreslagen minimal åtgärd** (tillägg i avsnitt 10 eller nytt stycke i avsnitt 6):

> *Känslig information ska krypteras vid lagring och överföring. Krypteringslösningar ska vara godkända av informationssäkerhetsansvarig.*

---

## 4. Slutlig riskbild — konsoliderad och QA-verifierad

Nedanstående lista är teamets fynd efter QA-kontroll, kompletterad med krypteringsfyndet.

| # | Fynd | Nivå | Poäng | Åtgärd | Blockerar styrelsebeslut? |
|---|---|---|---|---|---|
| F1 | "Säkerhetskänslig information" utan definition | 🔴 Kritisk | 20 | Klarläggning med MissionPoint + textändring | **JA** |
| F2 | Incidenthantering utan tidsgränser och rollansvar | 🔴 Kritisk | 16 | Textändring (avs. 9) | **JA** |
| F3 | MFA/autentiseringskrav saknas | 🔴 Kritisk | 16 | Textändring (nytt stycke i avs. 6 eller 10) | **JA** |
| F4 | Åtkomstkontroll och offboarding saknas | 🟠 Hög | 15 | Textändring (avs. 12 eller nytt stycke i avs. 6) | Nej — villkorat |
| F5 | Riskhanteringsprocess ej beskriven | 🟠 Hög | 12 | Textändring (avs. 6) | Nej — villkorat |
| F8 | Krypteringskrav saknas *(nytt QA-fynd)* | 🟠 Hög | 12 | En mening i avs. 6 eller 10 | Nej — villkorat |
| F6 | Förbättringsåtagande saknas | 🟡 Medium | 8 | En mening i avs. 6 | Nej |
| F7 | Utbildning/medvetenhet ej omnämnt | 🟡 Medium | 8 | En mening i avs. 12 | Nej |

**Definition av "blockerar":** Kritiska fynd (F1–F3) innebär att policyn i nuvarande skick antingen skapar direkt regulatorisk exponering (F1: potentiell säkerhetsskyddslags-aktivering), bryter mot GDPR art. 33 (F2: ingen 72h-process), eller lämnar den mest frekventa angreppsytan helt oreglerad (F3: ATO/nätfiske). Styrelsen bör inte godkänna utan att dessa är åtgärdade eller att MissionPoint aktivt och dokumenterat accepterar riskerna.

---

## 5. Styrkor som bekräftas — bevara vid revision

Dessa avsnitt är genuint välgjorda och ska inte röras vid kommande revision utan starka skäl.

| Styrka | Avsnitt | Motivering |
|---|---|---|
| AI-reglering med konkreta förbud och tillåtna användningsfall | 8 | Ovanligt specifikt och korrekt. Täcker GDPR art. 5 implicit. |
| EU/EES-krav för molntjänstlagring | 11.1 | Direkt GDPR-relevant, korrekt formulerat. |
| Hybridarbete reglerat | 10 | Grundläggande och tillräckligt för policynivå. |
| Leverantörsbedömning och PBA-krav | 11 | Proportionerligt och korrekt kopplat till GDPR art. 28. |
| Scope täcker konsulter och kundsystem | 3 | Kritiskt för en organisation med systemåtkomst — korrekt gjort. |

---

## 6. Rekommendation till styrelsen

### Beslutsalternativ

**Alternativ A — Godkänn med villkor (rekommenderas)**

Styrelsen godkänner policyn under förutsättning att F1, F2 och F3 är åtgärdade inom 30 dagar och att den reviderade versionen dokumenteras i revisionshistoriken (avs. 15) och fastställs av styrelsen eller delegerat organ.

F4, F5 och F8 åtgärdas inom 90 dagar som en del av ordinarie implementeringsplan.

> *Detta är ett rationellt beslut. Policyn är välstrukturerad för sin ambitionsnivå och har reella styrkor. De kritiska fynden är åtgärdbara med minimala textändringar — inte strukturella omskrivningar.*

**Alternativ B — Åtgärda F1–F3 innan styrelsemöte**

Om styrelsen föredrar att godkänna ett komplett dokument: åtgärda de tre kritiska fynden (skattad arbetstid: 2–4 timmar) och presentera v1.1 för beslut.

**Alternativ C — Avvisa och återremittera**

Inte motiverat. Policyn är ett seriöst dokument med identifierbara, reparabara brister — inte ett dokument med fundamentala strukturproblem.

---

### Sammanfattning i ett stycke för styrelseprotokoll

> *MissionPoints IT- och Informationssäkerhetspolicy v1.0 uppfyller minimumet för en kompakt policynivå inom flertalet områden och innehåller genuina styrkor inom AI-reglering och molnlagring. Tre kritiska brister identifieras: termen "säkerhetskänslig information" används utan definition (potentiell aktivering av säkerhetsskyddslagen), incidenthanteringen saknar tidsgränser och rollansvar (GDPR 72h-krav), samt att krav på flerfaktorsautentisering saknas (primär angreppsyta för konsultbolag). Styrelsen rekommenderas godkänna policyn villkorat på att dessa tre punkter åtgärdas inom 30 dagar och att reviderad version v1.1 fastställs.*

---

*Dokument färdigställt av: Kvalitetssäkrare | Granskat mot: Teamets samtliga fas 1–2-leveranser | Status: Redo för styrelsebeslut*
