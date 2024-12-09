"""UpgradeManager contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing

import eth_typing
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


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

    def autonity(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `autonity` on the UpgradeManager contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.autonity().call()
        return eth_typing.ChecksumAddress(return_value)

    def operator(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `operator` on the UpgradeManager contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.operator().call()
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
            "inputs": [],
            "name": "autonity",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "operator",
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
