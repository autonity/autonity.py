"""Accountability contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import enum
import typing
from dataclasses import dataclass

import eth_typing
import hexbytes
import web3
from web3.contract import contract


class Rule(enum.IntEnum):
    """Port of `enum Rule` on the IAccountability contract."""

    PN = 0
    PO = 1
    PVN = 2
    PVO = 3
    PVO12 = 4
    C = 5
    C1 = 6
    INVALID_PROPOSAL = 7
    INVALID_PROPOSER = 8
    EQUIVOCATION = 9


class EventType(enum.IntEnum):
    """Port of `enum EventType` on the IAccountability contract."""

    FAULT_PROOF = 0
    ACCUSATION = 1
    INNOCENCE_PROOF = 2


@dataclass
class BaseSlashingRates:
    """Port of `struct BaseSlashingRates` on the IAccountability contract."""

    low: int
    mid: int
    high: int


@dataclass
class Factors:
    """Port of `struct Factors` on the IAccountability contract."""

    collusion: int
    history: int
    jail: int


@dataclass
class Config:
    """Port of `struct Config` on the IAccountability contract."""

    innocence_proof_submission_window: int
    delta: int
    range: int
    base_slashing_rates: BaseSlashingRates
    factors: Factors


@dataclass
class Event:
    """Port of `struct Event` on the IAccountability contract."""

    event_type: EventType
    rule: Rule
    reporter: eth_typing.ChecksumAddress
    offender: eth_typing.ChecksumAddress
    raw_proof: hexbytes.HexBytes
    id: int
    block: int
    epoch: int
    reporting_block: int
    message_hash: int


class Accountability:
    """Accountability contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed Accountability contract.
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
    def AccountabilityFactorsUpdate(self) -> contract.ContractEvent:
        """Binding for `event AccountabilityFactorsUpdate` on the Accountability contract.

        Event emitted after accountability factors (collusion, history and jail) are
        updated
        """
        return self._contract.events.AccountabilityFactorsUpdate

    @property
    def BaseSlashingRateUpdate(self) -> contract.ContractEvent:
        """Binding for `event BaseSlashingRateUpdate` on the Accountability contract.

        Event emitted after base slashing rates are updated
        """
        return self._contract.events.BaseSlashingRateUpdate

    @property
    def CallFailed(self) -> contract.ContractEvent:
        """Binding for `event CallFailed` on the Accountability contract.

        This event is emitted when a call to an address fails in a protocol function
        (like finalize()).
        """
        return self._contract.events.CallFailed

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the Accountability contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the Accountability contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the Accountability contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the Accountability contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def InnocenceProven(self) -> contract.ContractEvent:
        """Binding for `event InnocenceProven` on the Accountability contract.

        Event emitted after receiving a proof-of-innocence cancelling an accusation.
        """
        return self._contract.events.InnocenceProven

    @property
    def NewAccusation(self) -> contract.ContractEvent:
        """Binding for `event NewAccusation` on the Accountability contract.

        Event emitted after receiving an accusation, the reported validator has a
        certain amount of time to submit a proof-of-innocence, otherwise, he gets
        slashed.
        """
        return self._contract.events.NewAccusation

    @property
    def NewFaultProof(self) -> contract.ContractEvent:
        """Binding for `event NewFaultProof` on the Accountability contract.

        Event emitted when a fault proof has been submitted. The reported validator will
        be silenced and slashed at the end of the current epoch.
        """
        return self._contract.events.NewFaultProof

    @property
    def ReporterRewarded(self) -> contract.ContractEvent:
        """Binding for `event ReporterRewarded` on the Accountability contract.

        Event emitted when a reporter is rewarded for submitting a valid proof
        """
        return self._contract.events.ReporterRewarded

    @property
    def SlashingEvent(self) -> contract.ContractEvent:
        """Binding for `event SlashingEvent` on the Accountability contract.

        Event emitted after a successful slashing.
        """
        return self._contract.events.SlashingEvent

    def can_accuse(
        self,
        _offender: eth_typing.ChecksumAddress,
        _rule: Rule,
        _block: int,
    ) -> typing.Tuple[bool, int]:
        """Binding for `canAccuse` on the Accountability contract.

        Parameters
        ----------
        _offender : eth_typing.ChecksumAddress
        _rule : Rule
        _block : int

        Returns
        -------
        bool
        int
        """
        return_value = self._contract.functions.canAccuse(
            _offender,
            int(_rule),
            _block,
        ).call()
        return (
            bool(return_value[0]),
            int(return_value[1]),
        )

    def can_slash(
        self,
        _offender: eth_typing.ChecksumAddress,
        _rule: Rule,
        _block: int,
    ) -> bool:
        """Binding for `canSlash` on the Accountability contract.

        Parameters
        ----------
        _offender : eth_typing.ChecksumAddress
        _rule : Rule
        _block : int

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.canSlash(
            _offender,
            int(_rule),
            _block,
        ).call()
        return bool(return_value)

    def get_beneficiary(
        self,
        _offender: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getBeneficiary` on the Accountability contract.

        Parameters
        ----------
        _offender : eth_typing.ChecksumAddress
            , the validator address of the offender

        Returns
        -------
        eth_typing.ChecksumAddress
            the relative beneficiary which is going to receive the rewards of the
            offender
        """
        return_value = self._contract.functions.getBeneficiary(
            _offender,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def get_config(
        self,
    ) -> Config:
        """Binding for `getConfig` on the Accountability contract.

        Returns
        -------
        Config
            config, the config of the accountability contract
        """
        return_value = self._contract.functions.getConfig().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            BaseSlashingRates(
                int(return_value[3][0]),
                int(return_value[3][1]),
                int(return_value[3][2]),
            ),
            Factors(
                int(return_value[4][0]),
                int(return_value[4][1]),
                int(return_value[4][2]),
            ),
        )

    def get_event(
        self,
        _id: int,
    ) -> Event:
        """Binding for `getEvent` on the Accountability contract.

        Parameters
        ----------
        _id : int
            , the event id

        Returns
        -------
        Event
            the relative accountability event
        """
        return_value = self._contract.functions.getEvent(
            _id,
        ).call()
        return Event(
            EventType(return_value[0]),
            Rule(return_value[1]),
            eth_typing.ChecksumAddress(return_value[2]),
            eth_typing.ChecksumAddress(return_value[3]),
            hexbytes.HexBytes(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
            int(return_value[8]),
            int(return_value[9]),
        )

    def get_events_length(
        self,
    ) -> int:
        """Binding for `getEventsLength` on the Accountability contract.

        Returns
        -------
        int
            the number of accountability events
        """
        return_value = self._contract.functions.getEventsLength().call()
        return int(return_value)

    def get_grace_period(
        self,
    ) -> int:
        """Binding for `getGracePeriod` on the Accountability contract.

        Returns
        -------
        int
            gracePeriod, the current grace period in accountability
        """
        return_value = self._contract.functions.getGracePeriod().call()
        return int(return_value)

    def get_history(
        self,
        _validator: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getHistory` on the Accountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , the validator address

        Returns
        -------
        int
            the number of times the validator has been punished in the past
        """
        return_value = self._contract.functions.getHistory(
            _validator,
        ).call()
        return int(return_value)

    def get_slashing_history(
        self,
        _validator: eth_typing.ChecksumAddress,
        _epoch: int,
    ) -> int:
        """Binding for `getSlashingHistory` on the Accountability contract.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            , the validator address
        _epoch : int
            , the epoch id

        Returns
        -------
        int
            the severity at which the validator was punished in that epoch
        """
        return_value = self._contract.functions.getSlashingHistory(
            _validator,
            _epoch,
        ).call()
        return int(return_value)

    def get_validator_accusation(
        self,
        _val: eth_typing.ChecksumAddress,
    ) -> Event:
        """Binding for `getValidatorAccusation` on the Accountability contract.

        Parameters
        ----------
        _val : eth_typing.ChecksumAddress
            , the validator address

        Returns
        -------
        Event
            the current accusation event against _val (if any)
        """
        return_value = self._contract.functions.getValidatorAccusation(
            _val,
        ).call()
        return Event(
            EventType(return_value[0]),
            Rule(return_value[1]),
            eth_typing.ChecksumAddress(return_value[2]),
            eth_typing.ChecksumAddress(return_value[3]),
            hexbytes.HexBytes(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
            int(return_value[8]),
            int(return_value[9]),
        )

    def get_validator_faults(
        self,
        _val: eth_typing.ChecksumAddress,
    ) -> typing.List[Event]:
        """Binding for `getValidatorFaults` on the Accountability contract.

        Parameters
        ----------
        _val : eth_typing.ChecksumAddress
            , the validator address

        Returns
        -------
        typing.List[Event]
            the history of faults of this validator
        """
        return_value = self._contract.functions.getValidatorFaults(
            _val,
        ).call()
        return [
            Event(
                EventType(return_value_elem[0]),
                Rule(return_value_elem[1]),
                eth_typing.ChecksumAddress(return_value_elem[2]),
                eth_typing.ChecksumAddress(return_value_elem[3]),
                hexbytes.HexBytes(return_value_elem[4]),
                int(return_value_elem[5]),
                int(return_value_elem[6]),
                int(return_value_elem[7]),
                int(return_value_elem[8]),
                int(return_value_elem[9]),
            )
            for return_value_elem in return_value
        ]

    def set_base_slashing_rates(
        self,
        _rates: BaseSlashingRates,
    ) -> contract.ContractFunction:
        """Binding for `setBaseSlashingRates` on the Accountability contract.

        Parameters
        ----------
        _rates : BaseSlashingRates

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setBaseSlashingRates(
            (_rates.low, _rates.mid, _rates.high),
        )

    def set_delta(
        self,
        _delta: int,
    ) -> contract.ContractFunction:
        """Binding for `setDelta` on the Accountability contract.

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

    def set_factors(
        self,
        _factors: Factors,
    ) -> contract.ContractFunction:
        """Binding for `setFactors` on the Accountability contract.

        Parameters
        ----------
        _factors : Factors

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setFactors(
            (_factors.collusion, _factors.history, _factors.jail),
        )

    def set_innocence_proof_submission_window(
        self,
        _window: int,
    ) -> contract.ContractFunction:
        """Binding for `setInnocenceProofSubmissionWindow` on the Accountability contract.

        Parameters
        ----------
        _window : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInnocenceProofSubmissionWindow(
            _window,
        )

    def set_range(
        self,
        _range: int,
    ) -> contract.ContractFunction:
        """Binding for `setRange` on the Accountability contract.

        Parameters
        ----------
        _range : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setRange(
            _range,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "internalType": "contract IAutonity",
                    "name": "_autonity",
                    "type": "address",
                },
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "innocenceProofSubmissionWindow",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "delta", "type": "uint256"},
                        {"internalType": "uint256", "name": "range", "type": "uint256"},
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "low",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "mid",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "high",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAccountability.BaseSlashingRates",
                            "name": "baseSlashingRates",
                            "type": "tuple",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "collusion",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "history",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "jail",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAccountability.Factors",
                            "name": "factors",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IAccountability.Config",
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
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "collusion",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "history",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "jail", "type": "uint256"},
                    ],
                    "indexed": False,
                    "internalType": "struct IAccountability.Factors",
                    "name": "oldFactors",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "collusion",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "history",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "jail", "type": "uint256"},
                    ],
                    "indexed": False,
                    "internalType": "struct IAccountability.Factors",
                    "name": "newFactors",
                    "type": "tuple",
                },
            ],
            "name": "AccountabilityFactorsUpdate",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "low", "type": "uint256"},
                        {"internalType": "uint256", "name": "mid", "type": "uint256"},
                        {"internalType": "uint256", "name": "high", "type": "uint256"},
                    ],
                    "indexed": False,
                    "internalType": "struct IAccountability.BaseSlashingRates",
                    "name": "oldRates",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "low", "type": "uint256"},
                        {"internalType": "uint256", "name": "mid", "type": "uint256"},
                        {"internalType": "uint256", "name": "high", "type": "uint256"},
                    ],
                    "indexed": False,
                    "internalType": "struct IAccountability.BaseSlashingRates",
                    "name": "newRates",
                    "type": "tuple",
                },
            ],
            "name": "BaseSlashingRateUpdate",
            "type": "event",
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
                    "indexed": True,
                    "internalType": "address",
                    "name": "_offender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_id",
                    "type": "uint256",
                },
            ],
            "name": "InnocenceProven",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_offender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_severity",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_id",
                    "type": "uint256",
                },
            ],
            "name": "NewAccusation",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_offender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_severity",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_id",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_epoch",
                    "type": "uint256",
                },
            ],
            "name": "NewFaultProof",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "_reporter",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_offender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_ntnReward",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_atnReward",
                    "type": "uint256",
                },
            ],
            "name": "ReporterRewarded",
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
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "eventId",
                    "type": "uint256",
                },
            ],
            "name": "SlashingEvent",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_offender", "type": "address"},
                {
                    "internalType": "enum IAccountability.Rule",
                    "name": "_rule",
                    "type": "uint8",
                },
                {"internalType": "uint256", "name": "_block", "type": "uint256"},
            ],
            "name": "canAccuse",
            "outputs": [
                {"internalType": "bool", "name": "_result", "type": "bool"},
                {"internalType": "uint256", "name": "_deadline", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_offender", "type": "address"},
                {
                    "internalType": "enum IAccountability.Rule",
                    "name": "_rule",
                    "type": "uint8",
                },
                {"internalType": "uint256", "name": "_block", "type": "uint256"},
            ],
            "name": "canSlash",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_offender", "type": "address"},
                {"internalType": "uint256", "name": "_ntnReward", "type": "uint256"},
            ],
            "name": "distributeRewards",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "_epochEnd", "type": "bool"}],
            "name": "finalize",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_offender", "type": "address"}
            ],
            "name": "getBeneficiary",
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
                            "name": "innocenceProofSubmissionWindow",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "delta", "type": "uint256"},
                        {"internalType": "uint256", "name": "range", "type": "uint256"},
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "low",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "mid",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "high",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAccountability.BaseSlashingRates",
                            "name": "baseSlashingRates",
                            "type": "tuple",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "collusion",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "history",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "jail",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAccountability.Factors",
                            "name": "factors",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IAccountability.Config",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
            "name": "getEvent",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getEventsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getGracePeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"}
            ],
            "name": "getHistory",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_epoch", "type": "uint256"},
            ],
            "name": "getSlashingHistory",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_val", "type": "address"}],
            "name": "getValidatorAccusation",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_val", "type": "address"}],
            "name": "getValidatorFaults",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event",
                    "name": "_event",
                    "type": "tuple",
                }
            ],
            "name": "handleAccusation",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event",
                    "name": "_event",
                    "type": "tuple",
                }
            ],
            "name": "handleInnocenceProof",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IAccountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum IAccountability.Rule",
                            "name": "rule",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "reporter",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "offender",
                            "type": "address",
                        },
                        {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint256", "name": "block", "type": "uint256"},
                        {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "reportingBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "messageHash",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAccountability.Event",
                    "name": "_event",
                    "type": "tuple",
                }
            ],
            "name": "handleMisbehaviour",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "low", "type": "uint256"},
                        {"internalType": "uint256", "name": "mid", "type": "uint256"},
                        {"internalType": "uint256", "name": "high", "type": "uint256"},
                    ],
                    "internalType": "struct IAccountability.BaseSlashingRates",
                    "name": "_rates",
                    "type": "tuple",
                }
            ],
            "name": "setBaseSlashingRates",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "_newCommittee",
                    "type": "address[]",
                }
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
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "collusion",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "history",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "jail", "type": "uint256"},
                    ],
                    "internalType": "struct IAccountability.Factors",
                    "name": "_factors",
                    "type": "tuple",
                }
            ],
            "name": "setFactors",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_window", "type": "uint256"}
            ],
            "name": "setInnocenceProofSubmissionWindow",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_range", "type": "uint256"}
            ],
            "name": "setRange",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
