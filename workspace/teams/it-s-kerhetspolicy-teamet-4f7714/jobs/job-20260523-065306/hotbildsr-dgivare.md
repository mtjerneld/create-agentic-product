# Hotbildsrådgivare

# Hotbildsbedömning: MissionPoints IT- och Informationssäkerhetspolicy v1.0
## Relevans mot aktuell hotintelligens — NCSC-SE, ENISA & sektorspecifika hotaktörer

**Roll:** Hotbildsrådgivare
**Fas:** Teknisk & strukturell policygranskning
**Datum:** 2026 (löpande hotbild)
**Referensdokument:** MissionPoint AB, IT- och Informationssäkerhetspolicy v1.0

---

## 1. Metodansats och antaganden

### Hotbildens relevans för MissionPoint

MissionPoint är en rådgivande konsultorganisation. Det innebär att hotbilden är **dubbel**:

1. **Direkt exponering** — MissionPoint som organisation är ett mål i sig: konsultfirmor med tillgång till klientdata inom säkerhetsanalyser, systemåtkomst och säkerhetskänslig information är attraktiva mål.
2. **Indirekt exponering** — MissionPoint är en potentiell angreppsvektor mot sina kunder. Om MissionPoint hanterar systemåtkomst till kunders miljöer är MissionPoint ett *supply chain-mål* — en bakdörr in i reglerade och potentiellt säkerhetskänsliga kundorganisationer.

> **Antagande B1:** Policy §7 nämner explicit "säkerhetsanalyser", "systemåtkomst" och "säkerhetskänslig information". Det innebär att MissionPoint med hög sannolikhet hanterar information som är av underrättelseintresse för statssponsrade aktörer. Hotbilden är därmed inte begränsad till opportunistiska kriminella.

> **Antagande B2:** MissionPoints klientbas inkluderar sannolikt organisationer i reglerade sektorer (finansiell, offentlig, kritisk infrastruktur) baserat på bolagets profil som säkerhetsrådgivare. Detta förstärker exponeringen som supply chain-mål.

---

## 2. Hotaktörskartläggning mot MissionPoints specifika profil

### 2.1 Statssponsrade aktörer — Direkt relevansbedömning

| Hotaktör | Ursprung | Relevans för MissionPoint | Metod | Adresseras i policy? |
|---|---|---|---|---|
| **APT29 / Cozy Bear** | Ryssland (SVR) | **KRITISK** — Specialiserad på konsult- och rådgivningsfirmor med M365-åtkomst; supply chain mot slutkunder | Supply chain-intrång, Microsoft 365-kompromittering, credential theft via OAuth | ❌ Inte adresserat |
| **APT28 / Fancy Bear** | Ryssland (GRU) | **HÖG** — Aktiv mot svenska organisationer; spearphishing mot individer med tillgång till känslig kunddata | Spearphishing, credential harvesting, riktade mejlattacker | ❌ Inte adresserat |
| **Lazarus Group** | Nordkorea | **MEDIUM** — Opportunistisk ransomware och datatjuvnad; konsultfirmor med värdefull kunddata är mål | Ransomware, finansiellt motiverad datastöld | ❌ Inte adresserat |

**Kritisk observation:** APT29 har dokumenterad historia av att kompromittera konsult- och IT-tjänsteföretag specifikt för att nå slutkunderna. MissionPoints roll som rådgivare med "systemåtkomst" till kundmiljöer (§7) gör denna hotvektor direkt tillämplig. Policyn innehåller **noll åtgärder** mot denna hottyp.

### 2.2 Kriminella hotaktörer — Direkt relevansbedömning

| Hottyp | Relevans | Angreppsvektor mot MissionPoint | Adresseras i policy? |
|---|---|---|---|
| **Ransomware** (LockBit 3.0, Black Basta, Cl0p) | **KRITISK** | Konsultfirmor med kunddata = högt lösensummevärde; dubbel utpressning (kryptering + datapublicering) vanlig taktik | ⚠️ Delvis — Incidenthantering nämns men utan ransomware-specifika åtgärder |
| **Business Email Compromise (BEC)** | **HÖG** | Rådgivare med direktkontakt mot kundernas ledning och ekonomifunktion; MissionPoints e-postkonton är attraktiva för BEC-attacker mot kunder | ❌ Inte adresserat |
| **Credential stuffing / kontoövertagning** | **HÖG** | Distansarbete + molntjänster + AI-verktyg = stor attackyta för kompromitterade inloggningsuppgifter | ❌ Inte adresserat |
| **Phishing mot AI-verktyg** | **MEDIUM** | Policy §8 tillåter ChatGPT, Copilot, Claude — dessa är nya angreppsytor (prompt injection, dataläckage via API) | ⚠️ Delvis — AI-regler finns men täcker inte säkerhetsrisker i AI-verktygen själva |

---

## 3. Hotspecifik analys: Vad saknas i policyn?

### 3.1 Supply chain-hotet — Det mest kritiska gapet

**Hotbild:** ENISA Threat Landscape 2024 rankar supply chain-attacker som en av de snabbast växande hotvektorerna. APT29s attack mot SolarWinds (2020) och MOVEit-kampanjen (Cl0p, 2023) visar att konsult- och IT-tjänsteföretag är primära mål *just för att de är inkörsportar*.

**Policyläget:**
- §11 (Leverantörshantering) adresserar MissionPoints egna leverantörer — men adresserar **inte** att MissionPoint självt är en leverantörsrisk för sina kunder.
- §4 erkänner att MissionPoint har "systemåtkomst" till kundmiljöer, men utan säkerhetskrav kopplade till denna åtkomst.
- Ingen policy för hantering av privilegierad åtkomst (PAM), inga krav på MFA för systemåtkomst, inga procedurer för åtkomstborttagning vid uppdragsavslut.

**Konkret riskscenarion:**
> En MissionPoint-konsult med aktiv systemåtkomst till tre kundmiljöer har sin laptop kompromitterad via spearphishing. Angriparen (APT29) använder lagrade sessionstoken och VPN-profiler för att röra sig lateralt in i samtliga tre kundmiljöer. MissionPoints policy saknar krav på sessionshantering, MFA-enforcement eller nätverkssegmentering.

**Riskpoäng: Sannolikhet 4 × Konsekvens 5 = 20 — KRITISK**

---

### 3.2 Ransomware-beredskap — Strukturellt otillräcklig

**Hotbild:** Ransomware är den dominerande hottypen mot europeiska organisationer (ENISA 2024, fjärde året i rad). Konsultfirmor med kunddata är attraktiva mål för dubbel utpressning: kryptering av egna system + hot om publicering av kundkontrakt, säkerhetsanalyser och personuppgifter.

**Policyläget:**
- §9 omnämner incidenthantering men saknar ransomware-specifika rutiner.
- Ingen nämning av: backup-strategi, offline-kopior, återställningstider (RTO/RPO), betalningspolicy, kommunikationsplan vid datapubliceringshot.
- Ingen referens till BC/DR (Business Continuity / Disaster Recovery).

**Konkret riskscenarion:**
> Black Basta krypterar MissionPoints filserver och hotar publicera kundernas säkerhetsanalyser om inte lösen betalas inom 72 timmar. MissionPoint har ingen dokumenterad policy för: Ska lösen betalas? Vem beslutar? Hur kommunicerar vi med kunder? Var finns backup? Kan vi återställa inom acceptable tid?

**Riskpoäng: Sannolikhet 4 × Konsekvens 5 = 20 — KRITISK**

---

### 3.3 Microsoft 365 och molntjänst-exponering — Specifik sårbarhet

**Hotbild:** NCSC-SE och Microsoft MSTIC har dokumenterat att APT29 systematiskt angriper M365-miljöer via:
- OAuth app-registreringar (illicit consent grants)
- Kompromitterade servicekonton
- Missbruk av Microsoft Graph API
- Angrepp mot MFA (SIM-swapping, MFA fatigue-attacker)

**Policyläget:**
- Policyn nämner Microsoft Copilot (§8) vilket indikerar M365-miljö.
- Ingen policy för: Villkorlig åtkomst (Conditional Access), MFA-krav, admin-kontoskydd, appregistreringsstyrning.
- §10 (Distansarbete) kräver "företagsdator" men specificerar inte tekniska kontroller (t.ex. krav på MFA, EDR, krypterad disk).

**Riskpoäng: Sannolikhet 4 × Konsekvens 4 = 16 — KRITISK**

---

### 3.4 Business Email Compromise (BEC) — Konsultspecifik sårbarhet

**Hotbild:** BEC-attacker mot konsultfirmor har en specifik mekanism: angriparen kompromitterar konsultens e-postkonto och kommunicerar sedan med *kunden* i konsultens namn — för att ändra betalningsinformation, extrahera känslig data eller plantera skadlig kod i kundmiljön.

**Policyläget:**
- Inget omnämnande av BEC som hottyp.
- Inga krav på e-postsäkerhet (SPF/DKIM/DMARC).
- Ingen procedur för verifiering av identitet vid kritiska instruktioner.
- Ingen medvetandehöjande utbildning nämnd i relation till social engineering.

**Riskpoäng: Sannolikhet 3 × Konsekvens 4 = 12 — HÖG**

---

### 3.5 AI-verktyg som angreppsyta — Nytt och underadresserat hot

**Hotbild:** ENISA Threat Landscape 2024 identifierar AI-system som en växande angreppsyta:
