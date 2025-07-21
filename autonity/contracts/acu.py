"""ACU contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing

import eth_typing
import web3
from web3.contract import contract


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
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the ACU contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the ACU contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the ACU contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the ACU contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def Rescaled(self) -> contract.ContractEvent:
        """Binding for `event Rescaled` on the ACU contract.

        The ACU quantity multiplier has been updated
        """
        return self._contract.events.Rescaled

    @property
    def Updated(self) -> contract.ContractEvent:
        """Binding for `event Updated` on the ACU contract.

        The ACU value was updated.
        """
        return self._contract.events.Updated

    def get_round(
        self,
    ) -> int:
        """Binding for `getRound` on the ACU contract.

        Returns
        -------
        int
            The Oracle round of the current ACU value.
        """
        return_value = self._contract.functions.getRound().call()
        return int(return_value)

    def get_scale(
        self,
    ) -> int:
        """Binding for `getScale` on the ACU contract.

        Returns
        -------
        int
            The decimal places used to represent the ACU as a fixed-point integer.
        """
        return_value = self._contract.functions.getScale().call()
        return int(return_value)

    def get_scale_factor(
        self,
    ) -> int:
        """Binding for `getScaleFactor` on the ACU contract.

        Returns
        -------
        int
            The multiplier for scaling numbers to the ACU scaled representation.
        """
        return_value = self._contract.functions.getScaleFactor().call()
        return int(return_value)

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

    def multiplier(
        self,
    ) -> int:
        """Binding for `multiplier` on the ACU contract.

        The quantity multiplier that is used to compute the ACU.

        Returns
        -------
        int
            Quantity multiplier
        """
        return_value = self._contract.functions.multiplier().call()
        return int(return_value)

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

    def rescale(
        self,
        new_quantity_multiplier: int,
    ) -> contract.ContractFunction:
        """Binding for `rescale` on the ACU contract.

        the quantity multiplier has precision of scaleFactor

        Parameters
        ----------
        new_quantity_multiplier : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.rescale(
            new_quantity_multiplier,
        )

    def scaled_quantities(
        self,
    ) -> typing.List[int]:
        """Binding for `scaledQuantities` on the ACU contract.

        The scaled quantities used to compute the ACU.

        Returns
        -------
        typing.List[int]
            Array of scaled quantities
        """
        return_value = self._contract.functions.scaledQuantities().call()
        return [int(return_value_elem) for return_value_elem in return_value]

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
            ACU value in fixed-point integer representation rescaled by the quantity
            multiplier
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
        {"inputs": [], "name": "ZeroValue", "type": "error"},
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
                    "internalType": "uint256",
                    "name": "newQuantityMultiplier",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "oldQuantityMultiplier",
                    "type": "uint256",
                },
            ],
            "name": "Rescaled",
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
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Updated",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "getRound",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getScale",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getScaleFactor",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
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
            "name": "multiplier",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "newQuantityMultiplier",
                    "type": "uint256",
                }
            ],
            "name": "rescale",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "scaledQuantities",
            "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
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
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
