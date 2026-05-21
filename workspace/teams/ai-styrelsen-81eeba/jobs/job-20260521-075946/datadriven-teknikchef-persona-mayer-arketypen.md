# Datadriven Teknikchef (persona: Mayer-arketypen)

# Individuell Analys – Datadriven Teknikchef (Mayer-arketypen)

**Ledamot:** Alexandra Mayer, Chief Technology Officer  
**Fas:** 2 – Individuell analys  
**Datum:** Session 1  
**Ämne:** Geografisk expansion – Danmark, Norge eller Finland? Organisk vs. förvärv?

---

## 1. Ramverk och krav för ståndpunkt

Innan jag tar ställning behöver jag etablera vilket evidensunderlag som är tillräckligt. Jag kräver data på tre nivåer:

| Nivå | Vad jag letar efter | Datakvalitet i befintligt underlag |
|------|--------------------|------------------------------------|
| Marknadsstorlek | Antal potentiella kunder (IT-bolag med ledning som köper rådgivning/board-as-a-service) | ⚠️ Måste uppskatta |
| Teknisk kompatibilitet | Infrastruktur, dataskyddslagar, AI-regulering per land | ✅ Kan härleda från GDPR + NIS2 |
| Skalbarhetsprofil | Kan delivery-modellen replikeras utan att kärnan bryts? | ⚠️ Antagandebaserat |

**Antaganden jag arbetar med:**  
- Mission Point levererar strategisk rådgivning, facilitation och/eller AI-driven beslutsstöd till IT-bolag
- Kärnprodukten är digitalt levererad eller hybridlevererad (möjliggör skalning utan linjär headcount-ökning)
- Bolaget är idag verksamt i Sverige och har svensk referensbas

---

## 2. Teknisk och operationell genomförbarhet per marknad

### 2.1 Danmark

**Marknadsstorlek (estimat):**  
Danmark har ca 3 200 IT-bolag med fler än 10 anställda (Eurostat/Danmarks Statistik, 2023). Av dessa är uppskattningsvis 400–600 i segmentet "tillväxtbolag med behov av strukturerat ledningsstöd" – Mission Points primära ICP.

**Teknisk infrastruktur:**  
- GDPR-kompatibelt, samma regelverk som Sverige → låg juridisk friktionskostnad
- Hög digitaliserings­mognad (EU Digital Economy Index: Danmark #1 i EU 2023)
- Copenhagen Tech-scenen är mogen; etablerade nätverk inom EIT Digital, TechBBQ

**Dataskydd och AI-regulering:**  
- EU AI Act appliceras identiskt som i Sverige → ingen extra compliance-overhead
- Datatilsynet (dansk motsvarighet till IMY) har snarlik praxis

**Skalbarhetsprofil:**  
- Språkbarriär: låg (hög engelskproficiency, skandinavisk begriplighet)
- Tidzon: identisk
- Kulturell affärslogik: hög likhet med Sverige, dock mer hierarki-skeptisk ("Janteloven"-dynamik kan påverka hur board-as-a-service positioneras)

**Risk:** Marknaden är liten i absoluta tal. CAC/LTV-kalkylen måste valideras – risk för att skaleffekterna uteblir om TAM inte är tillräcklig.

---

### 2.2 Norge

**Marknadsstorlek (estimat):**  
Ca 2 800 IT-bolag >10 anst. Oljefondens välstånd driver hög betalningsvilja. Oslo Tech-hub är koncentrerad och relationsstyrd.

**Teknisk infrastruktur:**  
- EES-land, inte EU → GDPR gäller via EES-avtalet, men bolag som processar norska myndigheters data kan möta ytterligare krav (NSM-regelverk)
- Potentiellt relevant om Mission Point riktar sig mot offentlig sektor i Norge

**Skalbarhetsprofil:**  
- Hög köpkraft → möjlighet att ta högre pris
- Starkare lokal förankring krävs ("kjøper av folk de kjenner")
- Valutarisk: NOK-exponering

---

### 2.3 Finland

**Marknadsstorlek (estimat):**  
Ca 2 400 IT-bolag >10 anst. Stark deep-tech-kultur (Nokia-arvet, Slush-ekosystemet). Mer benägen att adoptera ny teknologi tidigt.

**Teknisk infrastruktur:**  
- Full EU-medlem → identisk regulatorisk miljö som Sverige och Danmark
- Finskans språkbarriär är reell – engelska fungerar i tech-segmentet, men lokal förankring kräver finska

**Skalbarhetsprofil:**  
- Helsinki tech-community är tät och meritokratisk → snabbare word-of-mouth om produkten fungerar
- Lägre absolut TAM än Danmark, men högre "early adopter"-densitet

---

## 3. Organisk etablering vs. förvärv – teknisk och operationell analys

### 3.1 Organisk etablering

**Fördelar ur teknik/data-perspektiv:**
- Full kontroll över delivery-modell och datarkitektur från dag ett
- Ingen teknisk skuld från förvärvat bolags legacy-system
- KPI:er är rena och jämförbara med Sweden baseline

**Risker:**
- Inga lokala data att träna ev. AI-komponenter på (om produkten kräver lokal kontext)
- Time-to-first-revenue estimeras till 9–18 månader
- Kräver lokal BD-kapacitet utan existerande referensram

**Mätbar trigger för go/no-go:**  
Pilot med minst 3 betalande kunder i målmarknaden innan full etablering beslutas.

---

### 3.2 Förvärv

**Vad skulle vi köpa?**  
Bolag som är kandidater för konvertering till Mission Point-delivery bör uppfylla:

| Kriterium | Indikator |
|-----------|-----------|
| Befintlig kundrelation med IT-bolag | Fakturerande kunder i ICP |
| Kompetens inom ledarskapsutveckling, facilitation eller strategisk rådgivning | CV-bas + referenser |
| Teknisk skuld som är hanterbar | Inga proprietära plattformar som låser delivery-modellen |
| Kulturell alignment | Bedöms i DD-process |

**Kandidattyper i Danmark:**
- Boutique management consultancies med IT-fokus (t.ex. liknande Ative, Implement Consulting Group-spin-offs)
- Leadership development-bolag med tech-kunder
- Executive coaching-nätverk med digital delivery

> **Antagande:** Jag antar att denna typ av bolag existerar i Danmark givet marknadens mognad, men jag har inte primärdata. Detta måste verifieras med en faktisk market scan (LinkedIn Sales Navigator + Proff.dk + Bisnode).

**Risker med förvärv:**
- Integration­skostnad: kulturell konvertering är svårast att kvantifiera
- Prisrisk: multipelkostnad för ett litet konsultbolag i Danmark (typiskt 0,8–1,5x ARR)
- Teknisk DD kan avslöja beroenden som är svåra att bryta

**Min position:** Förvärv kan accelerera time-to-market med 12–18 månader, men **enbart om** målbolaget har ren delivery-modell utan proprietär teknologiskuld.

---

## 4. Kvantitativa KPI:er för beslut

Innan styrelsen kan rösta om expansion behöver följande mätvärden etableras eller estimeras:

```
TAM per marknad:
  Danmark:  ~500 bolag × avg contract value (ACV) = ?
  Norge:    ~350 bolag × (ACV × 1,3 pga köpkraft) = ?
  Finland:  ~300 bolag × ACV = ?

Breakeven-kalkyl organisk:
  Fixed cost (lokal närvaro, 1 FTE BD + overhead): ~1,2–1,8 MSEK/år
  Required signed customers år 1 för breakeven: ACV / 1,5M = ?

Förvärvskalyl:
  Target multiple: 1,0–1,5x ARR
  Integration OPEX (år 1): +30–40% av förvärvspris
  Synergy realization: antaget 24 månader
```

> **Brist i underlaget:** Utan Mission Points faktiska ACV och nuvarande CAC kan jag inte slutföra kalkylen. Jag arbetar med antagandet att ACV är i intervallet 150 000–400 000 SEK/år per kund, baserat på typiska management advisory-produkter för SME IT-bolag.

---

## 5. Teknisk rekommendation (preliminär, pre-deliberation)

### Vilket land?

**Danmark är det tekniskt starkaste valet** baserat på:
1. Lägst regulatorisk friktionskostnad (EU, GDPR-identiskt)
2. Högst digitaliserings­mognad → kortare sales cycle för digital delivery
3. Geografisk och kulturell proximitet → lägst operationell overhead
4. Starkast TAM i absoluta tal bland de tre alternativen

**Reservationer:**
- Marknaden är fortfarande liten; **om** strategin är att bygga en nordisk plattform bör sekvensen vara DK → NO → FI, inte tvärtom
- Finland är ett intressant alternativ om Mission Point har en tydlig AI-first produktpositionering – Helsingfors-scenen är mer tech-forward

### Entry-strategi?

**Organisk pilot först, förvärv som option i månad 9–12.**

Rationale:
- Organisk pilot ger ren data på om affärsmodellen håller i dansk kontext
- Förvärvsprocess tar 6–12 månader ändå → man kan köra parallella spår
- Förvärv bör inte ske utan minst ett kontrakt i Danmark som proof of demand

### Naturlig expansionsplan

```
Fas 1 (0–12 mån):  Danmark – organisk pilot, 3 pilot-kunder, mät NPS + ACV
Fas 2 (12–24 mån): Besluta förvärv DK eller gå vidare org. + öppna Norge
Fas 3 (24–36 mån): Finland baserat på om AI-komponenten är mogen nog
```

---

## 6. Öppna frågor och reservationer

1. **Vad är Mission Points faktiska delivery-modell?** Om produkten kräver fysisk närvaro förändras hela kalky
