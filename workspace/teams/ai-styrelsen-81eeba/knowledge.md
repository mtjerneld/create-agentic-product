# Kunskapsbas

## Om AI-styrelsen – Produkt & Koncept

### Vad är AI-styrelsen?
Ett agentbaserat deliberationssystem där fem AI-personas med distinkta roller, beslutslogiker och bias gemensamt analyserar strategiska frågor, delibererar transparent och fattar viktade beslut via omröstning. Designat för att vara repeterbart på nya strategifrågor utan ombyggnad.

### De fem ledamotspersonorna

| Ledamot | Arketyp | Beslutsprofil & bias |
|---|---|---|
| 🎯 Visionär Grundare | Jobs-arketypen | Ifrågasätter premisser, söker distinktion och genombrott, skeptisk till förvärv |
| 📊 Datadriven Teknikchef | Mayer-arketypen | Kräver mätbara triggers, evidensbaserade beslut, TAM-validering |
| 📈 Tillväxtinriktad Investerare | Andreessen-arketypen | Tolererar risk för hög avkastning, föredrar hastighet, positiv till förvärv under rätt villkor |
| ⚖️ Etisk Teknolog | Gebru-arketypen | Värderar ansvarsfull AI, medarbetaretik, regulatorisk noggrannhet, varnar för förvärvsrisker |
| ⚙️ Operativ Skalare | Sandberg-arketypen | Prioriterar intern beredskap, kontrollerbar exekvering, ett land i taget |

### Deliberationsflödet (etablerat i MVP)
1. **Fas 1 – Design & personas:** Ledamotsprofiler definieras
2. **Fas 2 – Individuell analys:** Varje ledamot producerar självständigt PM
3. **Fas 3 – Deliberation:** Varje ledamot läser övrigas PM → håller med / reviderar / kvarstår med motivering
4. **Fas 4 – Omröstning & beslut:** Strukturerad omröstning per vägval, majoritetsbeslut + minoritetsvotum → styrelsebeslut med nästa steg

### Definition of Done för framtida körningar
- Flödet körs end-to-end på strategifrågan
- Output läsbart och användbart för en IT-ledare inom 5 minuter
- Repeterbart utan ombyggnad

---

## Om Mission Point – Klient & Domän

### Vad Mission Point är (antaganden validerade i session 1)
Managementkonsultbolag med IT-fokus, verksamt primärt i Sverige. Erbjudande inom ledarskap, transformation och/eller AI-drivet beslutsstöd riktat till IT-bolagsledare. Erbjudandet är **relationsintensivt och personberoende** i leveransen – inte en ren SaaS-produkt.

### Målgrupp
IT-chefer, CTO:er och ledare på tech-bolag (primärt mid-large segment). Köpbeteendet är relationsbaserat med lång säljcykel.

### Konkurrenslandskap (nordiskt)
- **Danmark:** Implement Consulting Group är dominant lokal aktör med djupa kundrelationer. McKinsey, Deloitte och Accenture är etablerade.
- **Norge:** Mer fragmenterad marknad, färre nischaktörer inom IT-ledarskapsrådgivning.
- **Finland:** Stark lokal konsultmarknad (Reaktor, Futurice m.fl.), introvert köpbeteende, kräver djupa lokala relationer.

---

## Nordisk Expansionsanalys – Bestående Insikter

### Marknadskarakteristik per land

| Parameter | Danmark 🇩🇰 | Norge 🇳🇴 | Finland 🇫🇮 |
|---|---|---|---|
| TAM (estimat relevanssegment) | 400–600 bolag | 350–500 bolag | 300–450 bolag |
| Betalningsvilja | Hög | Mycket hög (oljefondspremium) | Medel |
| Kulturell proximitet till Sverige | Hög | Mycket hög | Medel (språkbarriär) |
| EU-medlemskap / GDPR-paritet | ✅ Ja | ❌ Nej (EEA) | ✅ Ja |
| Digitaliseringsmognad | #1 i EU (2023) | Hög | Hög |
| Konkurrenstäthet | Hög | Låg–medel | Medel–hög |
| Operativ friktionskostnad | Låg | Låg–medel | Medel |
| Regulatorisk komplexitet | Låg (Datatilsynet ≈ IMY) | Medel (utanför EU) | Låg |

### Nyckelinsikter om förvärv i konsultbranschen
> *"Det du köper är människor. Och människor lämnar."*

- Förvärv av konsultbolag innebär stark juridisk och etisk förpliktelse mot befintlig personal (Funktionærloven i DK, Arbeidsmiljøloven i NO)
- Kulturkonvertering till förvärvarens modell är ofta lika svårt som organisk uppbyggnad – men med extra komplexitet
- Styrelsens konsensus: **organisk etablering eller strategiskt partnerskap föredras** för konsultverksamhet

### Rekommenderad entry-modell för konsultbolag i Norden
1. Identifiera 2–3 champion clients via befintliga nätverk (cross-border pilot utan fast etablering)
2. Rekrytera lokal "opener" – en senior person med nätverk, inte ett team
3. Registrera juridisk entitet när intäktsbevis finns
4. Expandera ett land i taget

### Intern beredskap – kritiska krav innan expansion
Operativa varningsflaggor som måste adresseras oavsett marknad:
- Dokumenterade leveransprocesser (skalbar utan grundare)
- Skalbar onboarding av nya konsulter/leverantörer
- Säljkapacitet utanför befintligt nätverk
- Ledningsbandbredd för parallell expansion
- CRM/pipeline-system som stödjer ny geografi

---

## Processkvalitet & Lärdomar från Session 1

### Vad som fungerade väl
- Distinkta personaprofiler skapar genuint olika perspektiv och meningsskiljaktigheter – inte konsensus-teater
- Deliberationsfasen (Fas 3) är kritisk för att synliggöra **instrumentell konvergens** vs. **övertygad konvergens** – en viktig distinktion för beslutstagare
- Neutralt överläggningsdokument (mönsterkarta) ökar beslutskvaliteten markant

### Viktiga metodnoteringar
- **Antaganden måste explicitgöras tidigt** – samtliga ledamöter angav sina antaganden om Mission Points erbjudande, vilket möjliggjorde konstruktiv jämförelse
- **Konvergens är inte alltid starkt stöd** – i session 1 var "Danmark" fem ledamöters *minst-motstånd-val*, inte ett entusiastiskt ja. Denna distinktion ska alltid lyftas i slutprotokoll.
- Minoritetsvotum (Norge-rösten) innehöll den starkaste ACV-argumentationen och bör inte ignoreras i implementeringen

### Röstutfall Session 1
- **V1 (Land):** Danmark 4–1 (Norge fick 1 röst, Finland 0)
- **V2 (Entry-strategi):** Organisk etablering 3 röster, Strategiskt partnerskap 2 röster, Förvärv 0 röster
- **V3 (Sekvens):** Sverige → Danmark → Norge → Finland vann majoriteten

---

## Juridik & Compliance – Nordisk Referens

- **EU AI Act** appliceras identiskt i Sverige, Danmark och Finland – ingen extra compliance-overhead vid expansion inom EU
- **Norge** är EEA men ej EU – merarbete kring avtal, moms och eventuell etablering tillkommer
- **Datatilsynet** (DK) har snarlik praxis som svenska IMY – låg friktionskostnad för datahantering
- **Bias-risk:** AI-modeller tränade på svenska organisationsdata kan uppvisa bias vid tillämpning i andra nordiska marknader – rollstrukturer, beslutsvägar och ledarskapskultur skiljer sig åt
