# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model for an ERC20 token
"""

from autonity.utils import unsigned_tx_from_contract_call
from autonity.abi_manager import ABIManager

from web3.contract import Contract, ABI
from web3.exceptions import BadFunctionCallOutput
from web3.types import Address, ChecksumAddress, TxParams, Wei, ABIFunction
from web3 import Web3
from typing import Union, Optional


NAME_FUNCTION: ABIFunction = {
    "inputs": [],
    "name": "name",
    "outputs": [{"internalType": "string", "name": "", "type": "string"}],  # type: ignore
    "stateMutability": "pure",
    "type": "function",
}

SYMBOL_FUNCTION: ABIFunction = {
    "inputs": [],
    "name": "symbol",
    "outputs": [{"internalType": "string", "name": "", "type": "string"}],  # type: ignore
    "stateMutability": "pure",
    "type": "function",
}

DECIMALS_FUNCTION: ABIFunction = {
    "inputs": [],
    "name": "decimals",
    "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],  # type: ignore
    "stateMutability": "pure",
    "type": "function",
}


def add_missing_erc20_functions(abi: ABI) -> ABI:
    """
    The IERC20 ABI doesn't include these optional functions by
    default.  We add them in to all ERC20 contract ABIs, and check
    them at runtime.
    """
    function_names = [fn["name"] for fn in abi if fn["type"] == "function"]
    abi = list(abi)
    if "name" not in function_names:
        abi.append(NAME_FUNCTION)
    if "symbol" not in function_names:
        abi.append(SYMBOL_FUNCTION)
    if "decimals" not in function_names:
        abi.append(DECIMALS_FUNCTION)

    return abi


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
        if not abi:
            abi = add_missing_erc20_functions(ABIManager.load_abi("IERC20"))
        self.contract = web3.eth.contract(address, abi=abi)

    def name(self) -> Optional[str]:
        """
        Returns the token name (or None if not available).
        """
        # TODO try-catch here in case the function is not present.
        name_function = getattr(self.contract.functions, "name", None)
        try:
            return name_function().call() if name_function else None
        except BadFunctionCallOutput:
            return None

    def symbol(self) -> Optional[str]:
        """
        Returns the token symbol (or None if not available).
        """
        symbol_function = getattr(self.contract.functions, "symbol", None)
        try:
            return symbol_function().call() if symbol_function else None
        except BadFunctionCallOutput:
            return None

    def decimals(self) -> Optional[int]:
        """
        Returns the number of decimals used in the token (or None if not available).
        """
        decimals_function = getattr(self.contract.functions, "decimals", None)
        try:
            return decimals_function().call() if decimals_function else None
        except BadFunctionCallOutput:
            return None

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
