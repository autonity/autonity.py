# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
ABIManager class
"""

import autonity.abi

import importlib.resources  # type: ignore
import json
from web3.contract.contract import ABI
from typing import Dict


_CACHE: Dict[str, ABI] = {}


class ABIManager:
    """
    Access to bundled contract ABIs
    """

    @staticmethod
    def load_abi(contract_name: str) -> ABI:
        """
        Load (and cache) the ABI for a protocol contract.
        """
        if contract_name not in _CACHE:
            text = importlib.resources.read_text(autonity.abi, contract_name + ".abi")
            _CACHE[contract_name] = json.loads(text)

        return _CACHE[contract_name]

    @staticmethod
    def load_abi_file(file_name: str) -> ABI:
        """
        Load an ABI from a file.
        """
        with open(file_name, "r", encoding="utf8") as abi_f:
            return json.load(abi_f)
