# Åtgärdsstrateg

# Åtgärdsplan: Konkreta Förbättringsförslag
## MissionPoint AB — IT- och Informationssäkerhetspolicy v1.0

**Roll:** Åtgärdsstrateg
**Fas:** Gap-analys & riskvärdering — Prioriterade åtgärder
**Datum:** 2026
**Underlag:** Regulatorisk kartläggning, ISO/IEC-analys, Teknisk policygranskning, Hotbildsbedömning

---

## 0. Läsanvisning

Denna åtgärdsplan är teamets samlade operativa slutprodukt för Fas 2–3. Den bygger direkt på fynd från samtliga tidigare leveranser och är strukturerad för att vara **direkt handlingsbar** för MissionPoints IT-chef eller den informationssäkerhetsansvarige.

Åtgärderna är rangordnade efter riskpoäng (Sannolikhet × Konsekvens, max 25) och organiserade i fyra prioritetsnivåer med tillhörande åtgärdshorisonter:

| Nivå | Poäng | Horisont | Innebär |
|---|---|---|---|
| 🔴 Kritisk | 16–25 | 0–30 dagar | Stoppa pågående exponering — åtgärda omedelbart |
| 🟠 Hög | 9–15 | 90 dagar | Schemalagd åtgärd med tydlig ägare och deadline |
| 🟡 Medium | 4–8 | 6 månader | Planera in i ordinarie förbättringsarbete |
| 🟢 Låg | 1–3 | Ordinarie revision | Adressera vid nästa planerade policyrevision |

**Organisatorisk kalibrering:** MissionPoint är ett konsultbolag av mellanstor typ med hybridarbete, aktiv AI-användning och outsourcad IT-drift. Åtgärdsförslagen är kalibrerade för denna profil — inte för ett ISMS-moget industribolag. Ambitionen är att gå från "policy existerar" till "policy är genomförbar och regulatoriskt försvarbar".

---

## 1. Kritiska Åtgärder — 0–30 dagar

### 🔴 K1 — Etablera komplett incidenthanteringsprocess
**Riskpoäng: 20** (Sannolikhet 4 × Konsekvens 5)
**Regulatorisk grund:** GDPR art. 33–34, NIS2 art. 23, ISO 27001 A.5.24–A.5.28

**Problemet:**
Nuvarande §9 är ett embryo, inte en process. Den saknar tidsgränser, rollbeskrivningar, eskalationskedjor och extern rapporteringsplikt. En incident i morgon skulle hanteras ad hoc — med hög risk för GDPR-böter (72-timmarsregeln) och kontraktsbrott mot NIS2-bundna kunder.

**Konkret åtgärd:**
Skapa ett separat styrdokument: *Incidenthanteringsinstruktion v1.0* — och ersätt §9 med en referens till det dokumentet. Instruktionen ska som minst innehålla:

1. **Klassificeringsmatris** — tre nivåer: P1 (kritisk/personuppgifter), P2 (säkerhetsincident utan personuppgifter), P3 (misstänkt händelse)
2. **Rollbeskrivning** — vem är incident owner, vem eskalerar, vem kommunicerar externt
3. **Tidsgränser:**
   - P1 med personuppgifter: intern eskalation inom 4 timmar, IMY-anmälan inom 72 timmar
   - P2: intern hantering initierad inom 24 timmar
   - P3: loggning och bedömning inom 48 timmar
4. **Rapporteringskanaler** — vid NIS2-bundna kunduppdrag: check om kunden behöver notifieras (MissionPoint som leverantör i kedjan)
5. **Loggkrav** — alla incidenter loggas i register, följs upp med rotorsaksanalys

**Ersättande policytext för §9:**

```
9. Incidenthantering

MissionPoint ska ha en dokumenterad process för hantering av
informationssäkerhetsincidenter. Processen fastställs i MissionPoints
Incidenthanteringsinstruktion.

Alla medarbetare är skyldiga att omedelbart rapportera misstänkta
säkerhetsincidenter till informationssäkerhetsansvarig via [intern kanal].

Vid personuppgiftsincidenter gäller GDPR art. 33–34: bedömning av
anmälningsskyldighet till IMY ska slutföras inom 24 timmar från
kännedom. Anmälan till IMY ska ske inom 72 timmar om kraven är uppfyllda.

MissionPoint ska föra register över alla incidenter och genomföra
rotorsaksanalys för P1- och P2-klassade händelser.
```

---

### 🔴 K2 — Inför formell riskhanteringsprocess
**Riskpoäng: 20** (Sannolikhet 4 × Konsekvens 5)
**Regulatorisk grund:** ISO 27001 kl. 6.1, ISO 27005:2022, NIS2 art. 21 (indirekt via kundkrav)

**Problemet:**
Policyn anger att MissionPoint "arbetar riskbaserat" (§6) men definierar ingen process för hur risker identifieras, värderas, beslutas eller följs upp. Det är en deklaration utan mekanism. Om en kund eller revisor frågar "visa oss er riskprocess" finns ingenting att visa.

**Konkret åtgärd:**
Lägg till nytt avsnitt i policyn samt skapa en kortfattad *Riskhanteringsprocess* (1–2 sidor räcker för MissionPoints storlek). Processen ska innehålla:

1. **Riskidentifiering** — genomförs minst årligen och vid väsentliga förändringar (ny kundtyp, nytt system, ny tjänst)
2. **Riskvärdering** — Sannolikhet (1–5) × Konsekvens (1–5); dokumenteras i riskregister
3. **Riskbehandling** — fyra alternativ: acceptera, reducera, överföra, undvika
4. **Riskägarskap** — varje risk i registret har en namngiven ägare
5. **Uppföljning** — riskregistret ses över kvartalsvis av informationssäkerhetsansvarig

**Ny policytext — tillägg i §6:**

```
6.1 Riskhantering

MissionPoints riskbaserade ansats operationaliseras genom en löpande
riskhanteringsprocess. Processen beskrivs i MissionPoints
Riskhanteringsinstruktion och omfattar:

- Identifiering av informationssäkerhetsrisker kopplade till
  verksamheten, system, personal och kunduppdrag
- Bedömning av sannolikhet och konsekvens per risk
- Beslut om riskbehandling (reducera, acceptera, överföra, undvika)
- Dokumentation i löpande riskregister med namngiven riskägare
- Kvartalsvis uppföljning av informationssäkerhetsansvarig

Riskregistret är ett levande dokument och ska uppdateras vid
väsentliga förändringar i verksamheten.
```

---

### 🔴 K3 — Klargör hantering av säkerhetskänslig information och Säkerhetsskyddslagen
**Riskpoäng: 20** (Sannolikhet 4 × Konsekvens 5)
**Regulatorisk grund:** Säkerhetsskyddslagen (2018:585), SUA kap. 2

**Problemet:**
Policyn nämner "säkerhetskänslig information" i §7 utan att definiera begreppet, etablera hanteringsregler eller avgöra om Säkerhetsskyddslagen är tillämplig. Om MissionPoint hanterar säkerhetsskyddsklassad information utan att ha identifierat det är bolaget i potentiellt allvarligt lagbrott — med straffrättsliga konsekvenser.

**Konkret åtgärd:**

**Steg 1 — Omedelbar intern utredning (vecka 1):**
MissionPoints ledning och informationssäkerhetsansvarig ska genomföra en kartläggning:
- Vilka kunder hanterar säkerhetsskyddsklassad information?
- Har MissionPoint fått del av sådan information?
- Har säkerhetsskyddsavtal tecknats där sådant krävs?

**Steg 2 — Policytext:**
Oavsett utfall ska policyn revideras så att begreppet definieras och ansvaret tydliggörs:

```
7.2 Säkerhetskänslig information

Med säkerhetskänslig information avses i denna policy information som
rör Sveriges säkerhet eller som omfattas av Säkerhetsskyddslagen
(2018:585).

MissionPoint ska, innan uppdrag som innebär hantering av potentiellt
säkerhetsskyddsklassad information påbörjas, göra en bedömning av om
Säkerhetsskyddslagen är tillämplig. Vid osäkerhet ska extern juridisk
rådgivning inhämtas.

Om Säkerhetsskyddslagen bedöms tillämplig gäller dess krav fullt ut,
inklusive krav på säkerhetsskyddsavtal, säkerhetsprövning av personal
och fysisk säkerhet.
```

---

### 🔴 K4 — Etablera åtkomstkontroll och IAM-principer
**Riskpoäng: 16** (Sannolikhet 4 × Konsekvens 4)
**Regulatorisk grund:** ISO 27001 A.5.15–A.5.18, GDPR art. 25 (inbyggd integritet)

**Problemet:**
Policyn saknar helt regler för behörighetsstyrning. För ett konsultbolag som hanterar systemåtkomst till kundmiljöer (§7) och har personal som regelmässigt slutar eller byter uppdrag är detta en akut operationell risk. Oreglerad åtkomst är den vanligaste ingångsvektorn vid dataintrång.

**Konkret åtgärd:**
Lägg till nytt avsnitt
