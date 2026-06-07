#!/usr/bin/env bash
set -euo pipefail

echo "→ Checking code formatting..."
.venv/bin/black --check .
echo "✓ Format check passed."
