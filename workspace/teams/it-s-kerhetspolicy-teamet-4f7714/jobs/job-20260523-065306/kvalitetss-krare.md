# Kvalitetssäkrare

# Kvalitetsgranskning: Slutleverans
## MissionPoint AB — IT- och Informationssäkerhetspolicy v1.0
### Granskningsresultat inför överlämning till uppdragsgivaren

**Roll:** Kvalitetssäkrare
**Fas:** Rapportering & rekommendationer
**Datum:** 2026-02-27
**Underlag:** Samtliga teamleveranser (Complianceanalytiker, Standardspecialist, IT-säkerhetspolicygranskar, Hotbildsrådgivare, Gap- och Riskanalytiker, Åtgärdsstrateg)

---

## 1. Granskningens syfte och metod

Denna kvalitetsgranskning utgör det sista grindvaktssteget innan leveranspaketet överlämnas till MissionPoints IT-chef. Granskningen kontrollerar tre dimensioner:

1. **Intern konsistens** — Säger teamets leveranser samma saker? Finns motstridiga fynd eller rekommendationer?
2. **Faktakorrekthet och regulatorisk precision** — Är hänvisningar till regelverk och standarder korrekta och aktuella för Sverige 2025/2026?
3. **Fullständighet och handlingsbarhet** — Täcker leveranspaketet hela uppdraget? Kan IT-chefen faktiskt agera på det som levereras?

**Granskningsmetod:** Korsläsning av alla fas-leveranser mot (a) ursprunglig policytext, (b) teamets kunskapsbas och (c) varandra. Avvikelser flaggas med åtgärdsrekommendation.

---

## 2. Övergripande kvalitetsomdöme

> **Leveranspaketet håller sammantaget hög kvalitet och är klart för överlämning med fem villkorade korrigeringar och tre förtydliganden som måste adresseras före leverans.**

Teamets arbete är välstrukturerat, regulatoriskt välgrundat och internt konsistent i de väsentliga delarna. Den analytiska kedjan från gap-inventering → riskvärdering → åtgärdsplan är logisk och spårbar. Nedanstående avsnitt dokumenterar specifika avvikelser, luckor och inkonsistenser som kräver åtgärd.

---

## 3. Intern konsistensanalys

### 3.1 Avvikelser och motstridigheter mellan teamleveranser

| ID | Avvikelse | Berörd leverans | Bedömning | Åtgärd |
|---|---|---|---|---|
| **KA-01** | Gap-analytikern listar 23 identifierade gap men Åtgärdsstrategens plan adresserar explicit 14 åtgärdspunkter (K1–K5, H1–H4, M1–M3, L1–L2). Nio gap saknar explicit åtgärd i åtgärdsplanen. | Gap-analytiker vs. Åtgärdsstrateg | ⚠️ Inkonsistens | Se §3.2 nedan — identifiera och adressera de nio saknade |
| **KA-02** | IT-säkerhetsgranskarens bristmatris listar "Krypterings- och nyckelhantering" som Kritisk (S6), men Gap-analytikers riskvärdering placerar motsvarande G-06 som Hög (riskpoäng 12). Prioriteringsdiskrepans utan motivering. | IT-granskar vs. Gap-analytiker | ⚠️ Inkonsistens | Harmonisera prioritering; om nedgradering skett ska motivering dokumenteras |
| **KA-03** | Hotbildsrådgivarens analys lyfter M365-kompromittering (APT29) som kritisk exponering, men ingen av de efterföljande leveranserna omsätter detta i en konkret åtgärd (t.ex. MFA-krav, Conditional Access). | Hotbildsrådgivare vs. Åtgärdsstrateg | ⚠️ Lucka i kedja | Åtgärdsstrategens K4 (teknisk säkerhetsbaseline) bör explicit nämna M365-härdning och MFA som minimikrav |
| **KA-04** | Säkerhetsskyddslagen flaggas som öppen fråga av Complianceanalytikern (Antagande A3) och lämnas utanför av IT-säkerhetsgranskar. Frågan återkommer aldrig i åtgärdsplanen med ett konkret nästa steg för MissionPoint att stänga den. | Complianceanalytiker vs. Åtgärdsstrateg | ⚠️ Oavslutad tråd | Lägg till en explicit åtgärdspunkt: "Genomför juridisk screening mot Säkerhetsskyddslagen senast [datum]" |
| **KA-05** | NIS2-klassificeringen av MissionPoint formuleras konsekvent som antagande i tidiga leveranser, men i Åtgärdsstrategens text glider formuleringen i ett par ställen mot att behandla NIS2-krav som direkttillämpliga snarare än indirekta. | Åtgärdsstrateg | ⚠️ Precisionsbrist | Säkerställ att alla NIS2-referenser i åtgärdsplanen tydligt anger om kravet är direkt eller via leverantörskedja |

### 3.2 De nio gap utan explicit åtgärd

Baserat på korsläsning av Gap-analytikers G-01 till G-23 mot Åtgärdsstrategens åtgärdslista identifieras följande gap som saknar namngiven åtgärdspunkt:

| Gap-ID | Beskrivning | Riskpoäng (estimat) | Rekommenderad hantering |
|---|---|---|---|
| G-08 | Inga mätbara säkerhetsmål eller KPI:er | ~9 (Hög) | Lägg till i Åtgärdsstrategens H-lista: kräver att informationssäkerhetsansvarig sätter minst tre mätbara mål vid nästa ledningsgenomgång |
| G-09 | CISO-rollens mandat och eskalationsväg otydlig | ~10 (Hög) | Kräver uppdatering av §12 med explicit mandat och rapporteringsväg till ledning/styrelse |
| G-11 | Säkerhetsmedvetenhet och utbildning saknas helt | ~8 (Medium) | Minimiåtgärd: en obligatorisk onboarding-modul och årlig uppfriskning |
| G-14 | Fysisk säkerhet ej adresserad | ~6 (Medium) | Enkel tillägg i §3 (scope) och separat instruktion för kontorsmiljö |
| G-15 | Sårbarhetshanterings- och patchprocess saknas | ~12 (Hög) | Kritisk för konsultbolag med outsourcad IT — kräver SLA-krav mot IT-leverantör |
| G-17 | Loggar och övervakning ej omnämnda | ~9 (Hög) | Minsta krav: loggningspolicy som täcker åtkomst till kundsystem |
| G-19 | Informationsklassificeringens nivåer ej definierade | ~8 (Medium) | §7 nämner kategorier men inte klassificeringsnivåer; lägg till enkel fyrgradig modell |
| G-21 | Säkerhet i systemutveckling/integration saknas | ~6 (Medium) | Relevant om MissionPoint levererar tekniska lösningar; klargör scope |
| G-23 | Revisionshistorik i §15 är tom | ~4 (Medium) | Administrativt: fyll i vid publicering; lägg till process för ändringshantering |

> **Åtgärd:** Åtgärdsstrategens leverans kompletteras med ovanstående nio punkter före slutleverans. Alternativt samlas de i ett separat tillägg märkt "Åtgärder — Kompletterande lista" och bifogas åtgärdsplanen.

---

## 4. Faktakorrekthet och regulatorisk precision

### 4.1 Korrekta och välgrundade hänvisningar ✅

Följande regulatoriska hänvisningar har verifierats som korrekta och aktuella:

- **GDPR art. 33–34** (72-timmarsregel för personuppgiftsincidenter) — korrekt tillämpad i K1
- **NIS2 art. 23** (incidentrapportering) — korrekt tillämpat som indirekt krav via leverantörskedja
- **NIS2 art. 21** (säkerhetsåtgärder inklusive BC/DR och tredjepartsrisk) — korrekt
- **ISO 27001:2022 kl. 6.1** (riskhantering) — korrekt refererad
- **ISO 27001:2022 A.5.15–A.5.18** (IAM och åtkomstkontroll) — korrekt
- **GDPR art. 28** (personuppgiftsbiträdesavtal) — korrekt identifierat som relevant för MissionPoints dubbla roll
- **Dataskyddslagen (2018:218)** — korrekt noterad som komplement till GDPR

### 4.2 Regulatoriska preciseringar som behöver korrigeras

| ID | Avvikelse | Berörd leverans | Korrekt formulering |
|---|---|---|---|
| **KF-01** | Åtgärdsstrategens K1 anger att NIS2-anmälan ska ske till "MSB". Korrekt primär mottagare för NIS2-incidentrapporter är den *sektorsansvariga tillsynsmyndigheten* (t.ex. Finansinspektionen för finans, IVO för vård) — MSB är samordnande myndighet men inte alltid anmälningsmottagare. För ett konsultbolag som indirekt berörs är instruktionen att kunden anmäler; MissionPoint ska stödja kunden med underlag. | Åtgärdsstrateg K1 | Ersätt "anmälan till MSB" med "stöd kunden i anmälan till berörd tillsynsmyndighet; kontrollera per kund vilken myndighet som är mottagare" |
| **KF-02** | IMY anges korrekt som mottagare för GDPR-incidenter. Komplettera med att IMY-anmälan avser MissionPoints roll som *personuppgif
