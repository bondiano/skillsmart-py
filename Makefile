
install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=algorithms tests/

build: check
	poetry build

.PHONY: install test build
