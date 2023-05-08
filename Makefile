
.PHONY: check check-types check-syntax check-tests test

check: check-types check-syntax check-tests

check-syntax check-types:
	hatch run lint

check-tests test:
	hatch run test

coverage:
	hatch run cov

clean:
	hatch run clean

