from inspect import signature
from typing import Callable

from web3 import Web3

from autonity import factories, networks
from autonity.constants import AUTONITY_CONTRACT_ADDRESS
from autonity.contracts import ierc20


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
    ierc20.IERC20,
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
            contract = binding(w3, validator.liquid_contract)  # type: ignore
        elif wrapper.__name__ == "IERC20":
            contract = wrapper(w3, AUTONITY_CONTRACT_ADDRESS)  # type: ignore
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
