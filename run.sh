#!/usr/bin/env bash
set -euo pipefail
PY=python3
VENV=.venv

$PY -m venv "$VENV"
source "$VENV/bin/activate"
pip install -U pip
pip install -r requirements.txt

$PY src/simulate_odes.py --scenarios configs/scenarios.yml --out data/processed.parquet
$PY src/analyze_results.py --infile data/processed.parquet --out reports/figures

echo "Done. See reports/figures/ for output."