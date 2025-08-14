[![Python](https://img.shields.io/badge/Python-3.9%2B-informational)](#)
[![Type](https://img.shields.io/badge/Project-Risk%20Simulation-blue)](#)
[![Runs%20with](https://img.shields.io/badge/Makefile-supported-success)](#)

# Project


## Run with Make
```bash
make run
```

## Or run the script directly
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/simulate_odes.py --scenarios configs/scenarios.yml --out data/processed.parquet
python src/analyze_results.py --infile data/processed.parquet --out reports/figures
```

---
_Last updated 2025-08-14_
