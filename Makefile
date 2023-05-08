
.PHONY: check check-types check-syntax check-tests test

check: lint test

lint:
	hatch run lint

test:
	hatch run test

coverage:
	hatch run cov

clean:
	hatch run clean

