"""Oracle contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract


@dataclass
class Config:
    """Port of `struct Config` on the Oracle contract."""

    autonity: eth_typing.ChecksumAddress
    operator: eth_typing.ChecksumAddress
    vote_period: int
    outlier_detection_threshold: int
    outlier_slashing_threshold: int
    base_slashing_rate: int
    non_reveal_threshold: int
    reveal_reset_interval: int
    slashing_rate_cap: int


@dataclass
class Report:
    """Port of `struct Report` on the IOracle contract."""

    price: int
    confidence: int


@dataclass
class RoundData:
    """Port of `struct RoundData` on the IOracle contract."""

    round: int
    price: int
    timestamp: int
    success: bool


@dataclass
class VoterInfo:
    """Port of `struct VoterInfo` on the Oracle contract."""

    round: int
    commit: int
    performance: int
    non_reveal_count: int
    is_voter: bool
    report_available: bool


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
    def CallFailed(self) -> contract.ContractEvent:
        """Binding for `event CallFailed` on the Oracle contract.

        This event is emitted when a call to an address fails in a protocol function
        (like finalize()).
        """
        return self._contract.events.CallFailed

    @property
    def CommitRevealMissed(self) -> contract.ContractEvent:
        """Binding for `event CommitRevealMissed` on the Oracle contract.

        Emitted when a participant submitted commit in the previous round but did not
        submit reveal in the current round.
        """
        return self._contract.events.CommitRevealMissed

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the Oracle contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the Oracle contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the Oracle contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the Oracle contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def InvalidVote(self) -> contract.ContractEvent:
        """Binding for `event InvalidVote` on the Oracle contract.

        Emitted when an invalid report is submitted
        """
        return self._contract.events.InvalidVote

    @property
    def NewRound(self) -> contract.ContractEvent:
        """Binding for `event NewRound` on the Oracle contract.

        Emitted when a new voting round is started.
        """
        return self._contract.events.NewRound

    @property
    def NewSymbols(self) -> contract.ContractEvent:
        """Binding for `event NewSymbols` on the Oracle contract.

        Emitted when the oracle symbol list is updated
        """
        return self._contract.events.NewSymbols

    @property
    def NewVoter(self) -> contract.ContractEvent:
        """Binding for `event NewVoter` on the Oracle contract.

        Emitted when a new reporter submits a report
        """
        return self._contract.events.NewVoter

    @property
    def NoRevealPenalty(self) -> contract.ContractEvent:
        """Binding for `event NoRevealPenalty` on the Oracle contract.

        Emitted when a participant gets penalized for missing too many reveals in a
        certain window
        """
        return self._contract.events.NoRevealPenalty

    @property
    def Penalized(self) -> contract.ContractEvent:
        """Binding for `event Penalized` on the Oracle contract.

        Emitted when a participant gets penalized as an outlier
        """
        return self._contract.events.Penalized

    @property
    def PriceUpdated(self) -> contract.ContractEvent:
        """Binding for `event PriceUpdated` on the Oracle contract.

        Emitted when a new price is calculated for a symbol
        """
        return self._contract.events.PriceUpdated

    @property
    def SuccessfulVote(self) -> contract.ContractEvent:
        """Binding for `event SuccessfulVote` on the Oracle contract.

        Emitted when a valid report is accepted
        """
        return self._contract.events.SuccessfulVote

    @property
    def TotalOracleRewards(self) -> contract.ContractEvent:
        """Binding for `event TotalOracleRewards` on the Oracle contract.

        Emitted when oracle rewards are distributed
        """
        return self._contract.events.TotalOracleRewards

    def get_config(
        self,
    ) -> Config:
        """Binding for `getConfig` on the Oracle contract.

        Returns
        -------
        Config
            config, the current oracle config
        """
        return_value = self._contract.functions.getConfig().call()
        return Config(
            eth_typing.ChecksumAddress(return_value[0]),
            eth_typing.ChecksumAddress(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
            int(return_value[8]),
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

    def get_last_round_block(
        self,
    ) -> int:
        """Binding for `getLastRoundBlock` on the Oracle contract.

        Returns
        -------
        int
            the block at which the last completed round ended
        """
        return_value = self._contract.functions.getLastRoundBlock().call()
        return int(return_value)

    def get_new_vote_period(
        self,
    ) -> int:
        """Binding for `getNewVotePeriod` on the Oracle contract.

        Retrieve the new vote period that is going to be applied at the end of the vote
        round.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getNewVotePeriod().call()
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

    def get_non_reveal_threshold(
        self,
    ) -> int:
        """Binding for `getNonRevealThreshold` on the Oracle contract.

        Returns the tolerance for missed reveal count before the voter gets punished.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getNonRevealThreshold().call()
        return int(return_value)

    def get_reports(
        self,
        _symbol: str,
        _voter: eth_typing.ChecksumAddress,
    ) -> Report:
        """Binding for `getReports` on the Oracle contract.

        Parameters
        ----------
        _symbol : str
            , the target symbol
        _voter : eth_typing.ChecksumAddress
            , the target voter address

        Returns
        -------
        Report
            the latest report of that voter for that symbol
        """
        return_value = self._contract.functions.getReports(
            _symbol,
            _voter,
        ).call()
        return Report(int(return_value[0]), int(return_value[1]))

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

    def get_symbol_updated_round(
        self,
    ) -> int:
        """Binding for `getSymbolUpdatedRound` on the Oracle contract.

        Returns
        -------
        int
            the round at which the symbols got updated
        """
        return_value = self._contract.functions.getSymbolUpdatedRound().call()
        return int(return_value)

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

    def get_voter_info(
        self,
        _voter: eth_typing.ChecksumAddress,
    ) -> VoterInfo:
        """Binding for `getVoterInfo` on the Oracle contract.

        Parameters
        ----------
        _voter : eth_typing.ChecksumAddress
            , the voter address

        Returns
        -------
        VoterInfo
            the related voter information
        """
        return_value = self._contract.functions.getVoterInfo(
            _voter,
        ).call()
        return VoterInfo(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            bool(return_value[4]),
            bool(return_value[5]),
        )

    def get_voter_treasuries(
        self,
        _oracle_address: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getVoterTreasuries` on the Oracle contract.

        Parameters
        ----------
        _oracle_address : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
            his treasury address
        """
        return_value = self._contract.functions.getVoterTreasuries(
            _oracle_address,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def get_voter_validators(
        self,
        _oracle_address: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getVoterValidators` on the Oracle contract.

        Parameters
        ----------
        _oracle_address : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
            his node address
        """
        return_value = self._contract.functions.getVoterValidators(
            _oracle_address,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

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

    def set_commit_reveal_config(
        self,
        _threshold: int,
        _reset_interval: int,
    ) -> contract.ContractFunction:
        """Binding for `setCommitRevealConfig` on the Oracle contract.

        Setter for commit-reveal penalty mechanism configuration.

        Parameters
        ----------
        _threshold : int
        _reset_interval : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setCommitRevealConfig(
            _threshold,
            _reset_interval,
        )

    def set_slashing_config(
        self,
        _outlier_slashing_threshold: int,
        _outlier_detection_threshold: int,
        _base_slashing_rate: int,
        _slashing_rate_cap: int,
    ) -> contract.ContractFunction:
        """Binding for `setSlashingConfig` on the Oracle contract.

        Setter for the internal slashing and outlier detection configuration.

        Parameters
        ----------
        _outlier_slashing_threshold : int
        _outlier_detection_threshold : int
        _base_slashing_rate : int
        _slashing_rate_cap : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSlashingConfig(
            _outlier_slashing_threshold,
            _outlier_detection_threshold,
            _base_slashing_rate,
            _slashing_rate_cap,
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

        Setter for the vote period, new vote period will be applied at the end of the
        round.

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
                            "internalType": "contract IAutonity",
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
                        {
                            "internalType": "uint256",
                            "name": "nonRevealThreshold",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "revealResetInterval",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "slashingRateCap",
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
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "methodSignature",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "bytes",
                    "name": "returnData",
                    "type": "bytes",
                },
            ],
            "name": "CallFailed",
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
                    "internalType": "uint256",
                    "name": "_round",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_nonRevealCount",
                    "type": "uint256",
                },
            ],
            "name": "CommitRevealMissed",
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
                    "internalType": "string",
                    "name": "cause",
                    "type": "string",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "reporter",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "expValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "actualValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "extra",
                    "type": "uint8",
                },
            ],
            "name": "InvalidVote",
            "type": "event",
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
                    "indexed": False,
                    "internalType": "address",
                    "name": "reporter",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "extra",
                    "type": "uint8",
                },
            ],
            "name": "NewVoter",
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
                    "internalType": "uint256",
                    "name": "_round",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_missedReveal",
                    "type": "uint256",
                },
            ],
            "name": "NoRevealPenalty",
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
                    "internalType": "uint256",
                    "name": "_slashingAmount",
                    "type": "uint256",
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
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "price",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "round",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "string",
                    "name": "symbol",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "status",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "timestamp",
                    "type": "uint256",
                },
            ],
            "name": "PriceUpdated",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "reporter",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "extra",
                    "type": "uint8",
                },
            ],
            "name": "SuccessfulVote",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "ntnReward",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "atnReward",
                    "type": "uint256",
                },
            ],
            "name": "TotalOracleRewards",
            "type": "event",
        },
        {"stateMutability": "payable", "type": "fallback"},
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
            "name": "getConfig",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "contract IAutonity",
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
                        {
                            "internalType": "uint256",
                            "name": "nonRevealThreshold",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "revealResetInterval",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "slashingRateCap",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Oracle.Config",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getDecimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getLastRoundBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getNewVotePeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
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
            "inputs": [],
            "name": "getNonRevealThreshold",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "_symbol", "type": "string"},
                {"internalType": "address", "name": "_voter", "type": "address"},
            ],
            "name": "getReports",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint120", "name": "price", "type": "uint120"},
                        {
                            "internalType": "uint8",
                            "name": "confidence",
                            "type": "uint8",
                        },
                    ],
                    "internalType": "struct IOracle.Report",
                    "name": "",
                    "type": "tuple",
                }
            ],
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
            "name": "getSymbolUpdatedRound",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
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
            "inputs": [
                {"internalType": "address", "name": "_voter", "type": "address"}
            ],
            "name": "getVoterInfo",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "round", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "commit",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "performance",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "nonRevealCount",
                            "type": "uint256",
                        },
                        {"internalType": "bool", "name": "isVoter", "type": "bool"},
                        {
                            "internalType": "bool",
                            "name": "reportAvailable",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct Oracle.VoterInfo",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_oracleAddress", "type": "address"}
            ],
            "name": "getVoterTreasuries",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_oracleAddress", "type": "address"}
            ],
            "name": "getVoterValidators",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
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
                {"internalType": "uint256", "name": "_threshold", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "_resetInterval",
                    "type": "uint256",
                },
            ],
            "name": "setCommitRevealConfig",
            "outputs": [],
            "stateMutability": "nonpayable",
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
                {
                    "internalType": "uint256",
                    "name": "_slashingRateCap",
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
            "name": "updateVotersAndSymbol",
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
        {"stateMutability": "payable", "type": "receive"},
    ],
)
