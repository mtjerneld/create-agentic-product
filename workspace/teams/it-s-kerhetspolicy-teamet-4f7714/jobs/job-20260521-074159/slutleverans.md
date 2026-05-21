# Projektledare & Granskningskoordinator · Slutleverans

# Granskning av Hemsö Fastighets AB IT-policy v4.0 — Slutleverans

Denna rapport innehåller en fullständig analys av Hemsös IT-policy v4.0 samt konkreta, prioriterade förbättringsförslag inklusive färdig reviderad policytext. Rapporten är direkt användbar som beslutsunderlag för IT-chef, CFO och styrelse.

---

## Sammanfattning för beslutsfattare

Er IT-policy fyller en roll som ägarformulerande strategidokument — men den är **i praktiken oförändrad sedan 2019** och uppfyller inte det regulatoriska landskap som gäller 2025. Det finns inga tecken på aktiva lagbrott, men ni saknar dokumenterad förmåga att bevisa efterlevnad vid en tillsynsinspektion.

**Fem saker policyn gör bra:**
- Kopplar IT tydligt till affärsstrategi
- Väldefinierad styrningsmodell med styrelseansvar
- Korrekt grundstruktur för GDPR (biträdesavtal, åtkomstbegränsning)
- Microsoft-centrerad standardiseringstrategi är försvarbar
- Outsourcingmodell med centraliserad drift är välmotiverad

**Det övergripande problemet:** Policyn är ett strategidokument som försöker vara ett säkerhetsdokument — och misslyckas med båda. Den saknar operationell styrning, mätbara krav och adresserar inte de hot som faktiskt hotar er verksamhet idag.

| Dimension | Betyg | Kommentar |
|---|---|---|
| Regulatorisk täckning | 2/5 | Kritiska gap mot NIS2, ISO 27001 |
| Säkerhetsmognad | 2/5 | Reaktiva formuleringar, inga proaktiva kontroller |
| Aktualitet | 1/5 | 2019 års hotbild — inte 2025 |
| Ansvarsfördelning | 2/5 | CISO-roll saknas, IT-chefens mandat otydligt |
| Implementerbarhet | 2/5 | Inga kontroller, inga mätpunkter |

**Åtgärdsprogram totalt:** 6–9 månader. Fyra kritiska åtgärder kräver beslut inom 30 dagar.

> ⚠️ **Viktig förutsättning för alla NIS2-relaterade åtgärder:** Hemsös NIS2-klassificering är ett välgrundat antagande baserat på samhällskritisk hyresgästbas och ägarstruktur — men den måste bekräftas genom juridisk analys mot lag (2024:491) och dialog med MSB innan NIS2-specifika åtgärder initieras. Klassificeringen som *viktig verksamhet* är trolig men inte juridiskt fastställd.

---

## Del 1 — Identifierade brister

### Konsoliderad luckmatris

| # | Brist | Policyavsnitt | Primärt ramverk | Prioritet |
|---|---|---|---|---|
| L-01 | Ingen separat informationssäkerhetspolicy | Introduktion | ISO 27001 kl. 5.2 | 🔴 Kritisk |
| L-02 | Ingen incidenthanteringsprocess | §4 Säkerhet | NIS2 art. 23, ISO 27001 | 🔴 Kritisk |
| L-03 | OT/BMS-system utanför scope | §1 Introduktion | NIS2, Säkerhetsskyddslagen | 🔴 Kritisk |
| L-04 | NIS2-klassificering inte genomförd | Hela policyn | NIS2 lag 2024:491 | 🔴 Kritisk |
| L-05 | CISO-roll saknas | §7 Roller | NIS2 art. 20, ISO 27001 kl. 5.3 | 🟠 Hög |
| L-06 | Tredjepartsrisk/leverantörsstyrning otillräcklig | §5 Personuppgifter | GDPR art. 28, NIS2 art. 21 | 🟠 Hög |
| L-07 | Ingen klassificering av information | §3 Strategi | ISO 27001 A.5.12, MSB | 🟠 Hög |
| L-08 | Åtkomstkontroll/IAM-styrning saknas | §4 Säkerhet | ISO 27001 A.5.15–18, NIS2 | 🟠 Hög |
| L-09 | Ingen kontinuitetsplan/DR-policy | §4 Säkerhet | NIS2 art. 21, ISO 27001 | 🟠 Hög |
| L-10 | Ingen riskhanteringsprocess | §4 Säkerhet | ISO 27001 kl. 6.1, MSB | 🟠 Hög |
| L-11 | Inga mätbara säkerhetsmål | §2 Mål | ISO 27001 kl. 6.2 | 🟡 Medium |
| L-12 | AI och molntjänster oreglerade | §3 Strategi | GDPR, AI Act | 🟡 Medium |
| L-13 | Krypteringskrav saknas | §4 Säkerhet | GDPR art. 32, ISO 27001 A.8.24 | 🟡 Medium |
| L-14 | Sårbarhetshanterings­process saknas | §4 Säkerhet | NIS2 art. 21, ISO 27001 A.8.8 | 🟡 Medium |
| L-15 | Säkerhetsutbildning/awareness saknas | §3 Strategi | NIS2 art. 21, ISO 27001 kl. 7.2 | 🟡 Medium |
| L-16 | DPIA-process saknas | §5 Personuppgifter | GDPR art. 35 | 🟡 Medium |
| L-17 | Intern revision underspecificerad | §8 Hantering | ISO 27001 kl. 9.1, NIS2 | 🟡 Medium |
| L-18 | Datuminkonsistens (2019 vs. 2023) | §8 Hantering | Intern styrning | 🟡 Medium |
| L-19 | Nätverkssegmentering/Zero Trust saknas | §4 Säkerhet | ISO 27001 A.8.20–22 | 🟡 Medium |
| L-20 | LEK/PTS inte adresserat | Saknas | LEK SFS 2022:482 | 🟡 Medium |

---

## Del 2 — Konkreta förbättringsförslag med reviderad policytext

### 🔴 KRITISK — Åtgärd 1: Incidenthantering (åtgärda inom 30 dagar)

**Varför kritiskt:** NIS2 (lag 2024:491) kräver rapportering av allvarliga incidenter till NCSC inom 24 timmar (tidig varning) och 72 timmar (fullständig rapport). Utan dokumenterad process riskerar ni administrativa sanktionsavgifter på upp till 7 MEUR eller 1,4 % av global omsättning.

**Steg 1 — Lägg omedelbart till följande i avsnitt 4 (Säkerhet):**

> *"Hemsö ska ha en dokumenterad och testad process för hantering av informationssäkerhetsincidenter. Processen ska definiera klassificering, eskalering, intern hantering och extern rapportering i enlighet med gällande lagkrav. IT-chefen ansvarar för att processen upprättas, kommuniceras och övas regelbundet. Allvarliga incidenter rapporteras till NCSC i enlighet med NIS2-lagstiftningens tidsramar (24 timmar för tidig varning, 72 timmar för fullständig rapport)."*

**Steg 2 — Upprätta Riktlinje för incidenthantering (inom 30 dagar) innehållande:**
- Incidentdefinition med konkreta exempel
- Klassificeringsmodell: P1 (kritisk) / P2 (allvarlig) / P3 (mindre allvarlig)
- Eskaleringsvägar och kontaktlistor inkl. NCSC-SE och MSB
- NIS2-rapporteringsrutin med tidsgränser
- Rollfördelning under incident (IT-chef, CFO, kommunikationsansvarig)
- Krav på incidentlogg och post-mortem-analys

**Steg 3 — Genomför tabletop-övning (skrivbordsövning) med ledningsgruppen inom 60 dagar**, med ett ransomware-scenario som utgångspunkt.

---

### 🔴 KRITISK — Åtgärd 2: NIS2-klassificeringsanalys (åtgärda inom 30 dagar)

**Varför kritiskt:** NIS2 är i kraft sedan januari 2025. Policyn nämner inte NIS2 överhuvudtaget. Om Hemsö klassificeras som viktig verksamhet gäller rapporteringskrav, tekniska minimikrav och tillsynsansvar från dag ett.

**Konkret åtgärd:**
1. Uppdra åt juridisk rådgivare att genomföra klassificeringsanalys mot lag (2024:491) — uppskattad insats 3–5 dagars juridisk genomlysning
2. Dokumentera klassificeringen i ett formellt beslutsmemo signerat av CFO
3. Anmäl er till NCSC:s register om klassificering bekräftas
4. Lägg till följande i avsnitt 4 (Säkerhet) som interimåtgärd:

> *"Hemsö följer tillämpliga krav i NIS2-direktivet (lag 2024:491 om cybersäkerhet) och vidmakthåller en aktuell klassificeringsbedömning. IT-chefen ansvarar för att säkerhetsnivån uppfyller de minimikrav som följer av Hemsös NIS2-klassificering."*

---

### 🔴 KRITISK — Åtgärd 3: Utvidga scope till att inkludera OT/BMS-system (åtgärda inom 30 dagar)

**Varför kritiskt:** Hotaktören Volt Typhoon — identifierad av NCSC-SE som aktiv mot europeisk infrastruktur — riktar specifikt in sig på IT/OT-konvergens i samhällsfastigheter. Att fastighetstekniska system faller utanför IT-säkerhetsstyrningen är en direkt exploaterbar blindfläck.

**Reviderad policytext — avsnitt 1, ny sista mening i scope-stycket:**

> *"Med IT avses alla former av informationsbehandling med hjälp av arbetsplatsklienter, kommunikationsnätverk, affärssystem och applikationer. Därtill inkluderas operativ teknologi (OT) såsom fastighetstekniska styr- och övervakningssystem (BMS/BAS), passersystem och andra uppkopplade fastighetssystem som interagerar med eller delar nätverksinfrastruktur med Hemsös IT-miljö."*

**Kompletterande åtgärder:**
1. Inventera alla OT/BMS-system och deras anslutning till IT-nätverket
2. Upprätta separat riktlinje för OT-säkerhet med krav på nätverkssegmentering, åtkomststyrning och incidenthantering

---

### 🔴 KRITISK — Åtgärd 4: Upprätta separat Informationssäkerhetspolicy (inom 60 dagar)

**Varför kritiskt:** ISO 27001:2022 kl. 5.2 kräver ett dedikerat ledningsdokument för informationssäkerhet. Utan det saknar Hemsö grunden för ett fungerande ISMS, vilket påverkar förmågan att svara på krav från offentlig sektor och regulatorer.

**Nytt styrdokument — Informationssäkerhetspolicy för Hemsö (utkast):**

---

> **INFORMATIONSSÄKERHETSPOLICY — HEMSÖ FASTIGHETS AB**
> *Beslutad av styrelsen | Version 1.0*
>
> **Syfte och scope**
> Hemsö Fastighets AB ska skydda konfidentialitet, integritet och tillgänglighet för den information som hanteras inom organisationen. Denna policy gäller Hemsö Fastighets AB och dess helägda dotterbolag, samtliga anställda, konsulter och tredjepartsaktörer med åtkomst till Hemsös information och IT-miljö, inklusive operativa styrsystem (OT) i fastighetsbeståndet.
>
> **Ledningens åtagande**
> Styrelsen och ledningsgruppen åtar sig att: (1) avsätta tillräckliga resurser för informationssäkerhetsarbetet, (2) uppfylla tillämpliga lagkrav och avtalsförpliktelser, (3) kontinuerligt förbättra informationssäkerhetsnivån, och (4) personligen följa och verka för efterlevnad av denna policy.
>
> **Principer**
> Hemsös informationssäkerhetsarbete ska vara riskbaserat, systematiskt och bygga på erkända standarder (ISO/IEC 27001). Information ska klassificeras och hanteras i enlighet med dess känslighet. Tillgång till information ska styras av principen om minsta nödvändiga behörighet.
>
> **Säkerhetsmål**
> Hemsö ska: (1) upprätthålla en maximal tillgänglighet för affärskritiska system i enlighet med definierade RTO/RPO-nivåer, (2) säkerställa att alla anställda genomgår informationssäkerhetsutbildning minst en gång per år, (3) säkerställa att inga allvarliga incidenter lämnas oanmälda till berörd myndighet, och (4) genomföra riskbedömning av informationssäkerheten minst en gång per år.
>
> **Koppling till övriga styrdokument**
> Denna policy kompletteras av IT-policy, Riktlinje för IT, Riktlinje för incidenthantering och Riktlinje för informationsklassificering.

---

### 🟠 HÖG — Åtgärd 5: Inför CISO-roll i rollförteckningen (inom 30 dagar)

**Varför viktigt:** NIS2 artikel 20 kräver att ledningsorgan personligen ansvarar för cybersäkerhetsåtgärder. Utan en utsedd informationssäkerhetsansvarig saknas koordinering av samtliga säkerhetsinitiativ.

**Reviderad policytext — lägg till i avsnitt 7 (Roller och ansvar):**

> **CISO / Informationssäkerhetsansvarig**
> - Ansvarar för att upprätta, implementera och underhålla Hemsös informationssäkerhetsprogram
> - Äger processen för riskbedömning och riskbehandling
> - Äger incidenthanterings
