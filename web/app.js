"use strict";

const state = { brief: {}, team: null };

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

/* ---- Vyhantering ---- */
function showView(name) {
  $$(".view").forEach((v) => v.classList.toggle("active", v.id === "view-" + name));
  $$("#stepper li").forEach((li) => {
    const order = ["brief", "team", "run"];
    const here = order.indexOf(name);
    const mine = order.indexOf(li.dataset.step);
    li.classList.toggle("active", li.dataset.step === name);
    li.classList.toggle("done", mine < here);
  });
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

/* ---- Steg 1: Brief -> Team ---- */
$("#brief-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fd = new FormData(e.target);
  state.brief = Object.fromEntries(fd.entries());
  const btn = $("#brief-submit");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span>Sätter ihop teamet…';
  try {
    const resp = await fetch("/api/team", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ brief: state.brief }),
    });
    const data = await resp.json();
    if (!data.ok) throw new Error(data.error || "Okänt fel");
    state.team = data.team;
    renderTeam(data.team);
    showView("team");
  } catch (err) {
    toast("Kunde inte skapa team: " + err.message);
  } finally {
    btn.disabled = false;
    btn.textContent = "Sätt ihop teamet →";
  }
});

/* ---- Steg 2: Team-vy ---- */
function phaseOptions(selected) {
  const phases = [{ number: 0, name: "Koordinator" }].concat(state.team.phases || []);
  return phases
    .map(
      (p) =>
        `<option value="${p.number}" ${p.number === selected ? "selected" : ""}>` +
        `${p.number === 0 ? "" : "Fas " + p.number + ": "}${p.name}</option>`
    )
    .join("");
}

function renderTeam(team) {
  $("#team-rationale").textContent = team.rationale || "";

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
  (team.agents || []).forEach((a) => grid.appendChild(agentCard(a)));
}

function agentCard(a) {
  const el = document.createElement("div");
  el.className = "agent-card";
  el.dataset.name = a.name || slugify(a.title);
  el.dataset.emoji = a.emoji || "🧩";
  el.innerHTML = `
    <div class="ac-head">
      <span class="emoji">${a.emoji || "🧩"}</span>
      <span class="ac-title"><input class="f-title" value="${escapeAttr(a.title || "")}" /></span>
    </div>
    <label>Roll
      <textarea class="f-role" rows="3">${escapeHtml(a.role || "")}</textarea>
    </label>
    <div class="why">${escapeHtml(a.why || "")}</div>
    <div class="ac-foot">
      <select class="f-phase">${phaseOptions(a.phase ?? 1)}</select>
      <button type="button" class="remove">Ta bort</button>
    </div>`;
  el.querySelector(".remove").addEventListener("click", () => el.remove());
  return el;
}

$("#add-agent").addEventListener("click", () => {
  $("#team-grid").appendChild(
    agentCard({ name: "", title: "Ny agent", emoji: "✨", role: "", why: "Tillagd manuellt.", phase: 1 })
  );
});

$("#back-to-brief").addEventListener("click", () => showView("brief"));

function collectTeam() {
  const agents = $$("#team-grid .agent-card").map((el) => {
    const title = el.querySelector(".f-title").value.trim() || "Agent";
    return {
      name: el.dataset.name || slugify(title),
      title,
      emoji: el.dataset.emoji || "🧩",
      role: el.querySelector(".f-role").value.trim(),
      phase: parseInt(el.querySelector(".f-phase").value, 10) || 0,
      why: "",
    };
  });
  return { rationale: state.team.rationale, phases: state.team.phases, agents };
}

/* ---- Steg 3: Kör teamet ---- */
const runEls = { phases: {}, agents: {}, current: null };

$("#start-run").addEventListener("click", startRun);

async function startRun() {
  const team = collectTeam();
  if (!team.agents.length) {
    toast("Teamet behöver minst en agent.");
    return;
  }
  state.team = team;
  const task = $("#task").value.trim();

  $("#run-phases").innerHTML = "";
  $("#run-actions").hidden = true;
  runEls.phases = {};
  runEls.agents = {};
  runEls.current = null;
  setStatus("Startar…", "running");
  showView("run");

  try {
    const resp = await fetch("/api/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ team, task, brief: state.brief }),
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
    case "run_started":
      $("#run-task").textContent = ev.task || "";
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
    case "agent_done":
      finishAgent(ev);
      break;
    case "agent_error":
      errorAgent(ev);
      break;
    case "phase_done":
      if (runEls.phases[ev.phase]) runEls.phases[ev.phase].classList.add("done");
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

function finishAgent(ev) {
  const el = runEls.agents[ev.agent];
  if (!el) return;
  const st = el.querySelector(".ra-state");
  st.textContent = "klar";
  st.className = "ra-state done";
  const foot = el.querySelector(".ra-foot");
  foot.hidden = false;
  foot.innerHTML = `<span>${ev.chars || 0} tecken</span>`;
  if (ev.deliverable) {
    const a = document.createElement("a");
    a.textContent = "📄 " + ev.deliverable;
    a.addEventListener("click", () => openDoc(ev.deliverable));
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

$("#new-project").addEventListener("click", () => showView("brief"));

/* ---- Dokumentvisare ---- */
async function openDoc(name) {
  try {
    const resp = await fetch("/api/doc/" + encodeURIComponent(name));
    const text = await resp.text();
    $("#doc-title").textContent = name;
    $("#doc-body").textContent = text;
    $("#doc-modal").hidden = false;
  } catch (err) {
    toast("Kunde inte öppna dokumentet.");
  }
}
$("#doc-close").addEventListener("click", () => ($("#doc-modal").hidden = true));
$("#doc-modal").addEventListener("click", (e) => {
  if (e.target.id === "doc-modal") $("#doc-modal").hidden = true;
});

/* ---- Hjälpare ---- */
function escapeHtml(s) {
  return String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
}
function escapeAttr(s) {
  return escapeHtml(s).replace(/"/g, "&quot;");
}
