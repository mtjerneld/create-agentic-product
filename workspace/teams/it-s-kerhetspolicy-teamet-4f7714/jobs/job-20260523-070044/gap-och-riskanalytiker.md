# Gap- och Riskanalytiker

# Gap- & Riskanalys — MissionPoint IT- & Informationssäkerhetspolicy v1.0
**Roll:** Gap- och Riskanalytiker
**Fas:** Gap-analys & riskvärdering
**Datum:** 2026-02-27 | **Dokument:** MissionPoint IT- och Informationssäkerhetspolicy v1.0

---

## Metodologisk position

Detta dokument sammanställer, konsoliderar och rangordnar alla luckor identifierade av teamets fyra tidigare roller (Regulatorisk Complianceanalytiker, Standardspecialist, IT-säkerhetspolicygranskar, Hotbildsrådgivare). Riskvärdering sker enligt etablerad modell:

**Riskpoäng = Sannolikhet (1–5) × Konsekvens (1–5)**

| Nivå | Poäng | Åtgärdshorisont |
|---|---|---|
| Kritisk | 16–25 | 0–30 dagar |
| Hög | 9–15 | 90 dagar |
| Medium | 4–8 | 6 månader |
| Låg | 1–3 | Ordinarie revision |

**Kalibrering mot uppdraget:** Principen "less is more" är styrande. Luckor lyfts **endast** om de utgör regulatorisk exponering, operationell hotyta eller strukturell brist som undergräver policyn som styrdokument. "Nice to have" lyfts inte.

**Gemensamma antaganden (ärvda från fas 1–2):**
- MissionPoint är **inte** primär NIS2-aktör — NIS2 tillämpas via leverantörskedjeperspektivet (art. 21.3).
- Policyn är ensamt styrdokument; inga kompenserande underpolicyer eller processer kan antas existera.
- Säkerhetsskyddslagens aktiveringsstatus är **obekräftad** — detta är ett eget kritiskt fynd.
- MissionPoint hanterar systemåtkomst och säkerhetsanalyser hos kunder i potentiellt reglerade sektorer.

---

## 1. Konsoliderad luckmatris

Innan riskvärdering — fullständig inventering av identifierade luckor från fas 1–2, normaliserade och avduplicerade.

| ID | Lucka | Källa (roll) | Berört ramverk |
|---|---|---|---|
| G-01 | "Säkerhetskänslig information" listad utan definition eller hanteringsregler | Compliance, Granskar, Hotbild | Säkerhetsskyddslagen (2018:585) |
| G-02 | Incidenthantering saknar tidsgränser, rollbeskrivningar och eskalationskedja | Compliance, Standard, Granskar, Hotbild | GDPR art. 33 (72h), NIS2 art. 23 |
| G-03 | MFA/autentiseringskrav saknas helt | Granskar, Hotbild | GDPR art. 32, NIS2 art. 21 |
| G-04 | Riskhanteringsprocess omnämnd som princip men ingen process definierad | Standard, Granskar | ISO 27001 kl. 6.1, NIS2 art. 21 |
| G-05 | Offboarding/åtkomstkontroll vid avslut saknas | Granskar, Hotbild | GDPR art. 25, ISO 27001 A.5.18 |
| G-06 | Utbildning/säkerhetsmedvetenhet saknas | Standard, Hotbild | ISO 27001 kl. 7.2, NIS2 art. 21 |
| G-07 | Leverantörsstyrning otillräcklig — ingen kravnivå för kritiska leverantörer | Compliance, Standard | GDPR art. 28, NIS2 art. 21 |
| G-08 | Godkännandeprocess och policyägare saknas i dokumentet | Granskar | ISO 27001 kl. 5.1 |
| G-09 | Förbättringsåtagande saknas (continual improvement) | Standard | ISO 27001 kl. 5.2, kl. 10 |
| G-10 | Informationsklassificering — ingen klassificeringsstruktur, bara lista av informationstyper | Compliance, Standard | ISO 27002 A.5.12, MSB MSBFS 2020:6 |
| G-11 | Distansarbete — VPN-krav saknas | Granskar, Hotbild | ISO 27001 A.6.7, GDPR art. 32 |
| G-12 | Krypteringskrav saknas | Compliance, Granskar | GDPR art. 32, ISO 27001 A.8.24 |

---

## 2. Prioriterad risklista

### 🔴 KRITISK — Åtgärd inom 30 dagar

---

#### R-01 — Säkerhetsskyddslagens aktiveringsstatus obekräftad
**Källa:** G-01 | **Ramverk:** Säkerhetsskyddslagen (2018:585)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **4** — Konsultorganisation med systemåtkomst och säkerhetsanalyser; "säkerhetskänslig information" listad som hanterad kategori. Stor sannolikhet att lagen är tillämplig. |
| Konsekvens | **5** — Om lagen är tillämplig och organisationen saknar säkerhetsskyddsanalys och avtal kan det utgöra ett direkt lagbrott. Inga kompenserande kontroller kan antas. |
| **Riskpoäng** | **4 × 5 = 20 — KRITISK** |

**Preciserad lucka:** Avsnitt 7 listar "Säkerhetskänslig information" som en informationskategori MissionPoint hanterar, utan att definiera termen, ange hanteringsregler eller hänvisa till säkerhetsskyddslagen. Om organisationen bedriver säkerhetskänslig verksamhet eller är leverantör till sådan, utan att ha genomfört en säkerhetsskyddsanalys och tecknat erforderliga säkerhetsskyddsavtal, föreligger potentiellt lagbrott.

**Åtgärd:** Omedelbar dialog med kunden för att fastställa om säkerhetsskyddslagen är aktiverad. Antingen (a) ta bort termen "säkerhetskänslig information" ur policyn och ersätt med en neutral term som "skyddsvärd information", eller (b) bekräfta status och initiera säkerhetsskyddsanalys. **Detta är ett stoppkrav inför styrelsegodkännande.**

---

#### R-02 — Incidenthantering utan 72-timmarsregel och eskalationskedja
**Källa:** G-02 | **Ramverk:** GDPR art. 33, NIS2 art. 23 (indirekt)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **4** — Nätfiske och ATO är vanliga mot konsultbolag; incident är inte en hypotetisk situation utan ett sannolikt scenario inom ett år. |
| Konsekvens | **4** — Utebliven anmälan till IMY inom 72h är direkt sanktionsgrundande. Utan definierade roller och tidsgränser i policyn vet ingen vad som gäller när det väl händer. |
| **Riskpoäng** | **4 × 4 = 16 — KRITISK** |

**Preciserad lucka:** Avsnitt 9 nämner GDPR-anmälningsplikt men hänvisar till Integritetspolicyn utan att definiera: (1) 72-timmarsgränsen, (2) vem som beslutar om anmälningsplikt, (3) eskalationskedja internt. "Rapporteras så snart som möjligt till ledningen" är inte en process — det är en intention. Hotbildsanalysen bekräftar att MFA-brist (G-03) gör ATO till ett sannolikt incidentscenario.

**Åtgärd:** Komplettera avsnitt 9 med tre meningar: (1) explicit 72-timmarsregel vid personuppgiftsincident, (2) namngiven beslutsansvarig (informationssäkerhetsansvarig/CIO), (3) en mening om intern eskalation innan extern anmälan. Inga nya avsnitt behövs — kirurgisk tillägg i befintlig text.

---

#### R-03 — MFA/autentiseringskrav saknas för systemåtkomst hos kunder
**Källa:** G-03 | **Ramverk:** GDPR art. 32, NIS2 art. 21 (indirekt)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **5** — Kontoövertagande via stulna credentials är den vanligaste intrångsvektorn mot konsultbolag 2024–2025 (ENISA ETL 2024, NCSC-SE). Utan MFA-krav i policy finns inget skydd mot detta. |
| Konsekvens | **4** — MissionPoints åtkomst till kundsystem innebär att ett komprometterat konto ger angriparen fotfäste i kundens miljö. Supply chain-exponering maximerar konsekvensen. |
| **Riskpoäng** | **5 × 4 = 20 — KRITISK** |

**Preciserad lucka:** Policyn saknar varje krav på stark autentisering. Distansarbetsavsnittet (avs. 10) kräver företagsdator men nämner inte lösenordshantering, MFA eller VPN. För en organisation vars medarbetare har inloggningsuppgifter till kundsystem är detta den enskilt mest operationellt riskabla luckan.

**Åtgärd:** Lägg till en mening i avsnitt 10 (Distansarbete) eller avsnitt 12 (Ansvar) som kräver MFA för åtkomst till kundsystem och interna system med förhöjd känslighet. Alternativt ett minimalt nytt avsnitt "Åtkomstkontroll" med två–tre meningar. Behåll principen om kompakthet.

---

### 🟠 HÖG — Åtgärd inom 90 dagar

---

#### R-04 — Riskhantering saknar process trots explicit anspråk
**Källa:** G-04 | **Ramverk:** ISO 27001 kl. 6.1, NIS2 art. 21 (indirekt)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **3** — Avsaknad av riskprocess är vanlig i unga policyer; sannolikhet att det saknas i praktiken är hög. |
| Konsekvens | **4** — Policyn säger att MissionPoint "arbetar riskbaserat" (avs. 6) utan att definiera hur. Om en kund eller revisor begär dokumentation finns inget att visa. Skapar trovärdighetsproblem och potentiell avtalsexponering. |
| **Riskpoäng** | **3 × 4 = 12 — HÖG** |

**Preciserad lucka:** "Riskbaserat" är ett tomt löfte utan en minimiprocess. Policyn skapar en förväntning som den inte kan infria. Luckan är inte att MissionPoint saknar riskprocess i verkligheten — det vet vi inte — utan att policyn skapar ett anspråk utan substans.

**Åtgärd:** Antingen (a) stryk "riskbaserat" ur avsnitt 6 och ersätt med "proportionellt", eller (b) lägg till en mening som beskriver att riskbedömning sker vid varje nytt uppdrag och vid väsentliga förändringar. Alternativ (a) är enklast och håller minimumet.

---

#### R-05 — Offboarding och åtkomstkontroll vid avslut saknas
**Källa:** G-05 | **Ramverk:** GDPR art. 25, ISO 27001 A.5.18

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **4** — Kvarstående åtkomst efter uppdragsavslut är ett dokumenterat vanligt mönster i konsultorganisationer (insider-hot, ENISA ETL 2024). |
| Konsekvens | **3** — Kvarstående åtkomst till kundsystem efter uppdragsavslut är ett konkret hot mot kundens integritet och en potentiell GDPR-exponering för MissionPoint. |
| **Riskpoäng** | **4 × 3 = 12 — HÖG** |

**Preciserad lucka:** Policyn reglerar inte vad som händer när en anställd eller konsult slutar, eller när ett kunduppdrag avslutas. Ingen mening om återlämnande av åtkomst, radering av kunddata eller avslutsprocedur.

**Åtgärd:** En mening i avsnitt 12 (Ansvar) eller avsnitt 3 (Omfattning): "Vid avslut av anställning, konsultuppdrag eller kundrelation ska åtkomst till system och kunddata omedelbart återkallas och eventuell kunddata raderas eller återlämnas i enlighet med avtal."

---

#### R-06 — Säkerhetsutbildning saknas — inga krav på medarbetarbeteende
**Källa:** G-06 | **Ramverk:** ISO 27001 kl. 7.2, NIS2 art. 21 (indirekt)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **4** — Nätfiske är primär intrångsvektor; utan utbildningskrav i policy är det troligt att medarbetare saknar gemensam lägstanivå. |
| Konsekvens | **3** — Mänskliga misstag är den vanligaste incidentorsaken. Utan utbildningskrav i policy kan MissionPoint inte visa att man vidtagit "lämpliga åtgärder" enligt GDPR art. 32. |
| **Riskpoäng** | **4 × 3 = 12 — HÖG** |

**Preciserad lucka:** Policyn ställer krav på vad medarbetare *inte* får göra (dela data med AI, använda öppet Wi-Fi) men innehåller inget krav på att medarbetare ska ha grundläggande säkerhetsutbildning. En nyanställd konsult utan säkerhetsutbildning lyder formellt under policyn — men har inte fått de verktyg som krävs för att följa den.

**Åtgärd:** En mening i avsnitt 12 (Ansvar) under Ledningens ansvar: "Ledningen ansvarar för att alla medarbetare och konsulter erhåller grundläggande informationssäkerhetsutbildning vid introduktion och vid väsentliga förändringar av policyn."

---

#### R-07 — Leverantörsstyrning — ingen kravnivå för kritiska leverantörer
**Källa:** G-07 | **Ramverk:** GDPR art. 28, NIS2 art. 21 (indirekt)

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **3** — Att personuppgiftsbiträdesavtal saknas med molnleverantörer är vanligt i liknande organisationer. |
| Konsekvens | **3** — Saknat biträdesavtal med en leverantör som behandlar personuppgifter är direkt GDPR-brott. Komprometterad molntjänst utan avtalat säkerhetskrav ger MissionPoint minimal reklamationsrätt. |
| **Riskpoäng** | **3 × 3 = 9 — HÖG** |

**Preciserad lucka:** Avsnitt 11 anger att säkerhetsbedömning *kan* inkludera biträdesavtal ("där tillämpligt"). "Kan inkludera" och "där tillämpligt" är inte krav — det är en möjlighet. GDPR art. 28 kräver att biträdesavtal *ska* finnas när en leverantör behandlar personuppgifter, utan undantag.

**Åtgärd:** Ändra formuleringen i avsnitt 11 från "kan inkludera personuppgiftsbiträdesavtal där tillämpligt" till "ska inkludera personuppgiftsbiträdesavtal när leverantören behandlar personuppgifter". En ordning-förändring, ingen strukturell utökning.

---

### 🟡 MEDIUM — Åtgärd inom 6 månader

---

#### R-08 — Policyägare och godkännandeprocess saknas
**Källa:** G-08 | **Ramverk:** ISO 27001 kl. 5.1

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **2** — Styrelsebeslutet som är på gång *är* godkännandeprocessen; operativt sannolikt löst. |
| Konsekvens | **3** — Utan namngiven ägare vet ingen vem som kallar till revision eller kan fatta beslut om nöduppdatering vid incident. |
| **Riskpoäng** | **2 × 3 = 6 — MEDIUM** |

**Åtgärd:** Lägg till policyägarens roll (CIO) och godkännandeinstans (styrelsen) i avsnitt 14 eller som metadata i dokumenthuvudet. En rad.

---

#### R-09 — VPN-krav saknas i distansarbetsavsnittet
**Källa:** G-11 | **Ramverk:** ISO 27001 A.6.7, GDPR art. 32

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **3** — Medarbetare arbetar på kundkontor och externa miljöer; exponering mot osäkra nätverk är trolig utan VPN-krav. |
| Konsekvens | **2** — Öppna nätverk möjliggör avlyssning, men konsekvensen begränsas av att företagsdator krävs (avs. 10). |
| **Riskpoäng** | **3 × 2 = 6 — MEDIUM** |

**Åtgärd:** Komplettera avsnitt 10 med: "Vid arbete utanför kontoret ska VPN eller annan krypterad förbindelse användas för åtkomst till företagets och kunders system."

---

#### R-10 — Krypteringskrav saknas
**Källa:** G-12 | **Ramverk:** GDPR art. 32, ISO 27001 A.8.24

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **2** — Modern företagsdator har ofta diskkryptering aktiverad av default; inte säkert att luckan existerar i praktiken. |
| Konsekvens | **3** — Förlorad okrypterad dator med kunddata är en rapporteringspliktig GDPR-incident. |
| **Riskpoäng** | **2 × 3 = 6 — MEDIUM** |

**Åtgärd:** En mening i avsnitt 10 eller 12: "Företagsdatorer ska ha hårddiskkryptering aktiverad."

---

#### R-11 — Informationsklassificering — lista utan struktur
**Källa:** G-10 | **Ramverk:** ISO 27002 A.5.12, MSB MSBFS 2020:6

| Parameter | Bedömning |
|---|---|
| Sannolikhet | **2** — Avsaknad av klassificeringsstruktur är vanlig; men policyn listar faktiskt kategorier vilket ger viss struktur. |
| Konsekvens | **2** — Operationell konsekvens begränsas av att hanteringsreglerna (avs. 7) ändå kräver konfidentialitet för allt. |
| **Riskpoäng** | **2 × 2 = 4 — MEDIUM** |

**Åtgärd:** Kan hanteras vid ordinarie revision eller i ett separat klassificeringsdokument. Inte ett minimikrav för policynivå i en kompakt policy.

---

### 🟢 LÅG — Ordinarie revision

| ID | Lucka | Poäng | Motivering |
|---|---|---|---|
| R-12 | Förbättringsåtagande saknas (continual improvement) | **2** (1×2) | Strukturellt korrekt att ha, men påverkar inte operationell säkerhet eller regulatorisk exponering på kort sikt. |
| R-13 | Krypteringskrav för e-post och fildelning | **2** (1×2) | Kan adresseras i riktlinjer under policyn. Inte minimikrav på policynivå. |

---

## 3. Sammanfattande risköversikt

```
KRITISK (åtgärd 0–30 dagar)
├── R-01 Säkerhetsskyddslagens aktiveringsstatus        20p ████████████████████
├── R-02 Incidenthantering utan 72h-regel               16p ████████████████
└── R-03 MFA/autentiseringskrav saknas                  20p ████████████████████

HÖG (åtgärd inom 90 dagar)
├── R-04 Riskhantering — tomt anspråk                   12p ████████████
├── R-05 Offboarding/åtkomstkontroll saknas             12p ████████████
├── R-06 Säkerhetsutbildning saknas                     12p ████████████
└── R-07 Biträdesavtal — "kan" i stället för "ska"       9p █████████

MEDIUM (åtgärd inom 6 månader)
├── R-08 Policyägare och godkännandeprocess              6p ██████
├── R-09 VPN-krav saknas                                 6p ██████
├── R-10 Krypteringskrav saknas                          6p ██████
└── R-11 Informationsklassificering utan struktur        4p ████

LÅG (ordinarie revision)
├── R-12 Förbättringsåtagande                            2p ██
└── R-13 Kryptering e-post/fildelning                    2p ██
```

---

## 4. Stoppkrav inför styrelsegodkännande

Styrelsen bör **inte godkänna policyn i nuvarande form** utan att följande är hanterat:

> **S-1 (R-01):** Klarlägg om Säkerhetsskyddslagen är tillämplig. Ta bort eller definiera termen "säkerhetskänslig information" i avsnitt 7. Kräver dialog med kunden — **kan inte lösas av styrelsen utan underlag från ledningen.**

> **S-2 (R-02):** Komplettera avsnitt 9 med 72-timmarsregel och ansvarig beslutsfattare. Kirurgisk ändring — **kan göras innan styrelsemötet.**

> **S-3 (R-03):** Lägg till MFA-krav för systemåtkomst. En mening — **kan göras innan styrelsemötet.**

Styrelsen kan godkänna policyn **villkorligt** med krav att R-04 till R-07 åtgärdas inom 90 dagar, med rapportering tillbaka till styrelsen.

---

## 5. Vad som ska bevaras oförändrat

Per kickoff-briefens direktiv och tidigare fas-analyser — dessa delar av policyn fungerar och ska inte röras:

| Avsnitt | Styrka |
|---|---|
| Avsnitt 8 — AI-reglering | Konkret, specifik, ovanligt välformulerad. Bevaras intakt. |
| Avsnitt 11.1 — EU/EES-lagring | Korrekt GDPR-hantering. Bevaras intakt. |
| Avsnitt 5 — Leverantörskedjeperspektiv (NIS2) | Visar medvetenhet om indirekt NIS2-beröring. Bevaras intakt. |
| Avsnitt 10 — Distansarbete (grundstruktur) | Rätt principer; behöver komplettering med VPN och MFA, inte omskrivning. |

---

*Dokument producerat av Gap- och Riskanalytiker — underlag för fas 3 (förbättringsförslag & reviderad text).*
