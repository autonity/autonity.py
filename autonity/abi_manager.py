# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Access to bundled contract ABIs
"""

import json
import warnings
from os import path
from typing import Dict

from web3.contract.contract import ABI

_CACHE: Dict[str, ABI] = {}


def load_abi(contract_name: str) -> ABI:
    """
    Load (and cache) the ABI for a protocol contract.
    """
    if contract_name not in _CACHE:
        _CACHE[contract_name] = load_abi_file(
            path.join(path.dirname(__file__), "abi", f"{contract_name}.abi")
        )

    return _CACHE[contract_name]


def load_abi_file(file_name: str) -> ABI:
    """
    Load an ABI from a file.
    """
    with open(file_name, "r", encoding="utf8") as abi_f:
        return json.load(abi_f)


class ABIManager:
    """
    Deprecated class kept for backwards compatibility.
    """

    @staticmethod
    def load_abi(contract_name: str) -> ABI:
        warnings.warn(
            "abi_manager.ABIManager.load_abi has been replaced with "
            "abi_manager.load_abi and will be removed in a future release",
            DeprecationWarning,
        )
        return load_abi(contract_name)

    @staticmethod
    def load_abi_file(file_name: str) -> ABI:
        warnings.warn(
            "abi_manager.ABIManager.load_abi_file has been replaced with "
            "abi_manager.load_abi_file and will be removed in a future release",
            DeprecationWarning,
        )
        return load_abi_file(file_name)
