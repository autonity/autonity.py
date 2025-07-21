"""OmissionAccountability contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract


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
    def CallFailed(self) -> contract.ContractEvent:
        """Binding for `event CallFailed` on the OmissionAccountability contract.

        This event is emitted when a call to an address fails in a protocol function
        (like finalize()).
        """
        return self._contract.events.CallFailed

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the OmissionAccountability contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the OmissionAccountability contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the OmissionAccountability contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the OmissionAccountability contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def InactivityJailingEvent(self) -> contract.ContractEvent:
        """Binding for `event InactivityJailingEvent` on the OmissionAccountability contract."""
        return self._contract.events.InactivityJailingEvent

    @property
    def InactivitySlashingEvent(self) -> contract.ContractEvent:
        """Binding for `event InactivitySlashingEvent` on the OmissionAccountability contract."""
        return self._contract.events.InactivitySlashingEvent

    @property
    def TotalProposerRewards(self) -> contract.ContractEvent:
        """Binding for `event TotalProposerRewards` on the OmissionAccountability contract."""
        return self._contract.events.TotalProposerRewards

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

    def get_config(
        self,
    ) -> Config:
        """Binding for `getConfig` on the OmissionAccountability contract.

        Returns
        -------
        Config
            the current config
        """
        return_value = self._contract.functions.getConfig().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
        )

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

    def get_epoch_collusion_degree(
        self,
        _epoch_id: int,
    ) -> int:
        """Binding for `getEpochCollusionDegree` on the OmissionAccountability contract.

        Parameters
        ----------
        _epoch_id : int

        Returns
        -------
        int
            the collusion degree (number of punished validators) in that epoch
        """
        return_value = self._contract.functions.getEpochCollusionDegree(
            _epoch_id,
        ).call()
        return int(return_value)

    def get_epoch_collusion_degree_length(
        self,
    ) -> int:
        """Binding for `getEpochCollusionDegreeLength` on the OmissionAccountability contract.

        Returns
        -------
        int
            length of the collusion degree array
        """
        return_value = self._contract.functions.getEpochCollusionDegreeLength().call()
        return int(return_value)

    def get_faulty_proposers(
        self,
        _height: int,
    ) -> bool:
        """Binding for `getFaultyProposers` on the OmissionAccountability contract.

        Parameters
        ----------
        _height : int
            , height number

        Returns
        -------
        bool
            whether the proposer of that height was faulty or not
        """
        return_value = self._contract.functions.getFaultyProposers(
            _height,
        ).call()
        return bool(return_value)

    def get_faulty_proposers_in_window(
        self,
    ) -> int:
        """Binding for `getFaultyProposersInWindow` on the OmissionAccountability contract.

        Returns
        -------
        int
            the number of faulty proposers in the current window
        """
        return_value = self._contract.functions.getFaultyProposersInWindow().call()
        return int(return_value)

    def get_inactive_validators(
        self,
        _height: int,
        _validator: eth_typing.ChecksumAddress,
    ) -> bool:
        """Binding for `getInactiveValidators` on the OmissionAccountability contract.

        the result of this getter does not take into account the lookback window logic.
        It just signals whether the validator was included in the activity proof or not.

        Parameters
        ----------
        _height : int
            , height number
        _validator : eth_typing.ChecksumAddress
            , validator node address

        Returns
        -------
        bool
            whether the specified validator was inactive at the specified height
        """
        return_value = self._contract.functions.getInactiveValidators(
            _height,
            _validator,
        ).call()
        return bool(return_value)

    def get_inactivity_counter(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getInactivityCounter` on the OmissionAccountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , node address of the validator

        Returns
        -------
        int
            the current inactivity counter of the validator
        """
        return_value = self._contract.functions.getInactivityCounter(
            _validator,
        ).call()
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

    def get_last_active(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getLastActive` on the OmissionAccountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , node address of the validator

        Returns
        -------
        int
            the last block at which the validator was recorded as active.         -1
            means that they are not on an inactivity streak
        """
        return_value = self._contract.functions.getLastActive(
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

    def get_probation_periods(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getProbationPeriods` on the OmissionAccountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , node address of the validator

        Returns
        -------
        int
            the current probation period of the validator
        """
        return_value = self._contract.functions.getProbationPeriods(
            _validator,
        ).call()
        return int(return_value)

    def get_proposer_effort(
        self,
        _node_address: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getProposerEffort` on the OmissionAccountability contract.

        Parameters
        ----------
        _node_address : eth_typing.ChecksumAddress

        Returns
        -------
        int
            the proposer effort accumulated by the validator up to now
        """
        return_value = self._contract.functions.getProposerEffort(
            _node_address,
        ).call()
        return int(return_value)

    def get_repeated_offences(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getRepeatedOffences` on the OmissionAccountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , node address of the validator

        Returns
        -------
        int
            the current number of repeated offences of the validator
        """
        return_value = self._contract.functions.getRepeatedOffences(
            _validator,
        ).call()
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
            "name": "TotalProposerRewards",
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
            "inputs": [
                {"internalType": "uint256", "name": "_ntnReward", "type": "uint256"}
            ],
            "name": "distributeProposerRewards",
            "outputs": [],
            "stateMutability": "payable",
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
            "name": "getConfig",
            "outputs": [
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
                    "name": "",
                    "type": "tuple",
                }
            ],
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
                {"internalType": "uint256", "name": "_epochID", "type": "uint256"}
            ],
            "name": "getEpochCollusionDegree",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getEpochCollusionDegreeLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_height", "type": "uint256"}
            ],
            "name": "getFaultyProposers",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getFaultyProposersInWindow",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_height", "type": "uint256"},
                {"internalType": "address", "name": "_validator", "type": "address"},
            ],
            "name": "getInactiveValidators",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getInactivityCounter",
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
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getLastActive",
            "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
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
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getProbationPeriods",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"}
            ],
            "name": "getProposerEffort",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getRepeatedOffences",
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
                    "internalType": "struct IAutonity.CommitteeMember[]",
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
    ],
)
