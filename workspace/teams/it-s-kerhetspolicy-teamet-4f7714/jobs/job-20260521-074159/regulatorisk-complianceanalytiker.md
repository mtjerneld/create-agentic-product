# Regulatorisk Complianceanalytiker

# Regulatorisk Kartläggning & Granskningsbaseline
## Hemsö Fastighets AB – IT-policy v4.0

**Dokument:** Normativ granskningsbas  
**Utfärdat av:** Regulatorisk Complianceanalytiker  
**Datum:** 2025  
**Status:** Fastställd baseline för gap-analys

---

## 1. Organisatorisk kontextualisering

### Antaganden om Hemsö Fastighets AB
Hemsö Fastighets AB är ett av Sveriges största fastighetsbolag med fokus på samhällsfastigheter (skolor, vård, rättsväsende, försvar). Följande antaganden ligger till grund för regulatorisk klassificering:

- **Ägarstruktur:** Delvis statligt ägd (Tredje AP-fonden är stor ägare) — påverkar krav på transparens och intern styrning
- **Verksamhetskritikalitet:** Hyresgäster inkluderar offentlig sektor (försvaret, domstolar, sjukhus) — potentiell kritisk infrastruktur-koppling
- **IT-profil:** Outsourcad drift, Microsoft-centrerad miljö, molntjänster sannolikt aktiva
- **Personalstyrka:** Mellanstor organisation (~200–500 anställda baserat på publik information)
- **Geografisk räckvidd:** Sverige, troligen med internationella fastighetsinnehav

> ⚠️ **Kritiskt antagande:** Hemsö klassificeras preliminärt som en **viktig verksamhet** under NIS2 (kategori: fastighetsförvaltning med samhällskritisk hyresgästbas), vilket triggar ett betydande antal NIS2-krav. Om Hemsö levererar IT-tjänster till försvarssektorn kan klassificering som **väsentlig verksamhet** vara aktuell.

---

## 2. Tillämpliga regulatoriska ramverk

### 2.1 Ramverksöversikt

| Ramverk | Status | Tillämpningsnivå | Tvingande? |
|---|---|---|---|
| GDPR (EU 2016/679) | I kraft sedan 2018 | Hög – behandling av hyresgäst-, personal- och leverantörsdata | ✅ Ja |
| NIS2-direktivet (EU 2022/2555) | Implementerat i SE via lag (2024:491) | Medel-Hög – beroende på klassificering | ✅ Ja |
| DORA (EU 2022/2554) | I kraft jan 2025 | Låg – ej finansiell aktör, men leverantörskedjor kan beröras | ⚠️ Indirekt |
| MSB:s föreskrifter (MSBFS 2020:6, 2023:1) | I kraft | Hög – informationssäkerhet för organisationer av allmänt intresse | ✅ Ja |
| ISO/IEC 27001:2022 | Frivillig standard | Hög – defacto-krav vid upphandling av samhällsfastigheter | 🔵 Best practice |
| ISO/IEC 27002:2022 | Frivillig standard | Hög – kontrollkatalog för praktisk implementation | 🔵 Best practice |
| Dataskyddslagen (2018:218) | I kraft | Hög – kompletterar GDPR i svensk kontext | ✅ Ja |
| Säkerhetsskyddslagen (2018:585) | I kraft | Medel – om Hemsö hanterar säkerhetsskyddsklassad information | ⚠️ Villkorlig |
| PBL + Offentlighets- och sekretesslagen | I kraft | Låg-Medel | ✅ Delvis |

---

## 3. Detaljerad regulatorisk normkatalog

### 3.1 GDPR – EU 2016/679

Hemsö behandlar personuppgifter i flera kategorier: hyresgäster, anställda, leverantörskontakter, besökare. Följande artiklar utgör direkt normativa krav för IT-policyn:

| Artikel | Krav | Relevans för IT-policy |
|---|---|---|
| Art. 5 | Principerna för behandling (laglighet, ändamålsbegränsning, dataminimering, korrekthet, lagrings­begränsning, integritet & konfidentialitet) | Direkt – styr hur IT-system hanterar data |
| Art. 25 | Inbyggt dataskydd och dataskydd som standard (Privacy by Design/Default) | Direkt – krav på systemdesign och upphandling |
| Art. 28 | Krav på personuppgiftsbiträdesavtal (DPA) | Direkt – omnämns i policyn, kravnivån otillräcklig |
| Art. 32 | Lämpliga tekniska och organisatoriska säkerhetsåtgärder | Direkt – kryptering, pseudonymisering, kontinuitetstestning |
| Art. 33 | Anmälan av personuppgiftsincidenter till IMY inom 72 timmar | Saknas helt i policyn |
| Art. 34 | Underrättelse till registrerade vid högriskincidenter | Saknas helt i policyn |
| Art. 35 | Konsekvensbedömning (DPIA) för högriskbehandling | Saknas i policyn |
| Art. 37–39 | Dataskyddsombud (DPO) – krav vid storskalig behandling | Saknas i policyn |

**Normativt krav:** IT-policyn måste adressera Art. 32, 33, 34 och 35 explicit eller säkerställa att underliggande riktlinjer täcker dessa med tydlig hänvisning.

---

### 3.2 NIS2 – Lag (2024:491) om cybersäkerhet

NIS2 är den mest transformativa lagstiftningen för Hemsö sedan GDPR. Lagen trädde i kraft i Sverige 1 januari 2025.

#### Klassificeringsanalys

| Kriterium | Bedömning |
|---|---|
| Sektor | Fastigheter – ej explicit listad i NIS2 bilaga I eller II |
| Indirekt koppling | Levererar infrastruktur till offentlig sektor (hälso- och sjukvård, försvar, rättsväsende) |
| Storlekskriterie | Medelstort/stort företag – troligen >250 anst. eller >50M EUR omsättning |
| **Slutsats** | Hemsö faller troligen **inte** under NIS2 som direkt reglerad entitet, men kan påverkas via leverantörskedja om hyresgäster är NIS2-skyldiga |

> ⚠️ **Viktigt förbehåll:** Om Hemsö äger och driftar IT-infrastruktur som nyttjas av NIS2-skyldiga hyresgäster (t.ex. regionsjukhus, kriminalvård), kan Hemsö klassas som **kritisk leverantör** och träffas av Art. 21 krav via hyresgästernas riskhanteringsåtgärder.

#### Ändå tillämpliga NIS2-krav (god sed / indirekt krav):

| NIS2-artikel | Krav | Gap i nuvarande policy |
|---|---|---|
| Art. 21.2(a) | Riskanalys och informationssäkerhetspolicyer | Otillräcklig – policy saknar riskmetodik |
| Art. 21.2(b) | Incidenthantering | **Helt saknas** |
| Art. 21.2(c) | Kontinuitet, backup, katastrofåterställning | Omnämns ej |
| Art. 21.2(d) | Supply chain security | Omnämns ej explicit |
| Art. 21.2(e) | Säkerhet i nätverk och system | Ytlig – antivirus/brandvägg nämns men inga djupare krav |
| Art. 21.2(f) | Säkerhetsutvärdering och riskhantering vid anskaffning | Saknas |
| Art. 21.2(g) | Cyberhygien och utbildning | Omnämns svagt |
| Art. 21.2(h) | Kryptografi och kryptering | **Helt saknas** |
| Art. 21.2(i) | HR-säkerhet, access management | Omnämns inte |
| Art. 21.2(j) | MFA och säker kommunikation | **Helt saknas** |
| Art. 23 | Incidentrapportering (till NCSC/MSB) | **Helt saknas** |

---

### 3.3 MSB:s föreskrifter

#### MSBFS 2023:1 – Föreskrifter om informationssäkerhet för statliga myndigheter
> **Direkt tillämpbarhet:** Låg om Hemsö inte klassas som myndighet. Men som samhällsviktig aktör med statlig ägare är detta normgivande.

#### MSBFS 2020:6 – Föreskrifter och allmänna råd om informationssäkerhet
Tillämplig som best-practice-standard och potentiellt tvingande via avtal med statliga hyresgäster.

| Krav | Nuvarande status i policy |
|---|---|
| Ledningens ansvar för informationssäkerhet | Partiellt täckt – men ej strukturerat |
| Systematiskt informationssäkerhetsarbete (PDCA) | Saknas |
| Klassificering av information | **Saknas helt** |
| Riskhanteringsprocess | Saknas |
| Kontinuitetsplanering | Saknas |
| Incidenthantering | Saknas |
| Uppföljning och internrevision | Minimalt omnämnt |

---

### 3.4 DORA – EU 2022/2554

**Direkt tillämpbarhet:** Låg – DORA reglerar finansiella enheter (banker, försäkringsbolag, kapitalförvaltare m.fl.).

**Indirekt tillämpbarhet:** Hemsö kan påverkas om:
- Tredje AP-fonden ställer DORA-inspirerade krav på portföljbolag
- Hemsö anlitar IT-leverantörer som är DORA-reglerade och som vidarebefordrar krav

> **Slutsats:** DORA ingår inte i den primära granskningsbasen men dess principer kring **tre
