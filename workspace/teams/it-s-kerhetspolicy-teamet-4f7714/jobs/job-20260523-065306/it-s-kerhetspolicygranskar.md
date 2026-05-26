# IT-säkerhetspolicygranskar

# Teknisk & Strukturell Policygranskning
## MissionPoint AB — IT- och Informationssäkerhetspolicy v1.0

**Roll:** IT-säkerhetspolicygranskar
**Fas:** Teknisk & strukturell policygranskning
**Datum:** 2026-02-27
**Underlag:** Policy v1.0, Regulatorisk kartläggning (Complianceanalytiker), ISO/IEC-analys (Standardspecialist)

---

## 1. Granskningens syfte och metod

Denna granskning tar vid där den regulatoriska kartläggningen och ISO-analysen slutar. Fokus är det som en IT-chef faktiskt behöver för att *implementera* policyn: är den tekniskt korrekt, strukturellt komplett, tydlig i ansvarsfördelning och faktiskt genomförbar i en konsultverksamhet av MissionPoints typ?

Granskningen är organiserad i fem block:

1. Strukturell täckning — vad saknas helt
2. Teknisk precision — vad är otydligt, felaktigt eller ogenomförbart
3. Ansvarsfördelning — vem gör vad
4. Implementerbarhet — kan en medarbetare faktiskt följa policyn
5. Konsoliderad bristmatris med prioritering

**Metodantaganden:**
- Policyn granskas som *ensamt styrdokument* — inga kompletterande riktlinjer eller instruktioner antas finnas (i linje med Standardspecialistens Antagande 3)
- MissionPoint behandlas som ett konsultbolag med hybridarbete, aktiv AI-användning och outsourcad IT-drift
- Säkerhetsskyddslagen lämnas utanför denna granskning men flaggas som öppen fråga som måste stängas av MissionPoint separat (se Complianceanalytikerns Antagande A3)

---

## 2. Strukturell täckning — Vad saknas helt

### 2.1 Avsnitt som är obligatoriska men saknas

Nedanstående avsnitt är **helt frånvarande** i policyn. Varje avsnitt bedöms mot om det är ett krav (regulatoriskt eller standardbaserat) eller ett starkt rekommenderat element.

| # | Saknat avsnitt | Krav-grund | Prioritet |
|---|---|---|---|
| S1 | **Riskhanteringsprocess** — hur risker identifieras, värderas och beslutas | ISO 27001 kl. 6.1, 27005 | 🔴 Kritisk |
| S2 | **Incidenthantering — komplett process** med roller, eskalering, tidsgränser och NIS2-rapportering | NIS2 art. 23, ISO 27001 A.5.24–A.5.28 | 🔴 Kritisk |
| S3 | **Tillgångshantering / inventarium** — vilka system, enheter och informationstillgångar existerar | ISO 27001 A.5.9–A.5.10 | 🔴 Kritisk |
| S4 | **Åtkomstkontroll och IAM** — behörighetsprinciper, minsta privilegium, offboarding | ISO 27001 A.5.15–A.5.18 | 🔴 Kritisk |
| S5 | **Business Continuity / Disaster Recovery** — kontinuitetsplan och återställning | ISO 27001 kl. 8.8, NIS2 art. 21 | 🟠 Hög |
| S6 | **Krypterings- och nyckelhanteringspolicy** | ISO 27001 A.8.24, GDPR art. 32 | 🟠 Hög |
| S7 | **Säkerhetsmedvetenhet och utbildning** — obligatorisk utbildning, frekvens, uppföljning | ISO 27001 A.6.3 | 🟠 Hög |
| S8 | **Fysisk säkerhet** — kontor, klientutrustning, besökare | ISO 27001 A.7 | 🟡 Medium |
| S9 | **Sårbarhantering och patchning** — process för att hantera tekniska sårbarheter | ISO 27001 A.8.8 | 🟠 Hög |
| S10 | **Säker systemutveckling och testning** — relevant om MissionPoint levererar IT-lösningar | ISO 27001 A.8.25–A.8.31 | 🟡 Medium |
| S11 | **Loggning och övervakning** — vad loggas, hur länge, vem ansvarar | ISO 27001 A.8.15–A.8.16 | 🟠 Hög |
| S12 | **Separata underliggande styrdokument** — policyn refererar aldrig till riktlinjer eller instruktioner; hela hierarkin saknas | ISO 27001 kl. 5.2, 7.5 | 🟠 Hög |

**Observation:** Policyn saknar en komplett tillgångshierarki (se kunskapsbas §4 — referensstrukturen). Det finns ingen styrelsenivåpolicy separerad från operativa riktlinjer. Allt är sammanpressat i ett enda dokument utan referensdokument, vilket gör det omöjligt att underhålla och delegera ansvar på rätt nivå.

---

### 2.2 Avsnitt som är påbörjade men ofullständiga

| # | Avsnitt i policyn | Vad som saknas |
|---|---|---|
| T1 | **§7 Informationsklassning** — Listar informationstyper men har ingen klassificeringsskala | Inga nivåer definierade (t.ex. Öppen / Intern / Konfidentiell / Hemlig), ingen märkningsinstruktion, ingen hanteringsregel per nivå |
| T2 | **§9 Incidenthantering** — Nämner incidenttyper men har ingen process | Ingen rapporteringskedja, inga tidsgränser, ingen kontaktpunkt, ingen åtgärdsplan, ingen övningsfrekvens |
| T3 | **§11 Leverantörshantering** — Nämner säkerhetsbedömning men definierar inte vad den innebär | Inga minimikrav på leverantörer, inga kontraktuella klausuler, ingen revisionsrätt, ingen kontinuerlig uppföljning |
| T4 | **§6 Informationssäkerhetsprinciper** — Nämner riskbaserat arbete men operationaliserar det inte | Ingen riskprocess, ingen riskacceptansnivå, inga ägarroller per risk |
| T5 | **§12 Ansvar** — Extremt förenklad ansvarsfördelning | Se avsnitt 4 nedan |

---

## 3. Teknisk precision — Specifika tekniska brister

### 3.1 Åtkomstkontroll (§ saknas)

Policyn nämner att "information ska endast delas med behöriga personer" (§7) men definierar inte vad *behörighet* innebär, hur det beslutas, vem som godkänner, eller hur det återkallas. I en konsultorganisation med externa uppdragstagare och kundåtkomst är detta en akut brist.

**Specifika tekniska krav som saknas:**
- Minsta privilegiums-princip (least privilege) definierad
- MFA-krav — nämns inte alls i policyn
- Behörighetsgenomgång (access review) — frekvens och ansvarig
- Offboarding-process — vad händer med åtkomst när konsult avslutar uppdrag
- Separering av privilegierade konton (admin-konton vs. dagliga konton)

**Antagande:** Det är sannolikt att MissionPoint använder Microsoft 365 (Copilot nämns explicit i §8). Utan tydliga MFA- och IAM-krav är organisationen exponerad mot den APT29-metod som Standardspecialisten identifierar — credential harvesting mot M365.

### 3.2 Distansarbete (§10)

Avsnittet är korrekt i intention men tekniskt underspecificerat:

| Krav i §10 | Teknisk brist |
|---|---|
| "Företagsdator ska användas" | Definieras inte — BYOD-policy saknas, MDM-krav nämns inte |
| "Undvika öppna Wi-Fi-nätverk" | VPN-krav nämns inte — hur säkras trafiken om inte VPN specificeras? |
| "Information skyddas mot obehörig åtkomst" | Skärmlås, kryptering av lokal lagring (BitLocker/FileVault) nämns inte |
| Offentliga datorer ska undvikas | Rimligt, men ej kontrollerbart utan MDM/endpoint-hantering |

### 3.3 AI-verktyg (§8)

AI-avsnittet är det tekniskt mest genomarbetade i policyn och är ett styrkeområde relativt branschnormen. Följande preciseringar skulle dock stärka det:

| Befintlig regel | Teknisk brist / förtydligande behov |
|---|---|
| "Tillåtet om anonymiserad" | Vem avgör om information är tillräckligt anonymiserad? Ingen beslutspunkt definierad |
| Namngivna verktyg (ChatGPT, Copilot, Claude) | Statisk lista — förlegad nästa revision. Rekommendera principbaserad regel + separat godkännandelista |
| "Avtal och kundkrav styr" | Vilka kundkrav? Var dokumenteras dessa? Ingen process för att inhämta och lagra kundkrav kring AI |
| Inga regler för lokal AI (on-premise modeller) | Relevant om MissionPoint eller kund driftar egna modeller |
| Ingen distinktion enterprise vs. consumer-versioner | ChatGPT Free vs. ChatGPT Enterprise har fundamentalt olika datapolicy — policyn gör ingen skillnad |

**Rekommendation:** Splitta §8 i (a) principregler som är versionsstabila och (b) en separat, levande lista över godkända verktyg med versionsdatum.

### 3.4 Leverantörshantering (§11)

Tekniskt genomförbar men saknar kontrollerbara minimikrav:

| Befintlig text | Vad saknas |
|---|---|
| "Rimlig säkerhetsbedömning" | Vad är rimlig? Checklista, SOC2-certifikat, ISO 27
