BIN = ./.venv/bin
SRC = ./src/*.py
all: default
default: format lint typecheck test run

run:
	$(BIN)/python ./src/main.py

install: clean
	uv venv
	uv pip install -r requirements.txt

format:
	$(BIN)/ruff format

lint:
	$(BIN)/ruff check

typecheck:
	$(BIN)/mypy $(SRC)

test: format typecheck
	pytest $(SRC)

clean:
	rm -rf ./venv
	rm -rf ./.venv
	rm -rf ./.mypy_cache
	
