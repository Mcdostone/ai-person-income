.PHONY: run
PYTHON = python3
.DEFAULT_GOAL = run

run:
	$(PYTHON) ./project/main.py -f ./project/census-income-sample.data

run-full:
	$(PYTHON) ./project/main.py -f ./project/census-income-data.data