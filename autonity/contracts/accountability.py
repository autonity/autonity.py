"""Accountability contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import enum
import typing
from dataclasses import dataclass

import eth_typing
import hexbytes
import web3
from web3.contract import contract

__version__ = "v1.0.2-alpha"


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
class BaseSlashingRates:
    """Port of `struct BaseSlashingRates` on the Accountability contract."""

    low: int
    mid: int
    high: int


@dataclass
class Factors:
    """Port of `struct Factors` on the Accountability contract."""

    collusion: int
    history: int
    jail: int


@dataclass
class Config:
    """Port of `struct Config` on the Accountability contract."""

    innocence_proof_submission_window: int
    base_slashing_rates: BaseSlashingRates
    factors: Factors


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
    def InnocenceProven(self) -> contract.ContractEvent:
        """Binding for `event InnocenceProven` on the Accountability contract."""
        return self._contract.events.InnocenceProven

    @property
    def NewAccusation(self) -> contract.ContractEvent:
        """Binding for `event NewAccusation` on the Accountability contract."""
        return self._contract.events.NewAccusation

    @property
    def NewFaultProof(self) -> contract.ContractEvent:
        """Binding for `event NewFaultProof` on the Accountability contract."""
        return self._contract.events.NewFaultProof

    @property
    def SlashingEvent(self) -> contract.ContractEvent:
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
            BaseSlashingRates(
                int(return_value[1][0]),
                int(return_value[1][1]),
                int(return_value[1][2]),
            ),
            Factors(
                int(return_value[2][0]),
                int(return_value[2][1]),
                int(return_value[2][2]),
            ),
        )

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

    def history(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `history` on the Accountability contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.history(
            key0,
        ).call()
        return int(return_value)

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

    def set_committee(
        self,
        _new_committee: typing.List[eth_typing.ChecksumAddress],
    ) -> contract.ContractFunction:
        """Binding for `setCommittee` on the Accountability contract.

        setCommittee, called by the AC at epoch change, it removes stale committee from
        the reporter set, then replace the last committee with current committee, and
        set the current committee with the input new committee.

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
                            "internalType": "struct Accountability.BaseSlashingRates",
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
                            "internalType": "struct Accountability.Factors",
                            "name": "factors",
                            "type": "tuple",
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
                    "components": [
                        {"internalType": "uint256", "name": "low", "type": "uint256"},
                        {"internalType": "uint256", "name": "mid", "type": "uint256"},
                        {"internalType": "uint256", "name": "high", "type": "uint256"},
                    ],
                    "internalType": "struct Accountability.BaseSlashingRates",
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
                        {"internalType": "uint256", "name": "jail", "type": "uint256"},
                    ],
                    "internalType": "struct Accountability.Factors",
                    "name": "factors",
                    "type": "tuple",
                },
            ],
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
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "history",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
                    "internalType": "struct Accountability.BaseSlashingRates",
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
                    "internalType": "struct Accountability.Factors",
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
