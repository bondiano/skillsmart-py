
install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov-report xml

selfcheck:
	poetry check

check: selfcheck test

build: check
	poetry build

.PHONY: install test build