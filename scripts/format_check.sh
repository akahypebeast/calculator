#!/usr/bin/env bash
set -euo pipefail

if [ -f ".venv/Scripts/black" ]; then
    BLACK=".venv/Scripts/black"
else
    BLACK=".venv/bin/black"
fi

echo "→ Checking code formatting..."
$BLACK --check calculator/ main.py tests/
echo "✓ Format check passed."
