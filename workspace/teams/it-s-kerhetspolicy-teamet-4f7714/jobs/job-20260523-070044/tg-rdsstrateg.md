# Åtgärdsstrateg

# Åtgärdsplan — MissionPoint IT- & Informationssäkerhetspolicy v1.0
**Roll:** Åtgärdsstrateg | **Fas:** Gap-analys & riskvärdering — Konkreta förbättringsförslag
**Datum:** 2026-02-27 | **Princip:** Less is more — kirurgiska ingrepp, inga nya avsnitt

---

## Läsanvisning

Detta dokument omvandlar teamets samlade granskningsfynd till **konkreta, minimala textändringar** som MissionPoint kan genomföra direkt inför styrelsebeslut. Ingenting läggs till som inte är nödvändigt. Varje åtgärd är kopplad till ett specifikt fynd, en riskpoäng och en åtgärdshorisont.

**Antaganden som ärvs från tidigare faser:**
- MissionPoint är **inte** primär NIS2-aktör — leverantörskedjeperspektivet gäller.
- Säkerhetsskyddslagens aktiveringsstatus är **oklar** — ett fynd kräver klarläggning med kunden innan policyn kan godkännas.
- Policyn är ensamt styrande dokument tills vidare.
- Styrelsebeslutet som avses *är* godkännandeprocessen — det saknas explicit i dokumentet men antas vara underförstått.

---

## 1. Prioriterad åtgärdslista

Riskpoäng = Sannolikhet (1–5) × Konsekvens (1–5). Endast fynd på nivå **Kritisk (16–25)** och **Hög (9–15)** adresseras — i enlighet med minimumorientering.

| # | Fynd | S | K | Poäng | Nivå | Horisont | Åtgärdstyp |
|---|---|---|---|---|---|---|---|
| F1 | "Säkerhetskänslig information" listad utan definition | 4 | 5 | **20** | 🔴 Kritisk | 0–30 dagar | Klarläggning + textändring |
| F2 | Incidenthantering saknar tidsgränser och rollansvar | 4 | 4 | **16** | 🔴 Kritisk | 0–30 dagar | Textändring |
| F3 | MFA/lösenordskrav saknas helt | 4 | 4 | **16** | 🔴 Kritisk | 0–30 dagar | Textändring |
| F4 | Åtkomstkontroll och offboarding saknas | 3 | 5 | **15** | 🟠 Hög | 90 dagar | Textändring |
| F5 | Riskhanteringsprocess ej beskriven | 3 | 4 | **12** | 🟠 Hög | 90 dagar | Textändring |
| F6 | Förbättringsåtagande saknas (ISO 27001 kl. 5.2) | 2 | 4 | **8** | 🟡 Medium | 6 månader | En mening i avs. 6 |
| F7 | Säkerhetsmedvetenhet/utbildning ej omnämnt | 2 | 4 | **8** | 🟡 Medium | 6 månader | En mening i avs. 12 |

> **Medium och Låg-fynd** (informationsklassningsschema, loggning, fysisk säkerhet, godkännandeprocess m.m.) lyfts **inte** i denna fas — de hör hemma i ordinarie revision eller underliggande riktlinjer.

---

## 2. Kritiska åtgärder (0–30 dagar)

### F1 — "Säkerhetskänslig information" utan definition
**Fynd:** Avsnitt 7 listar "säkerhetskänslig information" som en informationskategori MissionPoint hanterar. Termen är en legal term of art under Säkerhetsskyddslagen (2018:585). Utan definition eller hanteringsregler är det oklart om lagen är aktiverad — och om den är det, saknas samtliga krav lagen ställer.

**Riskbild:** Om MissionPoint utför säkerhetsanalyser åt aktörer med säkerhetskänslig verksamhet (försvar, offentlig förvaltning, kritisk infrastruktur) kan lagen vara direkt tillämplig. En felanvändning av termen utan hanteringsregler är i sig ett compliance-problem.

**Obligatoriskt innan godkännande:**
> Bekräfta med MissionPoints ledning/juridisk rådgivare: Hanterar bolaget information som är klassificerad under Säkerhetsskyddslagen, eller är termen använd i mer allmän bemärkelse?

**Beroende av svaret — två spår:**

**Spår A — Termen är allmän (säkerhetsskyddslagen ej aktiverad):**
Byt ut termen i avsnitt 7 mot en neutral formulering.

*Nuvarande text (avs. 7):*
> [...] Säkerhetskänslig information

*Ersätt med:*
> [...] Information som av affärsmässiga eller regulatoriska skäl kräver särskilt skydd ("skyddsvärd information")

---

**Spår B — Säkerhetsskyddslagen är aktiverad:**
Policyn i sin nuvarande form är otillräcklig och kan inte godkännas av styrelsen utan att ett separat avsnitt om säkerhetsskyddade uppgifter tas fram. Detta är utanför ramen för en minimal policy — kunden behöver juridisk specialistrådgivning. Stoppa styrelsebeslut tills klarläggning skett.

---

### F2 — Incidenthantering saknar tidsgränser och rollansvar
**Fynd:** Avsnitt 9 beskriver vad incidenter *kan* vara och att de ska rapporteras "så snart som möjligt". GDPR art. 33 kräver 72-timmarsanmälan till Integritetsskyddsmyndigheten (IMY). NIS2-leverantörskrav förutsätter definierad process. "Så snart som möjligt" är inte en tidsgräns — det är en avsiktsförklaring.

**Åtgärd:** Lägg till tre meningar i avsnitt 9. Inga nya avsnitt behövs.

*Nuvarande text (avs. 9, andra stycket):*
> Övriga informationssäkerhetsincidenter ska rapporteras så snart som möjligt till ledningen och följas upp för att identifiera rotorsak och förebyggande åtgärder.

*Ersätt med:*
> Övriga informationssäkerhetsincidenter ska rapporteras omedelbart, och senast inom 24 timmar från upptäckt, till informationssäkerhetsansvarig (CIO eller delegat). Informationssäkerhetsansvarig ansvarar för att bedöma om incidenten kräver vidare eskalering, extern anmälan eller kundnotifiering. Samtliga incidenter ska dokumenteras och följas upp för att identifiera rotorsak och förebyggande åtgärder.

**Motivering:** 24-timmarsgränsen internt ger utrymme att hålla GDPR:s 72-timmarskrav till IMY. Rollbenämningen (CIO/delegat) är redan definierad i policyn — inga nya roller introduceras.

---

### F3 — MFA och lösenordskrav saknas
**Fynd:** Policyn innehåller inga tekniska minimikrav för autentisering. Kontoövertagande via stulna credentials är den dominerande intrångsvektorn mot konsultbolag med kundåtkomst (NCSC-SE 2024, ENISA ETL 2024). En policy som inte kräver MFA på system med kundåtkomst är defenslös mot det vanligaste angreppssättet. ISO 27001 A.5.17 och GDPR art. 32 kräver lämpliga tekniska åtgärder.

**Åtgärd:** Lägg till ett nytt underavsnitt 10.1 under Distansarbete, alternativt som ett kortfattat tillägg under avsnitt 6 (Informationssäkerhetsprinciper). Placering under avsnitt 10 är naturlig eftersom det redan reglerar teknisk användning.

*Förslag — nytt avsnitt 10.1 (Åtkomstsäkerhet):*
> **10.1 Åtkomstsäkerhet**
> Multifaktorautentisering (MFA) ska användas för åtkomst till alla system som innehåller kundinformation, personuppgifter eller MissionPoints affärssystem. Starka, unika lösenord ska användas och hanteras via av bolaget godkänd lösenordshanterare. Delade inloggningsuppgifter är inte tillåtna.

**Motivering:** Tre meningar. Täcker MFA-kravet, lösenordshygien och förbudet mot delade konton — de tre kontroller som direkt reducerar ATO-risken. Inget mer behövs på policynivå.

---

## 3. Höga åtgärder (90 dagar)

### F4 — Åtkomstkontroll och offboarding saknas
**Fynd:** Policyn saknar helt regler för behörighetstilldelning och vad som händer när en medarbetare eller konsult avslutar sitt uppdrag. Insider-hot och kvarstående åtkomst efter offboarding är identifierat som medium-hög risk för MissionPoints profil. GDPR art. 25 (inbyggt dataskydd) och ISO 27001 A.5.18 kräver att åtkomst styrs och återkallas.

**Åtgärd:** Lägg till tre meningar i avsnitt 12 (Ansvar) eller som underavsnitt 12.1.

*Förslag — tillägg i avsnitt 12:*
> Behörighet till system och information ska tilldelas enligt principen om minsta nödvändiga åtkomst och godkännas av informationssäkerhetsansvarig. Behörigheter ska ses över regelbundet. Vid avslut av anställning eller uppdrag ska samtliga åtkomsträttigheter återkallas omedelbart.

**Motivering:** Principen om minsta privilegium + offboarding-krav i tre meningar. Löser den mest akuta delen av IAM-luckan utan att skriva en full åtkomstkontrollpolicy.

---

### F5 — Riskhanteringsprocess ej beskriven
**Fynd:** Avsnitt 6 anger att MissionPoint "arbetar riskbaserat" men beskriver ingen process. ISO 27001 kl. 6.1 och ISO 27005 kräver en dokumenterad riskprocess. Utan detta är "riskbaserat arbete" en tom fras som inte skyddar bolaget vid revision eller kundgranskning.

**Åtgärd:** Lägg till två meningar i befintligt avsnitt 6 — inga nya avsnitt.

*Nuvarande text (avs. 6, sista stycket):*
> MissionPoint arbetar riskbaserat med informationssäkerhet. Säkerhetsåtgärder ska stå i proportion till identifierade risker, verksamhetens behov och kundkrav.

*Ersätt med:*
> MissionPoint arbetar riskbaserat med informationssäkerhet. Informationssäkerhetsansvarig ansvarar för att risker mot bolagets information och IT-resurser identifieras, bedöms och hanteras löpande, samt att resultatet dokumenteras. Säkerhetsåtgärder ska stå i proportion till identifierade risker, verksamhetens behov och kundkrav.

**Motivering:** En tillagd mening etablerar att riskprocessen är formaliserad och äger ett ansvar. Det räcker på policynivå — detaljprocessen hör hemma i ett underliggande dokument.

---

## 4. Medium-åtgärder (6 månader / ordinarie revision)

Dessa adresseras inte inför styrelsebeslut men noteras för nästa revisionscykel.

### F6 — Förbättringsåtagande saknas
*Åtgärd:* Lägg till en mening i avsnitt 6: *"MissionPoint strävar efter kontinuerlig förbättring av sitt informationssäkerhetsarbete."* En mening. Klar.

### F7 — Säkerhetsmedvetenhet saknas
*Åtgärd:* Lägg till en mening i avsnitt 12 (Medarbetares ansvar): *"Medarbetare ska genomgå grundläggande säkerhetsutbildning och hålla sig informerade om aktuella hot mot verksamheten."* Etablerar krav utan att specificera format eller frekvens — det hör hemma i HR-processer, inte policy.

---

## 5. Sammanfattning — vad styrelsen behöver veta

| Status | Villkor |
|---|---|
| ⛔ **Kan inte godkännas i nuläget** | F1 (säkerhetskänslig information) måste klaras ut med ledningen **innan** styrelsemötet. Spår A eller B avgör om policyn kan godkännas med villkor eller om ett stoppdokument behövs. |
| ✅ **Godkänn med villkor** | Om F1 klarläggs som Spår A (termen är allmän), kan styrelsen godkänna policyn villkorligt med krav på att F2 och F3 åtgärdas inom 30 dagar och att F4–F5 tas in i nästa version. |
| 💪 **Bevara styrkor** | AI-reglering (avs. 8) och EU/EES-lagringskrav (avs. 11.1) är genuint bra och ska inte röras. |

---

## 6. Implementeringsordning

```
Innan styrelsemötet
└── Klarlägg F1 med ledning/jurist → välj Spår A eller B

Vid styrelsebeslut (om Spår A)
└── Godkänn med villkorslista: F2 + F3 åtgärdas inom 30 dagar

Vecka 1–4 efter beslut
├── F2: Textändring avsnitt 9 (incidenttidsgräns + rollansvar)
└── F3: Nytt avsnitt 10.1 (MFA + lösenordskrav)

Månad 2–3 efter beslut
├── F4: Tillägg avsnitt 12 (åtkomstkontroll + offboarding)
└── F5: Textändring avsnitt 6 (riskprocess formaliseras)

Ordinarie revision (≤12 månader)
├── F6: Förbättringsåtagande, en mening
└── F7: Utbildningskrav, en mening
```

---

*Åtgärdsstrateg — MissionPoint-granskning v1.0 | 2026-02-27*
