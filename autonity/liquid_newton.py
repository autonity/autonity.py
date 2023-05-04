# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for the LiquidNewton contract for a given validator.  Note
that this contract also exposes functionality for claiming fees.
"""

from autonity.abi_manager import ABIManager
from autonity.erc20 import ERC20

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import Wei, ChecksumAddress


class LiquidNewton(ERC20):
    """
    The LiquidNewton contract.

    This is intended for internal use only. The naming mirrors
    the LiquidNewton contract in the Autonity code, but it's not very
    intuitive to have methods such as "claim_rewards" on a Token.
    Rather, this is more logically exposed by the Validator class.

    TODO: review this API (here and in the Autonity contracts).
    """

    def __init__(self, web3: Web3, address: ChecksumAddress):
        super().__init__(web3, address, ABIManager.load_abi("Liquid"))

    def unclaimed_rewards(self, account: ChecksumAddress) -> Wei:
        """
        See function `unclaimedRewards` on LiquidNewton.sol
        """
        return self.contract.functions.unclaimedRewards(account).call()

    def claim_rewards(self) -> ContractFunction:
        """
        Create a ContractFunction to claim rewards.  Use
        `create_contract_function_transaction` to use this in a
        transaction.  See function `claimRewards` on LiquidNewton.sol.
        """
        return self.contract.functions.claimRewards()
