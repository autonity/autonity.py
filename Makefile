
.PHONY: check check-types check-syntax check-tests test coverage lint clean build publish format update-abi release-prepare

check: lint test

lint:
	hatch run lint

test:
	hatch run test

coverage:
	hatch run cov

clean:
	hatch run clean

build:
	hatch build -t wheel

publish: clean build
	hatch publish

format:
	hatch run black autonity tests

update-abi:
	./scripts/update_abi

