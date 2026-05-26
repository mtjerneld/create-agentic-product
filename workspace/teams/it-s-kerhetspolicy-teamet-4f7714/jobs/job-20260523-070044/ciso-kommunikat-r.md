# CISO-kommunikatör

# Granskningsrapport — MissionPoint IT- & Informationssäkerhetspolicy v1.0
**CISO-kommunikatör | Fas: Rapportering & rekommendationer**
**För: IT-chef / CISO, MissionPoint AB | Datum: 2026-02-27 | Klassificering: Konfidentiell**

---

## Sammanfattning för beslutsfattare

Policyn är välskriven för sin ambition och bättre än genomsnittet för en organisation i MissionPoints storlek. Den ska **inte** godkännas i nuvarande form — men den är nära. Tre konkreta brister måste åtgärdas innan styrelsebeslut. Ytterligare två bör åtgärdas inom 90 dagar.

**Rekommendation:** Godkänn med villkor — återkom till styrelsen med reviderat dokument när de tre kritiska punkterna är åtgärdade. Bedömd tidsåtgång: 3–5 arbetsdagar.

---

## Vad fungerar — bevara detta

Innan bristerna: policyn har tre styrkor som är ovanliga och värdefulla. De ska inte röras vid revision.

| Styrka | Varför det spelar roll |
|---|---|
| **AI-reglering med konkreta exempel** | Explicit förbud mot att mata känslig information till ChatGPT, Copilot m.fl. — direkt relevant för en konsultorganisation och ovanligt välformulerat |
| **EU/EES-krav på molnlagring** | Explicit krav på att prioritera EU/EES-lagring skyddar mot GDPR-exponering vid leverantörsbyte |
| **Hybridarbete reglerat** | Grundläggande krav på företagsdator och undvikande av öppna nätverk finns — saknas hos många jämförbara organisationer |

---

## Kritiska brister — måste åtgärdas före styrelsebeslut

Tre fynd blockerar godkännande. Samtliga är åtgärdbara med minimala textändringar — inga nya avsnitt krävs.

---

### 🔴 Brist 1: "Säkerhetskänslig information" är en laddad juridisk term
**Risknivå:** Kritisk (20/25) | **Åtgärd krävs:** Omgående

**Vad problemet är:**
Avsnitt 7 listar "säkerhetskänslig information" som en informationskategori MissionPoint hanterar. Det är ett problem — termen är inte neutral. Den är en legal term under Säkerhetsskyddslagen (2018:585), ett av Sveriges striktaste regelverk, med krav på säkerhetsprövning av personal, tillstånd och myndighetsdialog.

**Vad det innebär i praktiken:**
Om MissionPoint faktiskt hanterar information som faller under säkerhetsskyddslagen — exempelvis analyser åt försvarsnära eller offentliga kunder — gäller lagen redan, oavsett vad policyn säger. Om organisationen *inte* hanterar sådan information skapar termen onödig regulatorisk exponering.

**Åtgärd — två alternativ:**

> **Alt A (om säkerhetsskyddslagen inte är tillämplig):**
> Ta bort "Säkerhetskänslig information" ur listan i avsnitt 7. Ersätt med "Konfidentiell information" eller "Känslig affärsinformation".

> **Alt B (om säkerhetsskyddslagen kan vara tillämplig):**
> Lägg till följande mening i avsnitt 7:
> *"MissionPoint hanterar inte information klassificerad som säkerhetsskyddsklassad enligt Säkerhetsskyddslagen (2018:585). Om sådant uppdrag aktualiseras ska detta hanteras separat med berört tillsynsorgan."*

**Innan textändring:** Ledningen måste bekräfta om MissionPoint har — eller planerar — uppdrag som involverar säkerhetsskyddsklassad information. Detta är en affärsfråga, inte bara en juridisk.

---

### 🔴 Brist 2: Incidenthanteringen saknar det som faktiskt gör den användbar
**Risknivå:** Kritisk (16/25) | **Åtgärd krävs:** Före styrelsebeslut

**Vad problemet är:**
Avsnitt 9 beskriver *att* incidenter ska rapporteras, men inte *till vem*, *inom vilken tid* eller *vad som händer sedan*. Under GDPR måste personuppgiftsincidenter anmälas till Integritetsskyddsmyndigheten inom **72 timmar**. Den tidsgränsen finns inte i policyn.

En policy som säger "rapportera incidenter till ledningen" utan tidsgräns eller roll är inte ett styrande dokument — det är en intention.

**Åtgärd — ersätt sista stycket i avsnitt 9 med:**

> *"Säkerhetsincidenter ska rapporteras till [informationssäkerhetsansvarig/CIO] snarast, senast inom 24 timmar från discovery. Vid incidenter som rör personuppgifter ska bedömning av anmälningsplikt till IMY ske inom 72 timmar (GDPR art. 33). Informationssäkerhetsansvarig beslutar om eskalation och extern rapportering."*

Tre meningar. Löser problemet.

---

### 🔴 Brist 3: Ingen autentiseringskrav — det vanligaste sättet att förlora kunddata
**Risknivå:** Kritisk (16/25) | **Åtgärd krävs:** Före styrelsebeslut

**Vad problemet är:**
Policyn ställer inga krav på hur medarbetare autentiserar sig — varken mot interna system eller mot kundsystem. För en organisation som har inloggningsuppgifter och VPN-åtkomst hos kunder är detta den mest direkta hotexponeringen: ett stulet lösenord ger angriparen tillgång till kundens miljö, inte bara MissionPoints.

Kontoövertagande via phishing och lösenordsstöld är den dominerande intrångsvektorn mot konsultorganisationer enligt NCSC-SE 2024 och ENISA Threat Landscape 2024.

**Åtgärd — lägg till ett nytt stycke i avsnitt 12 (Ansvar) eller avsnitt 10 (Distansarbete):**

> *"Flerfaktorsautentisering (MFA) ska användas för åtkomst till alla företagssystem, e-post och kundsystem där teknisk möjlighet finns. Starka, unika lösenord ska användas och hanteras via godkänd lösenordshanterare."*

---

## Höga brister — åtgärda inom 90 dagar

Dessa blockerar inte styrelsebeslut men skapar operationell risk om de lämnas oåtgärdade.

| # | Brist | Risknivå | Varför det spelar roll | Åtgärd |
|---|---|---|---|---|
| **H1** | Åtkomstkontroll och offboarding saknas | Hög (15/25) | En konsult vars åtkomst inte dras in vid uppdragsavslut är en kvarstående inkörsport till kundmiljöer | Lägg till i avsnitt 12: *"Åtkomst till system och kundmiljöer ska avslutas senast samma dag som anställning eller uppdrag upphör. Ansvarig: CIO."* |
| **H2** | Riskhantering omnämns som princip men beskrivs inte | Hög (12/25) | "Vi arbetar riskbaserat" utan process är inte styrande — det är en avsiktsförklaring | Lägg till i avsnitt 6: *"Riskbedömning av informationssäkerhet ska genomföras minst årligen och vid väsentliga förändringar i verksamheten. Ansvarig: informationssäkerhetsansvarig."* |

---

## Beslutsrekommendation

```
┌─────────────────────────────────────────────────────────┐
│  REKOMMENDATION TILL STYRELSEN                          │
│                                                         │
│  ⛔  Godkänn INTE i nuvarande form                     │
│                                                         │
│  ✅  Godkänn med villkor:                               │
│      Brist 1–3 åtgärdas (est. 3–5 arbetsdagar)         │
│      Reviderat dokument återkommer för formellt beslut  │
│                                                         │
│  📅  Nästa revision: senast 2027-02-27                  │
│      H1 och H2 adresseras vid revision om ej dessförinnan│
└─────────────────────────────────────────────────────────┘
```

---

## Åtgärdsplan — sammanfattad

| Prioritet | Åtgärd | Ansvarig | Klar senast |
|---|---|---|---|
| 🔴 Kritisk | Klargör och korrigera termen "säkerhetskänslig information" (Brist 1) | VD + CIO | Innan styrelsemöte |
| 🔴 Kritisk | Komplettera avsnitt 9 med 72h-gräns och rollansvar (Brist 2) | CIO | Innan styrelsemöte |
| 🔴 Kritisk | Lägg till MFA-krav i avsnitt 10 eller 12 (Brist 3) | CIO | Innan styrelsemöte |
| 🟠 Hög | Lägg till offboarding-mening i avsnitt 12 (H1) | CIO | 90 dagar |
| 🟠 Hög | Lägg till riskbedömningsåtagande i avsnitt 6 (H2) | CIO | 90 dagar |

---

## Noteringar och antaganden

Denna rapport bygger på teamets fullständiga granskning (regulatorisk analys, ISO/IEC 27001-mappning, teknisk strukturgranskning, hotbildsbedömning och konsoliderad riskanalys). Följande antaganden är styrande och ska verifieras av MissionPoint:

1. **NIS2-status:** MissionPoint antas *inte* vara primär NIS2-aktör. Om organisationen klassificeras som viktig eller väsentlig verksamhet höjs kravnivån väsentligt och en ny bedömning krävs.
2. **Säkerhetsskyddslagen:** Aktiveringsstatus är oklar och beror på kundportföljens karaktär — se Brist 1 ovan.
3. **Inga kompenserande dokument:** Granskningen antar att inga underliggande riktlinjer, processdokument eller rutiner existerar utöver policyn. Om sådana finns kan flera av bristerna vara delvis åtgärdade redan.

---

*Rapport producerad av IT-säkerhetspolicy-teamet. Konfidentiellt — avsett för intern styrelseanvändning.*
