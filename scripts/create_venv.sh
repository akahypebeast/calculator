#!/usr/bin/env bash
set -euo pipefail

echo "→ Creating virtual environment..."
python -m venv .venv

echo "→ Installing dependencies..."
.venv/bin/pip install --upgrade pip -q
.venv/bin/pip install -r requirements.txt -q

echo "✓ Environment ready. Activate with: source .venv/bin/activate"
