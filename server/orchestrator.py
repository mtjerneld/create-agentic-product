"""Team-orkestrering: föreslå ett agent-team och kör beständiga team mot jobb.

Ett team skapas en gång och sparas. Det kan sedan köra flera jobb över tid.
Mellan jobb bär teamet med sig en levande kunskapsbas (knowledge.md) som
project-lead uppdaterar efter varje jobb.
"""

import os
import re
import asyncio
from pathlib import Path

from anthropic import AsyncAnthropic

import store

ROOT = Path(__file__).resolve().parent.parent

BRIEF_FIELDS = [
    ("product", "Produkt"),
    ("audience", "Målgrupp"),
    ("markets", "Marknader"),
    ("ambition", "Ambition"),
    ("budget", "Budget"),
    ("timeline", "Tidplan"),
    ("existing", "Befintligt material"),
]


def _load_env():
    """Läser in .env från projektroten utan extra beroenden."""
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


_load_env()

MODEL = os.environ.get("TEAM_MODEL", "claude-sonnet-4-6")


def get_client() -> AsyncAnthropic:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY saknas. Skapa en .env-fil i projektroten "
            "(kopiera .env.example) och lägg in din Anthropic-nyckel."
        )
    return AsyncAnthropic(api_key=key)


def format_brief(brief: dict) -> str:
    lines = []
    for key, label in BRIEF_FIELDS:
        val = (brief.get(key) or "").strip() or "—"
        lines.append(f"{label}: {val}")
    return "\n".join(lines)


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return s or "agent"


# --- Steg 1: föreslå team -------------------------------------------------

TEAM_TOOL = {
    "name": "submit_team",
    "description": "Lämna in det föreslagna agent-teamet och fasplanen.",
    "input_schema": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Ett kort, beskrivande namn på teamet, t.ex. "
                               "'LinkedIn-teamet' eller 'Lanseringsteam Norden'.",
            },
            "rationale": {
                "type": "string",
                "description": "2-4 meningar på svenska om varför teamet ser ut som det gör.",
            },
            "phases": {
                "type": "array",
                "description": "2-4 arbetsfaser i ordning.",
                "items": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer", "description": "Fasnummer, börjar på 1."},
                        "name": {"type": "string"},
                        "goal": {"type": "string", "description": "Vad fasen ska leverera."},
                    },
                    "required": ["number", "name", "goal"],
                },
            },
            "agents": {
                "type": "array",
                "description": "5-9 agenter totalt, inklusive en project-lead.",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "kebab-case id, t.ex. competitor-analyst."},
                        "title": {"type": "string", "description": "Läsbar titel på svenska."},
                        "emoji": {"type": "string", "description": "En passande emoji."},
                        "role": {"type": "string", "description": "1-3 meningar om agentens ansvar."},
                        "tools": {"type": "string", "description": "Kort lista av verktyg/"
                                  "kapaciteter agenten använder, t.ex. 'konkurrentanalys, webbsök'."},
                        "phase": {"type": "integer", "description": "Fasnummer. 0 = project-lead/koordinator."},
                        "why": {"type": "string", "description": "Varför just denna agent behövs här."},
                    },
                    "required": ["name", "title", "emoji", "role", "tools", "phase", "why"],
                },
            },
        },
        "required": ["name", "rationale", "phases", "agents"],
    },
}

PROPOSE_SYSTEM = """Du är project-lead för ett ramverk som sätter ihop \
AI-drivna kreativa team. Ett team skapas en gång och återanvänds sedan för \
flera uppgifter över tid — det ska alltså vara ett bestående, kompetent team, \
inte en engångsgrupp.

Givet en projektbrief: sätt ihop det ideala teamet av specialiserade agenter.
Var kreativ och tänk bortom standardrollerna — lägg till roller som just detta
projekt kräver (t.ex. sustainability-advisor, pricing-strategist, packaging-designer).

Regler:
- Ge teamet ett kort, beskrivande namn.
- Inkludera alltid en project-lead med phase 0 (koordinator).
- Definiera 2-4 arbetsfaser anpassade efter projektet.
- 1-3 agenter per fas, 5-9 agenter totalt.
- Skriv allt på svenska.
Använd verktyget submit_team för att lämna in resultatet."""


async def propose_team(brief: dict) -> dict:
    client = get_client()
    msg = await client.messages.create(
        model=MODEL,
        max_tokens=2400,
        system=PROPOSE_SYSTEM,
        tools=[TEAM_TOOL],
        tool_choice={"type": "tool", "name": "submit_team"},
        messages=[{"role": "user", "content": f"Projektbrief:\n\n{format_brief(brief)}"}],
    )
    team = None
    for block in msg.content:
        if block.type == "tool_use" and block.name == "submit_team":
            team = dict(block.input)
            break
    if not team:
        raise RuntimeError("Modellen returnerade inget team.")

    team.setdefault("agents", [])
    team.setdefault("phases", [])
    team.setdefault("name", "Namnlöst team")
    if not any(a.get("phase") == 0 for a in team["agents"]):
        team["agents"].insert(0, {
            "name": "project-lead",
            "title": "Project Lead",
            "emoji": "🎯",
            "role": "Koordinerar teamet, driver arbetet framåt och kvalitetssäkrar leveranser.",
            "tools": "koordinering, kvalitetssäkring",
            "phase": 0,
            "why": "Behövs alltid för att hålla ihop projektet.",
        })
    return team


# --- Steg 2: kör ett jobb -------------------------------------------------

def _digest(deliverables: list, cap: int = 2500) -> str:
    out = []
    for title, text in deliverables:
        t = text.strip()
        if len(t) > cap:
            t = t[:cap] + "\n…(förkortat)"
        out.append(f"## {title}\n{t}")
    return "\n\n".join(out)


async def _stream_agent(client, agent_id, title, emoji, system, user, emit, save=None,
                        max_tokens=2800):
    """Streamar en agents svar. `save` = (team_id, job_id, filename) eller None."""
    await emit({"type": "agent_started", "agent": agent_id, "title": title, "emoji": emoji})
    parts = []
    try:
        async with client.messages.stream(
            model=MODEL,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        ) as stream:
            async for delta in stream.text_stream:
                parts.append(delta)
                await emit({"type": "agent_delta", "agent": agent_id, "text": delta})
    except Exception as e:  # noqa: BLE001
        await emit({"type": "agent_error", "agent": agent_id, "message": str(e)})
        raise
    full = "".join(parts).strip()
    deliverable = None
    if save:
        team_id, job_id, filename = save
        store.save_deliverable(team_id, job_id, filename, f"# {title}\n\n{full}\n")
        deliverable = filename
    await emit({
        "type": "agent_done", "agent": agent_id,
        "deliverable": deliverable, "chars": len(full),
    })
    return full


def _agent_system(title, role, tools, phase_name, phase_goal) -> str:
    tools_line = f"Verktyg/kapaciteter du förväntas använda: {tools}\n" if tools else ""
    return (
        f"Du är {title}, en agent i ett bestående AI-drivet kreativt produktteam.\n"
        f"Roll: {role}\n"
        f"{tools_line}"
        f"Fas: {phase_name} — {phase_goal}\n\n"
        "Producera en konkret, högkvalitativ leverans för din roll i denna fas. "
        "Var specifik och handlingsbar — inga generiska floskler. Använd teamets "
        "kunskapsbas där den är relevant så att arbetet bygger vidare på tidigare "
        "jobb. Gör rimliga antaganden där information saknas och var tydlig med dem. "
        "Formatera som ett markdown-dokument med tydliga rubriker. Skriv på svenska."
    )


DELIVERY_SYSTEM = """Du är {title}, project-lead för teamet. Hela teamet har \
arbetat klart och du ska nu sätta ihop teamets SLUTLEVERANS.

Slutleveransen är det konkreta, färdiga resultat som uppgiften bad om — i ett \
skick som kan användas direkt. Det är inte en process-sammanfattning och inte en \
beskrivning av vad teamet gjorde, utan själva produkten.

Skriv ett välformaterat markdown-dokument:
1. Börja med en kort orientering (1-2 meningar): vad detta är.
2. Därefter SJÄLVA LEVERANSEN i fullständigt, färdigt skick — t.ex. de färdiga
   texterna/inläggen/planen ordagrant, inte sammanfattat. Konsolidera och putsa
   agenternas arbete till en sammanhållen helhet, ta bort dubbletter och
   antagandeprat.
3. Avsluta med en kort sektion '## Nästa steg & att bevaka' (några punkter).

Skriv på svenska. Var konkret och utelämna inget av det faktiska innehållet."""


KNOWLEDGE_SYSTEM = """Du är project-lead och underhåller teamets kunskapsbas — \
ett bestående dokument som teamet bär med sig mellan jobb.

Du får den nuvarande kunskapsbasen och leveranserna från ett just avslutat jobb.
Skriv en UPPDATERAD kunskapsbas i markdown som:
- Behåller och förfinar varaktig research och insikter (om produkt, målgrupp,
  marknad, varumärke, ton, juridik) som är användbar för framtida jobb.
- Lägger till nya bestående insikter från det här jobbet.
- UTELÄMNAR det som var rent jobbspecifikt (själva leveranserna, engångstexter).
- Hålls kompakt och välstrukturerat — det här är ett referensdokument, inte ett arkiv.

Svara med enbart det färdiga markdown-dokumentet, börja med rubriken '# Kunskapsbas'."""


async def _update_knowledge(client, team_id, team_name, current, deliverables, emit):
    await emit({"type": "knowledge_updating"})
    user = (
        f"TEAM: {team_name}\n\n"
        f"NUVARANDE KUNSKAPSBAS:\n{current}\n\n"
        f"LEVERANSER FRÅN DET AVSLUTADE JOBBET:\n{_digest(deliverables)}"
    )
    msg = await client.messages.create(
        model=MODEL, max_tokens=2600, system=KNOWLEDGE_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in msg.content if b.type == "text").strip()
    if text:
        store.set_knowledge(team_id, text)
    await emit({"type": "knowledge_updated"})


async def run_team(team_id: str, job_id: str, task: str, emit) -> None:
    """Kör ett sparat team mot ett jobb. Streamar händelser via `emit`."""
    client = get_client()
    team = store.get_team(team_id)
    brief_text = format_brief(team.get("brief", {}))
    knowledge = store.get_knowledge(team_id)
    attachments = store.get_attachments_text(team_id, job_id)
    task = (task or "").strip() or "Ta produkten från koncept till lansering enligt faserna."

    agents = team.get("agents", [])
    phases = sorted(
        [p for p in team.get("phases", []) if p.get("number", 0) != 0],
        key=lambda p: p.get("number", 0),
    )
    lead = next((a for a in agents if a.get("phase") == 0), None)

    await emit({"type": "run_started", "task": task, "phases": phases})

    deliverables: list = []

    def attachments_block(cap: int = 24000) -> str:
        if not attachments:
            return ""
        parts = ["BIFOGADE DOKUMENT (underlag som hör till uppgiften):"]
        for name, text in attachments.items():
            t = text.strip()
            if len(t) > cap:
                t = t[:cap] + "\n…(förkortat)"
            parts.append(f"--- {name} ---\n{t}")
        return "\n\n".join(parts) + "\n"

    def context_block():
        block = f"PROJEKTBRIEF:\n{brief_text}\n\nTEAMETS KUNSKAPSBAS:\n{knowledge}\n"
        att = attachments_block()
        if att:
            block += f"\n{att}"
        return block

    # Kickoff från project-lead
    if lead:
        await emit({"type": "phase_started", "phase": 0, "name": "Kickoff", "goal": "Sätt riktningen"})
        kickoff = await _stream_agent(
            client, "lead-kickoff",
            f"{lead.get('title', 'Project Lead')} · Kickoff", lead.get("emoji", "🎯"),
            f"Du är {lead.get('title', 'Project Lead')}, project-lead för teamet.",
            "Skriv en kort kickoff-brief (max ~300 ord) på svenska i markdown: "
            "återge målet, de viktigaste prioriteringarna, och vad varje fas måste "
            f"leverera.\n\n{context_block()}\nUPPGIFT TILL TEAMET:\n{task}",
            emit, save=(team_id, job_id, "00-kickoff.md"),
        )
        deliverables.append(("Kickoff-brief", kickoff))
        await emit({"type": "phase_done", "phase": 0})

    # Arbetsfaser
    for phase in phases:
        num = phase.get("number", 0)
        await emit({
            "type": "phase_started", "phase": num,
            "name": phase.get("name", f"Fas {num}"), "goal": phase.get("goal", ""),
        })
        prior = _digest(deliverables)
        phase_agents = [a for a in agents if a.get("phase") == num]

        async def run_one(agent):
            title = agent.get("title") or agent.get("name", "Agent")
            user = f"{context_block()}\nUPPGIFT TILL TEAMET:\n{task}\n"
            if prior:
                user += f"\nLEVERANSER HITTILLS I DETTA JOBB:\n{prior}\n"
            user += "\nLevera ditt bidrag nu."
            return await _stream_agent(
                client, agent.get("name", slugify(title)), title, agent.get("emoji", "🧩"),
                _agent_system(title, agent.get("role", ""), agent.get("tools", ""),
                              phase.get("name", ""), phase.get("goal", "")),
                user, emit, save=(team_id, job_id, f"{slugify(title)}.md"),
            )

        results = await asyncio.gather(*(run_one(a) for a in phase_agents), return_exceptions=True)
        for agent, res in zip(phase_agents, results):
            if not isinstance(res, Exception):
                deliverables.append((agent.get("title") or agent.get("name", "Agent"), res))
        await emit({"type": "phase_done", "phase": num})

    # Slutleverans från project-lead
    if lead:
        await emit({"type": "phase_started", "phase": 999, "name": "Slutleverans",
                    "goal": "Sätt ihop teamets färdiga leverans"})
        delivery = await _stream_agent(
            client, "lead-delivery",
            f"{lead.get('title', 'Project Lead')} · Slutleverans", lead.get("emoji", "🎯"),
            DELIVERY_SYSTEM.format(title=lead.get("title", "Project Lead")),
            f"{context_block()}\nUPPGIFT TILL TEAMET:\n{task}\n\n"
            f"AGENTERNAS FULLSTÄNDIGA LEVERANSER:\n{_digest(deliverables, cap=9000)}",
            emit, save=(team_id, job_id, "slutleverans.md"), max_tokens=4096,
        )
        deliverables.append(("Slutleverans", delivery))
        await emit({"type": "phase_done", "phase": 999})

    # Uppdatera teamets kunskapsbas
    try:
        await _update_knowledge(client, team_id, team.get("name", ""), knowledge, deliverables, emit)
    except Exception as e:  # noqa: BLE001
        await emit({"type": "knowledge_error", "message": str(e)})

    await emit({"type": "run_done"})
