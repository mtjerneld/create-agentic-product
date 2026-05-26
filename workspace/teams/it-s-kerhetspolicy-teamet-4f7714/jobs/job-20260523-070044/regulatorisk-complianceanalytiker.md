# Regulatorisk Complianceanalytiker

# Regulatorisk Granskningsbaseline — MissionPoint AB
**Regulatorisk Complianceanalytiker | Fas 1 — Kartläggning & normativ bas**
*Datum: 2026-02-27 | Version: 1.0*

---

## Syfte med detta dokument

Detta dokument utgör den **normativa granskningsbas** mot vilken MissionPoints IT- och Informationssäkerhetspolicy v1.0 ska mätas. Dokumentet svarar på frågan: *Vad måste en policy som denna faktiskt innehålla — och ingenting mer?*

Tolkning av "minimum" är kalibrerad mot MissionPoints faktiska profil:
- Rådgivande konsultorganisation, ej operatör av kritisk infrastruktur
- Hanterar systemåtkomst och säkerhetsanalyser hos kunder
- Troligen **indirekt NIS2-berörd** som leverantör (art. 21.3) — ej primär NIS2-aktör
- Listar "säkerhetskänslig information" som informationskategori i policyn

> **Antagande:** MissionPoint är **inte** klassificerad som väsentlig eller viktig verksamhet under NIS2 i eget led. NIS2 tillämpas därför via leverantörskedjekravet. Om detta är felaktigt höjs kravnivån väsentligt — detta måste bekräftas med kunden innan slutlig bedömning.

---

## 1. Tillämpliga regulatoriska ramverk — MissionPoints profil

### 1.1 Tvingande ramverk (aktiverade)

| Ramverk | Aktiveringsskäl | Miniminivå som gäller |
|---|---|---|
| **GDPR (EU 2016/679)** | Hanterar personuppgifter (anställda, kunder, kontaktpersoner). Bekräftat i policyn avsnitt 7.1. | Art. 5 (grundprinciper), Art. 24 (lämpliga tekniska/org. åtgärder), Art. 25 (inbyggd dataskydd), Art. 28 (biträdesavtal), Art. 32 (säkerhet vid behandling), Art. 33-34 (incidentanmälan 72h) |
| **Dataskyddslagen (2018:218)** | Komplement till GDPR i Sverige, automatiskt tillämplig. | Inga tillkommande minimikrav utöver GDPR för denna profil. |
| **Säkerhetsskyddslagen (2018:585)** | ⚠️ **Potentiellt aktiverad.** Policyn avsnitt 7 listar "säkerhetskänslig information" som en hanterad informationskategori utan definition. Om MissionPoint utför säkerhetsanalyser åt aktörer med säkerhetskänslig verksamhet kan lagen vara direkt tillämplig. | Kräver omedelbar klarläggning med kunden. Kan ej bedömas som "minimum" utan bekräftad status. Se avsnitt 4 nedan. |

### 1.2 Indirekt tillämpliga ramverk (aktiverade via kundrelationer)

| Ramverk | Aktiveringsskäl | Miniminivå som gäller för MissionPoint |
|---|---|---|
| **NIS2 (EU 2022/2555 / SFS 2024:491)** | Konsultorg. med systemåtkomst hos kunder som sannolikt är NIS2-klassificerade. Art. 21.3 ställer krav på leverantörer. | Förmåga att uppfylla kundkrav kopplade till: riskhantering (art. 21.1), incidenthantering (art. 21.2a), leverantörssäkerhet (art. 21.2d), kontinuitet (art. 21.2c). Inte full NIS2-compliance, men dokumenterbar beredskap. |
| **DORA (EU 2022/2554)** | Om kunder är finansiella aktörer under DORA kan MissionPoint klassas som IKT-underleverantör. | Lägsta nivå: förmåga att presentera informationssäkerhetsrutiner och svara på leverantörsgranskning. Ingen direkt DORA-förpliktelse men indirekt avtalsexponering. |

### 1.3 Ramverk som *inte* är aktiverade för denna profil

| Ramverk | Skäl till exklusion |
|---|---|
| **MSB MSBFS 2020:6 / 2023:1** | Gäller myndigheter och organisationer av allmänt intresse. MissionPoint är privat konsultbolag — ej tillämplig som tvingande krav. Kan vara relevant som best practice-referens. |
| **PTS / LEK** | MissionPoint tillhandahåller inte elektroniska kommunikationstjänster. |
| **ISO 27001 (som tvingande krav)** | Frivillig standard. Aktiveras som krav vid specifik offentlig upphandling — inte generellt tillämplig. Används som strukturreferens i denna analys men genererar inga absoluta minimikrav. |

---

## 2. Normativ minimibaseline — vad måste finnas

Nedan definieras det **absoluta minimumet** per tillämpligt ramverk. Detta är granskningsbasen.

### 2.1 GDPR-minimum (tvingande)

| Krav | Rättslig grund | Krav på policynivå |
|---|---|---|
| Grundprinciper för behandling definierade | Art. 5 | Policy ska bekräfta ändamålsbegränsning, proportionalitet och laglighet — ej detaljbehandling, det räcker med hänvisning till integritetspolicy |
| Tekniska och organisatoriska skyddsåtgärder | Art. 32 | Policy ska ange att skyddsåtgärder tillämpas, inklusive kryptering och åtkomstkontroll som principer |
| Incidentanmälan personuppgifter — 72h | Art. 33 | Policy ska namnge ansvarig och bekräfta 72h-kravet explicit. Hänvisning till integritetspolicy är *otillräcklig* om den inte finns bilagd |
| Personuppgiftsbiträdesavtal | Art. 28 | Policy ska bekräfta att PuB-avtal tecknas vid leverantörsrelationer som involverar personuppgifter |
| Registrerades rättigheter | Art. 15–22 | Hanteras i integritetspolicy — policynivå behöver ej upprepa |

### 2.2 NIS2-leverantörsminimum (indirekt tvingande)

| Krav | Rättslig grund | Krav på policynivå |
|---|---|---|
| Riskbaserat förhållningssätt dokumenterat | Art. 21.1 | Policy ska bekräfta att riskbaserad metod tillämpas — *detta finns redan i avsnitt 6* |
| Incidenthanteringsförmåga | Art. 21.2a | Policy ska bekräfta att incidenter identifieras, hanteras och kan kommuniceras till berörda kunder. Tidsgräns behöver ej definieras exakt i policyn men processen måste existera |
| Leverantörssäkerhet | Art. 21.2d / Art. 21.3 | Policy ska bekräfta säkerhetsbedömning av underleverantörer — *delvis täckt i avsnitt 11* |
| Kontinuitet grundnivå | Art. 21.2c | Policy ska bekräfta att verksamhetskontinuitet beaktas — *saknas helt i nuvarande policy* |

### 2.3 Säkerhetsskyddslagen — om aktiverad

| Krav | Rättslig grund | Krav på policynivå |
|---|---|---|
| Definition av säkerhetskänslig information | SskL 2018:585, kap 1 §2 | Termen måste antingen **definieras** i policyn (vad avses) eller **raderas** om den inte är avsedd i lagens mening |
| Säkerhetsskyddsavtal vid leverantörsrelation | SskL kap 4 | Om aktiverad: policy ska bekräfta att säkerhetsskyddsavtal tecknas. Om ej aktiverad: termen ska rensas |

---

## 3. Kritiska tolkningsfrågor som måste lösas före granskningsbeslut

Dessa är inte granskningsfynd i sig — de är oklarheter som påverkar vilka krav som gäller.

### Fråga 1: Säkerhetsskyddslagen — aktiverad eller inte?

**Problemet:** Avsnitt 7 i policyn listar "säkerhetskänslig information" som en hanterad informationskategori. Termen har en specifik juridisk innebörd i Säkerhetsskyddslagen (2018:585). Om MissionPoint faktiskt hanterar information som faller under lagens definition — t.ex. vid uppdrag åt myndigheter, försvarssektorn eller annan säkerhetskänslig verksamhet — är lagen aktiverad och ställer krav långt utöver vad policyn innehåller.

**Konsekvens om aktiverad och ej adresserad:** Kritisk regulatorisk exponering. Möjliga sanktioner och avtalsbrott mot kunder med säkerhetsskyddsklassad verksamhet.

**Åtgärd krävs:** Bekräfta med MissionPoints ledning om de faktiskt hanterar information i lagens mening. Tre möjliga utfall:
- *(a) Nej* → Ta bort termen ur policyn och ersätt med "konfidentiell information"
- *(b) Ja, men marginellt* → Definiera termen i policyn med hänvisning till lagen och bekräfta att säkerhetsskyddsavtal tecknas
- *(c) Ja, i väsentlig utsträckning* → Policyn är otillräcklig som enda dokument; separat säkerhetsskyddsplan krävs

### Fråga 2: NIS2-klassificering av kunder

**Problemet:** Miniminivån för NIS2-leverantörskrav beror på om MissionPoints kunder faktiskt är NIS2-klassificerade och om de ställer dessa krav kontraktuellt.

**Antagande i denna analys:** Sannolikt relevant givet att MissionPoint utför säkerhetsanalyser och har systemåtkomst. Om kundbasen uteslutande är SME utan NIS2-klassificering faller detta krav bort.

**Åtgärd:** Konfirmera med säljansvarig/CIO vilka kundkategorier som är aktuella.

---

## 4. Granskningsbaseline — sammanfattande matris

Denna matris är den normativa mätpunkt som Fas 1 (gap-analys) ska mäta policyn mot.

| # | Minimikrav | Ramverk | Kravnivå | Måste finnas i policyn |
|---|---|---|---|---|
| B1 | Personuppgiftsincident — 72h-anmälan nämnd med ansvarig | GDPR art. 33 | **MÅSTE** | Ja |
| B2 | PuB-avtal bekräftas vid leverantörsrelationer med PU | GDPR art. 28 | **MÅSTE** | Ja |
| B3 | Tekniska skyddsåtgärder (kryptering, åtkomst) som princip | GDPR art. 32 | **MÅSTE** | Ja |
| B4 | "Säkerhetskänslig information" — definierad eller raderad | SskL 2018:585 | **KRITISK — kräver klarläggning** | Ja |
| B5 | Incidenthanteringsprocess — kan kommuniceras till kund | NIS2 art. 21.2a | **BÖR** (leverantörsled) | Ja |
| B6 | Kontinuitetsbeaktande — bekräftat i policyn | NIS2 art. 21.2c | **BÖR** (leverantörsled) | Nej — saknas |
| B7 | Riskbaserad metod — dokumenterad | NIS2 art. 21.1 / ISO 27001 | **BÖR** | Delvis finns |
| B8 | Säkerhetsbedömning av leverantörer — bekräftad | NIS2 art. 21.2d / GDPR art. 28 | **BÖR** | Delvis finns |

---

## 5. Vad som är utanför minimibedömningen

Följande krav är *inte* miniminivå för denna profil och ska **inte** generera ändringsförslag i fas 3:

- Formellt ISMS enligt ISO 27001 (klausul 4–10)
- MSB-klassificeringsscheman
- Detaljerade IAM-processer i policydokumentet
- KPI:er och mätbara säkerhetsmål
- Loggning och övervakning
- Sårbarhetsprogram
- OT/BMS-scope

Dessa är relevanta för organisationer med bredare regulatorisk exponering. För MissionPoint som kompakt konsultbolag hör de hemma i operativa styrdokument, inte i en övergripande säkerhetspolicy.

---

## 6. Rekommendation till teamet

**Fas 1 (gap-analys) kan påbörjas mot baselinen ovan med ett undantag:**

> ⚠️ **Håll B4 (Säkerhetsskyddslagen) i ett separat spår.** Gap-analysen kan visa var policyn träffar och missar mot GDPR och NIS2-leverantörskrav. Men fyndet kring "säkerhetskänslig information" kräver ett svar från kunden *innan* en rekommendation kan formuleras — rätt åtgärd beror helt på svaret. Presentera detta som en **öppen fråga med tre vägar** direkt till IT-chefen, parallellt med övrig analys.

---

*Dokument producerat av: Regulatorisk Complianceanalytiker*
*Nästa leverans: Fas 1 — Luckmatris (Inventering & gap-analys)*
