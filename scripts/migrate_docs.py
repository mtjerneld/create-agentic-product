"""Engångsmigrering: konverterar det gamla docs/-innehållet till ett sparat
team + dess första jobb i den nya workspace-modellen.

Kör:  python scripts/migrate_docs.py
"""

import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "server"))

import store  # noqa: E402

DOCS = ROOT / "docs"

# Rekonstruerat team utifrån docs/-innehållet (MissionPoint LinkedIn-redaktion).
TEAM = {
    "name": "MissionPoint LinkedIn-redaktion",
    "rationale": (
        "Ett redaktionsteam som tar fram LinkedIn-innehåll för MissionPoint. "
        "Bygger på en varumärkesanalys och en innehållsstrategi, producerar "
        "inlägg och kvalitetssäkrar inför publicering."
    ),
    "brief": {
        "product": "MissionPoint — tjänst/varumärke som kommunicerar via LinkedIn.",
        "audience": "IT-chefer och potentiella medarbetare i Sverige.",
        "markets": "Sverige",
        "ambition": "MVP — bygga upp en LinkedIn-närvaro.",
        "budget": "—",
        "timeline": "—",
        "existing": "Varumärkesanalys, innehållsstrategi och första inläggsbatch finns.",
    },
    "phases": [
        {"number": 1, "name": "Varumärke & strategi",
         "goal": "Förankra varumärket och lägga innehållsstrategin."},
        {"number": 2, "name": "Innehållsproduktion",
         "goal": "Skriva LinkedIn-inlägg för olika målgrupper."},
        {"number": 3, "name": "Granskning & publicering",
         "goal": "Kvalitetssäkra och planera publicering."},
    ],
    "agents": [
        {"name": "project-lead", "title": "Projektledare & Koordinator", "emoji": "🎯",
         "role": "Koordinerar redaktionen, sätter riktningen och kvalitetssäkrar leveranser.",
         "phase": 0, "why": "Håller ihop arbetet mellan faserna."},
        {"name": "varum-rkesanalytiker", "title": "Varumärkesanalytiker", "emoji": "🔎",
         "role": "Analyserar varumärket, tonläget och positioneringen som allt innehåll vilar på.",
         "phase": 1, "why": "Ger den varumärkesgrund som copy och strategi behöver."},
        {"name": "inneh-llsstrateg", "title": "Innehållsstrateg", "emoji": "🧭",
         "role": "Lägger innehållsstrategin och vinklar teman för LinkedIn-inläggen.",
         "phase": 1, "why": "Översätter varumärket till en konkret innehållsplan."},
        {"name": "linkedin-copywriter", "title": "LinkedIn-copywriter", "emoji": "✍️",
         "role": "Skriver färdiga LinkedIn-inlägg enligt strategin och tonläget.",
         "phase": 2, "why": "Producerar själva inläggstexterna."},
        {"name": "employer-branding-specialist", "title": "Employer Branding-specialist", "emoji": "🤝",
         "role": "Skriver innehåll riktat mot potentiella medarbetare och stärker arbetsgivarvarumärket.",
         "phase": 2, "why": "Täcker rekryterings- och kulturvinkeln på LinkedIn."},
        {"name": "linkedin-specialist-publiceringsstrateg",
         "title": "LinkedIn-specialist & Publiceringsstrateg", "emoji": "📣",
         "role": "Granskar inläggen mot LinkedIns format och lägger en publiceringsplan.",
         "phase": 3, "why": "Kvalitetssäkrar och optimerar inför publicering."},
    ],
}

# docs-fil -> filnamn i jobbmappen
DELIVERABLES = [
    "00-kickoff.md",
    "varum-rkesanalytiker.md",
    "inneh-llsstrateg.md",
    "linkedin-copywriter.md",
    "employer-branding-specialist.md",
    "linkedin-specialist-publiceringsstrateg.md",
    "99-sammanfattning.md",
]


def main():
    if not DOCS.exists():
        print("docs/ saknas — inget att migrera.")
        return

    existing = [t for t in store.list_teams() if t["name"] == TEAM["name"]]
    if existing:
        print(f"Teamet '{TEAM['name']}' finns redan ({existing[0]['id']}). Avbryter.")
        return

    team = store.create_team(TEAM)
    print(f"Skapade team: {team['id']}")

    job = store.create_job(team["id"], "Ta fram första batchen LinkedIn-inlägg för MissionPoint.")
    job_path = store.job_dir(team["id"], job["id"])
    copied = 0
    for name in DELIVERABLES:
        src = DOCS / name
        if src.exists():
            shutil.copyfile(src, job_path / name)
            copied += 1
        else:
            print(f"  (hoppar över saknad fil: {name})")
    store.update_job(team["id"], job["id"], status="done", finished=store.now_iso())
    print(f"Skapade jobb {job['id']} med {copied} leveranser.")

    # Initial kunskapsbas = varumärkesanalysen (teamets bestående research).
    brand = DOCS / "varum-rkesanalytiker.md"
    if brand.exists():
        body = brand.read_text(encoding="utf-8")
        # ta bort den tekniska första rubriken "# Varumärkesanalytiker"
        lines = body.splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        knowledge = (
            "# Kunskapsbas\n\n"
            "_Teamets bestående research. Förfinas automatiskt efter nästa jobb._\n\n"
            "## Varumärkesgrund (MissionPoint)\n"
            + "\n".join(lines).strip()
            + "\n"
        )
        store.set_knowledge(team["id"], knowledge)
        print("Initial kunskapsbas satt från varumärkesanalysen.")

    print("\nKlart. Starta appen och öppna teamet i 'Mina team'.")


if __name__ == "__main__":
    main()
