"""ACU contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing

import eth_typing
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


class ACU:
    """ACU contract binding.

    Computes the value of the ACU, an optimal currency basket of 7 free-floating fiat
    currencies.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed ACU contract.
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
    def BasketModified(self) -> contract.ContractEvent:
        """Binding for `event BasketModified` on the ACU contract.

        The ACU symbols, quantites, or scale were modified.
        """
        return self._contract.events.BasketModified

    @property
    def Updated(self) -> contract.ContractEvent:
        """Binding for `event Updated` on the ACU contract.

        The ACU value was updated.
        """
        return self._contract.events.Updated

    def modify_basket(
        self,
        symbols_: typing.List[str],
        quantities_: typing.List[int],
        scale_: int,
    ) -> contract.ContractFunction:
        """Binding for `modifyBasket` on the ACU contract.

        Modify the ACU symbols, quantites, or scale.

        Parameters
        ----------
        symbols_ : typing.List[str]
            The symbols used to retrieve prices
        quantities_ : typing.List[int]
            The basket quantity corresponding to each symbol
        scale_ : int
            The scale for quantities and the ACU value

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.modifyBasket(
            symbols_,
            quantities_,
            scale_,
        )

    def quantities(
        self,
    ) -> typing.List[int]:
        """Binding for `quantities` on the ACU contract.

        The basket quantities that are used to compute the ACU.

        Returns
        -------
        typing.List[int]
            Array of quantities
        """
        return_value = self._contract.functions.quantities().call()
        return [int(return_value_elem) for return_value_elem in return_value]

    def round(
        self,
    ) -> int:
        """Binding for `round` on the ACU contract.

        The Oracle round of the current ACU value.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.round().call()
        return int(return_value)

    def scale(
        self,
    ) -> int:
        """Binding for `scale` on the ACU contract.

        The decimal places used to represent the ACU as a fixed-point integer. It is
        also the scale used to represent the basket quantities.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.scale().call()
        return int(return_value)

    def scale_factor(
        self,
    ) -> int:
        """Binding for `scaleFactor` on the ACU contract.

        The multiplier for scaling numbers to the ACU scaled representation.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.scaleFactor().call()
        return int(return_value)

    def symbols(
        self,
    ) -> typing.List[str]:
        """Binding for `symbols` on the ACU contract.

        The symbols that are used to compute the ACU.

        Returns
        -------
        typing.List[str]
            Array of symbols
        """
        return_value = self._contract.functions.symbols().call()
        return [str(return_value_elem) for return_value_elem in return_value]

    def value(
        self,
    ) -> int:
        """Binding for `value` on the ACU contract.

        The latest ACU value that was computed.

        Returns
        -------
        int
            ACU value in fixed-point integer representation
        """
        return_value = self._contract.functions.value().call()
        return int(return_value)


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "string[]", "name": "symbols_", "type": "string[]"},
                {
                    "internalType": "uint256[]",
                    "name": "quantities_",
                    "type": "uint256[]",
                },
                {"internalType": "uint256", "name": "scale_", "type": "uint256"},
                {"internalType": "address", "name": "autonity", "type": "address"},
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "address", "name": "oracle", "type": "address"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {"inputs": [], "name": "InvalidBasket", "type": "error"},
        {"inputs": [], "name": "NoACUValue", "type": "error"},
        {"inputs": [], "name": "Unauthorized", "type": "error"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string[]",
                    "name": "symbols",
                    "type": "string[]",
                },
                {
                    "indexed": False,
                    "internalType": "uint256[]",
                    "name": "quantities",
                    "type": "uint256[]",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "scale",
                    "type": "uint256",
                },
            ],
            "name": "BasketModified",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "height",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "timestamp",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "round",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "value",
                    "type": "int256",
                },
            ],
            "name": "Updated",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "string[]", "name": "symbols_", "type": "string[]"},
                {
                    "internalType": "uint256[]",
                    "name": "quantities_",
                    "type": "uint256[]",
                },
                {"internalType": "uint256", "name": "scale_", "type": "uint256"},
            ],
            "name": "modifyBasket",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "quantities",
            "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "round",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "scale",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "scaleFactor",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
                {"internalType": "address", "name": "oracle", "type": "address"}
            ],
            "name": "setOracle",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbols",
            "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "update",
            "outputs": [{"internalType": "bool", "name": "status", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "value",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
