# CISO-kommunikatör

# Granskningsresultat: MissionPoints IT- och Informationssäkerhetspolicy
## Beslutsunderlag för IT-chef och informationssäkerhetsansvarig

**Producerat av:** CISO-kommunikatör
**Datum:** 2026-02-27
**Klassificering:** Konfidentiellt — internt beslutsunderlag
**Dokument:** MissionPoint AB, IT- och Informationssäkerhetspolicy v1.0
**Granskning genomförd av:** IT-säkerhetspolicyteamet (regulatorisk analys, ISO/IEC-granskning, teknisk strukturgranskning, hotbildsbedömning, gap- och riskanalys, åtgärdsstrategi)

---

## Sammanfattning för beslutsfattare

MissionPoints IT- och Informationssäkerhetspolicy v1.0 är ett välskrivet och välintentionerat grunddokument. Det visar att MissionPoint förstår sin roll, sin riskbild och sin skyldighet att hantera information ansvarsfullt.

**Men policyn är inte tillräcklig som den ser ut idag.**

Granskningen identifierade **23 luckor** mot gällande regelverk och branschstandard. Av dessa är **5 kritiska** — det vill säga brister som skapar omedelbar regulatorisk eller operationell exponering och som behöver åtgärdas inom 30 dagar.

Det handlar inte om att policyn är dålig. Det handlar om att den inte räcker som ensamt styrdokument för en organisation som hanterar systemåtkomst, säkerhetsanalyser och potentiellt säkerhetskänslig information åt kunder i reglerade sektorer. Den saknar de processer, rollbeskrivningar och tekniska krav som krävs för att faktiskt implementera det policyn lovar.

**Konsekvensen av passivitet är konkret:** En säkerhetsincident i morgon hanteras ad hoc. En kund med NIS2-förpliktelser begär leverantörsgranskning och MissionPoint saknar svar. Tillsynsmyndigheten frågar om riskhanteringsprocessen — den finns inte dokumenterad.

Åtgärderna är genomförbara. Nedan följer exakt vad som behöver göras, i vilken ordning och varför.

---

## Del 1 — Vad är bra i policyn

Innan bristerna: det som fungerar och som nästa version ska bygga vidare på.

| Styrka | Vad det innebär i praktiken |
|---|---|
| **Scopet är väldefinierat** (§3) | Täcker anställda, konsulter och uppdragstagare — ingen gråzon kring vem som omfattas |
| **AI-reglering är proaktiv** (§8) | Konkret förbud mot att dela känslig information med AI-verktyg; tydliga exempel på tillåtet och förbjudet — långt framme jämfört med branschnorm |
| **Rollen mot kunder är tydlig** (§4–5) | Policyn erkänner leverantörsrollen och NIS2-indirektheten utan att överdriva eget ansvar |
| **Datageografi adresseras** (§11.1) | EU/EES-prioritering för molntjänster är explicit — direkt relevant för GDPR-efterlevnad |
| **Personuppgifter hanteras separat** (§7.1) | GDPR-hänvisning och koppling till Integritetspolicyn är korrekt strukturerat |
| **Hybridarbete är reglerat** (§10) | Grundläggande regler för distansarbete finns — ovanligare än man tror i policydokument av denna typ |

---

## Del 2 — Kritiska brister som kräver omedelbar åtgärd

Dessa fem brister skapar regulatorisk exponering eller omedelbar operationell sårbarhet. Åtgärdshorisont: **0–30 dagar.**

---

### 🔴 K1 — Incidenthanteringsprocessen är ofullständig
**Riskpoäng: 20** | GDPR art. 33–34, NIS2 art. 23

**Problemet i klartext:**
§9 nämner att incidenter ska rapporteras och utredas. Det räcker inte. Det finns inga tidsgränser, inga definierade roller, ingen eskalationskedja och ingen koppling till GDPR:s 72-timmarskrav för rapportering till IMY. Om en incident inträffar i morgon vet ingen på MissionPoint exakt vad som ska göras, i vilken ordning och vem som ansvarar.

**Regulatorisk konsekvens:**
GDPR art. 33 kräver anmälan till IMY inom 72 timmar efter att en personuppgiftsincident konstaterats. Att missa denna tidsgräns är en av de vanligaste grunderna för sanktionsavgifter i Sverige. Dessutom: kunder med NIS2-förpliktelser förväntar sig att deras leverantörer har dokumenterade incidentprocesser — avsaknad är ett kontraktuellt problem.

**Vad som ska göras:**
Skapa ett separat styrdokument — *Incidenthanteringsinstruktion v1.0* — och ersätt §9 med en referens till det. Instruktionen ska som minst innehålla:

- Klassificeringsmatris med tre nivåer: P1 (personuppgiftsincident), P2 (säkerhetsincident utan personuppgifter), P3 (misstänkt händelse)
- Namngiven incident owner och tydlig eskalationskedja
- Tidsgränser: intern eskalation inom 4 timmar för P1; IMY-anmälan inom 72 timmar
- Checklista för extern kommunikation (kund, myndighet, berörda registrerade)
- Krav på rotorsaksanalys och dokumentation efter varje P1/P2-incident

**Ansvarig:** Informationssäkerhetsansvarig (CIO eller delegat per §6)
**Deadline:** 30 dagar

---

### 🔴 K2 — Ingen riskhanteringsprocess
**Riskpoäng: 20** | ISO 27001 kl. 6.1, ISO 27005

**Problemet i klartext:**
Policyn säger att MissionPoint "arbetar riskbaserat" (§6). Men det finns ingen beskriven process för hur risker identifieras, värderas, beslutas eller följs upp. En policy som säger att man arbetar riskbaserat utan att förklara hur är inte riskbaserad — det är ett önsketänkande.

**Praktisk konsekvens:**
Utan dokumenterad riskprocess kan MissionPoint inte förklara för kunder, revisorer eller tillsynsmyndigheter hur säkerhetsbeslut fattas. Det är också omöjligt att prioritera säkerhetsåtgärder på ett konsekvent sätt. Varje beslut om säkerhetsinvestering blir en magkänsla snarare än en underbyggd prioritering.

**Vad som ska göras:**
Lägg till ett nytt avsnitt i policyn — §X Riskhantering — med följande innehåll:

- En kortfattad riskbedömningsmodell (Sannolikhet × Konsekvens räcker)
- Krav på att en formell riskbedömning genomförs minst årligen, samt vid väsentliga förändringar
- Rollbeskrivning: vem ansvarar för att genomföra och dokumentera riskbedömningen
- Krav på att riskregister förs och att höga och kritiska risker eskaleras till ledningen

**Ansvarig:** CIO
**Deadline:** 30 dagar

---

### 🔴 K3 — Åtkomstkontroll och IAM saknas
**Riskpoäng: 20** | ISO 27001 A.5.15–A.5.18, GDPR art. 32

**Problemet i klartext:**
Policyn hanterar konfidentialitet som princip men innehåller inga tekniska eller organisatoriska krav på hur åtkomst faktiskt styrs. Principen om minsta privilegium (least privilege) nämns inte. Det finns inga krav på lösenordspolicy, multifaktorautentisering, behörighetsgenomgångar eller offboarding-process.

**Varför det är kritiskt för just MissionPoint:**
§7 konstaterar att MissionPoint hanterar systemåtkomst till kundsystem. Det innebär att en komprometterad MissionPoint-medarbetares credentials potentiellt ger åtkomst till kunders produktionsmiljöer. APT29 (Cozy Bear) är dokumenterat specialiserad på exakt denna typ av angrepp: credential theft mot konsult- och rådgivningsfirmor för att nå slutkunderna via supply chain.

**Vad som ska göras:**
Skapa en separat *Riktlinje för åtkomstkontroll* och referera till den från policyn. Riktlinjen ska minst täcka:

- Principen om minsta privilegium — all åtkomst beviljas restriktivt och med affärsmotivering
- MFA obligatoriskt för alla system, särskilt Microsoft 365 och kundsystem
- Process för behörighetsgenomgång (minst halvårsvis)
- Offboarding-checklista: åtkomst återkallas senast på sista anställningsdagen
- Separering av behörigheter för konsulter med tillgång till kundsystem

**Ansvarig:** CIO / IT-ansvarig
**Deadline:** 30 dagar

---

### 🔴 K4 — Tillgångshantering och systeminventarium saknas
**Riskpoäng: 16** | ISO 27001 A.5.9–A.5.10

**Problemet i klartext:**
Det finns ingen förteckning över vilka system, enheter och informationstillgångar som MissionPoint äger och ansvarar för. Det innebär att ingen vet vad som ska skyddas. En policy utan inventarium är som ett larm utan lista på vad som ska bevakas.

**Praktisk konsekvens:**
Utan inventarium är det omöjligt att genomföra meningsfulla riskbedömningar, säkerställa att uppdateringar och patchar når alla system, eller avgöra vad som ingår i scope vid en säkerhetsincident.

**Vad som ska göras:**
- Lägg till ett nytt avsnitt i policyn: §X Tillgångshantering
- Skapa ett basalt tillgångsinventarium (kan vara en tabell i ett
