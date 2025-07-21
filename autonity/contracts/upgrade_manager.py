"""UpgradeManager contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing

import eth_typing
import web3
from web3.contract import contract


class UpgradeManager:
    """UpgradeManager contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed UpgradeManager contract.
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
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the UpgradeManager contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the UpgradeManager contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the UpgradeManager contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the UpgradeManager contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def UpgradeResult(self) -> contract.ContractEvent:
        """Binding for `event UpgradeResult` on the UpgradeManager contract."""
        return self._contract.events.UpgradeResult

    def get_autonity(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getAutonity` on the UpgradeManager contract.

        Returns
        -------
        eth_typing.ChecksumAddress
            returns the autonity contract address
        """
        return_value = self._contract.functions.getAutonity().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_operator(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getOperator` on the UpgradeManager contract.

        Returns
        -------
        eth_typing.ChecksumAddress
            returns the operator address
        """
        return_value = self._contract.functions.getOperator().call()
        return eth_typing.ChecksumAddress(return_value)

    def upgrade(
        self,
        _target: eth_typing.ChecksumAddress,
        _data: str,
    ) -> contract.ContractFunction:
        """Binding for `upgrade` on the UpgradeManager contract.

        Parameters
        ----------
        _target : eth_typing.ChecksumAddress
            is the target contract address to be updated.
        _data : str
            is the contract creation code.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.upgrade(
            _target,
            _data,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address", "name": "_autonity", "type": "address"},
                {"internalType": "address", "name": "_operator", "type": "address"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
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
                    "indexed": True,
                    "internalType": "address",
                    "name": "contractAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool",
                },
            ],
            "name": "UpgradeResult",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "getAutonity",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOperator",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"}
            ],
            "name": "setOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_target", "type": "address"},
                {"internalType": "string", "name": "_data", "type": "string"},
            ],
            "name": "upgrade",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
