# CISO-kommunikatör

# Granskningsrapport: Hemsö Fastighets AB — IT-policy v4.0
## Beslutsunderlag för IT-ledning och styrelse

**Klassificering:** Intern — Begränsad distribution  
**Adresserat till:** IT-chef, CFO, VD  
**Upprättad av:** CISO-kommunikatör  
**Datum:** 2025  
**Underlag:** Fullständig teknisk granskning genomförd av specialistteam (regulatorisk analys, ISO/IEC-granskning, hotbildsbedömning, gap- och riskanalys, åtgärdsstrategisk planering)

---

## Sammanfattning för beslutsfattare

Er nuvarande IT-policy fungerar inte längre som ett tillräckligt styrningsinstrument. Den är i praktiken oförändrad sedan 2019, och omvärlden har förändrats fundamentalt sedan dess — NIS2 är i kraft, ransomware mot fastighetsbolag ökar, och era samhällsfastigheter gör er till ett prioriterat mål för statssponsrade hotaktörer.

**Det finns inga tecken på att ni aktivt brutit mot lagen — men ni saknar dokumenterad förmåga att bevisa det.**

Granskningen identifierar **12 strukturella brister**, varav **4 är kritiska** och kräver åtgärd inom 30 dagar för att undvika regulatorisk exponering och operationell sårbarhet. Total investeringshorisont för ett komplett åtgärdsprogram: **6–9 månader**.

---

## Nulägesbedömning

### Vad policyn gör bra

Det är viktigt att konstatera att policyn inte är värdelös — den fyller en roll som ägarformulerande strategidokument:

- Tydlig koppling mellan IT och affärsstrategi
- Väldefinierad styrningsmodell med styrelseansvar
- Korrekt hantering av GDPR-grundstruktur (biträdesavtal, åtkomstbegränsning)
- Microsoft-centrerad standardiseringstrategi är ändamålsenlig och försvarbar
- Outsourcingmodell med centraliserad drift är välmotiverad

### Det övergripande problemet

Policyn är ett **strategidokument som försöker vara ett säkerhetsdokument** — och misslyckas med båda. Den saknar operationell styrning, mätbara krav och adresserar inte de hot som faktiskt hotar er verksamhet idag.

**Betygsöversikt:**

| Dimension | Betyg | Innebär |
|---|---|---|
| Regulatorisk täckning | 2 / 5 | Kritiska gap mot NIS2 och ISO 27001 |
| Säkerhetsmognad | 2 / 5 | Reaktiva formuleringar, inga proaktiva kontroller |
| Aktualitet | 1 / 5 | 2019 års hotbild — inte 2025 |
| Ansvarsfördelning | 2 / 5 | CISO-roll saknas, IT-chefens mandat otydligt |
| Implementerbarhet | 2 / 5 | Ingen koppling till kontroller eller mätpunkter |

---

## Identifierade brister — Prioriterad åtgärdslista

Granskningen identifierar totalt 12 strukturella brister. Dessa presenteras nedan grupperade efter åtgärdshorisont.

---

### 🔴 Omedelbar åtgärd — Inom 30 dagar

Dessa brister innebär **aktiv regulatorisk och operationell exponering** idag. De kräver inte nödvändigtvis fullständiga lösningar inom 30 dagar, men beslutet om åtgärd och ansvarig måste fattas nu.

---

#### BRIST 1 — Ingen incidenthanteringsprocess

**Vad saknas:** Policyn nämner inte hur Hemsö ska identifiera, hantera eller rapportera en IT-säkerhetsincident. Det finns ingen process, ingen ansvarig och inga tidsramar.

**Varför det är kritiskt:** NIS2 (lag 2024:491) kräver att väsentliga och viktiga verksamheter rapporterar allvarliga incidenter till NCSC inom **24 timmar** (tidig varning) och **72 timmar** (fullständig rapport). Om ni drabbas av ett intrång imorgon — och inte kan visa att ni hade en fungerande process — är böter och tillsynsåtgärder en direkt konsekvens.

**Regulatorisk exponering:** NIS2 artikel 23, ISO 27001 klausul 6.1, MSB MSBFS 2023:1

**Åtgärd:**
1. Besluta omedelbart vem som äger incidenthantering (rekommendation: CISO-roll, se Brist 9)
2. Ta fram en grundläggande incidenthanteringsriktlinje med fyra obligatoriska element: detektering, klassificering, eskalering och rapportering
3. Lägg till en policyformulering i avsnitt 4 som explicit hänvisar till denna riktlinje
4. Genomför en bordsskiva (tabletop exercise) inom 60 dagar för att testa processen

> **Föreslagen policytext, avsnitt 4:**
> *"Hemsö ska ha en dokumenterad och testad process för hantering av informationssäkerhetsincidenter. Processen ska definiera klassificering, eskalering, intern hantering och extern rapportering i enlighet med gällande lagkrav. IT-chefen ansvarar för att processen upprättas, kommuniceras och övas regelbundet. Allvarliga incidenter rapporteras till NCSC i enlighet med NIS2-lagstiftningens tidsramar."*

---

#### BRIST 2 — NIS2-klassificering är inte gjord

**Vad saknas:** Hemsö har inte formellt fastställt om bolaget klassificeras som viktig eller väsentlig verksamhet enligt NIS2 (lag 2024:491). Policyn nämner inte NIS2 överhuvudtaget.

**Varför det är kritiskt:** NIS2 är i kraft sedan november 2024. Fastighetsbolag med samhällskritisk hyresgästbas — försvar, domstolar, sjukhus — är potentiellt klassificerade som **viktig verksamhet**. Om klassificering som väsentlig verksamhet är aktuell (exempelvis vid IT-tjänster mot försvaret) är kraven ännu strängare. Att inte veta var man står är i sig en styrningsbrist.

**Regulatorisk exponering:** NIS2 lag 2024:491, artikel 3 och 21

**Åtgärd:**
1. Genomför en juridisk klassificeringsanalys inom 30 dagar — involvera extern NIS2-kompetens
2. Anmäl er till NCSC:s register om klassificering bekräftas
3. Dokumentera klassificeringsbeslutet i ett styrelsebeslut
4. Uppdatera policyn med en explicit referens till NIS2 och er klassificering

---

#### BRIST 3 — OT och fastighetssystem (BMS/BAS) finns inte i scope

**Vad saknas:** Policyn definierar IT som "arbetsplatsklienter, kommunikationsnätverk och system." Fastighetstekniska system — styr- och övervakningssystem (BMS), passersystem, energisystem — omnämns inte.

**Varför det är kritiskt:** Hemsö förvaltar fastigheter åt offentlig sektor. Dessa fastigheter innehåller OT-system (Operational Technology) som i allt högre utsträckning är uppkopplade mot IT-nätverket. Hotaktören Volt Typhoon — identifierad av NCSC-SE och CISA som aktiv mot europeisk infrastruktur — riktar specifikt in sig på just denna OT/IT-konvergens i samhällsfastigheter. Ett intrång i ett fastighetssystem kan ge fysisk åtkomst, störa hyresgästernas verksamhet eller användas som brygga in i IT-miljön.

**Regulatorisk exponering:** NIS2, potentiellt Säkerhetsskyddslagen om försvarsrelaterade fastigheter

**Åtgärd:**
1. Inventera alla OT/BMS-system och deras anslutning till IT-nätverket
2. Utvidga policyns scope-definition att explicit inkludera fastighetstekniska system
3. Upprätta en separat riktlinje för OT-säkerhet med nätverkssegmentering, åtkomststyrning och incidenthantering för dessa system

> **Föreslagen policytext, avsnitt 1 — reviderad scope-definition:**
> *"Med IT avses alla former av informationsbehandling med hjälp av arbetsplatsklienter, kommunikationsnätverk, affärssystem och applikationer. Därtill inkluderas operativ teknologi (OT) såsom fastighetstekniska styr- och övervakningssystem (BMS/BAS), passersystem och andra uppkopplade fastighetssystem som interagerar med eller delar nätverksinfrastruktur med Hemsös IT-miljö."*

---

#### BRIST 4 — Ingen separat informationssäkerhetspolicy

**Vad saknas:** IT-policyn försöker täcka både IT-strategi och informationssäkerhet i ett dokument. ISO 27001:2022 kräver explicit ett separat ledningsdokument för informationssäkerhet som kommunicerar ledningens åtagande, definierar scope och etablerar principer.

**Varför det är kritiskt:** Utan ett dedikerat informationssäkerhetsdokument saknar Hemsö grunden för ett fungerande ledningssystem för informationssäkerhet (ISMS). Det påverkar direkt förmågan att certifiera sig, svara på krav från kunder i offentlig sektor och visa regulatorisk efterlevnad.

**Regulatorisk exponering:** ISO 27001:2022 klausul 5.2, MSB MSBFS 2020:6

**Åtgärd:**
1. Ta fram en separat "Informationssäkerhetspolicy" på en till två sidor, beslutad av styrelsen
2. Det befintliga IT-policydokumentet renodlas till IT-strategi och IT-styrning
3. Informationssäkerhetspolicyn ska som minst innehålla: ledningens åtagande, scope, säkerhetsprinciper, klassificeringsansats och koppling till riskhantering

---

### 🟠
