# Standardspecialist (ISO/IEC)

# ISO/IEC 27001/27002 — Regulatorisk baseline för MissionPoint

**Roll:** Standardspecialist (ISO/IEC)
**Fas:** Regulatorisk kartläggning & analys
**Datum:** 2025-01-27
**Dokument:** MissionPoint IT- och Informationssäkerhetspolicy v1.0

---

## 1. Metodologisk avgränsning

Uppdraget är "less is more" inför styrelsebeslut. Detta dokument identifierar **minimumet av ISO 27001/27002-krav** som en kompakt policy för en rådgivande konsultorganisation *måste* adressera — inte allt som kan adresseras. Krav märkta ⚑ är absoluta minimikrav. Krav märkta ○ är "nice to have" och lyfts inte vidare i denna fas.

**Antaganden (explicit):**
- MissionPoint är inte certifieringssökt mot ISO 27001 — standarden tillämpas som *best practice-baseline*, inte certifieringsrevision.
- MissionPoint hanterar systemåtkomst hos kunder och utför säkerhetsanalyser — detta aktiverar ett antal kontroller som annars hade kunnat prioriteras ned.
- Policyn är ensamt styrdokument tills vidare (inga underliggande riktlinjer bekräftade i materialet).

---

## 2. Minimikrav per ISO 27001:2022 — klausulnivå

Dessa är strukturkraven i standarden (kap. 4–10). Bedömning görs mot om policyn *möjliggör* uppfyllnad — inte om den fullständigt reglerar varje detalj.

| Klausul | Krav (minimum) | Status i policy | Bedömning |
|---|---|---|---|
| **4.1** Organisationens kontext | Förstå interna/externa faktorer som påverkar ISMS | Konsultroll och leverantörskedjeposition omnämns (avs. 4–5) | ✅ Tillräckligt på policynivå |
| **4.3** Scope | Definierat tillämpningsområde | Avs. 3 definierar personal, konsulter, system, kundsystem | ✅ Tillräckligt |
| **5.2** Ledningspolicy | Explicit ledningsengagemang, CIA-åtagande, förbättringsåtagande | CIA nämns i avs. 6. Ledningsansvar i avs. 12. Inget explicit förbättringsåtagande | ⚑ **Lucka: förbättringsåtagande saknas** |
| **5.3** Roller & ansvar | Informationssäkerhetsansvarig utsedd med mandat | CIO/delegat omnämns i avs. 6 | ✅ Tillräckligt på policynivå |
| **6.1** Riskhantering | Riskbaserat förhållningssätt dokumenterat | "Riskbaserat" omnämns i avs. 6, men ingen process | ⚑ **Lucka: ingen process angiven** |
| **6.2** Säkerhetsmål | Mätbara mål ska finnas | Saknas helt | ○ Inte krav på policynivå — kan delegeras till implementeringsdokument |
| **7.2** Kompetens | Säkerhetsutbildning/-medvetenhet | Saknas | ⚑ **Lucka: inget utbildningskrav** |
| **7.4** Kommunikation | Intern/extern kommunikationsplan | Saknas | ○ Kan hanteras operativt |
| **8.1** Operationell planering | Kontroller implementerade och utvärderade | Delvis (leverantör, incident, AI) | ✅ Tillräckligt på policynivå |
| **9.1** Uppföljning | Övervakning och mätning | Saknas | ○ Kan delegeras |
| **9.3** Ledningsgranskning | Ledningen granskar ISMS periodiskt | Avs. 14: "ses över minst årligen" | ✅ Tillräckligt |
| **10.2** Ständig förbättring | Explicit åtagande | Saknas | ⚑ Se 5.2 ovan — samma lucka |

---

## 3. Minimikrav per ISO 27002:2022 — kontrollnivå

Urval baserat på **MissionPoints specifika riskprofil**: konsultorganisation med systemåtkomst hos kunder, hanterar säkerhetsanalyser, leverantör i NIS2-kedjor. Endast kontroller som är **absoluta minimum** för denna profil listas.

### 3.1 Kontroller som policy MÅSTE adressera (⚑)

| Kontroll (ISO 27002) | Vad krävs | Status | Prioritet |
|---|---|---|---|
| **A.5.1** Policyer för informationssäkerhet | Policyn godkänd av ledning, kommunicerad, granskad | Godkännandeprocess oklar — versionshistorik tom (avs. 15) | ⚑ **Kritisk process-lucka** |
| **A.5.9** Inventarium av tillgångar | Informationstillgångar identifierade | Tillgångstyper listas (avs. 7) men inget inventarium | ○ Kan delegeras till operativt dokument |
| **A.5.15–5.16** Åtkomstkontroll | Behörighetsprinciper, IAM | "Behöriga personer" omnämns men inga principer (t.ex. minsta behörighet) | ⚑ **Lucka för konsultroll med systemåtkomst** |
| **A.5.19–5.22** Leverantörssäkerhet | Krav på leverantörer, avtal, uppföljning | Avs. 11 hanterar grundläggande bedömning + PBA | ✅ Tillräckligt på policynivå |
| **A.5.24–5.28** Incidenthantering | Definierad process, roller, tidsgränser | Avs. 9 saknar tidsgränser och rollansvar — är embryo, inte process | ⚑ **Känd kritisk lucka** |
| **A.6.3** Medvetenhetsutbildning | Obligatorisk säkerhetsutbildning | Saknas helt | ⚑ **Lucka** |
| **A.8.2** Privilegierad åtkomst | Hantering av administratörsrättigheter | Saknas | ⚑ **Hög risk — konsultroll med systemåtkomst** |
| **A.8.24** Kryptografi | Krypteringskrav | Saknas | ○ Kan delegeras till tekniskt dokument |
| **A.8.33** Skydd av testmiljöer | Test/prod-separation | Ej relevant på policynivå | ○ |

### 3.2 Kontroller som är styrkor — bevara (✅)

| Kontroll | Vad policyn gör rätt |
|---|---|
| **A.5.23** Informationssäkerhet vid molntjänst | Avs. 11.1 — EU/EES-lagring, konsekvensbedömning, PBA |
| **A.8.30–8.31** AI och externa tjänster | Avs. 8 — konkreta förbud, tillåtelsekriterier, medarbetaransvar |
| **A.6.7** Distansarbete | Avs. 10 — företagsdator, Wi-Fi-begränsning |
| **A.5.34** Integritet och sekretess | Avs. 7.1 — GDPR-hänvisning, integritetspolicy |

---

## 4. Den kritiska termen: "säkerhetskänslig information"

> **Avsnitt 7** i policyn listar "Säkerhetskänslig information" som en informationstyp MissionPoint hanterar — **utan definition, klassificeringskriterier eller hanteringsregler.**

Från ISO/IEC-perspektiv kolliderar detta med två krav:

1. **ISO 27001 A.5.12–A.5.13** (Klassificering och märkning): Informationsklassificering förutsätter att alla klasser är definierade. "Säkerhetskänslig" fungerar inte som klass om begreppet inte definieras.
2. **ISO 27002 A.5.9** (Tillgångsinventarium): Om organisationen hanterar en informationstyp måste den kunna identifiera vilken information som tillhör den typen.

**Konsekvens för ISO-efterlevnad:** Termen är antingen (a) en intern klassificeringsnivå som saknar definition, eller (b) en hänvisning till Säkerhetsskyddslagen som aktiverar ytterligare krav. Inget av alternativen är acceptabelt utan förtydligande.

**Rekommendation till teamet:** Klargör med MissionPoint om termen avser Säkerhetsskyddslagen-klassad information eller intern känslighetsklassning. ISO-kravet är detsamma oavsett: termen måste definieras eller strykas.

---

## 5. ISO-baserad minimibaseline — sammanfattning

Nedan är den **kortaste möjliga listan** med vad policyn måste adressera för att hålla ISO 27001/27002-minimum för MissionPoints profil. Inget annat lyfts till Fas 2.

| # | Lucka | ISO-krav | Prioritet (ISO-perspektiv) |
|---|---|---|---|
| L1 | Ingen riskprocess angiven — "riskbaserat" är en princip, inte en process | 27001 kl. 6.1 | ⚑ Kritisk |
| L2 | Incidenthantering saknar tidsgränser och rollansvar | 27002 A.5.24–5.26 | ⚑ Kritisk |
| L3 | Åtkomstkontrollprinciper saknas (minsta behörighet, IAM-process) | 27002 A.5.15–5.16, A.8.2 | ⚑ Kritisk — särskilt given konsultroll med systemåtkomst |
| L4 | Säkerhetsmedvetenhet/utbildningskrav saknas helt | 27001 kl. 7.2 / 27002 A.6.3 | ⚑ Hög |
| L5 | "Säkerhetskänslig information" odefinerad | 27001 A.5.12, + eventuell SäkL | ⚑ Kritisk — kräver kundklarläggning |
| L6 | Versionshistorik tom — godkännandeprocess ej synlig | 27002 A.5.1 | ⚑ Processkritisk inför styrelsebeslut |
| L7 | Förbättringsåtagande saknas i ledningspolicyn | 27001 kl. 5.2, 10.2 | Hög |

---

## 6. Överlämning till Fas 2

Följande luckor (L1–L6) förs vidare till riskbedömningsfasen för Sannolikhet × Konsekvens-värdering. **L7 kan hanteras med en enda menings tillägg** och behöver inte riskvärderas separat — föreslås som direkt textåtgärd i Fas 3.

**Notera till riskteamet:** L3 (åtkomstkontroll) bör värderas med förhöjd konsekvensparameter givet att MissionPoint per definition har systemåtkomst hos kunder — detta är inte en hypotetisk risk utan en operationell realitet för varje aktivt uppdrag.

---

*Dokument producerat av: Standardspecialist (ISO/IEC) | Nästa fas: Riskbedömning & prioritering*
