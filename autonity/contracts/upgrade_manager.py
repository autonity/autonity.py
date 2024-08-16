# Generated by pyabigen 0.2.0

import typing

import eth_typing
import web3
from web3.contract import contract

__version__ = "v0.14.0"

ADDRESS = typing.cast(
    eth_typing.ChecksumAddress, "0x3C368B86AF00565Df7a3897Cfa9195B9434A59f9"
)


class UpgradeManager:
    """UpgradeManager contract wrapper."""

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
    ):
        self._contract = w3.eth.contract(
            address=ADDRESS,
            abi=abi,
        )

    def autonity(
        self,
    ) -> eth_typing.ChecksumAddress:
        """See `autonity` on the UpgradeManager contract."""
        return_value = self._contract.functions.autonity().call()
        return eth_typing.ChecksumAddress(return_value)

    def operator(
        self,
    ) -> eth_typing.ChecksumAddress:
        """See `operator` on the UpgradeManager contract."""
        return_value = self._contract.functions.operator().call()
        return eth_typing.ChecksumAddress(return_value)

    def upgrade(
        self,
        _target: eth_typing.ChecksumAddress,
        _data: str,
    ) -> contract.ContractFunction:
        """See `upgrade` on the UpgradeManager contract."""
        return self._contract.functions.upgrade(
            _target,
            _data,
        )


abi = [
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
        "inputs": [{"internalType": "address", "name": "_account", "type": "address"}],
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
]
