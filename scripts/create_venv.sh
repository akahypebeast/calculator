#!/usr/bin/env bash
set -euo pipefail

echo "→ Creating virtual environment..."
python -m venv .venv

echo "→ Installing dependencies..."

# Windows vs Unix path
if [ -f ".venv/Scripts/pip" ]; then
    PIP=".venv/Scripts/pip"
    PYTHON=".venv/Scripts/python"
else
    PIP=".venv/bin/pip"
    PYTHON=".venv/bin/python"
fi

$PIP install --upgrade pip -q
$PIP install -r requirements.txt -q

echo "✓ Environment ready."
