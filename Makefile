all: default
default: format lint typecheck test


run:
	./venv/bin/python ./src/main.py

install: clean
	python -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

format:
	./venv/bin/ruff format

lint:
	./venv/bin/ruff check

typecheck:
	./venv/bin/mypy ./src/*.py

test:
	./venv/bin/pytest ./src/*.py

clean:
	rm -rf ./venv