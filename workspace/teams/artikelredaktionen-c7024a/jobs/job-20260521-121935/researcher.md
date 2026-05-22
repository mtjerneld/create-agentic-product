# Researcher

# 📚 Forskningsunderlag: AI-agenter – historik och distinktion mot skript

**Producerat av:** Researcher
**För:** Redaktör & Skribent
**Projekt:** Artikel om AI-agenter (~1 A4)

---

## 1. Definitioner – vad är en AI-agent?

En **AI-agent** är ett system som:
- **Uppfattar** sin omgivning (via input: text, data, sensorer, API-svar)
- **Resonerar** och fattar beslut baserat på mål
- **Agerar** för att förändra sin omgivning (via output: kommandon, text, verktygsanrop)
- **Itererar** – utvärderar resultatet och anpassar nästa steg

Klassisk akademisk definition (Russell & Norvig, *Artificial Intelligence: A Modern Approach*, 1995/2021):
> *"An agent is anything that can be perceived its environment through sensors and acts upon that environment through actuators."*

Nyckelegenskaper enligt forskningen: **autonomi, reaktivitet, pro-aktivitet och social förmåga** (Wooldridge & Jennings, 1995 – fortfarande standardreferens).

---

## 2. Historisk tidslinje

### 🔹 1950-talet – Teoretiska grunder
- Alan Turing (1950): *Computing Machinery and Intelligence* – lade grunden för tanken om maskiner som kan "tänka"
- John McCarthy (1956): myntade termen "Artificiell intelligens" vid Dartmouth-konferensen

### 🔹 1960–70-tal – Tidiga reaktiva system
- **ELIZA** (Joseph Weizenbaum, MIT, 1966): Tidigt konversationsprogram – *inte* en agent i modern mening, utan ett mönstermatchningsskript
- **STRIPS** (Fikes & Nilsson, 1971): Tidig planeringsalgoritm – föregångare till målstyrd agentkognition

### 🔹 1980-tal – Expertsystem
- System som **MYCIN** (Stanford) och **XCON** (DEC): regelbaserade system som simulerade expertbeslut
- Begränsning: Hårdkodade regler, ingen adaptivitet – mer avancerade skript än sanna agenter

### 🔹 1990-tal – Multi-agent-system (MAS) och BDI-agenter
- **BDI-modellen** (Belief-Desire-Intention, Rao & Georgeff, 1995): Formaliserade hur agenter håller interna representationer av världen och planerar utifrån mål
- Framväxt av **multi-agent-forskning** (MIT, ETH, Carnegie Mellon)
- **RoboCup** (1997): Autonoma agenter i realtidsmiljö – demonstrerade adaptivt beslutsfattande

### 🔹 2000–2010-tal – Reinforcement Learning & speldomäner
- **AlphaGo** (DeepMind, 2016): Agent tränad via reinforcement learning besegrade världsmästare i Go
- Agenter börjar hantera komplexa, dynamiska miljöer utan explicit programmering av varje steg

### 🔹 2020-talet – LLM-baserade agenter (nutid)
- **GPT-3/4** (OpenAI, 2020/2023): Stora språkmodeller ger agenter förmågan att resonera i naturligt språk
- **ReAct-ramverket** (Yao et al., 2022, Princeton/Google): Kombinerar *reasoning* och *acting* i LLM-agenter – ett genombrott för uppgiftsorienterade agenter
- **AutoGPT** (2023): Tidig populär implementation av självstyrande LLM-agent med verktygsanrop
- **LangChain, CrewAI, Microsoft AutoGen** (2023–2024): Ramverk för att bygga agentflöden och multi-agent-system
- **Anthropic Claude, OpenAI Assistants API, Google Gemini** (2024–): Inbyggd agentstöd i kommersiella plattformar

---

## 3. Agent vs. Skript – de kritiska skillnaderna

| Egenskap | Skript | AI-agent |
|---|---|---|
| **Styrning** | Fördefinierade steg, exekveras i ordning | Mål-styrd, bestämmer själv nästa steg |
| **Flexibilitet** | Hanterar bara förutsedda situationer | Hanterar oväntade situationer via resonemang |
| **Beslutsfattande** | Inga beslut – följer instruktioner | Fattar beslut baserat på kontext och mål |
| **Adaptivitet** | Statisk – ändras inte under körning | Dynamisk – anpassar beteende utifrån feedback |
| **Feltolerans** | Kraschar eller ger fel vid oväntad input | Kan omformulera strategi vid hinder |
| **Verktygsanvändning** | Anropar specificerade funktioner | Väljer *vilka* verktyg som behövs och *när* |
| **Exempel** | Bash-skript, makro, RPA-bot | AutoGPT, LangChain-agent, Claude-agent |

### Konkret illustration:
- **Skript:** "Om fil finns → läs den → skicka e-post" – varje steg hårdkodat
- **Agent:** "Se till att rapporten skickas" → agenten avgör själv att den måste leta efter filen, kontrollera att den är korrekt, formulera e-postmeddelandet och hantera eventuella fel längs vägen

---

## 4. Nyckelbegrepp att använda i artikeln

- **Autonomi** – agenten agerar utan konstant mänsklig styrning
- **Situationsmedvetenhet** – uppfattar och tolkar sin kontext
- **Målstyrning** – arbetar mot ett mål, inte ett skript
- **Verktygsanvändning (Tool use)** – kan anropa externa resurser dynamiskt
- **Agentic loop** – perception → resonemang → handling → utvärdering → repeat
- **Multi-agent-system** – flera agenter samarbetar, specialiserar sig, delegerar

---

## 5. Rekommenderade vinklar för artikeln

1. **"Från ELIZA till AutoGPT"** – dramatisk historisk båge som konkretiserar utvecklingen
2. **"Skriptet vet vad det ska göra – agenten vet varför"** – pedagogisk distinktion
3. **Relevansen nu:** Agenter börjar rulla ut i verkliga produkter (kundservice, kodning, analys) – detta är inte framtidsmusik

---

## 6. Källförteckning (rekommenderade primär-/sekundärkällor)

| Källa | Typ | Relevans |
|---|---|---|
| Russell & Norvig (2021), *AI: A Modern Approach* | Lärobok | Grunddefinitioner |
| Wooldridge & Jennings (1995), *Intelligent Agents* | Akademisk artikel | Agentegenskaper |
| Yao et al. (2022), *ReAct: Synergizing Reasoning and Acting in LLMs* | Forskningspaper | Modern LLM-agent-arkitektur |
| Turing (1950), *Computing Machinery and Intelligence* | Primärkälla | Historisk grund |
| OpenAI (2023), *Assistants API documentation* | Teknisk dok. | Nutida implementation |
| Weizenbaum (1966), *ELIZA* | Primärkälla | Kontrast mot riktiga agenter |

---

## ✅ Sammanfattning för skribenten

> AI-agenter har rötter i 1950-talets AI-forskning men har genomgått ett paradigmskifte med LLM:er under 2020-talet. Den centrala distinktionen mot skript handlar om **intentionalitet och adaptivitet**: skript exekverar, agenter resonerar. Artikeln bör ha en historisk båge från ELIZA → expertsystem → ReAct/AutoGPT, och landa i varför skillnaden mot skript är principiellt viktig – inte bara teknisk.

---

*Underlaget är klart för Skribent och Redaktör. 🟢*
