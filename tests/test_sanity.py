# type: ignore

from enum import IntEnum
from inspect import isclass, signature
from typing import List

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3.exceptions import ContractLogicError, ContractPanicError
from web3.contract.contract import ContractFunction, ContractEvent

import autonity
from autonity import contracts
from autonity.contracts.accountability import BaseSlashingRates, Factors

BINDINGS = [
    contracts.accountability.Accountability,
    contracts.acu.ACU,
    contracts.autonity.Autonity,
    contracts.inflation_controller.InflationController,
    contracts.liquid_logic.LiquidLogic,
    contracts.omission_accountability.OmissionAccountability,
    contracts.oracle.Oracle,
    contracts.stabilization.Stabilization,
    contracts.supply_control.SupplyControl,
    contracts.upgrade_manager.UpgradeManager,
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
    BaseSlashingRates: BaseSlashingRates(0, 0, 0),
    Factors: Factors(0, 0, 0),
}


def pytest_generate_tests(metafunc):
    if "test_case" not in metafunc.fixturenames:
        return

    test_cases = []
    ids = []

    for binding in BINDINGS:
        for attr_name in dir(binding):
            if not attr_name.startswith("_"):
                test_cases.append((binding.__name__, attr_name))
                ids.append(f"{binding.__name__}.{attr_name}")

    metafunc.parametrize("test_case", test_cases, ids=ids)


def get_test_args(function):
    return tuple(
        _get_arg_value(param.annotation)
        for param in signature(function).parameters.values()
        if param.name != "self"
    )


def _get_arg_value(type_):
    if isclass(type_):
        if issubclass(type_, IntEnum):
            return TEST_INPUTS[int]
        if issubclass(type_, tuple):
            inputs = [
                _get_arg_value(param.annotation)
                for param in signature(type_).parameters.values()
            ]
            return type_(*inputs)
    return TEST_INPUTS[type_]


def test_bindings_with_arbitrary_inputs(w3, test_case):
    binding_name, attr_name = test_case
    factory_function = getattr(autonity, binding_name)

    if factory_function is autonity.LiquidLogic:
        aut = autonity.Autonity(w3)
        validator = aut.get_validator(aut.get_validators()[0])
        binding = factory_function(w3, validator.liquid_state_contract)
    else:
        binding = factory_function(w3)

    attr = getattr(binding, attr_name)
    args = () if isinstance(attr, ContractEvent) else get_test_args(attr)

    try:
        return_value = attr(*args)
        assert return_value is not None
        if isinstance(return_value, ContractFunction):
            assert return_value.build_transaction()
    except (ContractLogicError, ContractPanicError):
        # The contract execution doesn't have to be successful,
        # only creating the Web3.py contract function instance does
        pass
