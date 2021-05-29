
install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=algorithms --cov-report xml tests/

build: check
	poetry build

.PHONY: install test build
