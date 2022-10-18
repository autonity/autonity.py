

install:
	pipenv install -d

check: check-types check-syntax check-tests


check-types:
	pipenv run mypy autonity tests

check-syntax:
	pipenv run flake8 autonity tests
	pipenv run pylint autonity tests

check-tests test:
	pipenv run python -m unittest discover tests
