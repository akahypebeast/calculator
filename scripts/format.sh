#!/usr/bin/env bash
set -euo pipefail

echo "→ Formatting code with black..."
.venv/bin/black .
echo "✓ Formatting done."
