"""FastAPI-server: GUI för att beställa ett agent-team och se det arbeta."""

import re
import json
import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

from orchestrator import propose_team, run_team

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
DOCS = ROOT / "docs"

app = FastAPI(title="Creative Product Team")


@app.post("/api/team")
async def api_team(request: Request):
    body = await request.json()
    try:
        team = await propose_team(body.get("brief", {}))
        return JSONResponse({"ok": True, "team": team})
    except Exception as e:  # noqa: BLE001
        return JSONResponse({"ok": False, "error": str(e)}, status_code=400)


@app.post("/api/run")
async def api_run(request: Request):
    body = await request.json()
    team = body.get("team", {})
    task = body.get("task", "")
    brief = body.get("brief", {})

    queue: asyncio.Queue = asyncio.Queue()

    async def emit(event):
        await queue.put(event)

    async def producer():
        try:
            await run_team(team, task, brief, emit)
        except Exception as e:  # noqa: BLE001
            await queue.put({"type": "error", "message": str(e)})
        finally:
            await queue.put(None)

    asyncio.create_task(producer())

    async def gen():
        while True:
            event = await queue.get()
            if event is None:
                break
            yield json.dumps(event, ensure_ascii=False) + "\n"

    return StreamingResponse(gen(), media_type="application/x-ndjson")


@app.get("/api/doc/{name}")
async def api_doc(name: str):
    if not re.fullmatch(r"[A-Za-z0-9._-]+\.md", name):
        return JSONResponse({"ok": False, "error": "Ogiltigt filnamn."}, status_code=400)
    path = DOCS / name
    if not path.exists():
        return JSONResponse({"ok": False, "error": "Dokumentet hittades inte."}, status_code=404)
    return PlainTextResponse(path.read_text(encoding="utf-8"))


app.mount("/", StaticFiles(directory=str(WEB), html=True), name="web")
