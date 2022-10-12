

install:
	pipenv install -d

check: check-types check-syntax check-tests


check-types:
	pipenv run mypy autonity tests

check-syntax:
	pipenv run flake8 autonity tests
	pipenv run pylint autonity
	pipenv run pylint --rcfile=pylintrc-tests tests

check-tests:
	pipenv run pytest tests