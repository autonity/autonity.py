# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for the LiquidNewton contract for a given validator.  Note
that this contract also exposes functionality for claiming fees.
"""

from autonity.abi_manager import ABIManager
from autonity.erc20 import ERC20
from autonity.utils import unsigned_tx_from_contract_call

from web3 import Web3
from web3.types import Wei, ChecksumAddress, TxParams


class LiquidNewton(ERC20):
    """
    The LiquidNewton contract.
    """

    def __init__(self, web3: Web3, address: ChecksumAddress):
        super().__init__(web3, address, ABIManager.load_abi("Liquid"))

    def unclaimed_rewards(self, account: ChecksumAddress) -> Wei:
        """
        See function `unclaimedRewards` on LiquidNewton.sol
        """
        return self.contract.functions.unclaimedRewards(account).call()

    def claim_rewards(self, from_addr: ChecksumAddress) -> TxParams:
        """
        Create a function to claim rewards for `from_addr`.  See function
        `claimRewards` on LiquidNewton.sol.
        """
        return unsigned_tx_from_contract_call(
            self.contract.functions.claimRewards(), from_addr=from_addr
        )
