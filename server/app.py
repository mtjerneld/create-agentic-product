"""FastAPI-server: GUI för beständiga AI-agentteam.

Ett team skapas en gång och sparas. Det kan sedan köra flera jobb över tid och
bär med sig en levande kunskapsbas mellan jobben.
"""

import json
import asyncio
from pathlib import Path

import markdown as md
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

import store
import documents
import export
from orchestrator import propose_team, run_team

DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
PDF_MIME = "application/pdf"

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"

app = FastAPI(title="MissionPoint AI Teams")

_MD_EXT = ["extra", "sane_lists", "toc"]


def render_md(text: str) -> str:
    return md.markdown(text or "", extensions=_MD_EXT)


def _err(msg: str, code: int = 400):
    return JSONResponse({"ok": False, "error": msg}, status_code=code)


def _docx(sections: list, filename: str):
    try:
        data = export.md_to_docx(sections)
    except Exception as e:  # noqa: BLE001
        return _err("Kunde inte skapa Word-fil: " + str(e), 500)
    return Response(
        content=data,
        media_type=DOCX_MIME,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


def _pdf(sections: list, filename: str):
    try:
        data = export.md_to_pdf(sections, title=filename.rsplit(".", 1)[0])
    except Exception as e:  # noqa: BLE001
        return _err("Kunde inte skapa PDF-fil: " + str(e), 500)
    return Response(
        content=data,
        media_type=PDF_MIME,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# --- teamförslag ----------------------------------------------------------

@app.post("/api/team")
async def api_propose_team(request: Request):
    body = await request.json()
    try:
        team = await propose_team(body.get("brief", {}))
        return JSONResponse({"ok": True, "team": team})
    except Exception as e:  # noqa: BLE001
        return _err(str(e))


# --- team CRUD ------------------------------------------------------------

@app.get("/api/teams")
async def api_list_teams():
    return JSONResponse({"ok": True, "teams": store.list_teams()})


@app.post("/api/teams")
async def api_create_team(request: Request):
    body = await request.json()
    team_in = body.get("team", {})
    team_in.setdefault("brief", body.get("brief", {}))
    try:
        team = store.create_team(team_in)
        return JSONResponse({"ok": True, "team": team})
    except Exception as e:  # noqa: BLE001
        return _err(str(e))


@app.get("/api/teams/{team_id}")
async def api_get_team(team_id: str):
    try:
        team = store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    team["jobs"] = store.list_jobs(team_id)
    knowledge = store.get_knowledge(team_id)
    team["knowledge"] = knowledge
    team["knowledgeHtml"] = render_md(knowledge)
    return JSONResponse({"ok": True, "team": team})


@app.put("/api/teams/{team_id}")
async def api_update_team(team_id: str, request: Request):
    try:
        store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    body = await request.json()
    fields = {k: body[k] for k in ("name", "rationale", "agents", "phases") if k in body}
    if "agents" in fields and not fields["agents"]:
        return _err("Teamet behöver minst en agent.")
    team = store.update_team(team_id, **fields)
    return JSONResponse({"ok": True, "team": team})


@app.delete("/api/teams/{team_id}")
async def api_delete_team(team_id: str):
    store.delete_team(team_id)
    return JSONResponse({"ok": True})


@app.get("/api/teams/{team_id}/knowledge")
async def api_knowledge(team_id: str):
    try:
        store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return JSONResponse({"ok": True, "html": render_md(store.get_knowledge(team_id))})


@app.put("/api/teams/{team_id}/knowledge")
async def api_update_knowledge(team_id: str, request: Request):
    try:
        store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    body = await request.json()
    text = (body.get("text") or "").strip()
    if not text:
        return _err("Kunskapsbasen kan inte vara tom.")
    store.set_knowledge(team_id, text)
    knowledge = store.get_knowledge(team_id)
    return JSONResponse({"ok": True, "knowledge": knowledge, "html": render_md(knowledge)})


@app.get("/api/teams/{team_id}/knowledge/docx")
async def api_knowledge_docx(team_id: str):
    try:
        store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return _docx([store.get_knowledge(team_id)], "kunskapsbas.docx")


@app.get("/api/teams/{team_id}/knowledge/pdf")
async def api_knowledge_pdf(team_id: str):
    try:
        store.get_team(team_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return _pdf([store.get_knowledge(team_id)], "kunskapsbas.pdf")


# --- jobb -----------------------------------------------------------------

@app.get("/api/teams/{team_id}/jobs/{job_id}")
async def api_get_job(team_id: str, job_id: str):
    try:
        job = store.get_job(team_id, job_id)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return JSONResponse({"ok": True, "job": job})


@app.get("/api/teams/{team_id}/jobs/{job_id}/doc/{name}")
async def api_job_doc(team_id: str, job_id: str, name: str):
    try:
        raw = store.read_deliverable(team_id, job_id, name)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    except ValueError as e:
        return _err(str(e), 400)
    return JSONResponse({"ok": True, "html": render_md(raw), "raw": raw})


@app.get("/api/teams/{team_id}/jobs/{job_id}/doc/{name}/docx")
async def api_job_doc_docx(team_id: str, job_id: str, name: str):
    try:
        raw = store.read_deliverable(team_id, job_id, name)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    except ValueError as e:
        return _err(str(e), 400)
    return _docx([raw], name[:-3] + ".docx")


@app.get("/api/teams/{team_id}/jobs/{job_id}/doc/{name}/pdf")
async def api_job_doc_pdf(team_id: str, job_id: str, name: str):
    try:
        raw = store.read_deliverable(team_id, job_id, name)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    except ValueError as e:
        return _err(str(e), 400)
    return _pdf([raw], name[:-3] + ".pdf")


@app.get("/api/teams/{team_id}/jobs/{job_id}/docx")
async def api_job_docx(team_id: str, job_id: str):
    try:
        names = store.list_deliverables(team_id, job_id)
        if not names:
            return _err("Jobbet har inga leveranser.", 404)
        sections = [store.read_deliverable(team_id, job_id, n) for n in names]
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return _docx(sections, job_id + ".docx")


@app.get("/api/teams/{team_id}/jobs/{job_id}/pdf")
async def api_job_pdf(team_id: str, job_id: str):
    try:
        names = store.list_deliverables(team_id, job_id)
        if not names:
            return _err("Jobbet har inga leveranser.", 404)
        sections = [store.read_deliverable(team_id, job_id, n) for n in names]
    except FileNotFoundError as e:
        return _err(str(e), 404)
    return _pdf(sections, job_id + ".pdf")


@app.get("/api/teams/{team_id}/jobs/{job_id}/attachment/{name}")
async def api_job_attachment(team_id: str, job_id: str, name: str):
    try:
        text = store.read_attachment_text(team_id, job_id, name)
    except FileNotFoundError as e:
        return _err(str(e), 404)
    except ValueError as e:
        return _err(str(e), 400)
    return JSONResponse({"ok": True, "text": text})


@app.post("/api/teams/{team_id}/jobs")
async def api_run_job(
    team_id: str,
    task: str = Form(""),
    files: list[UploadFile] = File(default=[]),
):
    try:
        team = store.get_team(team_id)
        job = store.create_job(team_id, task)
    except FileNotFoundError as e:
        return _err(str(e), 404)

    # Bilagor: extrahera text, spara original + text.
    attachments, attach_errors = [], []
    for f in files:
        raw = await f.read()
        if not raw:
            continue
        try:
            text = documents.extract_text(f.filename, raw)
            meta = store.save_attachment(team_id, job["id"], f.filename, raw, text)
            attachments.append(meta)
        except Exception as e:  # noqa: BLE001
            attach_errors.append(f"{f.filename}: {e}")
    if attachments:
        store.update_job(team_id, job["id"], attachments=attachments)

    queue: asyncio.Queue = asyncio.Queue()

    async def emit(event):
        await queue.put(event)

    async def producer():
        try:
            await emit({
                "type": "job_created", "jobId": job["id"], "team": team["name"],
                "attachments": attachments, "attachmentErrors": attach_errors,
            })
            await run_team(team_id, job["id"], task, emit)
            store.update_job(team_id, job["id"], status="done", finished=store.now_iso())
        except Exception as e:  # noqa: BLE001
            store.update_job(team_id, job["id"], status="error", finished=store.now_iso())
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


app.mount("/", StaticFiles(directory=str(WEB), html=True), name="web")
