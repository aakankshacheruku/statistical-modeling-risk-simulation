PY=python3
VENV=.venv

.PHONY: venv install run clean figures

venv:
	$(PY) -m venv $(VENV)

install: venv
	. $(VENV)/bin/activate && pip install -U pip && pip install -r requirements.txt

run: install
	. $(VENV)/bin/activate && $(PY) src/simulate_odes.py --scenarios configs/scenarios.yml --out data/processed.parquet
	. $(VENV)/bin/activate && $(PY) src/analyze_results.py --infile data/processed.parquet --out reports/figures

figures:
	@echo "Figures will be in reports/figures/"

clean:
	rm -rf $(VENV) data/*.parquet data/*.csv reports/figures/*.png