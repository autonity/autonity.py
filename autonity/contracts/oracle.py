"""Oracle contract binding and data structures."""

# This module has been generated using pyabigen v0.2.9

import typing

import eth_typing
import web3
from dataclasses import dataclass
from web3.contract import base_contract, contract

__version__ = "v0.14.0"


@dataclass
class RoundData:
    """Port of `struct RoundData` on the IOracle contract."""

    round: int
    price: int
    timestamp: int
    success: bool


class Oracle:
    """Oracle contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed Oracle contract.
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
    def NewRound(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewRound` on the Oracle contract."""
        return self._contract.events.NewRound

    @property
    def NewSymbols(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewSymbols` on the Oracle contract."""
        return self._contract.events.NewSymbols

    @property
    def Voted(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Voted` on the Oracle contract."""
        return self._contract.events.Voted

    def get_precision(
        self,
    ) -> int:
        """Binding for `getPrecision` on the Oracle contract.

        Precision to be used with price reports

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getPrecision().call()
        return int(return_value)

    def get_round(
        self,
    ) -> int:
        """Binding for `getRound` on the Oracle contract.

        Retrieve the current round ID.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getRound().call()
        return int(return_value)

    def get_round_data(
        self,
        _round: int,
        _symbol: str,
    ) -> RoundData:
        """Binding for `getRoundData` on the Oracle contract.

        Return price data for a specific round.

        Parameters
        ----------
        _round : int
            , the round for which the price should be returned.
        _symbol : str
            , the symbol for which the current price should be returned.

        Returns
        -------
        RoundData
        """
        return_value = self._contract.functions.getRoundData(
            _round,
            _symbol,
        ).call()
        return RoundData(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            bool(return_value[3]),
        )

    def get_symbols(
        self,
    ) -> typing.List[str]:
        """Binding for `getSymbols` on the Oracle contract.

        Retrieve the lists of symbols to be voted on. Need to be called by the Oracle
        Server as part of the init.

        Returns
        -------
        typing.List[str]
        """
        return_value = self._contract.functions.getSymbols().call()
        return [str(elem) for elem in return_value]

    def get_vote_period(
        self,
    ) -> int:
        """Binding for `getVotePeriod` on the Oracle contract.

        vote period to be used for price voting and aggregation

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getVotePeriod().call()
        return int(return_value)

    def get_voters(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """Binding for `getVoters` on the Oracle contract.

        Retrieve the current voters in the committee.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
        """
        return_value = self._contract.functions.getVoters().call()
        return [eth_typing.ChecksumAddress(elem) for elem in return_value]

    def last_round_block(
        self,
    ) -> int:
        """Binding for `lastRoundBlock` on the Oracle contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lastRoundBlock().call()
        return int(return_value)

    def last_voter_update_round(
        self,
    ) -> int:
        """Binding for `lastVoterUpdateRound` on the Oracle contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lastVoterUpdateRound().call()
        return int(return_value)

    def latest_round_data(
        self,
        _symbol: str,
    ) -> RoundData:
        """Binding for `latestRoundData` on the Oracle contract.

        Return latest available price data.

        Parameters
        ----------
        _symbol : str
            , the symbol from which the current price should be returned.

        Returns
        -------
        RoundData
        """
        return_value = self._contract.functions.latestRoundData(
            _symbol,
        ).call()
        return RoundData(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            bool(return_value[3]),
        )

    def new_symbols(
        self,
        key0: int,
    ) -> str:
        """Binding for `newSymbols` on the Oracle contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        str
        """
        return_value = self._contract.functions.newSymbols(
            key0,
        ).call()
        return str(return_value)

    def reports(
        self,
        key0: str,
        key1: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `reports` on the Oracle contract.

        Parameters
        ----------
        key0 : str
        key1 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.reports(
            key0,
            key1,
        ).call()
        return int(return_value)

    def round(
        self,
    ) -> int:
        """Binding for `round` on the Oracle contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.round().call()
        return int(return_value)

    def set_symbols(
        self,
        _symbols: typing.List[str],
    ) -> contract.ContractFunction:
        """Binding for `setSymbols` on the Oracle contract.

        Update the symbols to be requested. Only effective at the next round. Restricted
        to the operator account.

        Parameters
        ----------
        _symbols : typing.List[str]

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSymbols(
            _symbols,
        )

    def symbol_updated_round(
        self,
    ) -> int:
        """Binding for `symbolUpdatedRound` on the Oracle contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.symbolUpdatedRound().call()
        return int(return_value)

    def symbols(
        self,
        key0: int,
    ) -> str:
        """Binding for `symbols` on the Oracle contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        str
        """
        return_value = self._contract.functions.symbols(
            key0,
        ).call()
        return str(return_value)

    def vote_period(
        self,
    ) -> int:
        """Binding for `votePeriod` on the Oracle contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.votePeriod().call()
        return int(return_value)

    def voting_info(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> typing.Tuple[int, int, bool]:
        """Binding for `votingInfo` on the Oracle contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        int
        bool
        """
        return_value = self._contract.functions.votingInfo(
            key0,
        ).call()
        return (
            int(return_value[0]),
            int(return_value[1]),
            bool(return_value[2]),
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address[]", "name": "_voters", "type": "address[]"},
                {"internalType": "address", "name": "_autonity", "type": "address"},
                {"internalType": "address", "name": "_operator", "type": "address"},
                {"internalType": "string[]", "name": "_symbols", "type": "string[]"},
                {"internalType": "uint256", "name": "_votePeriod", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_round",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_height",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_timestamp",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_votePeriod",
                    "type": "uint256",
                },
            ],
            "name": "NewRound",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string[]",
                    "name": "_symbols",
                    "type": "string[]",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_round",
                    "type": "uint256",
                },
            ],
            "name": "NewSymbols",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_voter",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256[]",
                    "name": "_votes",
                    "type": "int256[]",
                },
            ],
            "name": "Voted",
            "type": "event",
        },
        {"stateMutability": "payable", "type": "fallback"},
        {
            "inputs": [],
            "name": "finalize",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPrecision",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getRound",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_round", "type": "uint256"},
                {"internalType": "string", "name": "_symbol", "type": "string"},
            ],
            "name": "getRoundData",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "round", "type": "uint256"},
                        {"internalType": "int256", "name": "price", "type": "int256"},
                        {
                            "internalType": "uint256",
                            "name": "timestamp",
                            "type": "uint256",
                        },
                        {"internalType": "bool", "name": "success", "type": "bool"},
                    ],
                    "internalType": "struct IOracle.RoundData",
                    "name": "data",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getSymbols",
            "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getVotePeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getVoters",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastRoundBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastVoterUpdateRound",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "string", "name": "_symbol", "type": "string"}],
            "name": "latestRoundData",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "round", "type": "uint256"},
                        {"internalType": "int256", "name": "price", "type": "int256"},
                        {
                            "internalType": "uint256",
                            "name": "timestamp",
                            "type": "uint256",
                        },
                        {"internalType": "bool", "name": "success", "type": "bool"},
                    ],
                    "internalType": "struct IOracle.RoundData",
                    "name": "data",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "newSymbols",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "", "type": "string"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "reports",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
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
            "inputs": [
                {"internalType": "address", "name": "_operator", "type": "address"}
            ],
            "name": "setOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string[]", "name": "_symbols", "type": "string[]"}
            ],
            "name": "setSymbols",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "_newVoters", "type": "address[]"}
            ],
            "name": "setVoters",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbolUpdatedRound",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "symbols",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_commit", "type": "uint256"},
                {"internalType": "int256[]", "name": "_reports", "type": "int256[]"},
                {"internalType": "uint256", "name": "_salt", "type": "uint256"},
            ],
            "name": "vote",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "votePeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "votingInfo",
            "outputs": [
                {"internalType": "uint256", "name": "round", "type": "uint256"},
                {"internalType": "uint256", "name": "commit", "type": "uint256"},
                {"internalType": "bool", "name": "isVoter", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ],
)
