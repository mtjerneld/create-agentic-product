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

---

## 2. Regulatoriskt ramverk — Sverige 2025

### Tvingande regelverk (relevanta för svenska organisationer)

| Ramverk | Noteringar |
|---|---|
| **GDPR (EU 2016/679)** | Hög relevans vid behandling av personal-, kund- och leverantörsdata. Kräver biträdesavtal, åtkomstkontroll, dataskyddspolicy. |
| **NIS2 (EU 2022/2555 / SE lag 2024:491)** | I kraft i Sverige. Kräver incidentrapportering (art. 23), tredjepartsrisk (art. 21), kontinuitetsplaner. Klassificering som *viktig* eller *väsentlig* verksamhet avgör kravnivå — **måste juridiskt fastställas per kund via dialog med MSB innan NIS2-åtgärder initieras.** |
| **Dataskyddslagen (2018:218)** | Kompletterar GDPR i svensk kontext. |
| **MSB:s föreskrifter (MSBFS 2020:6, 2023:1)** | Informationssäkerhet för organisationer av allmänt intresse. Kräver informationsklassificering. |
| **Säkerhetsskyddslagen (2018:585)** | Villkorlig — aktiveras om organisationen hanterar säkerhetsskyddsklassad information eller är leverantör till säkerhetskänslig verksamhet. |

### Villkorligt tillämpliga ramverk

| Ramverk | Noteringar |
|---|---|
| **DORA (EU 2022/2554)** | Primärt finansiella aktörer, men leverantörskedjor kan beröras indirekt. |
| **PTS / LEK** | Relevant om organisationen tillhandahåller elektroniska kommunikationstjänster — kontrollera per kund. |

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

Baserat på genomförd granskning — återkommande mönster att kontrollera i framtida uppdrag:

### Kritiska brister (ofta förekommande)
- **Ingen separat informationssäkerhetspolicy** — IT-policy och infosäkerhetspolicy blandas ihop; ISO 27001 kl. 5.2 kräver explicit ledningspolicy för informationssäkerhet.
- **Ingen incidenthanteringsprocess** — NIS2 art. 23 kräver definierad process och rapporteringskedjor.
- **OT/BMS-system utanför scope** — Fastighetstekniska system (Building Management Systems) saknas ofta i policyns tillämpningsområde trots att de är exponerade mot IT-nätverk och är ett prioriterat angreppsmål (Volt Typhoon m.fl.).
- **Datuminkonsistens och inaktuell versionskontroll** — Policy kan ha formellt nytt datum men vara oförändrad i sak sedan många år; alltid kontrollera interna datum mot innehållet.

### Höga brister
- Ingen riskhanteringsprocess (ISO 27001 kl. 6.1, ISO 27005)
- Tredjepartsrisk/leverantörsstyrning underreglerad (NIS2 art. 21, GDPR art. 28)
- IAM/behörighetsstyrning saknas (ISO 27001 A.5.15–A.5.18)
- BC/DR ej omnämnt (ISO 27001 kl. 8.8, NIS2 art. 21)
- CISO-roll saknas eller IT-chefens mandat otydligt (ISO 27001 kl. 5.3)
- Inga mätbara säkerhetsmål eller KPI:er (ISO 27001 kl. 6.2)

### Medium/Låg
- AI och molntjänster ej adresserade
- Informationsklassificering saknas (ISO 27002 A.5.12, MSB)
- Säkerhetsmedvetenhet/utbildning ej omnämnt

---

## 4. Korrekt policyhierarki (referensstruktur)

En funktionsduglig hierarki för informationssäkerhet:

```
Styrelsenivå:   IT-policy + Informationssäkerhetspolicy (separat)
       ↓
VD-nivå:        Riktlinjer per domän
                (IT-användning, klassificering, incidenthantering,
                tredjepartshantering, BC/DR)
       ↓
Operationell:   Instruktioner, processbeskrivningar, tekniska krav
       ↓
Kontrollnivå:   Tekniska säkerhetskrav, konfigurationsstandarder
```

---

## 5. Hotbildskunskap — Aktuell för svenska organisationer

### Statssponsrade aktörer (relevanta mot samhällsviktig infrastruktur)

| Aktör | Ursprung | Primär metod | Noterbart |
|---|---|---|---|
| APT28 / Fancy Bear | Ryssland (GRU) | Spearphishing, credential harvesting | Aktiv mot svensk samhällsviktig infrastruktur |
| APT29 / Cozy Bear | Ryssland (SVR) | Supply chain, Microsoft 365-intrång | Specifikt inriktad mot M365-miljöer |
| Volt Typhoon | Kina (PLA) | Living-off-the-land, OT/ICS via BMS | Direkt relevant för fastighetsautomation/BMS |
| Lazarus Group | Nordkorea | Ransomware, finansiellt motiverat | Opportunistisk mot alla sektorer |

### Kriminella hotaktörer
- **Ransomware** är den dominerande hottypen mot europeiska organisationer (ENISA Threat Landscape 2024) — fjärde året i rad.
- Aktiva grupper: Lockbit 3.0, Black Basta, Cl0p — riktade mot mellerstora europeiska fastighetsbolag.
- **Business Email Compromise (BEC)** — specifikt mot CFO/ekonomifunktioner vid fastighets- och hyresbetalningar.
- Organisationer med outsourcad IT-drift är extra exponerade (supply chain-risk).

### Sektorsspecifik exponering — samhällsfastigheter
- Hyresgäster inom offentlig sektor (försvar, domstolar, sjukhus, kriminalvård) gör fastighetsbolaget till ett **indirekt mål för underrättelseinhämtning**.
- OT/IT-konvergens (BMS kopplat mot IT-nätverk) är ett prioriterat angreppsmål som ofta saknas i policyens scope.

---

## 6. Sektorspecifik kunskap — Fastighetsbolag

- **NIS2-klassificering:** Fastighetsbolag med samhällskritisk hyresgästbas är preliminärt *viktig verksamhet*; om de levererar tjänster till försvarssektorn kan *väsentlig verksamhet* vara aktuellt. **Klassificeringen är alltid ett antagande tills det juridiskt fastställts.**
- **Ägarstruktur med statligt inslag** (t.ex. AP-fonder) medför höjda krav på transparens och intern styrning.
- **Outsourcad IT-drift** är vanligt i sektorn — aktiverar krav på leverantörsstyrning (ISO 27036, NIS2
