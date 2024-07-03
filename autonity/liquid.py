# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for the Liquid contract for a given validator.  Note
that this contract also exposes functionality for claiming fees.
"""

from typing import Tuple

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import ChecksumAddress, Wei

from autonity.abi_manager import load_abi
from autonity.erc20 import ERC20


class Liquid(ERC20):
    """
    The Liquid contract.

    This is intended for internal use only. The naming mirrors
    the Liquid contract in the Autonity code, but it's not very
    intuitive to have methods such as "claim_rewards" on a Token.
    Rather, this is more logically exposed by the Validator class.
    """

    def __init__(self, web3: Web3, address: ChecksumAddress):
        super().__init__(web3, address, load_abi("Liquid"))

    def validator(self) -> ChecksumAddress:
        """
        Get the validator for this contract.
        """
        return self.contract.functions.validator().call()

    def treasury(self) -> ChecksumAddress:
        """
        Get the treasury for this contract.
        """
        return self.contract.functions.treasury().call()

    def commissionRate(self) -> ChecksumAddress:
        """
        Get the commision rate for this contract.
        """
        return self.contract.functions.commissionRate().call()

    def unclaimed_rewards(self, account: ChecksumAddress) -> Tuple[Wei, Wei]:
        """
        See `unclaimedRewards` on Liquid.sol.
        """
        return self.contract.functions.unclaimedRewards(account).call()

    def claim_rewards(self) -> ContractFunction:
        """
        Create a ContractFunction to claim rewards.  Use
        `create_contract_function_transaction` to use this in a
        transaction.  See function `claimRewards` on LiquidNewton.sol.
        """
        return self.contract.functions.claimRewards()

    def locked_balance_of(self, delegator: ChecksumAddress) -> Wei:
        """
        See function `lockedBalanceOf` on Liquid.sol
        """
        return self.contract.functions.lockedBalanceOf(delegator).call()

    def unlocked_balance_of(self, delegator: ChecksumAddress) -> Wei:
        """
        See function `unlockedBalanceOf` on Liquid.sol
        """
        return self.contract.functions.unlockedBalanceOf(delegator).call()
