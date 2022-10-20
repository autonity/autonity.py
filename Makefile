
.PHONY: install check check-types check-syntax check-tests test

install:
	pip install -e .[dev]

check: check-types check-syntax check-tests

check-types:
	mypy autonity tests

check-syntax:
	flake8 autonity tests
	pylint autonity tests

check-tests test:
	python -m unittest discover tests
