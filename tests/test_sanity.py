# type: ignore

from enum import IntEnum
from inspect import isclass, signature
from typing import Callable, List

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.exceptions import ContractLogicError, ContractPanicError
from web3.contract.contract import ContractFunction

import autonity
from autonity.constants import AUTONITY_CONTRACT_ADDRESS
from autonity.contracts import ierc20


FACTORIES = [attr for attr in autonity.__dict__.values() if isinstance(attr, Callable)]
BINDINGS = FACTORIES + [
    ierc20.IERC20,  # IERC20 is used internally by aut-cli, not part of the public API
]

TEST_INPUTS = {
    bool: True,
    int: 1,
    str: "",
    ChecksumAddress: "0x0123456789abcDEF0123456789abCDef01234567",
    HexBytes: HexBytes(val=""),
    List[int]: [1],
    List[str]: [""],
    List[ChecksumAddress]: ["0x0123456789abcDEF0123456789abCDef01234567"],
}


def pytest_generate_tests(metafunc):
    if "contract_function" not in metafunc.fixturenames:
        return

    functions = []
    ids = []

    for binding in BINDINGS:
        w3 = Web3(autonity.networks.piccadilly.http_provider)

        if binding.__name__ == "Liquid":
            aut = autonity.Autonity(w3)
            validator = aut.get_validator(aut.get_validators()[0])
            contract = binding(w3, validator.liquid_contract)
        elif binding.__name__ == "IERC20":
            contract = binding(w3, AUTONITY_CONTRACT_ADDRESS)
        else:
            contract = binding(w3)

        for attr_name in dir(contract):
            if attr_name.startswith("_"):
                continue
            attr = getattr(contract, attr_name)
            if isinstance(attr, Callable):
                functions.append(attr)
                ids.append(f"{binding.__name__}.{attr_name}")

    metafunc.parametrize("contract_function", functions, ids=ids)


def get_input_value(type_):
    if isclass(type_):
        if issubclass(type_, IntEnum):
            return TEST_INPUTS[int]
        if issubclass(type_, tuple):
            inputs = [
                get_input_value(param.annotation)
                for param in signature(type_).parameters.values()
            ]
            return type_(*inputs)
    return TEST_INPUTS[type_]


def test_bindings_with_arbitrary_inputs(contract_function):
    inputs = {}
    if not isclass(contract_function):  # Not a ContractEvent
        inputs = [
            get_input_value(param.annotation)
            for param in signature(contract_function).parameters.values()
        ]
    try:
        return_value = contract_function(*inputs)
        assert return_value is not None
        if isinstance(return_value, ContractFunction):
            assert return_value.build_transaction()
    except (ContractLogicError, ContractPanicError):
        # The contract execution doesn't have to be successful,
        # only creating the Web3.py contract function instance does
        pass
