from inspect import signature
from typing import Callable

from web3 import Web3

from autonity import contracts, networks


WRAPPER_CLASSES = [
    contracts.Accountability,
    contracts.ACU,
    contracts.Autonity,
    contracts.InflationController,
    contracts.Liquid,
    contracts.NonStakableVesting,
    contracts.Oracle,
    contracts.Stabilization,
    contracts.SupplyControl,
    contracts.UpgradeManager,
]


def pytest_generate_tests(metafunc):
    if "contract_function" not in metafunc.fixturenames:
        return

    functions = []
    ids = []

    for wrapper_class in WRAPPER_CLASSES:
        w3 = Web3(networks.piccadilly.http_provider)

        if wrapper_class is contracts.Liquid:
            autonity = contracts.Autonity(w3)
            validator = autonity.get_validator(autonity.get_validators()[0])
            contract = wrapper_class(w3, validator.liquid_contract)
        else:
            contract = wrapper_class(w3)

        for attr_name in dir(contract):
            if attr_name.startswith("_"):
                continue
            attr = getattr(contract, attr_name)
            if isinstance(attr, Callable) and len(signature(attr).parameters) == 0:
                functions.append(attr)
                ids.append(f"{wrapper_class.__name__}.{attr_name}()")

    metafunc.parametrize("contract_function", functions, ids=ids)


def test_basic_calls(contract_function):
    assert contract_function() is not None
