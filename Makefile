.PHONY: run
PYTHON = python3
.DEFAULT_GOAL = run

install: 
	pip install -r requirements.txt

run:
	$(PYTHON) ./project/main.py -f ./project/census-income-sample.data

run-full:
	$(PYTHON) ./project/main.py -f ./project/census-income-data.data

clean:
	rm *.pdf