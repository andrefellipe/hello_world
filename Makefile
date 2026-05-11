.PHONY: help setup install format lint typecheck test audit validate matrix clean mutate docs

.DEFAULT_GOAL := help

help: ## Show this help menu
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: install ## Bootstrap the local development environment (installs dependencies and git hooks)
	poetry run pre-commit install
	poetry run pre-commit install --hook-type commit-msg

install: ## Install the project dependencies using Poetry
	poetry install

format: ## Run Ruff to format the codebase and fix auto-fixable errors
	poetry run ruff format .
	poetry run ruff check --fix .

lint: ## Run Ruff to check for linting errors without fixing them
	poetry run ruff check .

typecheck: ## Run Mypy for strict static type checking
	poetry run mypy src

test: ## Run Pytest with 100% coverage enforcement and XML reporting
	poetry run pytest --cov=hello_world --cov-report=term-missing --cov-report=xml --cov-fail-under=100

audit: ## Run pip-audit to scan dependencies for known security vulnerabilities
	poetry run pip-audit

docs: ## Serve the documentation locally with live hot-reloading
	poetry run mkdocs serve --livereload

validate: format lint typecheck test audit ## Run the complete local CI pipeline

matrix: ## Run the test suite across all supported Python versions using Nox
	poetry run nox

clean: ## Remove virtual environments, cache directories, and build artifacts
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	rm -rf .nox
	rm -f .coverage coverage.xml
	find . -type d -name "__pycache__" -exec rm -rf {} +

mutate: ## Run Mutmut for dual-tier mutation testing (bypasses Poetry hooks)
	poetry install --no-root
	rm -rf mutants/ .coverage
	.venv/bin/mutmut run; STATUS=$$?; poetry install; exit $$STATUS
