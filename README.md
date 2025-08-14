# Statistical Modeling & Risk Simulation

Time-dependent simulations (Lorenz system) with scenario sweeps, Monte Carlo stress tests, and reproducible reporting.

## Highlights
- Parameterized ODE simulation (Lorenz)
- Scenario sweeps via YAML config
- Aggregate metrics + matplotlib export

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run a set of scenarios
python src/simulate_odes.py --scenarios configs/scenarios.yml --out data/processed.parquet

# analyze and produce figures
python src/analyze_results.py --infile data/processed.parquet --out reports/figures
```
> If Parquet support is missing locally, the script will fall back to CSV automatically.

## Repo Structure
```
configs/            # YAML scenario definitions
src/                # simulators + analysis
notebooks/          # EDA/final report (optional)
reports/figures/    # exported plots
data/               # raw/processed (ignored by git)
```

## Requirements
- Python 3.9+
- numpy, pandas, scipy, matplotlib, pyyaml, jupyter

---
Created 2025-08-14
