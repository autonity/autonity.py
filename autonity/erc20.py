# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model for an ERC20 token
"""

from autonity.utils import unsigned_tx_from_contract_call
from autonity.abi_manager import ABIManager

from web3.contract import Contract, ABI
from web3.types import Address, ChecksumAddress, TxParams, Wei
from web3 import Web3
from typing import Union, Optional


class ERC20:
    """
    Wrapper class for an ERC20 contract
    """

    contract: Contract

    def __init__(
        self,
        web3: Web3,
        address: Union[Address, ChecksumAddress],
        abi: Optional[ABI] = None,
    ):
        abi = abi or ABIManager.load_abi("IERC20")
        self.contract = web3.eth.contract(address, abi=abi)

    def total_supply(self) -> Wei:
        """
        Total supply (in Wei) of the token.
        """
        return self.contract.functions.totalSupply().call()

    def balance_of(self, account: ChecksumAddress) -> Wei:
        """
        Returns the balance (in Wei) of a particular address.
        """
        return self.contract.functions.balanceOf(account).call()

    def allowance(self, owner: ChecksumAddress, spender: ChecksumAddress) -> Wei:
        """
        Returns the quantity (in Wei) that `owner` has granted `spender`
        permission to spend.
        """
        return self.contract.functions.balanceOf(owner, spender).call()

    def transfer(
        self, from_addr: ChecksumAddress, recipient: ChecksumAddress, amount: Wei
    ) -> TxParams:
        """
        Create a transaction transferring `amount` (in Wei) from
        `from_addr` to `recipient`.
        """
        return unsigned_tx_from_contract_call(
            self.contract.functions.transfer(recipient, amount), from_addr=from_addr
        )

    def approve(
        self, from_addr: ChecksumAddress, spender: ChecksumAddress, amount: Wei
    ) -> TxParams:
        """
        Create a transaction granting `spender` permission to spend
        `amount` (in Wei) of tokens held by `from_addr`.
        """
        return unsigned_tx_from_contract_call(
            self.contract.functions.approve(spender, amount), from_addr=from_addr
        )

    def transfer_from(
        self,
        from_addr: ChecksumAddress,
        spender: ChecksumAddress,
        recipient: ChecksumAddress,
        amount: Wei,
    ) -> TxParams:
        """
        Create a transaction transferring `amount` (in Wei) of the tokens
        held by `spender` to `recipient`.  `spender` must previously
        have granted `from_addr` permission to spend these tokens, via
        an `approve` transaction.
        """
        return unsigned_tx_from_contract_call(
            self.contract.functions.transferFrom(spender, recipient, amount),
            from_addr=from_addr,
        )

    # TODO: expose events?
    #   event Transfer(address indexed from, address indexed to, uint256 value);
    #   event Approval(address indexed owner, address indexed spender, uint256 value);
