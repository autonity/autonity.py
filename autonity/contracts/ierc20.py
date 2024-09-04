"""IERC20 contract binding and data structures."""

# This module has been generated using pyabigen v0.2.8

import typing

import eth_typing
import web3
from web3.contract import base_contract, contract

__version__ = "v0.14.0"


class IERC20:
    """IERC20 contract binding.

    Interface of the ERC20 standard as defined in the EIP.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed IERC20 contract.
    """

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(
            address=address,
            abi=ABI,
        )

    @property
    def Approval(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Approval` on the IERC20 contract.

        Emitted when the allowance of a `spender` for an `owner` is set by a call to
        {approve}. `value` is the new allowance.
        """
        return self._contract.events.Approval

    @property
    def Transfer(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Transfer` on the IERC20 contract.

        Emitted when `value` tokens are moved from one account (`from`) to another
        (`to`). Note that `value` may be zero.
        """
        return self._contract.events.Transfer

    def allowance(
        self,
        owner: eth_typing.ChecksumAddress,
        spender: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `allowance` on the IERC20 contract.

        Returns the remaining number of tokens that `spender` will be allowed to spend
        on behalf of `owner` through {transferFrom}. This is zero by default. This value
        changes when {approve} or {transferFrom} are called.

        Parameters
        ----------
        owner : eth_typing.ChecksumAddress
        spender : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.allowance(
            owner,
            spender,
        ).call()
        return int(return_value)

    def approve(
        self,
        spender: eth_typing.ChecksumAddress,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `approve` on the IERC20 contract.

        Sets `amount` as the allowance of `spender` over the caller's tokens. Returns a
        boolean value indicating whether the operation succeeded. IMPORTANT: Beware that
        changing an allowance with this method brings the risk that someone may use both
        the old and the new allowance by unfortunate transaction ordering. One possible
        solution to mitigate this race condition is to first reduce the spender's
        allowance to 0 and set the desired value afterwards:
        https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729 Emits an
        {Approval} event.

        Parameters
        ----------
        spender : eth_typing.ChecksumAddress
        amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.approve(
            spender,
            amount,
        )

    def balance_of(
        self,
        account: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `balanceOf` on the IERC20 contract.

        Returns the amount of tokens owned by `account`.

        Parameters
        ----------
        account : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.balanceOf(
            account,
        ).call()
        return int(return_value)

    def total_supply(
        self,
    ) -> int:
        """Binding for `totalSupply` on the IERC20 contract.

        Returns the amount of tokens in existence.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalSupply().call()
        return int(return_value)

    def transfer(
        self,
        recipient: eth_typing.ChecksumAddress,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transfer` on the IERC20 contract.

        Moves `amount` tokens from the caller's account to `recipient`. Returns a
        boolean value indicating whether the operation succeeded. Emits a {Transfer}
        event.

        Parameters
        ----------
        recipient : eth_typing.ChecksumAddress
        amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transfer(
            recipient,
            amount,
        )

    def transfer_from(
        self,
        sender: eth_typing.ChecksumAddress,
        recipient: eth_typing.ChecksumAddress,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transferFrom` on the IERC20 contract.

        Moves `amount` tokens from `sender` to `recipient` using the allowance
        mechanism. `amount` is then deducted from the caller's allowance. Returns a
        boolean value indicating whether the operation succeeded. Emits a {Transfer}
        event.

        Parameters
        ----------
        sender : eth_typing.ChecksumAddress
        recipient : eth_typing.ChecksumAddress
        amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transferFrom(
            sender,
            recipient,
            amount,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Transfer",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "spender", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"}
            ],
            "name": "balanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
