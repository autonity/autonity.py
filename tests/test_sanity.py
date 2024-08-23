from inspect import signature
from typing import Callable

from web3 import Web3

from autonity import factories, networks


WRAPPERS = [
    factories.Accountability,
    factories.ACU,
    factories.Autonity,
    factories.InflationController,
    factories.Liquid,
    factories.NonStakableVesting,
    factories.Oracle,
    factories.Stabilization,
    factories.SupplyControl,
    factories.UpgradeManager,
]


def pytest_generate_tests(metafunc):
    if "contract_function" not in metafunc.fixturenames:
        return

    functions = []
    ids = []

    for wrapper in WRAPPERS:
        w3 = Web3(networks.piccadilly.http_provider)

        if wrapper.__name__ == "Liquid":
            autonity = factories.Autonity(w3)
            validator = autonity.get_validator(autonity.get_validators()[0])
            contract = wrapper(w3, validator.liquid_contract)
        else:
            contract = wrapper(w3)

        for attr_name in dir(contract):
            if attr_name.startswith("_"):
                continue
            attr = getattr(contract, attr_name)
            if isinstance(attr, Callable) and len(signature(attr).parameters) == 0:
                functions.append(attr)
                ids.append(f"{wrapper.__name__}.{attr_name}()")

    metafunc.parametrize("contract_function", functions, ids=ids)


def test_basic_calls(contract_function):
    assert contract_function() is not None
