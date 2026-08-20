#!/usr/bin/env bash
# Local CI: run before committing (Linux / macOS).
set -euo pipefail
cd "$(dirname "$0")"

echo "==> validate logos.json + art references"
python3 validate.py ..

echo "==> CI OK"
