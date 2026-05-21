#!/usr/bin/env bash
# Startar Creative Product Team-appen lokalt.
set -e

cd "$(dirname "$0")/.."
ROOT="$(pwd)"

if [ ! -f .env ]; then
  echo "OBS: ingen .env hittades. Kopiera .env.example till .env och lägg in din"
  echo "ANTHROPIC_API_KEY innan du kör en körning."
fi

if [ ! -d .venv ]; then
  echo "Skapar virtuell miljö (.venv)…"
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate
echo "Installerar beroenden…"
pip install -q -r server/requirements.txt

PORT="${PORT:-8000}"
echo ""
echo "Appen körs på http://localhost:${PORT}"
echo ""
cd server
exec uvicorn app:app --host 0.0.0.0 --port "${PORT}"
