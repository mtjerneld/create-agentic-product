# Kunskapsbas

## IT-säkerhetspolicy-teamet

---

## 1. Teamets uppdragstyp & arbetsmetodik

### Typiskt uppdrag
Granskning, gap-analys och förbättringsförslag för IT-säkerhetspolicyer hos svenska organisationer. Målgrupp för leveranserna är IT-chefer, CISO, CFO och styrelsenivå.

### Fasmodell (etablerad)
1. **Fas 1 – Inventering & gap-analys:** Kartlägg policyn avsnitt för avsnitt mot relevanta regelverk. Leverans: strukturerad luckmatris.
2. **Fas 2 – Riskbedömning & prioritering:** Rangordna brister efter regulatorisk och operationell risk. Leverans: prioriterad risklista (Kritisk / Hög / Medium / Låg).
3. **Fas 3 – Förbättringsförslag & reviderad text:** Konkreta ändringsförslag med motivering, färdig policytext där relevant.

Faserna körs sekventiellt men kan ha parallella spår inom fas 3.

### Riskvärderingsmodell
- **Riskpoäng = Sannolikhet (1–5) × Konsekvens (1–5)**, max 25
- Kritisk: 16–25 (åtgärd 0–30 dagar), Hög: 9–15 (90 dagar), Medium: 4–8 (6 månader), Låg: 1–3 (ordinarie revision)

### Konsekvensparametrar (vad värderas vid risksättning)
- Regulatorisk exponering — sanktionsrisk, tillsynsrisk, avtalsbrott
- Operationell skada — förlust av funktionsförmåga, driftstörning
- Affärsskada — förtroende, kundförlust, competitive damage
- Hotaktörsexponering — hur direkt luckan är utnyttjbar av identifierade hotaktörer

### Sannolikhetskalibrering
Bedöms mot: (1) hur vanligt fyndet är i liknande organisationer, (2) hur aktuella hotaktörer opererar mot just denna organisationstyp, (3) om inga kompenserande kontroller kan antas existera (om policyn är ensamt styrdokument — vanligt i fas 1).

### "Less is more"-uppdrag — lärdomar
En uppdragstyp är policygranskningar inför styrelsebeslut där kunden explicit vill ha ett kompakt dokument. Principer för dessa uppdrag:
- Bedöm **bara mot regulatoriskt och operationellt minimum** — lyft inte "nice to have".
- Rekommendationsformatet är **"godkänn / godkänn med villkor / åtgärda först"** — styrelsen ska kunna fatta beslut, inte läsa en rapport.
- Åtgärdsförslag ska vara **kirurgiska** — skärp befintlig text, lägg inte till nya avsnitt om inte nödvändigt.
- Medium-fynd (poäng 4–8) kan ändå tas med om åtgärden är trivial (en mening), men detta ska noteras explicit som avvikelse från minimumorientering.

---

## 2. Regulatoriskt ramverk — Sverige 2025

### Tvingande regelverk

| Ramverk | Noteringar |
|---|---|
| **GDPR (EU 2016/679)** | Hög relevans vid behandling av personal-, kund- och leverantörsdata. Kräver biträdesavtal, åtkomstkontroll, dataskyddspolicy. Art. 33: 72h-regel för incidentanmälan. Art. 28: biträdesavtal med leverantörer. |
| **NIS2 (EU 2022/2555 / SE lag 2024:491)** | I kraft i Sverige. Kräver incidentrapportering (art. 23), tredjepartsrisk (art. 21), kontinuitetsplaner. Klassificering som *viktig* eller *väsentlig* verksamhet avgör kravnivå — **måste juridiskt fastställas per kund via dialog med MSB innan NIS2-åtgärder initieras.** |
| **Dataskyddslagen (2018:218)** | Kompletterar GDPR i svensk kontext. Inga egna minimikrav utöver GDPR för konsultprofil. |
| **MSB:s föreskrifter (MSBFS 2020:6, 2023:1)** | Informationssäkerhet för organisationer av allmänt intresse. Kräver informationsklassificering. |
| **Säkerhetsskyddslagen (2018:585)** | Villkorlig — aktiveras om organisationen hanterar säkerhetsskyddsklassad information eller är leverantör till säkerhetskänslig verksamhet. **OBS:** Om ett policydokument använder termen "säkerhetskänslig information" utan definition eller hanteringsregler är det ett kritiskt fynd — kräver omedelbar klarläggning med kunden. Termen är en legal term of art och ska aldrig användas löst i policydokumentation. |

### Villkorligt tillämpliga ramverk

| Ramverk | Noteringar |
|---|---|
| **DORA (EU 2022/2554)** | Primärt finansiella aktörer, men leverantörskedjor kan beröras indirekt. |
| **PTS / LEK** | Relevant om organisationen tillhandahåller elektroniska kommunikationstjänster — kontrollera per kund. |

### NIS2 — Leverantörskedjeperspektiv
Organisationer som inte själva är NIS2-klassificerade kan ändå vara **indirekt NIS2-berörda** som leverantörer till klassificerade kunder (art. 21.2b och art. 21.3). Detta är särskilt relevant för konsult- och rådgivningsbolag som hanterar systemåtkomst eller säkerhetsanalyser åt kunder i reglerade sektorer. NIS2 tillämpas då på leverantörsnivå, inte som primär aktör. Kravnivån är lägre men aktiveras via kundavtal och kundkrav — förmågan att uppfylla dessa krav ska vara dokumenterad i policyn.

### Best practice-standarder (de facto krav vid offentlig upphandling)

| Standard | Relevans |
|---|---|
| **ISO/IEC 27001:2022** | Strukturkrav för hela ISMS-hierarkin (10 klausuler, kap. 4–10). Kräver bl.a. scope-definition, ledningspolicy, riskprocess, mätbara mål. |
| **ISO/IEC 27002:2022** | Kontrollkatalog för operationell implementation. |
| **ISO/IEC 27005:2022** | Riskhantering informationssäkerhet. |
| **ISO/IEC 27017/27018** | Molntjänstsäkerhet resp. personuppgifter i moln — aktiveras vid outsourcad drift. |
| **ISO/IEC 27036** | Leverantörssäkerhet — aktiveras vid tredjepartsrelationer. |

---

## 3. Vanliga strukturella brister i IT-policyer

Återkommande mönster att kontrollera i varje uppdrag.

### Kritiska brister (ofta förekommande)
- **"Säkerhetskänslig information" utan definition** — Om termen förekommer i policyn utan hanteringsregler är säkerhetsskyddslagen potentiellt aktiverad. Kräver omedelbar klarläggning med kunden. Termen ska aldrig lämnas odefinierad i ett policydokument. Två spår: ta bort termen (om lagen ej tillämplig) eller lägg till hänvisning och hanteringsregler (om tillämplig).
- **Ingen separat informationssäkerhetspolicy** — IT-policy och infosäkerhetspolicy blandas ihop; ISO 27001 kl. 5.2 kräver explicit ledningspolicy för informationssäkerhet.
- **Ingen incidenthanteringsprocess** — NIS2 art. 23 och GDPR art. 33 (72h) kräver definierad process med tidsgränser, rollbeskrivningar och eskalationskedjor. Avsnitt om incidenter som saknar dessa element räknas som embryo, inte process.
- **MFA/autentiseringskrav saknas** — Frånvaro av MFA-krav är kritisk för organisationer med systemåtkomst hos kunder; primär hotvektor (kontoövertagande/ATO). Gäller även lösenordskrav och privilegierad åtkomst.
- **OT/BMS-system utanför scope** — Fastighetstekniska system saknas ofta i policyns tillämpningsområde trots IT-nätverksexponering.
- **Datuminkonsistens och inaktuell versionskontroll** — Policy kan ha formellt nytt datum men vara oförändrad i sak sedan många år.
- **Ingen formell riskhanteringsprocess** — ISO 27001 kl. 6.1 / ISO 27005 kräver dokumenterad process; dess frånvaro är ofta kritisk.
- **Tillgångshantering saknas helt** — Inget systeminventarium, ingen klassificering av informationstillgångar (ISO 27001 A.5.9–A.5.10).
- **Åtkomstkontroll och IAM saknas** — Inga behörighetsprinciper, ingen offboarding-process (ISO 27001 A.5.15–A.5.18, GDPR art. 25). Offboarding är särskilt kritisk för konsultorganisationer med bred systemåtkomst.

### Höga brister
- Tredjepartsrisk/leverantörsstyrning underreglerad (NIS2 art. 21, GDPR art. 28)
- Business Continuity / Disaster Recovery ej omnämnt (ISO 27001 kl. 8.8, NIS2 art. 21)
- CISO-roll saknas eller IT-chefens mandat otydligt (ISO 27001 kl. 5.3)
- Inga mätbara säkerhetsmål eller KPI:er (ISO 27001 kl. 6.2)
- Kryptering och nyckelhantering — inga tekniska krav specificerade (ISO 27001 A.8.24–A.8.25, GDPR art. 32)
- Säkerhetsmedvetenhet/utbildning ej omnämnt (ISO 27001 kl. 7.2, NIS2 art. 21)
- Policyns ägare och godkännandeprocess ej explicit angiven — vem kallar till revision, vem fastställer dokumentet?

### Medium/Låg
- AI och molntjänster ej adresserade (se styrkor nedan)
- Informationsklassificering saknas (ISO 27002 A.5.12, MSB)
- Loggning och övervakning saknas (ISO 27001 A.8.15–A.8.16)
- Sårbarhetshantering saknas
- Fysisk säkerhet ej adresserad
- Ingen scope-definition med geografiska gränser och explicit undantag
- Förbättringsåtagande saknas (ISO 27001 kl. 5.2) — kan åtgärdas med en mening

### Vad som faktiskt fungerar bra (mönster att bevara)
- **Proaktiv AI-reglering** — Konkret förbud mot att dela känslig information med namngivna AI-verktyg (ChatGPT, Copilot m.fl.) med tydliga exempel är ovanligt och värdefullt; bevara och stärk vid revision.
- **EU/EES-datageografi för molntjänster** — Explicit krav på EU/EES-lagring är direkt GDPR-relevant och korrekt strukturerat; skyddar mot exponering vid leverantörsbyte.
- **Hybridarbete reglerat** — Grundläggande regler för distansarbete (krav på företagsdator, förbud mot öppna nätverk) är ovanligare än man tror.
- **Scope täcker konsulter och kundsystem** — Kritiskt för konsultorganisationer med systemåtkomst; korrekt gjort när det förekommer.
- **Leverantörsbedömning med PBA/biträdesavtalskrav** — Proportionerligt och korrekt kopplat till GDPR art. 28 när det finns.

---

## 4. Konsultorganisationer med systemåtkomst — specifik profil

Insikter specifika för rådgivande IT-konsultbolag som hanterar systemåtkomst och säkerhetsanalyser hos kunder. Tillämpbar på liknande uppdrag.

### Regulatorisk profil
- Primärt GDPR-berörda (personal- och kunddata).
- Typiskt **indirekt NIS2-berörda** via leverantörskedjekravet (art. 21.3) — ej primär aktör. Bekräfta alltid NIS2-klassificering med kunden; om obekräftad, anta leverantörskedjeperspektiv som default.
- Säkerhetsskyddslagen villkorligt aktiverad beroende på kundportfölj (försvarsnära, offentlig sektor).

### Hotbild (NCSC-SE, ENISA ETL 2024, MSB 2024)
Konsultbolag med systemåtkomst är **attraktiva indirekta mål** — intrång mot konsulten ger fotfäste hos kunden.

| Hottyp | Relevans | Prioritet |
|---|---|---|
| Nätfiske / spear-phishing | Primär intrångsvektor mot medarbetare med kundkontakt | Mycket hög |
| Kontoövertagande (ATO) | Stulna credentials → direkt åtkomst till kundsystem | Mycket hög |
| Supply chain-angrepp | Konsulten *är* en supply chain-komponent | Hög |
| Ransomware | Krypterar kunddata i konsultens miljö | Hög |
| Dataintrång via molntjänster/tredjeparter | Outsourcad drift exponerar mot leverantörsintrång | Hög |
| Statssponsrade aktörer (APT) | Konsulter med åtkomst till offentlig/försvarsnära sektor är explicita mål | Medium–Hög |
| Insider-hot / kvarstående åtkomst | Ofullständig offboarding ger f.d. personal/konsulter kvarstående åtkomst | Medium |

### Policykrav som är extra kritiska för denna profil
- **MFA** — obligatorisk för alla externa system och kundsystemsåtkomst; primärt försvar mot ATO.
- **Offboarding-process** — formell process för att återkalla åtkomst vid avslut; frånvaro är direkt kopplad till insider-hot och kvarstående åtkomst.
- **Incidenthantering med kundnotifiering** — process måste inkludera hur och när kunder notifieras vid säkerhetsincident.
- **Leverantörsstyrning** — krav på PBA/biträdesavtal, säkerhetsbedömning av underleverantörer.

---

## 5. ISO 27001 — Minimikrav för kompakt policy (ej certifieringssökt)

När uppdragets ambition är minimum/kompakt dokument (ej certifiering), är dessa ISO 27001-klausuler de som en policy *måste* möjliggöra uppfyllnad av. Krav markerade ⚑ är absoluta på policynivå.

| Klausul | Minimikrav | Bedömningsprincip |
|---|---|---|
| **4.3** Scope | Definierat tillämpningsområde | ⚑ Måste finnas explicit |
| **5.2** Ledningspolicy | CIA-åtagande, förbättringsåtagande, ledningsengagemang | ⚑ Förbättringsåtagande saknas ofta — kan åtgärdas med en mening |
| **5.3** Roller & ansvar | Informationssäkerhetsansvarig utsedd med mandat | ⚑ Måste namnges eller rolldefineras |
| **6.1** Riskhantering | Riskbaserat förhållningssätt med dokumenterad process | ⚑ "Riskbaserat" som princip utan process räcker inte |
| **7.2** Kompetens | Säkerhetsutbildning/-medvetenhet omnämnt | ⚑ Ofta saknas helt |
| **8.1** Operationell kontroll | Åtkomstkontroll, leverantörskontroll, incidenthantering omnämnt | ⚑ Nivå: principerna ska finnas, inte fullständiga processer |
| **9.1** Uppföljning | Mätning och utvärdering möjliggjord | ○ Kan delegeras till implementeringsdokument |
| **10.1** Förbättring | Explicit åtagande om kontinuerlig förbättring | ⚑ En mening räcker |
