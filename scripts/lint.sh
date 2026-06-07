#!/usr/bin/env bash
set -euo pipefail

echo "→ Running pylint..."
.venv/bin/pylint calculator/ main.py tests/
echo "✓ Lint passed."
