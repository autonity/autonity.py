"""Accountability contract binding and data structures."""

# This module has been generated using pyabigen v0.2.10

import enum
import typing
from dataclasses import dataclass

import eth_typing
import hexbytes
import web3
from web3.contract import base_contract, contract

__version__ = "f6bcaae767bebf7271a94b2239b67314f8deac38"


class Rule(enum.IntEnum):
    """Port of `enum Rule` on the Accountability contract."""

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
    """Port of `enum EventType` on the Accountability contract."""

    FAULT_PROOF = 0
    ACCUSATION = 1
    INNOCENCE_PROOF = 2


@dataclass
class Config:
    """Port of `struct Config` on the Accountability contract."""

    innocence_proof_submission_window: int
    base_slashing_rate_low: int
    base_slashing_rate_mid: int
    collusion_factor: int
    history_factor: int
    jail_factor: int
    slashing_rate_precision: int


@dataclass
class Event:
    """Port of `struct Event` on the Accountability contract."""

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
    def InnocenceProven(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event InnocenceProven` on the Accountability contract."""
        return self._contract.events.InnocenceProven

    @property
    def NewAccusation(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewAccusation` on the Accountability contract."""
        return self._contract.events.NewAccusation

    @property
    def NewFaultProof(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewFaultProof` on the Accountability contract."""
        return self._contract.events.NewFaultProof

    @property
    def SlashingEvent(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event SlashingEvent` on the Accountability contract."""
        return self._contract.events.SlashingEvent

    def beneficiaries(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `beneficiaries` on the Accountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.beneficiaries(
            key0,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

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

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the Accountability contract.

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

    def epoch_period(
        self,
    ) -> int:
        """Binding for `epochPeriod` on the Accountability contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.epochPeriod().call()
        return int(return_value)

    def events(
        self,
        key0: int,
    ) -> Event:
        """Binding for `events` on the Accountability contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        Event
        """
        return_value = self._contract.functions.events(
            key0,
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

    def get_validator_accusation(
        self,
        _val: eth_typing.ChecksumAddress,
    ) -> Event:
        """Binding for `getValidatorAccusation` on the Accountability contract.

        Parameters
        ----------
        _val : eth_typing.ChecksumAddress

        Returns
        -------
        Event
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

        Returns
        -------
        typing.List[Event]
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

    def handle_accusation(
        self,
        _event: Event,
    ) -> contract.ContractFunction:
        """Binding for `handleAccusation` on the Accountability contract.

        Handle an accusation event. Need to be called by a registered validator account
        as the treasury-linked account will be used in case of a successful slashing
        event.

        Parameters
        ----------
        _event : Event

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.handleAccusation(
            (
                int(_event.event_type),
                int(_event.rule),
                _event.reporter,
                _event.offender,
                _event.raw_proof,
                _event.id,
                _event.block,
                _event.epoch,
                _event.reporting_block,
                _event.message_hash,
            ),
        )

    def handle_innocence_proof(
        self,
        _event: Event,
    ) -> contract.ContractFunction:
        """Binding for `handleInnocenceProof` on the Accountability contract.

        Handle an innocence proof. Need to be called by a registered validator account
        as the treasury-linked account will be used in case of a successful slashing
        event.

        Parameters
        ----------
        _event : Event

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.handleInnocenceProof(
            (
                int(_event.event_type),
                int(_event.rule),
                _event.reporter,
                _event.offender,
                _event.raw_proof,
                _event.id,
                _event.block,
                _event.epoch,
                _event.reporting_block,
                _event.message_hash,
            ),
        )

    def handle_misbehaviour(
        self,
        _event: Event,
    ) -> contract.ContractFunction:
        """Binding for `handleMisbehaviour` on the Accountability contract.

        Handle a misbehaviour event. Need to be called by a registered validator account
        as the treasury-linked account will be used in case of a successful slashing
        event.

        Parameters
        ----------
        _event : Event

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.handleMisbehaviour(
            (
                int(_event.event_type),
                int(_event.rule),
                _event.reporter,
                _event.offender,
                _event.raw_proof,
                _event.id,
                _event.block,
                _event.epoch,
                _event.reporting_block,
                _event.message_hash,
            ),
        )

    def set_committee(
        self,
        _new_committee: typing.List[eth_typing.ChecksumAddress],
    ) -> contract.ContractFunction:
        """Binding for `setCommittee` on the Accountability contract.

        setCommittee is called by autonity only on new epoch, it remove stale committee
        from the reporter set, then replace the last committee with current committee,
        and set the current committee with the input new committee.

        Parameters
        ----------
        _new_committee : typing.List[eth_typing.ChecksumAddress]

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setCommittee(
            _new_committee,
        )

    def slashing_history(
        self,
        key0: eth_typing.ChecksumAddress,
        key1: int,
    ) -> int:
        """Binding for `slashingHistory` on the Accountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress
        key1 : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.slashingHistory(
            key0,
            key1,
        ).call()
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
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "innocenceProofSubmissionWindow",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseSlashingRateLow",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseSlashingRateMid",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "collusionFactor",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "historyFactor",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "jailFactor",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "slashingRatePrecision",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Accountability.Config",
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
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "beneficiaries",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_offender", "type": "address"},
                {
                    "internalType": "enum Accountability.Rule",
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
                    "internalType": "enum Accountability.Rule",
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
            "inputs": [],
            "name": "config",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "innocenceProofSubmissionWindow",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "baseSlashingRateLow",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "baseSlashingRateMid",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "collusionFactor",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "historyFactor", "type": "uint256"},
                {"internalType": "uint256", "name": "jailFactor", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "slashingRatePrecision",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_ntnReward", "type": "uint256"},
            ],
            "name": "distributeRewards",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "epochPeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "events",
            "outputs": [
                {
                    "internalType": "enum Accountability.EventType",
                    "name": "eventType",
                    "type": "uint8",
                },
                {
                    "internalType": "enum Accountability.Rule",
                    "name": "rule",
                    "type": "uint8",
                },
                {"internalType": "address", "name": "reporter", "type": "address"},
                {"internalType": "address", "name": "offender", "type": "address"},
                {"internalType": "bytes", "name": "rawProof", "type": "bytes"},
                {"internalType": "uint256", "name": "id", "type": "uint256"},
                {"internalType": "uint256", "name": "block", "type": "uint256"},
                {"internalType": "uint256", "name": "epoch", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "reportingBlock",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "messageHash", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "_epochEnd", "type": "bool"}],
            "name": "finalize",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_val", "type": "address"}],
            "name": "getValidatorAccusation",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "enum Accountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum Accountability.Rule",
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
                    "internalType": "struct Accountability.Event",
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
                            "internalType": "enum Accountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum Accountability.Rule",
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
                    "internalType": "struct Accountability.Event[]",
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
                            "internalType": "enum Accountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum Accountability.Rule",
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
                    "internalType": "struct Accountability.Event",
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
                            "internalType": "enum Accountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum Accountability.Rule",
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
                    "internalType": "struct Accountability.Event",
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
                            "internalType": "enum Accountability.EventType",
                            "name": "eventType",
                            "type": "uint8",
                        },
                        {
                            "internalType": "enum Accountability.Rule",
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
                    "internalType": "struct Accountability.Event",
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
                {"internalType": "uint256", "name": "_newPeriod", "type": "uint256"}
            ],
            "name": "setEpochPeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "name": "slashingHistory",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
