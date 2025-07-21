"""SupplyControl contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing

import eth_typing
import web3
from web3.contract import contract


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
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the SupplyControl contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the SupplyControl contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the SupplyControl contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the SupplyControl contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

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

        Returns
        -------
        int
            The supply of Auton available for minting.
        """
        return_value = self._contract.functions.availableSupply().call()
        return int(return_value)

    def get_stabilizer(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getStabilizer` on the SupplyControl contract.

        Returns
        -------
        eth_typing.ChecksumAddress
            The address of the stabilizer contract
        """
        return_value = self._contract.functions.getStabilizer().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_total_supply(
        self,
    ) -> int:
        """Binding for `getTotalSupply` on the SupplyControl contract.

        Returns
        -------
        int
            The initial total supply of Auton
        """
        return_value = self._contract.functions.getTotalSupply().call()
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
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "oldValue",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "newValue",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateAddress",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "oldValue",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "newValue",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateBool",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "oldValue",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "newValue",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateInt",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "oldValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateUint",
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
            "inputs": [],
            "name": "getStabilizer",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTotalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
    ],
)
