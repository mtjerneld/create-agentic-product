# Kvalitetssäkrare

# Kvalitetsgranskning: Slutleverans
## Hemsö Fastighets AB — IT-policy v4.0, Analyspaket

**Utfärdad av:** Kvalitetssäkrare  
**Datum:** 2025  
**Granskningsunderlag:** Samtliga fas 1–3 leveranser från Regulatorisk Complianceanalytiker, Standardspecialist (ISO/IEC), IT-säkerhetspolicygranskar, Hotbildsrådgivare, Gap- och Riskanalytiker samt Åtgärdsstrateg  
**Status:** Slutgodkänd för leverans till uppdragsgivare — med villkor

---

## 1. Granskningssammanfattning

Teamets samlade analyspaketet håller **genomgående hög kvalitet** och är ovanligt välstrukturerat för ett uppdrag av denna komplexitet. Materialet är handlingsbart, prioriterat och täcker de regulatoriska ramverk som är relevanta för en svensk organisation av Hemsös profil. Nedan dokumenteras de kvarstående brister som måste åtgärdas innan leverans, samt förbättringar som stärker paketets användbarhet för målgruppen (IT-chefer).

**Sammantagen bedömning:**

| Dimension | Betyg | Kommentar |
|---|---|---|
| Regulatorisk täckning | 4/5 | Mycket god täckning, ett gap kring PTS/LEK |
| Intern konsistens | 3/5 | Viss terminologisk inkonsistens och motstridiga prioriteringar |
| Handlingsbarhet | 4/5 | Stark — men några åtgärder saknar ägarskap och budget |
| Faktarobusthet | 4/5 | Välgrundade antaganden, men ett behöver verifieras omgående |
| Målgruppsanpassning | 3/5 | För teknisk i delar — behöver tydligare exekutivt lager |

---

## 2. Kritiska brister som måste åtgärdas före leverans

> Dessa punkter utgör **stoppers** — leverans bör inte ske utan att de adresserats eller explicit flaggats som öppna frågor.

---

### 🔴 Brist 1: Obekräftat NIS2-klassificeringsantagande presenteras som faktum

**Var i materialet:** Regulatorisk Complianceanalytiker (avsnitt 1), Hotbildsrådgivare (avsnitt 2), Gap- och Riskanalytiker (L-07, L-08), Åtgärdsstrateg (åtgärd nr 2)

**Problem:**  
Antagandet att Hemsö klassificeras som *viktig verksamhet* under NIS2 genomsyrar hela analyspaketets rekommendationer. Detta är ett rimligt antagande, men det presenteras i delar av materialet som en etablerad sanning snarare än en hypotes som kräver juridisk verifiering. Om klassificeringen är felaktig faller ett stort antal högt prioriterade åtgärder bort eller sänks i prioritet.

**Konsekvens om fel:**  
Hemsö investerar resurser i NIS2-compliance som de inte lagstiftningsvägen är skyldiga till. Trovärdigheten hos analyspaketets övriga rekommendationer skadas.

**Krav före leverans:**  
Lägg till en tydlig och enhetlig disclaimer i samtliga berörda avsnitt med följande formulering (eller likvärdig):

> *"NIS2-klassificeringen är ett antagande baserat på Hemsös samhällskritiska hyresgästbas och ägarstruktur. Klassificeringen måste bekräftas genom juridisk analys mot lag (2024:491) och dialog med MSB innan NIS2-relaterade åtgärder initieras."*

**Ansvar:** Regulatorisk Complianceanalytiker och Gap- och Riskanalytiker uppdaterar sina dokument. Åtgärdsstrateg lägger till detta som åtgärd nr 0 (föregår alla NIS2-åtgärder).

---

### 🔴 Brist 2: Motstridiga prioriteringsordningar mellan Gap- och Riskanalytiker och Åtgärdsstrateg

**Var i materialet:** Gap- och Riskanalytiker (prioriterad risklista), Åtgärdsstrateg (åtgärdsmatris rad 1–4)

**Problem:**  
Gap- och Riskanalytikern rankar **L-01 (ingen separat informationssäkerhetspolicy)** som riskpoäng 16 (KRITISK). Åtgärdsstrategens matris rankar incidenthanteringsprocess som åtgärd nr 1 och informationssäkerhetspolicyn som nr 4 — utan att motivera omordningen.

En IT-chef som läser båda dokumenten parallellt får motstridiga signaler om vad som ska göras först. Det underminerar paketets trovärdighet som beslutsstöd.

**Krav före leverans:**  
Åtgärdsstrategens prioriteringslogik måste explicit motiveras i ett kortfattat resonemang (2–4 meningar). Alternativt justeras ordningen så att den är konsistent med riskpoängen, eller så skapas ett gemensamt prioriteringsdokument (se rekommendation i avsnitt 4).

---

### 🔴 Brist 3: Saknat regelverk — PTS och LEK (Lagen om elektronisk kommunikation)

**Var i materialet:** Regulatorisk Complianceanalytiker (ramverksöversikt)

**Problem:**  
Hemsö driver outsourcad IT-drift och troligen nätverk inom fastighetsstocken (inklusive offentliga byggnader). Lagen om elektronisk kommunikation (LEK, SFS 2022:482) och PTS föreskrifter om robust elektronisk kommunikation är potentiellt tillämpliga — särskilt om Hemsö tillhandahåller nätverksinfrastruktur till hyresgäster i kritiska verksamheter.

LEK omnämns inte någonstans i materialet, varken som bekräftat tillämpligt eller som explicit bortvalt.

**Krav före leverans:**  
Complianceanalytikern lägger till en rad i ramverksöversikten (avsnitt 2.1) för LEK/PTS med en kort applicerbarhetsanalys. Om bedömningen är att LEK inte är tillämplig ska det motiveras.

---

## 3. Väsentliga förbättringar (bör åtgärdas, stoppar inte leverans)

---

### 🟠 Förbättring 1: Inget exekutivt sammanfattningslager för IT-chefer

**Problem:**  
Analyspaketets styrka — djupet — är också dess svaghet ur ett leveransperspektiv. Materialet är sammantaget mycket omfattande. En IT-chef som ska använda det som beslutsstöd inför styrelseledning behöver ett koncentrerat exekutivt lager: *"Vad är det viktigaste? Vad kostar det? Vad händer om vi inte gör det?"*

**Rekommendation:**  
Skapa ett **Executive Summary-dokument på 1–2 sidor** med följande struktur:

- **Tre meningarsbedömning** av policyn nuläge
- **Topp 5 åtgärder** med angiven tidshorisont och uppskattad resursinsats
- **Regulatorisk riskexponering** om inget görs (sanktion, incident, tillsyn)
- **Föreslagen beslutspunkt** för styrelsepresentation

Ansvaret för detta dokument faller naturligen på Åtgärdsstrategens leverans som ett kompletterande appendix.

---

### 🟠 Förbättring 2: Textförslagen i Åtgärdsstrategens leverans är ofullständiga

**Problem:**  
Åtgärdsstrategens leverans innehåller åtgärdsmatrisen och strukturerade rekommendationer, men de faktiska **revideringstextförslagen** (dvs. konkret ny policytext) förefaller avkortade i det underlag som granskats. Fas 3 i kickoff-briefen specificerar explicit *"Föreslå ny/reviderad policytext där det behövs"*.

Specifikt saknas utkasttext för:
- Ny sektion om incidenthantering
- Ny sektion om behörighetsstyrning/IAM
- Reviderat avsnitt 4 (Säkerhet) med moderniserat hotskydd

**Rekommendation:**  
Åtgärdsstrategens dokument kompletteras med konkreta textblock för åtminstone de tre kritiska sektionerna (incidenthantering, IAM, uppdaterat säkerhetsavsnitt). Dessa bör märkas som *"Förslag — kräver juridisk och verksamhetsmässig granskning av Hemsö"*.

---

### 🟠 Förbättring 3: Datuminkonsistensen i policyn — ingen åtgärd specificerad

**Problem:**  
Tre av analysdokumenten identifierar datuminkonsistensen (beslutat 2019 vs. datum i sidhuvud 2023) som en trovärdighetsbrist. Åtgärdsstrategens matris rankar detta som åtgärd nr 10 ("Versionskontroll-inkonsistens, Medium, insats Låg") men ger ingen konkret instruktion om hur Hemsö löser det.

Specifikt är det oklart om:
1. Policyn faktiskt reviderades 2023 men versionsförteckningen inte uppdaterades, eller
2. Datumen i sidhuvudet är ett kopieringsfel

**Rekommendation:**  
Åtgärdsstrategens punkt 10 kompletteras med en explicit instruktion: *"Hemsös IT-chef verifierar om en 2023-revision genomfördes. Om ja: uppdatera versionsförteckningen till v5.0 med korrekt datum och beslutad av-information. Om nej: ta bort 2023-datumen och ersätt med faktisk revisionsdatum vid nästa revidering."*

---

### 🟡 Förbättring 4: AI och molntjänster behandlas fragmenterat

**Problem:**  
Hotbildsrådgivaren lyfter AI-risker som en emergent hotvektor. Åtgärdsstrategens matris nämner "AI och molntjänster" som åtgärd nr 12
