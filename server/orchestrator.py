"""Team-orkestrering: föreslå ett agent-team och kör det fas för fas mot Claude API."""

import os
import re
import asyncio
from pathlib import Path

from anthropic import AsyncAnthropic

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"

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
                        "phase": {"type": "integer", "description": "Fasnummer. 0 = project-lead/koordinator."},
                        "why": {"type": "string", "description": "Varför just denna agent behövs här."},
                    },
                    "required": ["name", "title", "emoji", "role", "phase", "why"],
                },
            },
        },
        "required": ["rationale", "phases", "agents"],
    },
}

PROPOSE_SYSTEM = """Du är project-lead för ett ramverk som snabbt sätter ihop ett \
AI-drivet kreativt team. Teamet tar en produktidé från koncept till lansering.

Givet en projektbrief: sätt ihop det ideala teamet av specialiserade agenter.
Var kreativ och tänk bortom standardrollerna — lägg till roller som just detta
projekt kräver (t.ex. sustainability-advisor, pricing-strategist, packaging-designer).

Regler:
- Inkludera alltid en project-lead med phase 0 (koordinator).
- Definiera 2-4 arbetsfaser (t.ex. research, koncept/design, byggande, lansering)
  anpassade efter projektet.
- 1-3 agenter per fas, 5-9 agenter totalt.
- Skriv allt på svenska.
Använd verktyget submit_team för att lämna in resultatet."""


async def propose_team(brief: dict) -> dict:
    client = get_client()
    msg = await client.messages.create(
        model=MODEL,
        max_tokens=2200,
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
    if not any(a.get("phase") == 0 for a in team["agents"]):
        team["agents"].insert(0, {
            "name": "project-lead",
            "title": "Project Lead",
            "emoji": "🎯",
            "role": "Koordinerar teamet, driver arbetet framåt och kvalitetssäkrar leveranser.",
            "phase": 0,
            "why": "Behövs alltid för att hålla ihop projektet.",
        })
    return team


# --- Steg 2: kör teamet ---------------------------------------------------

def _digest(deliverables: list, cap: int = 2500) -> str:
    out = []
    for title, text in deliverables:
        t = text.strip()
        if len(t) > cap:
            t = t[:cap] + "\n…(förkortat)"
        out.append(f"## {title}\n{t}")
    return "\n\n".join(out)


async def _stream_agent(client, agent_id, title, emoji, system, user, emit, save_as=None):
    await emit({"type": "agent_started", "agent": agent_id, "title": title, "emoji": emoji})
    parts = []
    try:
        async with client.messages.stream(
            model=MODEL,
            max_tokens=2800,
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
    if save_as:
        DOCS_DIR.mkdir(exist_ok=True)
        (DOCS_DIR / save_as).write_text(f"# {title}\n\n{full}\n", encoding="utf-8")
        deliverable = save_as
    await emit({"type": "agent_done", "agent": agent_id, "deliverable": deliverable, "chars": len(full)})
    return full


def _agent_system(title, role, phase_name, phase_goal) -> str:
    return (
        f"Du är {title}, en agent i ett AI-drivet kreativt produktteam.\n"
        f"Roll: {role}\n"
        f"Fas: {phase_name} — {phase_goal}\n\n"
        "Producera en konkret, högkvalitativ leverans för din roll i denna fas. "
        "Var specifik och handlingsbar — inga generiska floskler. Gör rimliga "
        "antaganden där information saknas och var tydlig med dem. "
        "Formatera som ett markdown-dokument med tydliga rubriker. Skriv på svenska."
    )


async def run_team(team: dict, task: str, brief: dict, emit) -> None:
    client = get_client()
    brief_text = format_brief(brief)
    task = (task or "").strip() or "Ta produkten från koncept till lansering enligt faserna."

    agents = team.get("agents", [])
    phases = sorted(
        [p for p in team.get("phases", []) if p.get("number", 0) != 0],
        key=lambda p: p.get("number", 0),
    )
    lead = next((a for a in agents if a.get("phase") == 0), None)

    await emit({"type": "run_started", "task": task, "phases": phases})

    deliverables: list = []

    # Kickoff från project-lead
    if lead:
        await emit({"type": "phase_started", "phase": 0, "name": "Kickoff", "goal": "Sätt riktningen"})
        kickoff = await _stream_agent(
            client, "lead-kickoff",
            f"{lead.get('title', 'Project Lead')} · Kickoff", lead.get("emoji", "🎯"),
            f"Du är {lead.get('title', 'Project Lead')}, project-lead för teamet.",
            "Skriv en kort kickoff-brief (max ~300 ord) på svenska i markdown: "
            "återge målet, de viktigaste prioriteringarna, och vad varje fas måste "
            f"leverera.\n\nPROJEKTBRIEF:\n{brief_text}\n\nUPPGIFT TILL TEAMET:\n{task}",
            emit, save_as="00-kickoff.md",
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
            user = (
                f"PROJEKTBRIEF:\n{brief_text}\n\nUPPGIFT TILL TEAMET:\n{task}\n"
            )
            if prior:
                user += f"\nLEVERANSER FRÅN TIDIGARE FASER:\n{prior}\n"
            user += "\nLevera ditt bidrag nu."
            return await _stream_agent(
                client, agent.get("name", slugify(title)), title, agent.get("emoji", "🧩"),
                _agent_system(title, agent.get("role", ""), phase.get("name", ""), phase.get("goal", "")),
                user, emit, save_as=f"{slugify(title)}.md",
            )

        results = await asyncio.gather(*(run_one(a) for a in phase_agents), return_exceptions=True)
        for agent, res in zip(phase_agents, results):
            if not isinstance(res, Exception):
                deliverables.append((agent.get("title") or agent.get("name", "Agent"), res))
        await emit({"type": "phase_done", "phase": num})

    # Avslutande sammanfattning från project-lead
    if lead:
        await emit({"type": "phase_started", "phase": 999, "name": "Sammanfattning", "goal": "Knyt ihop"})
        await _stream_agent(
            client, "lead-summary",
            f"{lead.get('title', 'Project Lead')} · Sammanfattning", lead.get("emoji", "🎯"),
            f"Du är {lead.get('title', 'Project Lead')}, project-lead för teamet.",
            "Alla agenter har levererat. Skriv en avslutande sammanfattning på svenska "
            "i markdown: vad teamet producerat, konkreta nästa steg, och risker att "
            f"bevaka.\n\nPROJEKTBRIEF:\n{brief_text}\n\nUPPGIFT:\n{task}\n\n"
            f"ALLA LEVERANSER:\n{_digest(deliverables)}",
            emit, save_as="99-sammanfattning.md",
        )
        await emit({"type": "phase_done", "phase": 999})

    await emit({"type": "run_done"})
