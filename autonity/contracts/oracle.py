# Generated by pyabigen 0.2.2

import typing

import eth_typing
import web3
from web3.contract import base_contract, contract

__version__ = "v0.14.0"


class RoundData(typing.NamedTuple):
    """See `struct RoundData` on the IOracle contract."""

    round: int
    price: int
    timestamp: int
    success: bool


class Oracle:
    """Oracle contract wrapper."""

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(
            address=address,
            abi=abi,
        )

    @property
    def NewRound(self) -> typing.Type[base_contract.BaseContractEvent]:
        """See `event NewRound` on the Oracle contract."""
        return self._contract.events.NewRound

    @property
    def NewSymbols(self) -> typing.Type[base_contract.BaseContractEvent]:
        """See `event NewSymbols` on the Oracle contract."""
        return self._contract.events.NewSymbols

    @property
    def Voted(self) -> typing.Type[base_contract.BaseContractEvent]:
        """See `event Voted` on the Oracle contract."""
        return self._contract.events.Voted

    def get_precision(
        self,
    ) -> int:
        """See `getPrecision` on the Oracle contract."""
        return_value = self._contract.functions.getPrecision().call()
        return int(return_value)

    def get_round(
        self,
    ) -> int:
        """See `getRound` on the Oracle contract."""
        return_value = self._contract.functions.getRound().call()
        return int(return_value)

    def get_round_data(
        self,
        _round: int,
        _symbol: str,
    ) -> RoundData:
        """See `getRoundData` on the Oracle contract."""
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
        """See `getSymbols` on the Oracle contract."""
        return_value = self._contract.functions.getSymbols().call()
        return [str(elem) for elem in return_value]

    def get_vote_period(
        self,
    ) -> int:
        """See `getVotePeriod` on the Oracle contract."""
        return_value = self._contract.functions.getVotePeriod().call()
        return int(return_value)

    def get_voters(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """See `getVoters` on the Oracle contract."""
        return_value = self._contract.functions.getVoters().call()
        return [eth_typing.ChecksumAddress(elem) for elem in return_value]

    def last_round_block(
        self,
    ) -> int:
        """See `lastRoundBlock` on the Oracle contract."""
        return_value = self._contract.functions.lastRoundBlock().call()
        return int(return_value)

    def last_voter_update_round(
        self,
    ) -> int:
        """See `lastVoterUpdateRound` on the Oracle contract."""
        return_value = self._contract.functions.lastVoterUpdateRound().call()
        return int(return_value)

    def latest_round_data(
        self,
        _symbol: str,
    ) -> RoundData:
        """See `latestRoundData` on the Oracle contract."""
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
        """See `newSymbols` on the Oracle contract."""
        return_value = self._contract.functions.newSymbols(
            key0,
        ).call()
        return str(return_value)

    def reports(
        self,
        key0: str,
        key1: eth_typing.ChecksumAddress,
    ) -> int:
        """See `reports` on the Oracle contract."""
        return_value = self._contract.functions.reports(
            key0,
            key1,
        ).call()
        return int(return_value)

    def round(
        self,
    ) -> int:
        """See `round` on the Oracle contract."""
        return_value = self._contract.functions.round().call()
        return int(return_value)

    def set_symbols(
        self,
        _symbols: typing.List[str],
    ) -> contract.ContractFunction:
        """See `setSymbols` on the Oracle contract."""
        return self._contract.functions.setSymbols(
            _symbols,
        )

    def symbol_updated_round(
        self,
    ) -> int:
        """See `symbolUpdatedRound` on the Oracle contract."""
        return_value = self._contract.functions.symbolUpdatedRound().call()
        return int(return_value)

    def symbols(
        self,
        key0: int,
    ) -> str:
        """See `symbols` on the Oracle contract."""
        return_value = self._contract.functions.symbols(
            key0,
        ).call()
        return str(return_value)

    def vote(
        self,
        _commit: int,
        _reports: typing.List[int],
        _salt: int,
    ) -> contract.ContractFunction:
        """See `vote` on the Oracle contract."""
        return self._contract.functions.vote(
            _commit,
            _reports,
            _salt,
        )

    def vote_period(
        self,
    ) -> int:
        """See `votePeriod` on the Oracle contract."""
        return_value = self._contract.functions.votePeriod().call()
        return int(return_value)

    def voting_info(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> typing.Tuple[int, int, bool]:
        """See `votingInfo` on the Oracle contract."""
        return_value = self._contract.functions.votingInfo(
            key0,
        ).call()
        return (
            int(return_value[0]),
            int(return_value[1]),
            bool(return_value[2]),
        )


abi = [
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
    {"stateMutability": "payable", "type": "fallback"},
    {"stateMutability": "payable", "type": "receive"},
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
                    {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
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
                    {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
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
        "inputs": [{"internalType": "address", "name": "_operator", "type": "address"}],
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
]
