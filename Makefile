
install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run coverage run -m pytest

build: check
	poetry build

.PHONY: install test build
