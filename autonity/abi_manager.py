# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
ABIManager class
"""

import json
from os import path
from typing import Dict

from web3.contract.contract import ABI

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
            _CACHE[contract_name] = ABIManager.load_abi_file(
                path.join(path.dirname(__file__), "abi", f"{contract_name}.abi")
            )

        return _CACHE[contract_name]

    @staticmethod
    def load_abi_file(file_name: str) -> ABI:
        """
        Load an ABI from a file.
        """
        with open(file_name, "r", encoding="utf-8") as abi_f:
            return json.load(abi_f)
