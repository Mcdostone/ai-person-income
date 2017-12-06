.PHONY: run
PYTHON = python3
.DEFAULT_GOAL = run

install: 
	pip install -r requirements.txt

run:
	$(PYTHON) ./project/main.py -f ./project/census-income-data.data -t ./project/census-income-test.test --save income.pdf

clean:
	rm *.pdf