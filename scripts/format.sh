#!/usr/bin/env bash
set -euo pipefail

if [ -f ".venv/Scripts/black" ]; then
    BLACK=".venv/Scripts/black"
else
    BLACK=".venv/bin/black"
fi

echo "→ Formatting code with black..."
$BLACK calculator/ main.py tests/
echo "✓ Formatting done."
