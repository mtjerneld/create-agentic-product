# Startar Creative Product Team-appen lokalt (Windows/PowerShell).
$ErrorActionPreference = "Stop"

Set-Location (Join-Path $PSScriptRoot "..")

if (-not (Test-Path ".env")) {
    Write-Host "OBS: ingen .env hittades. Kopiera .env.example till .env och lägg in din"
    Write-Host "ANTHROPIC_API_KEY innan du kör en körning."
}

if (-not (Test-Path ".venv")) {
    Write-Host "Skapar virtuell miljö (.venv)..."
    python -m venv .venv
}

$venvPython = Join-Path (Resolve-Path ".venv") "Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    throw "Hittar inte $venvPython - virtuell miljö skapades inte korrekt."
}

Write-Host "Installerar beroenden..."
& $venvPython -m pip install -q -r server/requirements.txt

$port = if ($env:PORT) { $env:PORT } else { "8000" }
Write-Host ""
Write-Host "Appen körs på http://localhost:$port"
Write-Host ""

Set-Location server
& $venvPython -m uvicorn app:app --host 0.0.0.0 --port $port
