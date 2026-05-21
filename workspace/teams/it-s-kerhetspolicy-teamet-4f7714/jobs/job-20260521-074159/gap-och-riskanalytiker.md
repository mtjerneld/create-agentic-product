# Gap- och Riskanalytiker

# Gap- & Riskanalys: Hemsö Fastighets AB — IT-policy v4.0
## Prioriterad risklista med klassificering

**Upprättad av:** Gap- och Riskanalytiker
**Datum:** 2025
**Underlag:** Regulatorisk kartläggning (Complianceanalytiker), ISO/IEC-analys (Standardspecialist), Teknisk policygranskning (IT-säkerhetspolicygranskar), Hotbildsanalys (Hotbildsrådgivare)
**Status:** Fas 2 — Leverans för Gap-analys & Riskvärdering

---

## Metodologi

### Riskvärderingsmodell

Varje identifierad lucka värderas längs två dimensioner:

| Dimension | Skala | Beskrivning |
|---|---|---|
| **Sannolikhet** | 1–5 | Hur troligt att luckan leder till incident/tillsyn under kommande 12 månader |
| **Konsekvens** | 1–5 | Regulatorisk, finansiell och operationell skada om luckan exploateras |
| **Riskpoäng** | S × K | Produkt av ovanstående, max 25 |

### Klassificering

| Riskpoäng | Klass | Färg | Åtgärdstidplan |
|---|---|---|---|
| 16–25 | 🔴 KRITISK | Röd | Omedelbar åtgärd — 0–30 dagar |
| 9–15 | 🟠 HÖG | Orange | Åtgärd inom 90 dagar |
| 4–8 | 🟡 MEDIUM | Gul | Åtgärd inom 6 månader |
| 1–3 | 🟢 LÅG | Grön | Planeras in i ordinarie revisionsarbete |

### Regulatorisk exponeringsmarkör

Varje risk märks med tillämpliga ramverk som primärt driver kravet:

- 🇪🇺 **GDPR** — Dataskyddsförordningen
- 🛡️ **NIS2** — Cybersäkerhetsdirektivet (SE-lag 2024:491)
- 📋 **ISO27K** — ISO/IEC 27001:2022 + 27002:2022
- 🏛️ **MSB** — MSB:s föreskrifter MSBFS 2020:6 / 2023:1
- 🔒 **SSL** — Säkerhetsskyddslagen (villkorlig)

---

## DEL 1 — Konsoliderad Luckmatris

Sammanfattning av alla identifierade luckor från fas 1–2, organiserade efter policyavsnitt.

| # | Lucka | Källa (fas 1-analyser) | Policyavsnitt | Primärt ramverk |
|---|---|---|---|---|
| L-01 | Ingen separat informationssäkerhetspolicy | ISO-spec, IT-sec | Introduktion | 📋 ISO27K |
| L-02 | Ingen incidenthanteringsprocess definierad | Alla fyra analytiker | §4 Säkerhet | 🛡️ NIS2, 📋 ISO27K |
| L-03 | Ingen klassificering av information | Compliance, ISO-spec | §3 Strategi | 📋 ISO27K, 🏛️ MSB |
| L-04 | Ingen åtkomstkontroll/IAM-styrning | IT-sec, Hotbild | §4 Säkerhet | 📋 ISO27K, 🛡️ NIS2 |
| L-05 | Tredjepartsrisk/leverantörsstyrning otillräcklig | Compliance, ISO-spec | §5 Personuppgifter | 🇪🇺 GDPR, 🛡️ NIS2 |
| L-06 | Ingen kontinuitetsplan/DR-policy | IT-sec, Hotbild | §4 Säkerhet | 🛡️ NIS2, 📋 ISO27K |
| L-07 | OT/BMS-system saknas helt i scope | Hotbild | §1 Introduktion | 🛡️ NIS2, 🔒 SSL |
| L-08 | Ingen riskhanteringsprocess | ISO-spec, Compliance | §4 Säkerhet | 📋 ISO27K, 🏛️ MSB |
| L-09 | CISO-roll saknas helt | IT-sec, Compliance | §7 Roller | 🛡️ NIS2, 📋 ISO27K |
| L-10 | Datuminkonsistens — policy ej uppdaterad sedan 2019 | IT-sec, ISO-spec | §8 Hantering | 📋 ISO27K |
| L-11 | Inga mätbara säkerhetsmål (KPI/KRI) | IT-sec, ISO-spec | §2 Mål | 📋 ISO27K |
| L-12 | Säkerhetsskyddslagen inte adresserad | Compliance, Hotbild | Saknas | 🔒 SSL |
| L-13 | Personuppgiftshantering ytlig — avsaknad av DPIA-process | Compliance | §5 Personuppgifter | 🇪🇺 GDPR |
| L-14 | AI och molntjänster inte reglerade | IT-sec | §3 Strategi | 📋 ISO27K, 🇪🇺 GDPR |
| L-15 | Medvetenhet och utbildning inte specifik för säkerhet | ISO-spec | §3 Strategi | 📋 ISO27K, 🛡️ NIS2 |
| L-16 | Revision och intern kontroll underspecificerad | Compliance, ISO-spec | §8 Hantering | 📋 ISO27K, 🛡️ NIS2 |
| L-17 | Nätverkssegmentering och Zero Trust saknas | IT-sec, Hotbild | §4 Säkerhet | 📋 ISO27K |
| L-18 | Supply chain-säkerhet (mjukvara/hårdvara) | Hotbild | §3, §5 | 🛡️ NIS2 |
| L-19 | Visselblåsning/säker rapporteringskanal saknas | Compliance | §7 Roller | 🇪🇺 GDPR, NIS2 |
| L-20 | Krypteringskrav saknas | IT-sec | §4 Säkerhet | 📋 ISO27K, 🇪🇺 GDPR |

---

## DEL 2 — Prioriterad Risklista

### 🔴 KRITISKA RISKER (Riskpoäng 16–25) — Omedelbar åtgärd krävs

---

#### RISK-01: Ingen incidenthanteringsprocess
> **Lucka:** L-02

| Parameter | Värde |
|---|---|
| **Sannolikhet** | 5/5 — Incidenter inträffar löpande; frånvaro av process garanterar hanteringsbrist |
| **Konsekvens** | 5/5 — NIS2 kräver 24h-anmälan; utebliven rapport ger böter + reputationsskada |
| **Riskpoäng** | **25/25** |
| **Ramverk** | 🛡️ NIS2 art. 23, 📋 ISO27K kl. 9.1, 🏛️ MSB MSBFS 2023:1 |

**Preciserat gap:** Policyn nämner "krishantering" i en bisats under §4 men innehåller noll operationellt innehåll: ingen definierad process, inga ansvariga, inga anmälningsskyldigheter, ingen länk till MSB/NCSC. NIS2-lagen (2024:491) kräver att väsentliga och viktiga verksamheter kan anmäla incidenter inom **24 timmar (preliminär varning)** och **72 timmar (fullständig rapport)**.

**Konsekvens om ej åtgärdat:** Tillsynsmyndighet (NCSC/IMY) kan utdöma administrativa sanktionsavgifter. För NIS2-viktiga verksamheter: upp till 7 MEUR eller 1,4 % av global omsättning.

**Åtgärdskrav:**
1. Upprätta dedikerat styrdokument: *Riktlinje för incidenthantering och rapportering*
2. Definiera incidentklassificering (P1–P4) med eskaleringsmatris
3. Peka ut CSIRT-kontakt och rapporteringsansvarig mot MSB/NCSC
4. Inkludera trigger-mekanism i IT Policy §4: *"Vid säkerhetsincidenter ska Hemsös riktlinje för incidenthantering aktiveras"*

---

#### RISK-02: CISO-roll och informationssäkerhetsansvar saknas
> **Lucka:** L-09

| Parameter | Värde |
|---|---|
| **Sannolikhet** | 5/5 — Organisationsstruktur redan etablerad utan CISO-funktion |
| **Konsekvens** | 4/5 — Alla övriga risker förvärras utan ägare; NIS2 kräver ledningsansvar |
| **Riskpoäng** | **20/25** |
| **Ramverk** | 🛡️ NIS2 art. 20, 📋 ISO27K kl. 5.1–5.3, 🏛️ MSB |

**Preciserat gap:** §7 Roller listar Styrelse, VD och CFO men nämner inte IT-chef i rollbeskrivning, och saknar helt en CISO- eller motsvarande informationssäkerhetsansvarig. NIS2 artikel 20 kräver att **ledningsorgan personligen ansvarar** för cybersäkerhetsåtgärder och genomgår regelbunden utbildning. ISO 27001:2022 kl. 5.3 kräver utpekade roller med definierat mandat.

**Konsekvens om ej åtgärdat:** NIS2-tillsyn kan riktas direkt mot styrelseledamöter personligen. Utan CISO-funktion saknas koordinering av samtliga säkerhetsinitiativ — ett strukturellt styrningsfel.

**Åtgärd
