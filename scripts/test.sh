#!/usr/bin/env bash
set -euo pipefail

if [ -f ".venv/Scripts/pytest" ]; then
    PYTEST=".venv/Scripts/pytest"
else
    PYTEST=".venv/bin/pytest"
fi

echo "→ Running tests..."
$PYTEST -v
