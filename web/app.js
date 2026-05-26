"use strict";

const state = {
  brief: {},          // ifylld brief
  proposedTeam: null, // team-förslag innan det sparats
  team: null,         // aktuellt sparat team (fullt objekt)
  files: [],          // bilagor vald för nästa jobb
};

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

/* ---- Vyhantering ---- */
function showView(name) {
  $$(".view").forEach((v) => v.classList.toggle("active", v.id === "view-" + name));
  const stepper = $("#stepper");
  stepper.hidden = !(name === "brief" || name === "team");
  if (!stepper.hidden) {
    $$("#stepper li").forEach((li) =>
      li.classList.toggle("active", li.dataset.step === name)
    );
  }
  window.scrollTo(0, 0);
}

function toast(msg) {
  const t = $("#toast");
  t.textContent = msg;
  t.hidden = false;
  clearTimeout(toast._t);
  toast._t = setTimeout(() => (t.hidden = true), 6000);
}

function slugify(s) {
  return (s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "agent";
}

function escapeHtml(s) {
  return String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
}
function escapeAttr(s) {
  return escapeHtml(s).replace(/"/g, "&quot;");
}

function fmtDate(iso) {
  if (!iso) return "—";
  try {
    return new Date(iso).toLocaleString("sv-SE", {
      year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit",
    });
  } catch (e) {
    return iso;
  }
}

async function apiJSON(url, opts) {
  const resp = await fetch(url, opts);
  const data = await resp.json().catch(() => ({}));
  if (!resp.ok || data.ok === false) {
    throw new Error(data.error || "Serverfel (" + resp.status + ")");
  }
  return data;
}

/* ===================================================================== *
 *  DASHBOARD — Mina team
 * ===================================================================== */
async function loadDashboard() {
  showView("teams");
  const grid = $("#teams-grid");
  grid.innerHTML = '<div class="muted">Laddar…</div>';
  try {
    const data = await apiJSON("/api/teams");
    renderDashboard(data.teams || []);
  } catch (err) {
    grid.innerHTML = "";
    toast("Kunde inte ladda team: " + err.message);
  }
}

function renderDashboard(teams) {
  const grid = $("#teams-grid");
  const empty = $("#teams-empty");
  grid.innerHTML = "";
  empty.hidden = teams.length > 0;
  teams.forEach((t) => {
    const el = document.createElement("div");
    el.className = "team-tile";
    el.innerHTML = `
      <h3>${escapeHtml(t.name)}</h3>
      <p class="muted tile-rationale">${escapeHtml(t.rationale || "")}</p>
      <div class="tile-meta">
        <span>${t.agentCount} agenter</span>
        <span>${t.jobCount} jobb</span>
      </div>
      <div class="tile-foot muted">Senast aktiv: ${fmtDate(t.lastActivity)}</div>`;
    el.addEventListener("click", () => loadWorkspace(t.id));
    grid.appendChild(el);
  });
}

$("#brand").addEventListener("click", loadDashboard);
$("#brand").addEventListener("keydown", (e) => {
  if (e.key === "Enter" || e.key === " ") loadDashboard();
});
$("#new-team-btn").addEventListener("click", startNewTeam);
$("#new-team-empty").addEventListener("click", startNewTeam);

function startNewTeam() {
  state.brief = {};
  state.proposedTeam = null;
  $("#brief-form").reset();
  showView("brief");
}

$("#brief-cancel").addEventListener("click", loadDashboard);

/* ===================================================================== *
 *  STEG 1: Brief -> teamförslag
 * ===================================================================== */
$("#brief-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fd = new FormData(e.target);
  state.brief = Object.fromEntries(fd.entries());
  const btn = $("#brief-submit");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span>Sätter ihop teamet…';
  try {
    const data = await apiJSON("/api/team", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ brief: state.brief }),
    });
    state.proposedTeam = data.team;
    renderProposedTeam(data.team);
    showView("team");
  } catch (err) {
    toast("Kunde inte skapa team: " + err.message);
  } finally {
    btn.disabled = false;
    btn.textContent = "Sätt ihop teamet →";
  }
});

/* ===================================================================== *
 *  STEG 2: Redigera och spara teamet
 * ===================================================================== */
function phaseOptions(phases, selected) {
  const all = [{ number: 0, name: "Koordinator" }].concat(phases || []);
  return all
    .map(
      (p) =>
        `<option value="${p.number}" ${p.number === selected ? "selected" : ""}>` +
        `${p.number === 0 ? "" : "Fas " + p.number + ": "}${escapeHtml(p.name)}</option>`
    )
    .join("");
}

function renderProposedTeam(team) {
  $("#team-rationale").textContent = team.rationale || "";
  $("#team-name").value = team.name || "";

  const plan = $("#phase-plan");
  plan.innerHTML = (team.phases || [])
    .map(
      (p) =>
        `<div class="phase-chip"><b>Fas ${p.number}: ${escapeHtml(p.name)}</b>` +
        `<span>${escapeHtml(p.goal || "")}</span></div>`
    )
    .join("");

  const grid = $("#team-grid");
  grid.innerHTML = "";
  (team.agents || []).forEach((a) => grid.appendChild(agentCard(a, team.phases)));
}

function agentCard(a, phases) {
  const el = document.createElement("div");
  el.className = "agent-card";
  el.dataset.name = a.name || slugify(a.title);
  el.dataset.emoji = a.emoji || "🧩";
  el.dataset.why = a.why || "";
  el.innerHTML = `
    <div class="ac-head">
      <span class="emoji">${a.emoji || "🧩"}</span>
      <span class="ac-title"><input class="f-title" value="${escapeAttr(a.title || "")}" /></span>
    </div>
    <label>Instruktion
      <textarea class="f-role" rows="3">${escapeHtml(a.role || "")}</textarea>
    </label>
    <label>Verktyg / kapaciteter
      <input class="f-tools" value="${escapeAttr(a.tools || "")}" placeholder="t.ex. webbsök, konkurrentanalys" />
    </label>
    <div class="ac-foot">
      <select class="f-phase">${phaseOptions(phases, a.phase ?? 1)}</select>
      <button type="button" class="remove">Ta bort</button>
    </div>`;
  el.querySelector(".remove").addEventListener("click", () => el.remove());
  return el;
}

function collectAgents(gridSelector) {
  return $$(gridSelector + " .agent-card").map((el) => {
    const title = el.querySelector(".f-title").value.trim() || "Agent";
    return {
      name: el.dataset.name || slugify(title),
      title,
      emoji: el.dataset.emoji || "🧩",
      role: el.querySelector(".f-role").value.trim(),
      tools: el.querySelector(".f-tools").value.trim(),
      phase: parseInt(el.querySelector(".f-phase").value, 10) || 0,
      why: el.dataset.why || "",
    };
  });
}

$("#add-agent").addEventListener("click", () => {
  $("#team-grid").appendChild(
    agentCard(
      { name: "", title: "Ny agent", emoji: "✨", role: "", tools: "", why: "Tillagd manuellt.", phase: 1 },
      state.proposedTeam.phases
    )
  );
});

$("#back-to-brief").addEventListener("click", () => showView("brief"));

function collectProposedTeam() {
  return {
    name: $("#team-name").value.trim() || "Namnlöst team",
    rationale: state.proposedTeam.rationale,
    phases: state.proposedTeam.phases,
    agents: collectAgents("#team-grid"),
  };
}

$("#save-team").addEventListener("click", async () => {
  const team = collectProposedTeam();
  if (!team.agents.length) {
    toast("Teamet behöver minst en agent.");
    return;
  }
  const btn = $("#save-team");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span>Sparar…';
  try {
    const data = await apiJSON("/api/teams", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ team, brief: state.brief }),
    });
    toast("Teamet sparades.");
    await loadWorkspace(data.team.id);
  } catch (err) {
    toast("Kunde inte spara team: " + err.message);
  } finally {
    btn.disabled = false;
    btn.textContent = "Spara team ✓";
  }
});

/* ===================================================================== *
 *  TEAM-ARBETSYTA
 * ===================================================================== */
async function loadWorkspace(teamId) {
  try {
    const data = await apiJSON("/api/teams/" + teamId);
    state.team = data.team;
    renderWorkspace(data.team);
    showView("workspace");
  } catch (err) {
    toast("Kunde inte öppna teamet: " + err.message);
    loadDashboard();
  }
}

function renderWorkspace(team) {
  $("#ws-name").textContent = team.name;
  $("#ws-rationale").textContent = team.rationale || "";
  $("#ws-knowledge").innerHTML = team.knowledgeHtml || "<p class='muted'>Tom kunskapsbas.</p>";
  $("#ws-knowledge-dl").href = "/api/teams/" + team.id + "/knowledge/docx";
  knowledgeEdit(false);
  $("#ws-task").value = "";
  state.files = [];
  renderFileList();

  teamEdit(false);
  renderAgentList(team);
  renderJobs(team);
}

function renderAgentList(team) {
  const agents = $("#ws-agents");
  agents.innerHTML = "";
  const byPhase = {};
  (team.agents || []).forEach((a) => {
    (byPhase[a.phase] = byPhase[a.phase] || []).push(a);
  });
  Object.keys(byPhase)
    .sort((a, b) => a - b)
    .forEach((ph) => {
      byPhase[ph].forEach((a) => {
        const el = document.createElement("div");
        el.className = "ws-agent";
        const phaseLabel = ph === "0" ? "Koordinator" : "Fas " + ph;
        el.innerHTML = `
          <span class="emoji">${a.emoji || "🧩"}</span>
          <div class="ws-agent-main">
            <div class="ws-agent-top">
              <b>${escapeHtml(a.title || a.name)}</b>
              <span class="ws-agent-phase">${phaseLabel}</span>
            </div>
            <p class="ws-agent-role">${escapeHtml(a.role || "")}</p>
            ${a.tools ? `<p class="ws-agent-tools">🛠 <b>Verktyg:</b> ${escapeHtml(a.tools)}</p>` : ""}
          </div>`;
        agents.appendChild(el);
      });
    });
}

function renderJobs(team) {
  const wrap = $("#ws-jobs");
  wrap.innerHTML = "";
  const jobs = team.jobs || [];
  if (!jobs.length) {
    wrap.innerHTML = "<p class='muted'>Inga jobb än. Ge teamet en uppgift ovan.</p>";
    return;
  }
  jobs.forEach((job) => {
    const el = document.createElement("div");
    el.className = "job-row";
    const statusCls = job.status === "done" ? "done" : job.status === "error" ? "error" : "running";
    const all = job.deliverables || [];
    const jobDl = all.length
      ? `<a class="dl-btn job-dl" href="/api/teams/${team.id}/jobs/${job.id}/docx">⬇ Word</a>`
      : "";
    el.innerHTML = `
      <div class="job-head">
        <span class="job-status ${statusCls}">${job.status}</span>
        <span class="job-task" title="${escapeAttr(job.task || "")}">${escapeHtml(job.task || "(ingen uppgiftstext)")}</span>
        <span class="job-date muted">${fmtDate(job.created)}</span>
        ${jobDl}
      </div>
      <div class="job-docs"></div>`;
    const docs = el.querySelector(".job-docs");
    const FINAL = "slutleverans.md";

    if (all.includes(FINAL)) {
      const main = document.createElement("button");
      main.type = "button";
      main.className = "doc-final";
      main.innerHTML = "⭐ Öppna slutleverans";
      main.addEventListener("click", () => openDoc(team.id, job.id, FINAL));
      el.querySelector(".job-head").after(main);
    }

    all.filter((n) => n !== FINAL).forEach((name) => {
      const a = document.createElement("button");
      a.type = "button";
      a.className = "doc-chip";
      a.textContent = "📄 " + name;
      a.addEventListener("click", () => openDoc(team.id, job.id, name));
      docs.appendChild(a);
    });
    if (!all.length) {
      docs.innerHTML = "<span class='muted'>Inga leveranser.</span>";
    } else if (all.length === 1 && all[0] === FINAL) {
      docs.remove();
    } else {
      docs.insertAdjacentHTML("afterbegin", "<span class='docs-label muted'>Underlag:</span>");
    }

    const att = job.attachments || [];
    if (att.length) {
      const row = document.createElement("div");
      row.className = "job-docs";
      row.insertAdjacentHTML("afterbegin", "<span class='docs-label muted'>Bilagor:</span>");
      att.forEach((a) => {
        const b = document.createElement("button");
        b.type = "button";
        b.className = "doc-chip att-chip";
        b.textContent = "📎 " + a.name;
        b.addEventListener("click", () => openAttachment(team.id, job.id, a.name));
        row.appendChild(b);
      });
      el.appendChild(row);
    }
    wrap.appendChild(el);
  });
}

$("#ws-delete").addEventListener("click", async () => {
  if (!state.team) return;
  if (!confirm("Ta bort teamet \"" + state.team.name + "\" och all dess historik?")) return;
  try {
    await apiJSON("/api/teams/" + state.team.id, { method: "DELETE" });
    toast("Teamet togs bort.");
    loadDashboard();
  } catch (err) {
    toast("Kunde inte ta bort: " + err.message);
  }
});

/* ---- Kunskapsbas: redigering ---- */
function knowledgeEdit(on) {
  $("#ws-knowledge").hidden = on;
  $("#ws-knowledge-editor").hidden = !on;
  $("#ws-knowledge-edit").hidden = on;
  if (on) {
    $("#ws-knowledge-text").value = (state.team && state.team.knowledge) || "";
    $("#ws-knowledge-text").focus();
  }
}

$("#ws-knowledge-edit").addEventListener("click", () => knowledgeEdit(true));
$("#ws-knowledge-cancel").addEventListener("click", () => knowledgeEdit(false));

$("#ws-knowledge-save").addEventListener("click", async () => {
  if (!state.team) return;
  const text = $("#ws-knowledge-text").value.trim();
  if (!text) {
    toast("Kunskapsbasen kan inte vara tom.");
    return;
  }
  const btn = $("#ws-knowledge-save");
  btn.disabled = true;
  try {
    const data = await apiJSON("/api/teams/" + state.team.id + "/knowledge", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    state.team.knowledge = data.knowledge;
    state.team.knowledgeHtml = data.html;
    $("#ws-knowledge").innerHTML = data.html || "";
    knowledgeEdit(false);
    toast("Kunskapsbasen sparades.");
  } catch (err) {
    toast("Kunde inte spara: " + err.message);
  } finally {
    btn.disabled = false;
  }
});

/* ---- Teamet: redigering ---- */
function teamEdit(on) {
  $("#ws-agents").hidden = on;
  $("#ws-team-editor").hidden = !on;
  $("#ws-team-edit").hidden = on;
  if (on && state.team) {
    const grid = $("#ws-team-grid");
    grid.innerHTML = "";
    (state.team.agents || []).forEach((a) =>
      grid.appendChild(agentCard(a, state.team.phases))
    );
  }
}

$("#ws-team-edit").addEventListener("click", () => teamEdit(true));
$("#ws-team-cancel").addEventListener("click", () => teamEdit(false));
$("#ws-add-agent").addEventListener("click", () => {
  $("#ws-team-grid").appendChild(
    agentCard(
      { name: "", title: "Ny agent", emoji: "✨", role: "", tools: "", why: "Tillagd manuellt.", phase: 1 },
      state.team.phases
    )
  );
});

$("#ws-team-save").addEventListener("click", async () => {
  if (!state.team) return;
  const agents = collectAgents("#ws-team-grid");
  if (!agents.length) {
    toast("Teamet behöver minst en agent.");
    return;
  }
  const btn = $("#ws-team-save");
  btn.disabled = true;
  try {
    await apiJSON("/api/teams/" + state.team.id, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ agents }),
    });
    toast("Teamet sparades.");
    await loadWorkspace(state.team.id);
  } catch (err) {
    toast("Kunde inte spara team: " + err.message);
  } finally {
    btn.disabled = false;
  }
});

/* ---- Bilagor ---- */
function fmtSize(bytes) {
  if (bytes < 1024) return bytes + " B";
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(0) + " kB";
  return (bytes / 1024 / 1024).toFixed(1) + " MB";
}

function renderFileList() {
  const wrap = $("#ws-file-list");
  wrap.innerHTML = "";
  state.files.forEach((f, i) => {
    const el = document.createElement("div");
    el.className = "file-item";
    el.innerHTML = `<span>📄 ${escapeHtml(f.name)}</span>
      <span class="muted">${fmtSize(f.size)}</span>
      <button type="button" class="file-remove" title="Ta bort">✕</button>`;
    el.querySelector(".file-remove").addEventListener("click", () => {
      state.files.splice(i, 1);
      renderFileList();
    });
    wrap.appendChild(el);
  });
}

$("#ws-files").addEventListener("change", (e) => {
  const ok = ["pdf", "txt", "md"];
  Array.from(e.target.files).forEach((f) => {
    const ext = f.name.split(".").pop().toLowerCase();
    if (!ok.includes(ext)) {
      toast(`${f.name}: filtypen stöds inte (PDF, TXT, MD).`);
      return;
    }
    state.files.push(f);
  });
  e.target.value = "";
  renderFileList();
});

/* ===================================================================== *
 *  KÖR ETT JOBB
 * ===================================================================== */
const runEls = { phases: {}, agents: {}, current: null };

$("#ws-start").addEventListener("click", startRun);
$("#back-to-workspace").addEventListener("click", () => loadWorkspace(state.team.id));

async function startRun() {
  if (!state.team) return;
  const task = $("#ws-task").value.trim();

  $("#run-phases").innerHTML = "";
  $("#run-actions").hidden = true;
  let taskLabel = task || "(hela processen koncept → lansering)";
  if (state.files.length) taskLabel += `  ·  ${state.files.length} bifogade dokument`;
  $("#run-task").textContent = taskLabel;
  runEls.phases = {};
  runEls.agents = {};
  runEls.current = null;
  setStatus("Startar…", "running");
  showView("run");

  try {
    const form = new FormData();
    form.append("task", task);
    state.files.forEach((f) => form.append("files", f, f.name));
    const resp = await fetch("/api/teams/" + state.team.id + "/jobs", {
      method: "POST",
      body: form,
    });
    if (!resp.ok || !resp.body) {
      const data = await resp.json().catch(() => ({}));
      throw new Error(data.error || "Servern kunde inte starta körningen.");
    }
    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buf = "";
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      let nl;
      while ((nl = buf.indexOf("\n")) >= 0) {
        const line = buf.slice(0, nl).trim();
        buf = buf.slice(nl + 1);
        if (line) handleEvent(JSON.parse(line));
      }
    }
  } catch (err) {
    setStatus("Fel", "error");
    toast("Körningen avbröts: " + err.message);
    $("#run-actions").hidden = false;
  }
}

function setStatus(text, cls) {
  const pill = $("#run-status");
  pill.textContent = text;
  pill.className = "status-pill " + (cls || "");
}

function handleEvent(ev) {
  switch (ev.type) {
    case "job_created":
      state.jobId = ev.jobId;
      if (ev.attachments && ev.attachments.length) {
        toast(`${ev.attachments.length} dokument bifogade som kontext.`);
      }
      (ev.attachmentErrors || []).forEach((m) => toast("Bilaga hoppades över — " + m));
      break;
    case "run_started":
      setStatus("Arbetar…", "running");
      break;
    case "phase_started":
      addPhase(ev);
      break;
    case "agent_started":
      addAgent(ev);
      break;
    case "agent_delta":
      appendDelta(ev.agent, ev.text);
      break;
    case "agent_search":
      appendSearch(ev.agent, ev.query);
      break;
    case "agent_done":
      finishAgent(ev);
      break;
    case "agent_error":
      errorAgent(ev);
      break;
    case "phase_done":
      if (runEls.phases[ev.phase]) runEls.phases[ev.phase].classList.add("done");
      break;
    case "knowledge_updating":
      setStatus("Uppdaterar kunskapsbas…", "running");
      break;
    case "knowledge_updated":
      break;
    case "knowledge_error":
      toast("Kunskapsbasen kunde inte uppdateras: " + (ev.message || ""));
      break;
    case "run_done":
      setStatus("Klar ✓", "done");
      $("#run-actions").hidden = false;
      break;
    case "error":
      setStatus("Fel", "error");
      toast(ev.message || "Ett fel uppstod.");
      $("#run-actions").hidden = false;
      break;
  }
}

function addPhase(ev) {
  const sec = document.createElement("section");
  sec.className = "run-phase";
  sec.innerHTML =
    `<h3><span class="phase-dot"></span>${escapeHtml(ev.name || "Fas")}</h3>` +
    (ev.goal ? `<p class="phase-goal">${escapeHtml(ev.goal)}</p>` : "");
  $("#run-phases").appendChild(sec);
  runEls.phases[ev.phase] = sec;
  runEls.current = sec;
}

function addAgent(ev) {
  const el = document.createElement("div");
  el.className = "run-agent";
  el.innerHTML = `
    <div class="ra-head">
      <span class="emoji">${ev.emoji || "🧩"}</span>
      <span class="ra-name">${escapeHtml(ev.title || ev.agent)}</span>
      <span class="ra-state working">arbetar</span>
    </div>
    <div class="ra-body"></div>
    <div class="ra-foot" hidden></div>`;
  el.querySelector(".ra-head").addEventListener("click", () => el.classList.toggle("collapsed"));
  (runEls.current || $("#run-phases")).appendChild(el);
  runEls.agents[ev.agent] = el;
}

function appendDelta(id, text) {
  const el = runEls.agents[id];
  if (!el) return;
  const body = el.querySelector(".ra-body");
  const atBottom = body.scrollHeight - body.scrollTop - body.clientHeight < 40;
  body.textContent += text;
  if (atBottom) body.scrollTop = body.scrollHeight;
}

function appendSearch(id, query) {
  const el = runEls.agents[id];
  if (!el) return;
  const body = el.querySelector(".ra-body");
  const atBottom = body.scrollHeight - body.scrollTop - body.clientHeight < 40;
  body.textContent += query
    ? `\n🔍 Webbsökning: "${query}"\n`
    : "\n🔍 Webbsökning\n";
  if (atBottom) body.scrollTop = body.scrollHeight;
}

function finishAgent(ev) {
  const el = runEls.agents[ev.agent];
  if (!el) return;
  const st = el.querySelector(".ra-state");
  st.textContent = "klar";
  st.className = "ra-state done";
  const foot = el.querySelector(".ra-foot");
  foot.hidden = false;
  foot.innerHTML = `<span>${ev.chars || 0} tecken</span>`;
  if (ev.searches) {
    const s = document.createElement("span");
    s.textContent = `🔍 ${ev.searches} webbsökning${ev.searches === 1 ? "" : "ar"}`;
    foot.appendChild(s);
  }
  if (ev.deliverable && state.team && state.jobId) {
    const a = document.createElement("button");
    a.type = "button";
    a.className = "show-result";
    a.textContent = "Visa resultat ▸";
    a.addEventListener("click", () =>
      openDoc(state.team.id, state.jobId, ev.deliverable)
    );
    foot.appendChild(a);
  }
}

function errorAgent(ev) {
  const el = runEls.agents[ev.agent];
  if (!el) return;
  const st = el.querySelector(".ra-state");
  st.textContent = "fel";
  st.className = "ra-state error";
  el.querySelector(".ra-body").textContent += "\n\n⚠ " + (ev.message || "Fel");
}

/* ===================================================================== *
 *  RESULTATPANEL (sidopanel)
 * ===================================================================== */
function openPanel(title, html, docxUrl) {
  $("#panel-title").textContent = title;
  $("#panel-body").innerHTML = html;
  $("#panel-body").scrollTop = 0;
  const dl = $("#panel-download");
  if (docxUrl) {
    dl.href = docxUrl;
    dl.hidden = false;
  } else {
    dl.removeAttribute("href");
    dl.hidden = true;
  }
  $("#panel").hidden = false;
}

function closePanel() {
  $("#panel").hidden = true;
}

async function openDoc(teamId, jobId, name) {
  openPanel(name, "<p class='muted'>Laddar…</p>");
  try {
    const data = await apiJSON(
      `/api/teams/${teamId}/jobs/${jobId}/doc/${encodeURIComponent(name)}`
    );
    const docxUrl = `/api/teams/${teamId}/jobs/${jobId}/doc/${encodeURIComponent(name)}/docx`;
    openPanel(name, data.html || "", docxUrl);
  } catch (err) {
    closePanel();
    toast("Kunde inte öppna dokumentet: " + err.message);
  }
}

async function openAttachment(teamId, jobId, name) {
  openPanel("📎 " + name, "<p class='muted'>Laddar…</p>");
  try {
    const data = await apiJSON(
      `/api/teams/${teamId}/jobs/${jobId}/attachment/${encodeURIComponent(name)}`
    );
    const body =
      "<p class='muted'>Extraherad text — det här är vad teamet fick som kontext.</p>" +
      "<pre class='att-text'>" + escapeHtml(data.text || "") + "</pre>";
    openPanel("📎 " + name, body);
  } catch (err) {
    closePanel();
    toast("Kunde inte öppna bilagan: " + err.message);
  }
}

$("#panel-close").addEventListener("click", closePanel);
$("#panel").addEventListener("click", (e) => {
  if (e.target.id === "panel") closePanel();
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !$("#panel").hidden) closePanel();
});

/* ---- Tema-toggle ---- */
(function initTheme() {
  const saved = localStorage.getItem("mp-theme");
  if (saved === "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
  }
  function icon() {
    $("#theme-toggle").textContent =
      document.documentElement.getAttribute("data-theme") === "dark" ? "☀️" : "🌙";
  }
  icon();
  $("#theme-toggle").addEventListener("click", () => {
    const html = document.documentElement;
    if (html.getAttribute("data-theme") === "dark") {
      html.removeAttribute("data-theme");
      localStorage.setItem("mp-theme", "light");
    } else {
      html.setAttribute("data-theme", "dark");
      localStorage.setItem("mp-theme", "dark");
    }
    icon();
  });
})();

/* ---- Start ---- */
loadDashboard();
