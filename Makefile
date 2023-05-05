
.PHONY: check check-types check-syntax check-tests test

check: check-types check-syntax check-tests

check-types:
	mypy autonity tests

check-syntax:
	hatch run lint

check-tests test:
	hatch run test

coverage:
	hatch run cov

clean:
	hatch run clean

