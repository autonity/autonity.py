# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model for an ERC20 token
"""

from autonity.abi_manager import ABIManager

from web3.contract.contract import Contract, ABI, ContractFunction
from web3.exceptions import BadFunctionCallOutput, ContractLogicError
from web3.types import Address, ChecksumAddress, ABIFunction
from web3 import Web3
from typing import Union, Optional

# pylint: disable=too-many-arguments


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
        except (BadFunctionCallOutput, ContractLogicError):
            return None

    def symbol(self) -> Optional[str]:
        """
        Returns the token symbol (or None if not available).
        """
        symbol_function = getattr(self.contract.functions, "symbol", None)
        try:
            return symbol_function().call() if symbol_function else None
        except (BadFunctionCallOutput, ContractLogicError):
            return None

    def decimals(self) -> int:
        """
        Returns the number of decimals used in the token (or None if not available).
        """
        decimals_function = getattr(self.contract.functions, "decimals", None)
        try:
            return decimals_function().call() if decimals_function else 0
        except (BadFunctionCallOutput, ContractLogicError):
            # https://ethereum.stackexchange.com/questions/100039/whats-the-default-erc20-decimals
            return 0

    def total_supply(self) -> int:
        """
        Total supply in "token units" (divide by 10^decimals for value in whole tokens).
        """
        return self.contract.functions.totalSupply().call()

    def balance_of(self, account: ChecksumAddress) -> int:
        """
        Returns the balance of a particular address in "token units"
        (divide by 10^decimals for value in whole tokens).
        """
        return self.contract.functions.balanceOf(account).call()

    def allowance(self, owner: ChecksumAddress, spender: ChecksumAddress) -> int:
        """
        Returns the quantity that `owner` has granted `spender` permission
        to spend.  Given in "token units" (divide by 10^decimals for
        value in whole tokens).
        """
        return self.contract.functions.allowance(owner, spender).call()

    def transfer(
        self,
        recipient: ChecksumAddress,
        amount: int,
    ) -> ContractFunction:
        """
        Create a transaction transferring `amount` in "token units"
        (units of 1/10^decimals) to `recipient`.
        """
        return self.contract.functions.transfer(recipient, amount)

    def approve(
        self,
        spender: ChecksumAddress,
        amount: int,
    ) -> ContractFunction:
        """
        Create a transaction granting `spender` permission to spend
        `amount` in "token units" (units of 1/10^decimals) held by
        `from_addr`.
        """
        return self.contract.functions.approve(spender, amount)

    def transfer_from(
        self,
        spender: ChecksumAddress,
        recipient: ChecksumAddress,
        amount: int,
    ) -> ContractFunction:
        """
        Create a transaction transferring `amount` in "token units" (units
        of 1/10^decimals) of the tokens held by `spender` to
        `recipient`.  `spender` must previously have granted
        `from_addr` permission to spend these tokens, via an `approve`
        transaction.
        """
        return self.contract.functions.transferFrom(spender, recipient, amount)

    # TODO: expose events?
    #   event Transfer(address indexed from, address indexed to, uint256 value);
    #   event Approval(address indexed owner, address indexed spender, uint256 value);
