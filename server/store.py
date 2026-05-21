"""Filbaserad lagring för beständiga team, deras jobb och kunskapsbaser.

Layout:
    workspace/teams/<team-id>/team.json
    workspace/teams/<team-id>/knowledge.md
    workspace/teams/<team-id>/jobs/<job-id>/job.json
    workspace/teams/<team-id>/jobs/<job-id>/<deliverable>.md
"""

import re
import json
import shutil
import uuid
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
TEAMS_DIR = WORKSPACE / "teams"

KNOWLEDGE_SEED = (
    "# Kunskapsbas\n\n"
    "_Teamet har ännu inte byggt upp någon bestående kunskap. "
    "Den fylls på automatiskt efter teamets första jobb._\n"
)


# --- hjälpare -------------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "namnlost"


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def team_dir(team_id: str) -> Path:
    return TEAMS_DIR / team_id


def job_dir(team_id: str, job_id: str) -> Path:
    return team_dir(team_id) / "jobs" / job_id


# --- team -----------------------------------------------------------------

def list_teams() -> list:
    out = []
    if not TEAMS_DIR.exists():
        return out
    for d in TEAMS_DIR.iterdir():
        tj = d / "team.json"
        if not d.is_dir() or not tj.exists():
            continue
        team = _read_json(tj)
        jobs = list_jobs(team["id"])
        out.append({
            "id": team["id"],
            "name": team["name"],
            "rationale": team.get("rationale", ""),
            "agentCount": len(team.get("agents", [])),
            "jobCount": len(jobs),
            "created": team.get("created"),
            "lastActivity": jobs[0]["created"] if jobs else team.get("created"),
        })
    out.sort(key=lambda t: t.get("lastActivity") or "", reverse=True)
    return out


def get_team(team_id: str) -> dict:
    tj = team_dir(team_id) / "team.json"
    if not tj.exists():
        raise FileNotFoundError("Teamet hittades inte.")
    return _read_json(tj)


def create_team(data: dict) -> dict:
    name = (data.get("name") or "").strip() or "Namnlöst team"
    team_id = f"{slugify(name)[:28]}-{uuid.uuid4().hex[:6]}"
    team = {
        "id": team_id,
        "name": name,
        "created": now_iso(),
        "brief": data.get("brief", {}),
        "rationale": data.get("rationale", ""),
        "phases": data.get("phases", []),
        "agents": data.get("agents", []),
    }
    d = team_dir(team_id)
    (d / "jobs").mkdir(parents=True, exist_ok=True)
    _write_json(d / "team.json", team)
    (d / "knowledge.md").write_text(KNOWLEDGE_SEED, encoding="utf-8")
    return team


def update_team(team_id: str, **fields) -> dict:
    team = get_team(team_id)
    team.update(fields)
    _write_json(team_dir(team_id) / "team.json", team)
    return team


def delete_team(team_id: str) -> None:
    d = team_dir(team_id)
    if d.exists():
        shutil.rmtree(d)


# --- kunskapsbas ----------------------------------------------------------

def get_knowledge(team_id: str) -> str:
    kp = team_dir(team_id) / "knowledge.md"
    return kp.read_text(encoding="utf-8") if kp.exists() else KNOWLEDGE_SEED


def set_knowledge(team_id: str, text: str) -> None:
    (team_dir(team_id) / "knowledge.md").write_text(text.strip() + "\n", encoding="utf-8")


# --- jobb -----------------------------------------------------------------

def list_jobs(team_id: str) -> list:
    jd = team_dir(team_id) / "jobs"
    out = []
    if not jd.exists():
        return out
    for d in jd.iterdir():
        jj = d / "job.json"
        if d.is_dir() and jj.exists():
            job = _read_json(jj)
            job["deliverables"] = list_deliverables(team_id, job["id"])
            out.append(job)
    out.sort(key=lambda j: j.get("created") or "", reverse=True)
    return out


def get_job(team_id: str, job_id: str) -> dict:
    jj = job_dir(team_id, job_id) / "job.json"
    if not jj.exists():
        raise FileNotFoundError("Jobbet hittades inte.")
    job = _read_json(jj)
    job["deliverables"] = list_deliverables(team_id, job_id)
    return job


def create_job(team_id: str, task: str) -> dict:
    get_team(team_id)  # validerar att teamet finns
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    job_id = f"job-{stamp}"
    d = job_dir(team_id, job_id)
    # om två jobb startas samma sekund
    suffix = 1
    while d.exists():
        suffix += 1
        job_id = f"job-{stamp}-{suffix}"
        d = job_dir(team_id, job_id)
    d.mkdir(parents=True)
    job = {
        "id": job_id,
        "teamId": team_id,
        "task": (task or "").strip(),
        "status": "running",
        "created": now_iso(),
        "finished": None,
    }
    _write_json(d / "job.json", job)
    return job


def update_job(team_id: str, job_id: str, **fields) -> dict:
    jj = job_dir(team_id, job_id) / "job.json"
    job = _read_json(jj)
    job.update(fields)
    _write_json(jj, job)
    return job


# --- leveranser -----------------------------------------------------------

def list_deliverables(team_id: str, job_id: str) -> list:
    d = job_dir(team_id, job_id)
    if not d.exists():
        return []
    files = sorted(p.name for p in d.iterdir() if p.suffix == ".md")
    return files


def save_deliverable(team_id: str, job_id: str, filename: str, content: str) -> None:
    (job_dir(team_id, job_id) / filename).write_text(content, encoding="utf-8")


def read_deliverable(team_id: str, job_id: str, name: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+\.md", name or ""):
        raise ValueError("Ogiltigt filnamn.")
    p = job_dir(team_id, job_id) / name
    if not p.exists():
        raise FileNotFoundError("Dokumentet hittades inte.")
    return p.read_text(encoding="utf-8")


# --- bilagor --------------------------------------------------------------

def attachments_dir(team_id: str, job_id: str) -> Path:
    return job_dir(team_id, job_id) / "attachments"


def _safe_name(filename: str) -> str:
    base, dot, ext = (filename or "").rpartition(".")
    base = base or filename or "fil"
    ext = re.sub(r"[^A-Za-z0-9]+", "", ext).lower()
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", base).strip("-") or "fil"
    return f"{stem}.{ext}" if ext else stem


def save_attachment(team_id: str, job_id: str, filename: str,
                    raw: bytes, text: str) -> dict:
    """Sparar originalfilen + den extraherade texten. Returnerar metadata."""
    d = attachments_dir(team_id, job_id)
    d.mkdir(parents=True, exist_ok=True)
    name = _safe_name(filename)
    # undvik krockar
    target = d / name
    n = 1
    while target.exists():
        n += 1
        stem, dot, ext = name.rpartition(".")
        name = f"{stem}-{n}.{ext}" if dot else f"{name}-{n}"
        target = d / name
    target.write_bytes(raw)
    (d / (name + ".txt")).write_text(text, encoding="utf-8")
    return {"name": name, "chars": len(text)}


def get_attachments_text(team_id: str, job_id: str) -> dict:
    """Returnerar {filnamn: extraherad text} för alla bilagor på ett jobb."""
    d = attachments_dir(team_id, job_id)
    out = {}
    if not d.exists():
        return out
    for p in sorted(d.iterdir()):
        if p.name.endswith(".txt"):
            out[p.name[:-4]] = p.read_text(encoding="utf-8")
    return out


def read_attachment_text(team_id: str, job_id: str, name: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", name or ""):
        raise ValueError("Ogiltigt filnamn.")
    p = attachments_dir(team_id, job_id) / (name + ".txt")
    if not p.exists():
        raise FileNotFoundError("Bilagan hittades inte.")
    return p.read_text(encoding="utf-8")
