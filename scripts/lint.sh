#!/usr/bin/env bash
set -euo pipefail

if [ -f ".venv/Scripts/pylint" ]; then
    PYLINT=".venv/Scripts/pylint"
else
    PYLINT=".venv/bin/pylint"
fi

echo "→ Running pylint..."
$PYLINT calculator/ main.py tests/
echo "✓ Lint passed."
