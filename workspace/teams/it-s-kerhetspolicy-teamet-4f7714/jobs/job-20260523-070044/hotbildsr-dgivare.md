# Hotbildsrådgivare

# Hotbildsbedömning — MissionPoint IT- & Informationssäkerhetspolicy v1.0

**Roll:** Hotbildsrådgivare
**Fas:** Teknisk & strukturell policygranskning
**Underlag:** NCSC-SE, ENISA Threat Landscape 2024, MSB Årsrapport 2024
**Datum:** 2026-02-27

---

## 1. Metodologisk avgränsning

Uppdraget är "less is more". Denna analys svarar på en enda fråga:

> **Täcker policyn de hotbilder som faktiskt träffar en organisation med MissionPoints profil — eller finns det kritiska blinda fläckar som gör policyn tandlös mot verkliga angrepp?**

Jag bedömer inte mot fullständighetskrav i standarder. Jag bedömer mot hur hotaktörerna faktiskt opererar mot rådgivande konsultorganisationer med systemåtkomst hos kunder.

**Antaganden:**
- MissionPoint hanterar inloggningsuppgifter, VPN-åtkomst och konfidentiella dokument i kunders miljöer.
- MissionPoint är ett attraktivt indirekt mål — angrepp mot konsulten ger åtkomst till kunden.
- Policyn är ensamt styrande dokument tills vidare.

---

## 2. Aktuell hotbild mot MissionPoints profil

Baserat på NCSC-SE, ENISA Threat Landscape 2024 och MSB:s löpande rapportering är följande hottyper mest relevanta för en rådgivande IT-konsultorganisation i Sverige 2025–2026.

| Hottyp | Källa | Relevans för MissionPoint | Frekvens |
|---|---|---|---|
| **Nätfiske / spear-phishing** | NCSC-SE 2024, ENISA ETL 2024 | Primär intrångsvektor mot konsultbolag; medarbetare med kundkontakt är måltavla | Mycket hög |
| **Identitetsstöld / kontoövertagande (ATO)** | ENISA ETL 2024 | Stulna credentials ger direkt åtkomst till kundsystem via MissionPoints konton | Mycket hög |
| **Supply chain-angrepp** | NCSC-SE 2024 | MissionPoint *är* en supply chain-komponent — intrång ger angriparen fotfäste hos kunder | Hög |
| **Ransomware** | MSB 2024, ENISA ETL 2024 | Träffar konsultbolag direkt; krypterar kunddata i MissionPoints miljö | Hög |
| **Dataintrång via tredjepartstjänster / molntjänster** | ENISA ETL 2024 | Outsourcad IT-drift exponerar MissionPoint mot leverantörsintrång | Hög |
| **Statligt sponsrade aktörer (APT)** | NCSC-SE 2024, SÄPO ÅR 2024 | Konsultbolag med åtkomst till offentlig sektor eller försvarsnära kunder är explicita mål | Medium–Hög (kontextberoende) |
| **Insider-hot** | ENISA ETL 2024 | Konsulter med bred systemåtkomst; offboarding-brister ger kvarstående åtkomst | Medium |

---

## 3. Hotmappning mot policyn — vad täcks, vad saknas

### 3.1 Nätfiske & kontoövertagande (ATO)

**Hotbild:** Nätfiske är den dominerande initiala intrångsvektorn mot svenska organisationer (NCSC-SE 2024). Spear-phishing riktat mot konsulter med kundåtkomst är en etablerad taktik hos både kriminella grupper och statliga aktörer. Kontoövertagande via stulna credentials — ofta utan att MFA finns — är den vanligaste orsaken till supply chain-intrång.

**Policytäckning:**
- Avsnitt 10 kräver företagsdator och avråder från öppet Wi-Fi. ✅
- **Inget krav på MFA.** Policyn nämner inte multifaktorautentisering någonstans.
- Inget krav på lösenordshantering eller lösenordspolicy.
- Inget utbildningskrav som adresserar phishing-kännedom.

**Bedömning:** Kritisk blinda fläck. MFA är 2025 inte ett "nice to have" — det är den enskilt mest effektiva kontroll mot kontoövertagande och är explicit rekommenderat av NCSC-SE, CISA och ENISA. En konsultorganisation vars medarbetare loggar in i kundsystem utan MFA-krav i policyn har en direkt exploaterbar lucka.

**Riskpoäng:** Sannolikhet 5 × Konsekvens 4 = **20 — Kritisk**

---

### 3.2 Supply chain-angrepp

**Hotbild:** NCSC-SE identifierar supply chain-angrepp som en av de mest prioriterade hoten mot svenska organisationer 2024. Angripare komprometterar leverantörer med svagare säkerhet för att nå primärmålet. MissionPoint är per definition en supply chain-komponent hos sina kunder.

**Policytäckning:**
- Avsnitt 5 erkänner leverantörskedjepositionen och NIS2-kopplingen. ✅
- Avsnitt 11 kräver säkerhetsbedömning av MissionPoints egna leverantörer. ✅
- **Policyn reglerar inte hur MissionPoint skyddar sin roll som leverantör** — dvs. vilka säkerhetsgarantier MissionPoint kan ge sina kunder om den egna miljön.
- Ingen reglering av segmentering mellan kundmiljöer — risk för lateral rörelse om en kundåtkomst komprometteras och kan nå en annan kunds data.

**Bedömning:** Hög. Avsnitt 5 är en positiv ansats men stannar på erkännande-nivå. Det saknas en operationell princip om att MissionPoints egna system och åtkomster är isolerade per kund. Detta är det centrala skyddet mot att ett intrång hos MissionPoint sprider sig till alla kunder.

**Riskpoäng:** Sannolikhet 3 × Konsekvens 5 = **15 — Hög**

---

### 3.3 Ransomware

**Hotbild:** Ransomware är fortsatt den mest skadliga hottypen mot svenska organisationer (MSB 2024). Konsultbolag är attraktiva mål — de hanterar data med högt konfidentialitetsvärde och har ofta svagare säkerhet än sina kunder.

**Policytäckning:**
- Incidenthantering omnämns i avsnitt 9. ✅ (om än knapphändigt)
- **Inget krav på backup eller återställningsförmåga.** Om MissionPoints system krypteras finns ingen policyankrad förmåga att återhämta sig.
- Inget krav på nätverkssegmentering eller endpoint-skydd.

**Bedömning:** Hög. Frånvaron av backup-krav är en direkt lucka mot ransomware-scenariot. En policy som hanterar incidenter men inte mandaterar att det finns något att återställa till är inkonsekvent. Detta är ett minimum som kan adresseras med en enda mening.

**Riskpoäng:** Sannolikhet 4 × Konsekvens 4 = **16 — Kritisk**

---

### 3.4 Insider-hot & offboarding

**Hotbild:** Insider-hot — avsiktliga eller oavsiktliga — är konsekvent högt rankade av ENISA. För konsultorganisationer med bred systemåtkomst är offboarding-brister en specifik risk: avgångna medarbetare behåller aktiva konton i kundsystem.

**Policytäckning:**
- **Ingen reglering av åtkomstkontroll, behörighetstilldelning eller offboarding.**
- Avsnitt 12 nämner medarbetaransvar generellt men ingen process för hur åtkomster hanteras vid anställningens slut.

**Bedömning:** Hög, specifikt för en organisation som hanterar privilegierad åtkomst i kunders miljöer. Om en konsult slutar och deras kundåtkomster inte återkallas omedelbart är det en direkt hotexponeringslucka.

**Riskpoäng:** Sannolikhet 4 × Konsekvens 3 = **12 — Hög**

---

### 3.5 Statliga aktörer / APT (kontextberoende)

**Hotbild:** SÄPO och NCSC-SE varnar 2024 explicit för att konsultbolag med åtkomst till offentlig sektor, försvar, energi eller telekommunikation är sekundära mål för statliga aktörer (primärt Ryssland, Kina — Volt Typhoon, Cozy Bear m.fl.).

**Policytäckning:**
- Avsnitt 7 listar "säkerhetskänslig information" utan definition. ⚠️
- Ingen reglering som adresserar om MissionPoint har kunder i sektorer som gör dem till APT-mål.

**Bedömning:** Kan ej fullt bedömas utan kundkännedom. Flaggan om "säkerhetskänslig information" i avsnitt 7 är dock direkt relevant — om MissionPoint utför uppdrag åt kunder med säkerhetskänslig verksamhet är hotexponeringen mot statliga aktörer hög och policyn är inte kalibrerad för det scenariot. Denna risk är redan flaggad av Regulatorisk Complianceanalytiker som kritisk fynd.

**Riskpoäng (basscenario, ej säkerhetskänslig verksamhet):** Sannolikhet 2 × Konsekvens 5 = **10 — Hög**

---

## 4. Sammanfattning — Hotbaserade kritiska luckor

| Lucka | Relaterat hot | Riskpoäng | Prioritet | Föreslagen minimal åtgärd i policyn |
|---|---|---|---|---|
| **MFA saknas** | ATO, phishing, supply chain | 20 | 🔴 Kritisk | En mening: krav på MFA vid åtkomst till kundsystem och företagssystem |
| **Backup/återställning saknas** | Ransomware | 16 | 🔴 Kritisk | En mening: krav på regelbunden säkerhetskopiering av verksamhetskritisk data |
| **Ingen segmenteringsprincip per kund** | Supply chain-spridning | 15 | 🟠 Hög | En mening: kundmiljöer och åtkomster ska hanteras isolerat från varandra |
| **Offboarding/åtkomstkontroll saknas** | Insider-hot, kontoövertagande | 12 | 🟠 Hög | En mening: åtkomst till kundsystem ska återkallas vid anställningens upphörande |
| **"Säkerhetskänslig information" odefinerad** | APT, Säkerhetsskyddslagen | Okänt | ⚠️ Kräver klarläggning | Definition eller borttagning av termen — se Complianceanalytikers fynd |

---

## 5. Vad policyn faktiskt skyddar mot — hotbildsmässiga styrkor

Det är relevant att notera att policyn *inte* är tom på hotrelevanta kontroller:

- **AI-reglering (avs. 8):** Direkt relevant mot dataläckage-hotet via LLM-tjänster — ett reellt och växande hotscenario som ENISA lyfter 2024. Styrkan är välkalibrerad.
- **Distansarbetsregler (avs. 10):** Öppet Wi-Fi-förbud och krav på företagsdator adresserar den vanligaste osäkrade accesspunkten i hybridarbete.
- **Leverantörsbedömning (avs. 11):** Adresserar tredjepartsrisken mot MissionPoints egna leverantörer — relevant mot supply chain-hot underifrån.

Dessa avsnitt bör bevaras oförändrade.

---

## 6. Slutsats till styrelsen

Policyn har en trovärdig grundstruktur för en kompakt organisation. Men den missar **två kritiska hotrelaterade kontroller** som inte kan motiveras bort med "less is more":

1. **MFA** — utan detta är policyn inte försvarbar mot den dominerande intrångsvektorn 2025.
2. **Backup** — utan detta saknar incidenthanteringsavsnittet ett fundament.

Dessa är inte strukturkrav från ISO-standarder. De är svar på faktiska angrepp mot organisationer av MissionPoints typ, dokumenterade av NCSC-SE och ENISA under 2024. Båda kan adresseras med en mening vardera i befintliga avsnitt — ingen ny bulk krävs.

Styrelsens beslut bör vara: **godkänn med villkor** — de två kritiska luckorna åtgärdas innan policyn träder i kraft.

---

*Hotbildsrådgivare | Baserat på NCSC-SE Årsöversikt 2024, ENISA Threat Landscape 2024, MSB Årsrapport 2024, SÄPO Årsbok 2024*
