"""Oracle contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


@dataclass
class Config:
    """Port of `struct Config` on the Oracle contract."""

    autonity: eth_typing.ChecksumAddress
    operator: eth_typing.ChecksumAddress
    vote_period: int
    outlier_detection_threshold: int
    outlier_slashing_threshold: int
    base_slashing_rate: int


@dataclass
class RoundData:
    """Port of `struct RoundData` on the IOracle contract."""

    round: int
    price: int
    timestamp: int
    success: bool


class Oracle:
    """Oracle contract binding.

    This contract implements the Oracle for the Autonity Protocol, allowing voters to
    submit price reports and aggregate them while detecting outliers.

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
    def NewRound(self) -> contract.ContractEvent:
        """Binding for `event NewRound` on the Oracle contract."""
        return self._contract.events.NewRound

    @property
    def NewSymbols(self) -> contract.ContractEvent:
        """Binding for `event NewSymbols` on the Oracle contract."""
        return self._contract.events.NewSymbols

    @property
    def Penalized(self) -> contract.ContractEvent:
        """Binding for `event Penalized` on the Oracle contract."""
        return self._contract.events.Penalized

    @property
    def Voted(self) -> contract.ContractEvent:
        """Binding for `event Voted` on the Oracle contract."""
        return self._contract.events.Voted

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the Oracle contract.

        Returns
        -------
        Config
        """
        return_value = self._contract.functions.config().call()
        return Config(
            eth_typing.ChecksumAddress(return_value[0]),
            eth_typing.ChecksumAddress(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
        )

    def distribute_rewards(
        self,
        _ntn: int,
    ) -> contract.ContractFunction:
        """Binding for `distributeRewards` on the Oracle contract.

        Parameters
        ----------
        _ntn : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.distributeRewards(
            _ntn,
        )

    def get_decimals(
        self,
    ) -> int:
        """Binding for `getDecimals` on the Oracle contract.

        Decimal places to be used with price reports

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getDecimals().call()
        return int(return_value)

    def get_new_voters(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """Binding for `getNewVoters` on the Oracle contract.

        Retrieve the list of new participants in the Oracle process.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
        """
        return_value = self._contract.functions.getNewVoters().call()
        return [
            eth_typing.ChecksumAddress(return_value_elem)
            for return_value_elem in return_value
        ]

    def get_reward_period_performance(
        self,
        _voter: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getRewardPeriodPerformance` on the Oracle contract.

        Retrieve the performance for a voter in this reward (epoch) period.

        Parameters
        ----------
        _voter : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getRewardPeriodPerformance(
            _voter,
        ).call()
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

        Retrieve the lists of symbols to be voted on.

        Returns
        -------
        typing.List[str]
        """
        return_value = self._contract.functions.getSymbols().call()
        return [str(return_value_elem) for return_value_elem in return_value]

    def get_vote_period(
        self,
    ) -> int:
        """Binding for `getVotePeriod` on the Oracle contract.

        Retrieve the vote period.

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

        Retrieve the list of participants in the Oracle process.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
        """
        return_value = self._contract.functions.getVoters().call()
        return [
            eth_typing.ChecksumAddress(return_value_elem)
            for return_value_elem in return_value
        ]

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

    def reports(
        self,
        key0: str,
        key1: eth_typing.ChecksumAddress,
    ) -> typing.Tuple[int, int]:
        """Binding for `reports` on the Oracle contract.

        Parameters
        ----------
        key0 : str
        key1 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        int
        """
        return_value = self._contract.functions.reports(
            key0,
            key1,
        ).call()
        return (
            int(return_value[0]),
            int(return_value[1]),
        )

    def set_slashing_config(
        self,
        _outlier_slashing_threshold: int,
        _outlier_detection_threshold: int,
        _base_slashing_rate: int,
    ) -> contract.ContractFunction:
        """Binding for `setSlashingConfig` on the Oracle contract.

        Setter for the internal slashing and outlier detection configuration.

        Parameters
        ----------
        _outlier_slashing_threshold : int
        _outlier_detection_threshold : int
        _base_slashing_rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSlashingConfig(
            _outlier_slashing_threshold,
            _outlier_detection_threshold,
            _base_slashing_rate,
        )

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
            list of string symbols to be used. E.g. "ATN-USD"

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSymbols(
            _symbols,
        )

    def set_vote_period(
        self,
        _vote_period: int,
    ) -> contract.ContractFunction:
        """Binding for `setVotePeriod` on the Oracle contract.

        Setter for the vote period.

        Parameters
        ----------
        _vote_period : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setVotePeriod(
            _vote_period,
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

    def update_voters(
        self,
    ) -> contract.ContractFunction:
        """Binding for `updateVoters` on the Oracle contract.

        Called when the previous round is ended. Updates the voter info for new voters.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.updateVoters()

    def voter_info(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> typing.Tuple[int, int, int, bool, bool]:
        """Binding for `voterInfo` on the Oracle contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        int
        int
        bool
        bool
        """
        return_value = self._contract.functions.voterInfo(
            key0,
        ).call()
        return (
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            bool(return_value[3]),
            bool(return_value[4]),
        )

    def voter_treasuries(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `voterTreasuries` on the Oracle contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.voterTreasuries(
            key0,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def voter_validators(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `voterValidators` on the Oracle contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.voterValidators(
            key0,
        ).call()
        return eth_typing.ChecksumAddress(return_value)


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address[]", "name": "_voters", "type": "address[]"},
                {
                    "internalType": "address[]",
                    "name": "_nodeAddresses",
                    "type": "address[]",
                },
                {
                    "internalType": "address[]",
                    "name": "_treasuries",
                    "type": "address[]",
                },
                {"internalType": "string[]", "name": "_symbols", "type": "string[]"},
                {
                    "components": [
                        {
                            "internalType": "contract Autonity",
                            "name": "autonity",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "operator",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "votePeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "int256",
                            "name": "outlierDetectionThreshold",
                            "type": "int256",
                        },
                        {
                            "internalType": "int256",
                            "name": "outlierSlashingThreshold",
                            "type": "int256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseSlashingRate",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Oracle.Config",
                    "name": "_config",
                    "type": "tuple",
                },
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
                    "name": "_participant",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "_symbol",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "_median",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "uint120",
                    "name": "_reported",
                    "type": "uint120",
                },
            ],
            "name": "Penalized",
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
            "name": "config",
            "outputs": [
                {
                    "internalType": "contract Autonity",
                    "name": "autonity",
                    "type": "address",
                },
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "uint256", "name": "votePeriod", "type": "uint256"},
                {
                    "internalType": "int256",
                    "name": "outlierDetectionThreshold",
                    "type": "int256",
                },
                {
                    "internalType": "int256",
                    "name": "outlierSlashingThreshold",
                    "type": "int256",
                },
                {
                    "internalType": "uint256",
                    "name": "baseSlashingRate",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_ntn", "type": "uint256"}],
            "name": "distributeRewards",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
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
            "name": "getDecimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getNewVoters",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_voter", "type": "address"}
            ],
            "name": "getRewardPeriodPerformance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
                        {"internalType": "uint256", "name": "price", "type": "uint256"},
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
            "inputs": [{"internalType": "string", "name": "_symbol", "type": "string"}],
            "name": "latestRoundData",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "round", "type": "uint256"},
                        {"internalType": "uint256", "name": "price", "type": "uint256"},
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
            "inputs": [
                {"internalType": "string", "name": "", "type": "string"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "reports",
            "outputs": [
                {"internalType": "uint120", "name": "price", "type": "uint120"},
                {"internalType": "uint8", "name": "confidence", "type": "uint8"},
            ],
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
                {
                    "internalType": "int256",
                    "name": "_outlierSlashingThreshold",
                    "type": "int256",
                },
                {
                    "internalType": "int256",
                    "name": "_outlierDetectionThreshold",
                    "type": "int256",
                },
                {
                    "internalType": "uint256",
                    "name": "_baseSlashingRate",
                    "type": "uint256",
                },
            ],
            "name": "setSlashingConfig",
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
                {"internalType": "uint256", "name": "_votePeriod", "type": "uint256"}
            ],
            "name": "setVotePeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "_newVoters",
                    "type": "address[]",
                },
                {"internalType": "address[]", "name": "_treasury", "type": "address[]"},
                {
                    "internalType": "address[]",
                    "name": "_validator",
                    "type": "address[]",
                },
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
            "inputs": [],
            "name": "updateVoters",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_commit", "type": "uint256"},
                {
                    "components": [
                        {"internalType": "uint120", "name": "price", "type": "uint120"},
                        {
                            "internalType": "uint8",
                            "name": "confidence",
                            "type": "uint8",
                        },
                    ],
                    "internalType": "struct IOracle.Report[]",
                    "name": "_reports",
                    "type": "tuple[]",
                },
                {"internalType": "uint256", "name": "_salt", "type": "uint256"},
                {"internalType": "uint8", "name": "_extra", "type": "uint8"},
            ],
            "name": "vote",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "voterInfo",
            "outputs": [
                {"internalType": "uint256", "name": "round", "type": "uint256"},
                {"internalType": "uint256", "name": "commit", "type": "uint256"},
                {"internalType": "uint256", "name": "performance", "type": "uint256"},
                {"internalType": "bool", "name": "isVoter", "type": "bool"},
                {"internalType": "bool", "name": "reportAvailable", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "voterTreasuries",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "voterValidators",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ],
)
