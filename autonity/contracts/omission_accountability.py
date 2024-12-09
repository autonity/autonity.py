"""OmissionAccountability contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


@dataclass
class Config:
    """Port of `struct Config` on the OmissionAccountability contract."""

    inactivity_threshold: int
    lookback_window: int
    past_performance_weight: int
    initial_jailing_period: int
    initial_probation_period: int
    initial_slashing_rate: int
    delta: int


class OmissionAccountability:
    """OmissionAccountability contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed OmissionAccountability contract.
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
    def InactivityJailingEvent(self) -> contract.ContractEvent:
        """Binding for `event InactivityJailingEvent` on the OmissionAccountability contract."""
        return self._contract.events.InactivityJailingEvent

    @property
    def InactivitySlashingEvent(self) -> contract.ContractEvent:
        """Binding for `event InactivitySlashingEvent` on the OmissionAccountability contract."""
        return self._contract.events.InactivitySlashingEvent

    def scale_factor(
        self,
    ) -> int:
        """Binding for `SCALE_FACTOR` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.SCALE_FACTOR().call()
        return int(return_value)

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the OmissionAccountability contract.

        Returns
        -------
        Config
        """
        return_value = self._contract.functions.config().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
        )

    def distribute_proposer_rewards(
        self,
        _ntn_reward: int,
    ) -> contract.ContractFunction:
        """Binding for `distributeProposerRewards` on the OmissionAccountability contract.

        Parameters
        ----------
        _ntn_reward : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.distributeProposerRewards(
            _ntn_reward,
        )

    def epoch_collusion_degree(
        self,
        key0: int,
    ) -> int:
        """Binding for `epochCollusionDegree` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.epochCollusionDegree(
            key0,
        ).call()
        return int(return_value)

    def faulty_proposers(
        self,
        key0: int,
    ) -> bool:
        """Binding for `faultyProposers` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.faultyProposers(
            key0,
        ).call()
        return bool(return_value)

    def faulty_proposers_in_window(
        self,
    ) -> int:
        """Binding for `faultyProposersInWindow` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.faultyProposersInWindow().call()
        return int(return_value)

    def get_absentees_last_height(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """Binding for `getAbsenteesLastHeight` on the OmissionAccountability contract.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
        """
        return_value = self._contract.functions.getAbsenteesLastHeight().call()
        return [
            eth_typing.ChecksumAddress(return_value_elem)
            for return_value_elem in return_value
        ]

    def get_delta(
        self,
    ) -> int:
        """Binding for `getDelta` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getDelta().call()
        return int(return_value)

    def get_inactivity_score(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getInactivityScore` on the OmissionAccountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getInactivityScore(
            _validator,
        ).call()
        return int(return_value)

    def get_lookback_window(
        self,
    ) -> int:
        """Binding for `getLookbackWindow` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getLookbackWindow().call()
        return int(return_value)

    def get_scale_factor(
        self,
    ) -> int:
        """Binding for `getScaleFactor` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getScaleFactor().call()
        return int(return_value)

    def get_total_effort(
        self,
    ) -> int:
        """Binding for `getTotalEffort` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getTotalEffort().call()
        return int(return_value)

    def inactive_validators(
        self,
        key0: int,
        key1: eth_typing.ChecksumAddress,
    ) -> bool:
        """Binding for `inactiveValidators` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : int
        key1 : eth_typing.ChecksumAddress

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.inactiveValidators(
            key0,
            key1,
        ).call()
        return bool(return_value)

    def inactivity_counter(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `inactivityCounter` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.inactivityCounter(
            key0,
        ).call()
        return int(return_value)

    def inactivity_scores(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `inactivityScores` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.inactivityScores(
            key0,
        ).call()
        return int(return_value)

    def last_active(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `lastActive` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lastActive(
            key0,
        ).call()
        return int(return_value)

    def probation_periods(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `probationPeriods` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.probationPeriods(
            key0,
        ).call()
        return int(return_value)

    def proposer_effort(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `proposerEffort` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.proposerEffort(
            key0,
        ).call()
        return int(return_value)

    def repeated_offences(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `repeatedOffences` on the OmissionAccountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.repeatedOffences(
            key0,
        ).call()
        return int(return_value)

    def set_delta(
        self,
        _delta: int,
    ) -> contract.ContractFunction:
        """Binding for `setDelta` on the OmissionAccountability contract.

        Parameters
        ----------
        _delta : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setDelta(
            _delta,
        )

    def set_inactivity_threshold(
        self,
        _inactivity_threshold: int,
    ) -> contract.ContractFunction:
        """Binding for `setInactivityThreshold` on the OmissionAccountability contract.

        Parameters
        ----------
        _inactivity_threshold : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInactivityThreshold(
            _inactivity_threshold,
        )

    def set_initial_jailing_period(
        self,
        _initial_jailing_period: int,
    ) -> contract.ContractFunction:
        """Binding for `setInitialJailingPeriod` on the OmissionAccountability contract.

        Parameters
        ----------
        _initial_jailing_period : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInitialJailingPeriod(
            _initial_jailing_period,
        )

    def set_initial_probation_period(
        self,
        _initial_probation_period: int,
    ) -> contract.ContractFunction:
        """Binding for `setInitialProbationPeriod` on the OmissionAccountability contract.

        Parameters
        ----------
        _initial_probation_period : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInitialProbationPeriod(
            _initial_probation_period,
        )

    def set_initial_slashing_rate(
        self,
        _initial_slashing_rate: int,
    ) -> contract.ContractFunction:
        """Binding for `setInitialSlashingRate` on the OmissionAccountability contract.

        Parameters
        ----------
        _initial_slashing_rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInitialSlashingRate(
            _initial_slashing_rate,
        )

    def set_lookback_window(
        self,
        _lookback_window: int,
    ) -> contract.ContractFunction:
        """Binding for `setLookbackWindow` on the OmissionAccountability contract.

        Parameters
        ----------
        _lookback_window : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setLookbackWindow(
            _lookback_window,
        )

    def set_past_performance_weight(
        self,
        _past_performance_weight: int,
    ) -> contract.ContractFunction:
        """Binding for `setPastPerformanceWeight` on the OmissionAccountability contract.

        Parameters
        ----------
        _past_performance_weight : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setPastPerformanceWeight(
            _past_performance_weight,
        )

    def total_effort(
        self,
    ) -> int:
        """Binding for `totalEffort` on the OmissionAccountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalEffort().call()
        return int(return_value)


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "internalType": "address payable",
                    "name": "_autonity",
                    "type": "address",
                },
                {"internalType": "address", "name": "_operator", "type": "address"},
                {
                    "internalType": "address[]",
                    "name": "_treasuries",
                    "type": "address[]",
                },
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "inactivityThreshold",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lookbackWindow",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "pastPerformanceWeight",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "initialJailingPeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "initialProbationPeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "initialSlashingRate",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "delta", "type": "uint256"},
                    ],
                    "internalType": "struct OmissionAccountability.Config",
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
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "releaseBlock",
                    "type": "uint256",
                },
            ],
            "name": "InactivityJailingEvent",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
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
                    "name": "releaseBlock",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "isJailbound",
                    "type": "bool",
                },
            ],
            "name": "InactivitySlashingEvent",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "SCALE_FACTOR",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "config",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "inactivityThreshold",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "lookbackWindow",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "pastPerformanceWeight",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "initialJailingPeriod",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "initialProbationPeriod",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "initialSlashingRate",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "delta", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_ntnReward", "type": "uint256"}
            ],
            "name": "distributeProposerRewards",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "epochCollusionDegree",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "faultyProposers",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "faultyProposersInWindow",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "_epochEnded", "type": "bool"}],
            "name": "finalize",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAbsenteesLastHeight",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getDelta",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getInactivityScore",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getLookbackWindow",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getScaleFactor",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTotalEffort",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "inactiveValidators",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "inactivityCounter",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "inactivityScores",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "lastActive",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "probationPeriods",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "proposerEffort",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "repeatedOffences",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "address", "name": "addr", "type": "address"},
                        {
                            "internalType": "uint256",
                            "name": "votingPower",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                    ],
                    "internalType": "struct Autonity.CommitteeMember[]",
                    "name": "_committee",
                    "type": "tuple[]",
                },
                {
                    "internalType": "address[]",
                    "name": "_treasuries",
                    "type": "address[]",
                },
            ],
            "name": "setCommittee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_delta", "type": "uint256"}
            ],
            "name": "setDelta",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_epochBlock", "type": "uint256"}
            ],
            "name": "setEpochBlock",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_inactivityThreshold",
                    "type": "uint256",
                }
            ],
            "name": "setInactivityThreshold",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_initialJailingPeriod",
                    "type": "uint256",
                }
            ],
            "name": "setInitialJailingPeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_initialProbationPeriod",
                    "type": "uint256",
                }
            ],
            "name": "setInitialProbationPeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_initialSlashingRate",
                    "type": "uint256",
                }
            ],
            "name": "setInitialSlashingRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_lookbackWindow",
                    "type": "uint256",
                }
            ],
            "name": "setLookbackWindow",
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
                    "internalType": "uint256",
                    "name": "_pastPerformanceWeight",
                    "type": "uint256",
                }
            ],
            "name": "setPastPerformanceWeight",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalEffort",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
