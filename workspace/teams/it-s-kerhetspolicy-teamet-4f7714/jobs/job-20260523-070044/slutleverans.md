# Projektledare & Granskningskoordinator · Slutleverans

# Granskningsrapport: MissionPoint IT- & Informationssäkerhetspolicy v1.0

Detta är teamets samlade slutleverans — ett beslutsunderlag för styrelsen med konkreta fynd, riskvärderingar och färdiga textändringar. Dokumentet ersätter alla delrapporter.

---

## Övergripande bedömning

Policyn är välskriven för sin ambition och bättre än genomsnittet för en organisation i MissionPoints storlek. Den ska **inte godkännas i nuvarande form** — men den är nära. Tre konkreta brister måste åtgärdas innan styrelsebeslut. Ytterligare tre bör åtgärdas inom 90 dagar.

**Rekommendation:** Godkänn med villkor. Åtgärda de tre kritiska punkterna (bedömd arbetstid: 2–4 timmar), dokumentera i revisionshistoriken och fastställ v1.1.

---

## Vad fungerar — bevara oförändrat

| Styrka | Varför det spelar roll |
|---|---|
| **AI-reglering med konkreta förbud** (avs. 8) | Explicit förbud mot att mata känslig information till ChatGPT, Copilot m.fl. — direkt relevant och ovanligt välformulerat |
| **EU/EES-krav på molnlagring** (avs. 11.1) | Skyddar mot GDPR-exponering vid leverantörsbyte; korrekt formulerat |
| **Hybridarbete reglerat** (avs. 10) | Krav på företagsdator och förbud mot öppna nätverk — saknas hos många jämförbara organisationer |
| **Leverantörsbedömning och PBA-krav** (avs. 11) | Proportionerligt och korrekt kopplat till GDPR art. 28 |
| **Scope täcker konsulter och kundsystem** (avs. 3) | Kritiskt för en organisation med systemåtkomst — korrekt gjort |

---

## Kritiska brister — blockerar styrelsebeslut

### 🔴 Brist 1 — "Säkerhetskänslig information" utan definition
**Riskpoäng: 20/25 (Sannolikhet 4 × Konsekvens 5)**

Avsnitt 7 listar "Säkerhetskänslig information" som en informationskategori MissionPoint hanterar — utan definition, hanteringsregler eller hänvisning till regelverk. Termen är inte neutral: den är en legal term under **Säkerhetsskyddslagen (2018:585)**, ett av Sveriges striktaste regelverk med krav på säkerhetsprövning av personal, tillstånd och myndighetsdialog.

Om MissionPoint faktiskt hanterar säkerhetsskyddsklassad information — t.ex. vid uppdrag åt försvarsnära eller offentliga kunder — gäller lagen redan och policyn är grovt otillräcklig. Om organisationen *inte* hanterar sådan information skapar termen onödig regulatorisk exponering.

**Obligatorisk åtgärd innan textändring:** Ledningen bekräftar om MissionPoint har eller planerar uppdrag med säkerhetsskyddsklassad information.

**Spår A — Säkerhetsskyddslagen är inte tillämplig:**
Ta bort "Säkerhetskänslig information" ur listan i avsnitt 7 och ersätt med:

> Information som av affärsmässiga eller regulatoriska skäl kräver särskilt skydd

**Spår B — Säkerhetsskyddslagen kan vara tillämplig:**
Lägg till följande mening i avsnitt 7:

> MissionPoint hanterar inte information klassificerad som säkerhetsskyddsklassad enligt Säkerhetsskyddslagen (2018:585). Om sådant uppdrag aktualiseras ska detta hanteras separat med berört tillsynsorgan.

*(Om säkerhetsskyddslagen faktiskt är aktiverad i väsentlig utsträckning är policyn otillräcklig som enda dokument — separat juridisk rådgivning och säkerhetsskyddsanalys krävs.)*

---

### 🔴 Brist 2 — Incidenthantering saknar det som gör den användbar
**Riskpoäng: 16/25 (Sannolikhet 4 × Konsekvens 4)**

Avsnitt 9 beskriver *att* incidenter ska rapporteras, men inte *till vem*, *inom vilken tid* eller *vad som händer sedan*. GDPR art. 33 kräver anmälan till IMY inom **72 timmar**. Formuleringen "rapporteras så snart som möjligt till ledningen" är en avsiktsförklaring, inte en process.

**Ersätt det sista stycket i avsnitt 9 med:**

> Övriga informationssäkerhetsincidenter ska rapporteras till informationssäkerhetsansvarig (CIO eller delegat) snarast, och senast inom 24 timmar från upptäckt. Vid incidenter som rör personuppgifter ska bedömning av anmälningsplikt till IMY ske inom 72 timmar (GDPR art. 33). Informationssäkerhetsansvarig ansvarar för att bedöma om incidenten kräver vidare eskalering, extern anmälan eller kundnotifiering. Samtliga incidenter ska dokumenteras och följas upp för att identifiera rotorsak och förebyggande åtgärder.

---

### 🔴 Brist 3 — Inga autentiseringskrav
**Riskpoäng: 20/25 (Sannolikhet 5 × Konsekvens 4)**

Policyn ställer inga krav på hur medarbetare autentiserar sig — varken mot interna system eller mot kundsystem. Kontoövertagande via phishing och lösenordsstöld är den dominerande intrångsvektorn mot konsultorganisationer (NCSC-SE 2024, ENISA Threat Landscape 2024). Ett stulet lösenord ger angriparen direkt tillgång till kundens miljö via MissionPoints konton. GDPR art. 32 och ISO 27001 A.5.17 kräver lämpliga tekniska åtgärder.

**Lägg till nytt avsnitt 10.1 efter avsnitt 10:**

> **10.1 Åtkomstsäkerhet**
>
> Multifaktorautentisering (MFA) ska användas för åtkomst till alla system som innehåller kundinformation, personuppgifter eller MissionPoints affärssystem. Starka, unika lösenord ska användas och hanteras via av bolaget godkänd lösenordshanterare. Delade inloggningsuppgifter är inte tillåtna.

---

## Höga brister — åtgärda inom 90 dagar

### 🟠 Brist 4 — Åtkomstkontroll och offboarding saknas
**Riskpoäng: 15/25 (Sannolikhet 4 × Konsekvens 3) — GDPR art. 25, ISO 27001 A.5.18**

Policyn reglerar inte vad som händer när en anställd eller konsult avslutar sitt uppdrag. Kvarstående åtkomst till kundsystem är ett konkret och dokumenterat riskscenario för konsultorganisationer.

**Lägg till i avsnitt 12 (Ansvar):**

> Behörighet till system och information ska tilldelas enligt principen om minsta nödvändiga åtkomst. Vid avslut av anställning eller uppdrag ska samtliga åtkomsträttigheter återkallas omedelbart. Ansvarig: CIO.

---

### 🟠 Brist 5 — Riskhanteringsprocess ej beskriven
**Riskpoäng: 12/25 (Sannolikhet 3 × Konsekvens 4) — ISO 27001 kl. 6.1, NIS2 art. 21**

Avsnitt 6 anger att MissionPoint "arbetar riskbaserat" utan att beskriva hur. Det skapar ett åtagande som policyn inte kan infria vid revision eller kundgranskning.

**Ersätt det befintliga stycket i avsnitt 6 om riskbaserat arbete med:**

> MissionPoint arbetar riskbaserat med informationssäkerhet. Informationssäkerhetsansvarig ansvarar för att risker mot bolagets information och IT-resurser identifieras, bedöms och hanteras löpande, samt att resultatet dokumenteras. Säkerhetsåtgärder ska stå i proportion till identifierade risker, verksamhetens behov och kundkrav.

---

### 🟠 Brist 6 — Krypteringskrav saknas
**Riskpoäng: 12/25 (Sannolikhet 3 × Konsekvens 4) — GDPR art. 32, ISO 27001 A.8.24**

Policyn ställer inga krav på kryptering av känslig information, varken i vila eller transit. För en organisation som hanterar systemåtkomst och konfidentiella dokument hos kunder är detta en reell lucka.

**Lägg till en mening i avsnitt 6 eller avsnitt 10:**

> Känslig information ska krypteras vid lagring och överföring. Godkända krypteringslösningar fastställs av informationssäkerhetsansvarig.

---

## Sammanfattande åtgärdsplan

| # | Åtgärd | Ansvarig | Horisont | Blockerar styrelsebeslut |
|---|---|---|---|---|
| **1** | Klargör "säkerhetskänslig information" och uppdatera avs. 7 | VD + CIO | Omgående | **Ja** |
| **2** | Komplettera avs. 9 med 72h-regel och rollansvar | CIO | Omgående | **Ja** |
| **3** | Lägg till avs. 10.1 om MFA och lösenordshantering | CIO | Omgående | **Ja** |
| **4** | Lägg till offboarding-mening i avs. 12 | CIO | 90 dagar | Nej |
| **5** | Uppdatera riskformuleringen i avs. 6 | CIO | 90 dagar | Nej |
| **6** | Lägg till krypteringskrav i avs. 6 eller 10 | CIO | 90 dagar | Nej |
| **7** | Fyll i revisionshistoriken (avs. 15) vid styrelsebeslut | CIO | Vid beslut | Processformalia |

---

## Antaganden som måste verifieras av MissionPoint

1. **NIS2-status:** MissionPoint antas inte vara primär NIS2-aktör. Om organisationen klassificeras som viktig eller väsentlig verksamhet höjs kravnivån väsentligt och en ny bedömning krävs — dialog med MSB rekommenderas.
2. **Säkerhetsskyddslagen:** Aktiveringsstatus avgörs av kundportföljens karaktär — se Brist 1 ovan. Måste bekräftas av ledningen innan policyn kan godkännas.
3. **Kompenserande dokument:** Granskningen antar att inga underliggande riktlinjer eller processdokument existerar. Om sådana finns kan flera brister vara delvis åtgärdade redan.

---

## Nästa steg & att bevaka

- **Omgående:** Ledningens svar på säkerhetsskyddsfrågan (Brist 1) — detta är ett stoppkrav och kan inte delegeras till CIO ensam.
- **Inför styrelsemötet:** Reviderad v1.1 med de tre kritiska ändringarna. Fyll i revisionshistoriken (avs. 15) med datum, ändring och beslutsfattare.
- **Inom 90 dagar:** Genomför Brist 4–6. Dokumentera att riskbedömningsprocessen som avs. 6 nu utlovar faktiskt existerar och är tilldelad CIO.
- **Inför nästa revision (senast 2027-02-27):** Utvärdera om NIS2-leverantörskrav från kunder har ökat i avtalskedjan — kontraktuella krav kan höja miniminivån. Överväg att ta fram ett kortfattat underliggande processdokument för incidenthantering som avlastar policyn.
- **Löpande:** AI-regleringen i avs. 8 är tidskänslig — bevaka att listan över tillåtna verktyg hålls aktuell i takt med att marknaden förändras.
