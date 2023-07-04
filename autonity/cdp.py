# Copyright (C) 2015-2023 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the CDP Web3.py external module
"""

from __future__ import annotations

from autonity.abi_manager import ABIManager
from autonity.oracle import RoundData

import os

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import ChecksumAddress, Wei

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-arguments

CONTRACT_ADDRESS = "0x47c5e40890bcE4a473A49D7501808b9633F29782"
"""
The default CDP contract address.
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
        os.path.join(os.path.dirname(__file__), "abi", "CDP.abi")
    )


class CDP(object):
    """
    Web3 module representing CDP-specific API.
    """

    def __init__(self, web3: Web3):
        super().__init__(
            web3,
            web3.to_checksum_address(CONTRACT_ADDRESS),
            ABIManager.load_abi("CDP"),
        )

    @staticmethod
    def address() -> ChecksumAddress:
        """
        Return the deterministic address of the CDP contract.
        """
        return Web3.to_checksum_address(CONTRACT_ADDRESS)

    def available_to_withdraw(self, owner: ChecksumAddress) -> Wei:
        """
        Generated from CDP ABI
        See `availableToWithdraw` on the CDP contract.
        Quantity of collateral that is available to withdraw.
        Mutability: view
        """
        return self.contract.functions.availableToWithdraw(owner).call()

    def borrow(self, quantity: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `borrow` on the CDP contract.
        Borrow money using deposited collateral
        Mutability: nonpayable
        """
        return self.contract.functions.borrow(quantity)

    def borrow_capability(self, owner: ChecksumAddress) -> Wei:
        """
        Generated from CDP ABI
        See `borrowCapability` on the CDP contract.
        Maximum quantity of exchange coin that can be borrowed by the CDP owner.
        Mutability: view
        """
        return self.contract.functions.borrowCapability(owner).call()

    def claim_position(self, cdpOwner: ChecksumAddress) -> ContractFunction:
        """
        Generated from CDP ABI
        See `claimPosition` on the CDP contract.
        Liquidate a CDP
        Mutability: payable
        """
        return self.contract.functions.claimPosition(cdpOwner)

    def collateral(self, owner: ChecksumAddress) -> Wei:
        """
        Generated from CDP ABI
        See `collateral` on the CDP contract.
        Total collateral deposited by the user.
        Mutability: view
        """
        return self.contract.functions.collateral(owner).call()

    def debt(self, owner: ChecksumAddress) -> Wei:
        """
        Generated from CDP ABI
        See `debt` on the CDP contract.
        Total debt owed by an account (that is, principle ATN minted or &#34;debt position&#34;, plus &#34;borrow interest&#34; due).
        Mutability: view
        """
        return self.contract.functions.debt(owner).call()

    def deposit(self, quantity: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `deposit` on the CDP contract.
        Deposit a quantity of collateral in a CDP
        Mutability: nonpayable
        """
        return self.contract.functions.deposit(quantity)

    def finalize(self) -> ContractFunction:
        """
        Generated from CDP ABI
        See `finalize` on the CDP contract.
        Update teh price data by calling the oracle with the CDP symbols (collateral/debt)
        Mutability: nonpayable
        """
        return self.contract.functions.finalize()

    def get_borrow_interest_rate(self) -> Wei:
        """
        Generated from CDP ABI
        See `getBorrowInterestRate` on the CDP contract.
        Get the annualized interest borrow rate for the CDP
        Mutability: view
        """
        return self.contract.functions.getBorrowInterestRate().call()

    def get_collateral_token(self) -> ChecksumAddress:
        """
        Generated from CDP ABI
        See `getCollateralToken` on the CDP contract.
        Get the ERC20 token accepted as collateral by this CDP
        Mutability: view
        """
        return self.contract.functions.getCollateralToken().call()

    def get_liquidation_ratio(self) -> Wei:
        """
        Generated from CDP ABI
        See `getLiquidationRatio` on the CDP contract.
        TODO: implementGet the liquidation ration for the CDP
        Mutability: view
        """
        return self.contract.functions.getLiquidationRatio().call()

    def get_minimum_collateralization_ratio(self) -> Wei:
        """
        Generated from CDP ABI
        See `getMinimumCollateralizationRatio` on the CDP contract.
        Get the collateralization ratio for the CDP
        Mutability: view
        """
        return self.contract.functions.getMinimumCollateralizationRatio().call()

    def get_minimum_debt_requirement(self) -> Wei:
        """
        Generated from CDP ABI
        See `getMinimumDebtRequirement` on the CDP contract.
        Get the current minimum borrow threshold for the CDP
        Mutability: view
        """
        return self.contract.functions.getMinimumDebtRequirement().call()

    def get_precision(self) -> Wei:
        """
        Generated from CDP ABI
        See `getPrecision` on the CDP contract.
        Getter to retrieve the precision used in calculations for the CDP
        Mutability: pure
        """
        return self.contract.functions.getPrecision().call()

    def get_price_data(self) -> RoundData:
        """
        Generated from CDP ABI
        See `getPriceData` on the CDP contract.
        Get the current price data used by the CDP, price data are updated by the oracle
        Mutability: view
        """
        return self.contract.functions.getPriceData().call()

    def interest_owed(self, owner: ChecksumAddress) -> Wei:
        """
        Generated from CDP ABI
        See `interestOwed` on the CDP contract.
        Retrieve the interest onwed on a CDP at the current block height
        Mutability: view
        """
        return self.contract.functions.interestOwed(owner).call()

    def is_liquidatable(self, cdpOwner: ChecksumAddress) -> bool:
        """
        Generated from CDP ABI
        See `isLiquidatable` on the CDP contract.
        Check if a position is liquidatable. A position is liquidatable if the collateral is below the liquidation ratio
        Mutability: view
        """
        return self.contract.functions.isLiquidatable(cdpOwner).call()

    def is_liquidated(self, owner: ChecksumAddress) -> bool:
        """
        Generated from CDP ABI
        See `isLiquidated` on the CDP contract.
        Is the CDP in a liquidated state
        Mutability: view
        """
        return self.contract.functions.isLiquidated(owner).call()

    def repay(self) -> ContractFunction:
        """
        Generated from CDP ABI
        See `repay` on the CDP contract.
        Repay a debt with the debt token (plus interests)
        Mutability: payable
        """
        return self.contract.functions.repay()

    def set_borrow_interest_rate(self, rate: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setBorrowInterestRate` on the CDP contract.
        Set the annualized interest rate for borrowing
        Mutability: nonpayable
        """
        return self.contract.functions.setBorrowInterestRate(rate)

    def set_liquidation_ratio(self, ratio: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setLiquidationRatio` on the CDP contract.
        Set the liquidation ratio, expressed in percentage
        Mutability: nonpayable
        """
        return self.contract.functions.setLiquidationRatio(ratio)

    def set_minimum_collateralization_ratio(self, ratio: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setMinimumCollateralizationRatio` on the CDP contract.
        Set the collateralization ratio, expressed in percentage
        Mutability: nonpayable
        """
        return self.contract.functions.setMinimumCollateralizationRatio(ratio)

    def set_minimum_debt_requirement(self, threshold: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setMinimumDebtRequirement` on the CDP contract.
        Set the minimum borrow threshold.
        Mutability: nonpayable
        """
        return self.contract.functions.setMinimumDebtRequirement(threshold)

    def set_oracle_address(self, _oracle: ChecksumAddress) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setOracleAddress` on the CDP contract.
        Replace the price oracle address
        Mutability: nonpayable
        """
        return self.contract.functions.setOracleAddress(_oracle)

    def set_supply_control_address(self, supplyControl: ChecksumAddress) -> ContractFunction:
        """
        Generated from CDP ABI
        See `setSupplyControlAddress` on the CDP contract.
        Replace the supply control address
        Mutability: nonpayable
        """
        return self.contract.functions.setSupplyControlAddress(supplyControl)

    def withdraw(self, quantity: Wei) -> ContractFunction:
        """
        Generated from CDP ABI
        See `withdraw` on the CDP contract.
        Withdraw collateral from the CDP
        Mutability: nonpayable
        """
        return self.contract.functions.withdraw(quantity)
