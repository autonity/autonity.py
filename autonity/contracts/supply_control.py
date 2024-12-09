"""SupplyControl contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing

import eth_typing
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


class SupplyControl:
    """SupplyControl contract binding.

    Controls the supply of Auton on the network.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed SupplyControl contract.
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
    def Burn(self) -> contract.ContractEvent:
        """Binding for `event Burn` on the SupplyControl contract.

        Auton was burned.
        """
        return self._contract.events.Burn

    @property
    def Mint(self) -> contract.ContractEvent:
        """Binding for `event Mint` on the SupplyControl contract.

        Auton was minted.
        """
        return self._contract.events.Mint

    def available_supply(
        self,
    ) -> int:
        """Binding for `availableSupply` on the SupplyControl contract.

        The supply of Auton available for minting.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.availableSupply().call()
        return int(return_value)

    def set_stabilizer(
        self,
        stabilizer_: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setStabilizer` on the SupplyControl contract.

        Update the stabilizer that is authorized to mint and burn.

        Parameters
        ----------
        stabilizer_ : eth_typing.ChecksumAddress
            The new stabilizer account

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setStabilizer(
            stabilizer_,
        )

    def stabilizer(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `stabilizer` on the SupplyControl contract.

        The account that is authorized to mint and burn.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.stabilizer().call()
        return eth_typing.ChecksumAddress(return_value)

    def total_supply(
        self,
    ) -> int:
        """Binding for `totalSupply` on the SupplyControl contract.

        The total supply of Auton under management.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalSupply().call()
        return int(return_value)


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address", "name": "autonity", "type": "address"},
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "address", "name": "stabilizer_", "type": "address"},
            ],
            "stateMutability": "payable",
            "type": "constructor",
        },
        {"inputs": [], "name": "InvalidAmount", "type": "error"},
        {"inputs": [], "name": "InvalidRecipient", "type": "error"},
        {"inputs": [], "name": "Unauthorized", "type": "error"},
        {"inputs": [], "name": "ZeroValue", "type": "error"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                }
            ],
            "name": "Burn",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Mint",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "availableSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "burn",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "operator", "type": "address"}
            ],
            "name": "setOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "stabilizer_", "type": "address"}
            ],
            "name": "setStabilizer",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "stabilizer",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
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
    ],
)
