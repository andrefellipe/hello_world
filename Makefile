.PHONY: install format lint typecheck test mutate clean

install:
	poetry install

format:
	poetry run ruff format .
	poetry run ruff check --fix .

lint:
	poetry run ruff check .

typecheck:
	poetry run mypy src

test:
	poetry run pytest

mutate:
	poetry run mutmut run

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
