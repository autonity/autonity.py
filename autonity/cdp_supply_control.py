# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the CDPSupplyControl Web3.py external module
"""

from __future__ import annotations

from autonity.abi_manager import ABIManager

import os

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import ChecksumAddress, Wei

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-arguments

CONTRACT_ADDRESS = "0x47e9Fbef8C83A1714F1951F142132E6e90F5fa5D"
"""
The default CDPSupplyControl contract address.
"""


def get_contract_version() -> str:
    """
    Returns the version of the Autonity contract which this library is aligned with,
    and that is bundled with the library.
    """
    version_path = os.path.join(os.path.dirname(__file__), "abi", "autonity-commit.txt")
    if not os.path.exists(version_path):
        return "N/A"
    with open(version_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def get_contract_abi_path() -> str:
    """
    Returns the Autonity contract ABI path bundled with the library.
    This can be used in to load the ABI from a 3rd party app or library
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "abi", "CDPSupplyControl.abi")
    )


class CDPSupplyControl(object):
    """
    Web3 module representing CDPSupplyControl-specific API.
    """

    def __init__(self, web3: Web3):
        super().__init__(
            web3,
            web3.to_checksum_address(CONTRACT_ADDRESS),
            ABIManager.load_abi("CDPSupplyControl"),
        )

    @staticmethod
    def address() -> ChecksumAddress:
        """
        Return the deterministic address of the CDPSupplyControl contract.
        """
        return Web3.to_checksum_address(CONTRACT_ADDRESS)

    def burn(self) -> ContractFunction:
        """
        Simulate burn of tokens by depositing it to the supply
        See `burn` on the CDPSupplyControl contract.
        Mutability: payable
        """
        return self.contract.functions.burn().call()

    def deposit(self) -> ContractFunction:
        """
        deposity liquidity to the supply
        See `deposit` on the CDPSupplyControl contract.
        Mutability: payable
        """
        return self.contract.functions.deposit().call()

    def getAvailableSupply(self) -> Wei:
        """
        retrieve the current available supply
        See `getAvailableSupply` on the CDPSupplyControl contract.
        Mutability: view
        """
        return self.contract.functions.getAvailableSupply().call()

    def getCDPAddress(self) -> ChecksumAddress:
        """

        See `getCDPAddress` on the CDPSupplyControl contract.
        Mutability: view
        """
        return self.contract.functions.getCDPAddress().call()

    def getTotalSupply(self) -> Wei:
        """
        retrieve the total supply deposited to the contract
        See `getTotalSupply` on the CDPSupplyControl contract.
        Mutability: view
        """
        return self.contract.functions.getTotalSupply().call()

    def mint(self, recipient: ChecksumAddress, amount: Wei) -> ContractFunction:
        """
        Issue ATN to a CDP owner
        See `mint` on the CDPSupplyControl contract.
        Mutability: nonpayable
        """
        return self.contract.functions.mint(recipient, amount).call()

    def setCDPAddress(self, _cdp: ChecksumAddress) -> ContractFunction:
        """
        Set the CDP contract address,
        See `setCDPAddress` on the CDPSupplyControl contract.
        Mutability: nonpayable
        """
        return self.contract.functions.setCDPAddress(_cdp).call()

    def withdraw(self, quantity: Wei) -> ContractFunction:
        """
        Withdraw liquidity from the supply
        See `withdraw` on the CDPSupplyControl contract.
        Mutability: nonpayable
        """
        return self.contract.functions.withdraw(quantity).call()
