# type: ignore

from dataclasses import is_dataclass
from enum import IntEnum
from inspect import isclass, signature
from typing import Callable, List

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.contract.contract import ContractFunction, ContractEvent

import autonity
from autonity import factory
from autonity.constants import AUTONITY_CONTRACT_VERSION
from autonity.contracts.accountability import BaseSlashingRates, Factors
from autonity.contracts.autonity import Config, Contracts, Policy, Protocol
from autonity.factory import LiquidLogic
from tests.mock_provider import CONTRACT_ADDRESSES, MockProvider, make_address

BINDINGS = [attr for attr in autonity.__dict__.values() if isinstance(attr, Callable)]


def _fake_config(_: Web3) -> Config:
    return Config(
        policy=Policy(
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            make_address(11),
            make_address(12),
            0,
            0,
        ),
        contracts=Contracts(
            CONTRACT_ADDRESSES["accountability"],
            CONTRACT_ADDRESSES["oracle"],
            CONTRACT_ADDRESSES["acu"],
            CONTRACT_ADDRESSES["supply_control"],
            CONTRACT_ADDRESSES["stabilization"],
            CONTRACT_ADDRESSES["upgrade_manager"],
            CONTRACT_ADDRESSES["inflation_controller"],
            CONTRACT_ADDRESSES["omission_accountability"],
            CONTRACT_ADDRESSES["auctioneer"],
        ),
        protocol=Protocol(
            make_address(13),
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ),
        contract_version=AUTONITY_CONTRACT_VERSION,
    )


factory._config.cache_clear()
factory._config = _fake_config


TEST_INPUTS = {
    bool: True,
    int: 1,
    str: "",
    ChecksumAddress: make_address(0),
    HexBytes: HexBytes(val=""),
    List[int]: [1],
    List[str]: [""],
    List[ChecksumAddress]: [make_address(0)],
    BaseSlashingRates: BaseSlashingRates(0, 0, 0),
    Factors: Factors(0, 0, 0),
}


def pytest_generate_tests(metafunc):
    if "test_input" not in metafunc.fixturenames:
        return

    w3 = Web3(MockProvider())
    test_inputs = []
    ids = []

    for binding in BINDINGS:
        if binding is LiquidLogic:
            contract = binding(w3, CONTRACT_ADDRESSES["liquid_logic"])
        else:
            contract = binding(w3)

        for attr_name in dir(contract):
            if attr_name.startswith("_"):
                continue
            attr = getattr(contract, attr_name)
            if isinstance(attr, Callable):
                if isinstance(attr, ContractEvent):
                    test_inputs.append((attr, tuple()))
                    ids.append(f"{binding.__name__}.{attr_name}")
                elif hasattr(attr, "_f"):  # multimethod
                    for i, method in enumerate(attr._f.methods, 1):
                        test_inputs.append((attr, get_test_args(method.implementation)))
                        ids.append(f"{binding.__name__}.{attr_name}/{i}")
                else:
                    test_inputs.append((attr, get_test_args(attr)))
                    ids.append(f"{binding.__name__}.{attr_name}")

    metafunc.parametrize("test_input", test_inputs, ids=ids)


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
        if is_dataclass(type_):
            inputs = [
                _get_arg_value(param.annotation)
                for param in signature(type_).parameters.values()
            ]
            return type_(*inputs)
    return TEST_INPUTS[type_]


def test_bindings_with_arbitrary_inputs(test_input):
    binding, args = test_input
    return_value = binding(*args)
    assert return_value is not None

    if isinstance(return_value, ContractFunction):
        built_transaction = return_value.build_transaction(
            {
                "from": make_address(14),
                "nonce": 0,
                "gas": 210000,
                "gasPrice": 1,
                "chainId": 1,
            }
        )
        assert built_transaction["data"].startswith("0x")
