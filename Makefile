
install:
	poetry install

test:
	poetry run pytest -s

build: check
	poetry build

.PHONY: install test build
