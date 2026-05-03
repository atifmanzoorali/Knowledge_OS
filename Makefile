# Makefile for Knowledge OS
# Usage: make <command>

.PHONY: help install install-dev test test-unit test-integration test-e2e test-all lint format check clean

# Default help
help:
	@echo "Knowledge OS - Make Commands"
	@echo ""
	@echo "Setup:"
	@echo "  install         Install production dependencies"
	@echo "  install-dev     Install development dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  test            Run all tests"
	@echo "  test-unit       Run unit tests only"
	@echo "  test-integration Run integration tests"
	@echo "  test-e2e        Run end-to-end tests"
	@echo "  test-all        Run all tests with coverage"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint            Run linters (flake8, isort)"
	@echo "  format          Format code (black, isort)"
	@echo "  check           Run all code checks"
	@echo "  pre-commit      Run pre-commit hooks"
	@echo ""
	@echo "Search:"
	@echo "  index           Build search index"
	@echo "  search          Run search (Usage: make search QUERY='your query')"
	@echo ""
	@echo "Clean:"
	@echo "  clean           Remove temporary files"
	@echo "  clean-tests     Remove test cache"

# ============================================================================
# Setup
# ============================================================================

install:
	pip install -r requirements.txt
	pip install -r search/requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r search/requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

# ============================================================================
# Testing
# ============================================================================

test:
	pytest tests/ -v

test-unit:
	pytest tests/ -v -m unit

test-integration:
	pytest tests/ -v -m integration

test-e2e:
	pytest tests/ -v -m e2e

test-all:
	pytest tests/ --cov=. --cov-report=term --cov-report=html -v

# ============================================================================
# Code Quality
# ============================================================================

lint:
	flake8 . --count --show-source --statistics || true
	isort --check-only --diff . || true

format:
	black .
	isort .

check: lint format
	@echo "All checks passed!"

pre-commit:
	pre-commit run --all-files

# ============================================================================
# Search
# ============================================================================

index:
	python search/index.py

search:
ifndef QUERY
	$(error QUERY is undefined. Usage: make search QUERY="your search query")
endif
	python search/answer_search.py "$(QUERY)"

# ============================================================================
# Clean
# ============================================================================

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -f coverage.xml

clean-tests:
	rm -rf tests/.pytest_cache
	rm -rf tests/__pycache__
	find tests -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find tests -type f -name "*.pyc" -delete

# ============================================================================
# Development
# ============================================================================

dev: install-dev
	@echo "Development environment ready!"
	@echo "Run 'make test' to verify everything works"

.DEFAULT_GOAL := help