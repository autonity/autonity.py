"""Auctioneer contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract


@dataclass
class Config:
    """Port of `struct Config` on the Auctioneer contract."""

    liquidation_auction_duration: int
    interest_auction_duration: int
    interest_auction_discount: int
    interest_auction_threshold: int


@dataclass
class Auction:
    """Port of `struct Auction` on the AuctionLib contract."""

    id: int
    amount: int
    start_price: int
    start_timestamp: int


class Auctioneer:
    """Auctioneer contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed Auctioneer contract.
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
    def AuctionedDebt(self) -> contract.ContractEvent:
        """Binding for `event AuctionedDebt` on the Auctioneer contract."""
        return self._contract.events.AuctionedDebt

    @property
    def AuctionedInterest(self) -> contract.ContractEvent:
        """Binding for `event AuctionedInterest` on the Auctioneer contract."""
        return self._contract.events.AuctionedInterest

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the Auctioneer contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the Auctioneer contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the Auctioneer contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the Auctioneer contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def NewInterestAuction(self) -> contract.ContractEvent:
        """Binding for `event NewInterestAuction` on the Auctioneer contract."""
        return self._contract.events.NewInterestAuction

    @property
    def PriceUnavailable(self) -> contract.ContractEvent:
        """Binding for `event PriceUnavailable` on the Auctioneer contract."""
        return self._contract.events.PriceUnavailable

    def bid_debt(
        self,
        debtor: eth_typing.ChecksumAddress,
        liquidatable_round: int,
        ntn_amount: int,
    ) -> contract.ContractFunction:
        """Binding for `bidDebt` on the Auctioneer contract.

        Place a bid to liquidate a CDP that is undercollateralized

        Parameters
        ----------
        debtor : eth_typing.ChecksumAddress
            The address of the CDP owner
        liquidatable_round : int
        ntn_amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.bidDebt(
            debtor,
            liquidatable_round,
            ntn_amount,
        )

    def bid_interest(
        self,
        auction: int,
        ntn_amount: int,
    ) -> contract.ContractFunction:
        """Binding for `bidInterest` on the Auctioneer contract.

        Place a bid on an interest auction

        Parameters
        ----------
        auction : int
            The ID of the auction
        ntn_amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.bidInterest(
            auction,
            ntn_amount,
        )

    def get_auction(
        self,
        auction: int,
    ) -> Auction:
        """Binding for `getAuction` on the Auctioneer contract.

        Get an auction by ID

        Parameters
        ----------
        auction : int
            The ID of the auction

        Returns
        -------
        Auction
        """
        return_value = self._contract.functions.getAuction(
            auction,
        ).call()
        return Auction(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
        )

    def get_collateral_token(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getCollateralToken` on the Auctioneer contract.

        Get the address of the collateral token

        Returns
        -------
        eth_typing.ChecksumAddress
            the address of the collateral token
        """
        return_value = self._contract.functions.getCollateralToken().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_config(
        self,
    ) -> Config:
        """Binding for `getConfig` on the Auctioneer contract.

        Get the current Auctioneer configuration

        Returns
        -------
        Config
            the current configuration
        """
        return_value = self._contract.functions.getConfig().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
        )

    def get_proceed_address(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getProceedAddress` on the Auctioneer contract.

        Get the proceed address

        Returns
        -------
        eth_typing.ChecksumAddress
            the proceed address
        """
        return_value = self._contract.functions.getProceedAddress().call()
        return eth_typing.ChecksumAddress(return_value)

    def max_liquidation_return(
        self,
        debtor: eth_typing.ChecksumAddress,
        liquidatable_round: int,
    ) -> int:
        """Binding for `maxLiquidationReturn` on the Auctioneer contract.

        Get the maximum amount of NTN that can be returned to a liquidator for a given
        CDP

        Parameters
        ----------
        debtor : eth_typing.ChecksumAddress
            The address of the CDP owner
        liquidatable_round : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxLiquidationReturn(
            debtor,
            liquidatable_round,
        ).call()
        return int(return_value)

    def min_interest_payment(
        self,
        auction: int,
    ) -> int:
        """Binding for `minInterestPayment` on the Auctioneer contract.

        Get the minimum amount of NTN that can be paid for an interest auction

        Parameters
        ----------
        auction : int
            The ID of the auction

        Returns
        -------
        int
        """
        return_value = self._contract.functions.minInterestPayment(
            auction,
        ).call()
        return int(return_value)

    def open_auctions(
        self,
    ) -> typing.List[Auction]:
        """Binding for `openAuctions` on the Auctioneer contract.

        Get all open interest auctions

        Returns
        -------
        typing.List[Auction]
            An array of all open interest auctions
        """
        return_value = self._contract.functions.openAuctions().call()
        return [
            Auction(
                int(return_value_elem[0]),
                int(return_value_elem[1]),
                int(return_value_elem[2]),
                int(return_value_elem[3]),
            )
            for return_value_elem in return_value
        ]

    def set_interest_auction_discount(
        self,
        discount: int,
    ) -> contract.ContractFunction:
        """Binding for `setInterestAuctionDiscount` on the Auctioneer contract.

        Set the interest auction discount

        Parameters
        ----------
        discount : int
            The discount applied to the interest auction

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInterestAuctionDiscount(
            discount,
        )

    def set_interest_auction_duration(
        self,
        duration: int,
    ) -> contract.ContractFunction:
        """Binding for `setInterestAuctionDuration` on the Auctioneer contract.

        Set the interest auction duration

        Parameters
        ----------
        duration : int
            The duration of the interest auction

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInterestAuctionDuration(
            duration,
        )

    def set_interest_auction_threshold(
        self,
        threshold: int,
    ) -> contract.ContractFunction:
        """Binding for `setInterestAuctionThreshold` on the Auctioneer contract.

        Set the interest auction threshold

        Parameters
        ----------
        threshold : int
            The threshold for starting an interest auction

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInterestAuctionThreshold(
            threshold,
        )

    def set_liquidation_auction_duration(
        self,
        duration: int,
    ) -> contract.ContractFunction:
        """Binding for `setLiquidationAuctionDuration` on the Auctioneer contract.

        Set the liquidation auction duration

        Parameters
        ----------
        duration : int
            The duration of the liquidation auction

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setLiquidationAuctionDuration(
            duration,
        )

    def set_proceed_address(
        self,
        proceed_address_: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setProceedAddress` on the Auctioneer contract.

        Set the proceeds address

        Parameters
        ----------
        proceed_address_ : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setProceedAddress(
            proceed_address_,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "liquidationAuctionDuration",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionDuration",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionDiscount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionThreshold",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Auctioneer.Config",
                    "name": "config_",
                    "type": "tuple",
                },
                {
                    "internalType": "address",
                    "name": "stabilization_",
                    "type": "address",
                },
                {"internalType": "address", "name": "oracle_", "type": "address"},
                {
                    "internalType": "address",
                    "name": "collateralToken_",
                    "type": "address",
                },
                {"internalType": "address", "name": "autonity_", "type": "address"},
                {"internalType": "address", "name": "operator_", "type": "address"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "minimumBid", "type": "uint256"},
                {"internalType": "uint256", "name": "bid", "type": "uint256"},
            ],
            "name": "BidTooLow",
            "type": "error",
        },
        {"inputs": [], "name": "InsufficientAllowance", "type": "error"},
        {"inputs": [], "name": "InvalidAmount", "type": "error"},
        {"inputs": [], "name": "InvalidAuctionId", "type": "error"},
        {
            "inputs": [{"internalType": "string", "name": "message", "type": "string"}],
            "name": "InvalidParameter",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "round", "type": "uint256"}],
            "name": "InvalidRound",
            "type": "error",
        },
        {"inputs": [], "name": "NotLiquidatable", "type": "error"},
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "PRBMath_MulDiv18_Overflow",
            "type": "error",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
                {"internalType": "uint256", "name": "denominator", "type": "uint256"},
            ],
            "name": "PRBMath_MulDiv_Overflow",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "UD60x18", "name": "x", "type": "uint256"}],
            "name": "PRBMath_UD60x18_Sqrt_Overflow",
            "type": "error",
        },
        {"inputs": [], "name": "TransferFailed", "type": "error"},
        {"inputs": [], "name": "Unauthorized", "type": "error"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "debtor",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "biddor",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "collateralAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "debtAmount",
                    "type": "uint256",
                },
            ],
            "name": "AuctionedDebt",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "biddor",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "interestAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "paymentAmount",
                    "type": "uint256",
                },
            ],
            "name": "AuctionedInterest",
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
                    "name": "auctionId",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "startTimestamp",
                    "type": "uint256",
                },
            ],
            "name": "NewInterestAuction",
            "type": "event",
        },
        {"anonymous": False, "inputs": [], "name": "PriceUnavailable", "type": "event"},
        {
            "inputs": [
                {"internalType": "address", "name": "debtor", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "liquidatableRound",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "ntnAmount", "type": "uint256"},
            ],
            "name": "bidDebt",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "auction", "type": "uint256"},
                {"internalType": "uint256", "name": "ntnAmount", "type": "uint256"},
            ],
            "name": "bidInterest",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "auction", "type": "uint256"}
            ],
            "name": "getAuction",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "startPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "startTimestamp",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct AuctionLib.Auction",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCollateralToken",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getConfig",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "liquidationAuctionDuration",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionDuration",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionDiscount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interestAuctionThreshold",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Auctioneer.Config",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getProceedAddress",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "debtor", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "liquidatableRound",
                    "type": "uint256",
                },
            ],
            "name": "maxLiquidationReturn",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "auction", "type": "uint256"}
            ],
            "name": "minInterestPayment",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "openAuctions",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "startPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "startTimestamp",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct AuctionLib.Auction[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "paidInterest",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "discount", "type": "uint256"}
            ],
            "name": "setInterestAuctionDiscount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "duration", "type": "uint256"}
            ],
            "name": "setInterestAuctionDuration",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "threshold", "type": "uint256"}
            ],
            "name": "setInterestAuctionThreshold",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "duration", "type": "uint256"}
            ],
            "name": "setLiquidationAuctionDuration",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "operator_", "type": "address"}
            ],
            "name": "setOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "oracle_", "type": "address"}
            ],
            "name": "setOracle",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "proceedAddress_",
                    "type": "address",
                }
            ],
            "name": "setProceedAddress",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "stabilization_", "type": "address"}
            ],
            "name": "setStabilization",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
