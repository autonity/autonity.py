"""Accountability Web3 external module."""

from enum import Enum
from typing import List, Tuple, TypedDict

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.contract.contract import Contract

from autonity.abi_manager import ABIManager


# https://docs.autonity.org/concepts/architecture/#protocol-contract-addresses
ACCOUNTABILITY_CONTRACT_ADDRESS = "0x5a443704dd4B594B382c22a083e2BD3090A6feF3"

# https://github.com/autonity/autonity/blob/4073f24786ce5c99bef80238aa798482ae13fd33/autonity/solidity/contracts/Accountability.sol#L23
EventType = Enum("EventType", ["Accusation", "FaultProof", "InnocenceProof"], start=0)

# https://github.com/autonity/autonity/blob/4073f24786ce5c99bef80238aa798482ae13fd33/autonity/solidity/contracts/Accountability.sol#L30
Rule = Enum(
    "Rule",
    [
        "PN",
        "PO",
        "PVN",
        "PVO",
        "PVO12",
        "C",
        "C1",
        "InvalidProposal",
        "InvalidProposer",
        "Equivocation",
    ],
    start=0,
)


class AccountabilityEvent(TypedDict):
    """
    https://docs.autonity.org/reference/api/accountability/#response-2
    """

    chunks: int
    chunk_id: int
    event_type: str
    rule: str
    reporter: ChecksumAddress
    offender: ChecksumAddress
    raw_proof: str
    block: int
    epoch: int
    reporting_block: int
    message_hash: int


def event_from_tuple(
    value: Tuple[
        int, int, int, int, ChecksumAddress, ChecksumAddress, bytes, int, int, int, int
    ]
) -> AccountabilityEvent:
    """
    Create an instance from the tuple returned by Web3 contract calls.
    """
    assert len(value) == 11
    for i in (0, 1, 2, 3, 7, 8, 9, 10):
        assert isinstance(value[i], int)
    assert isinstance(value[4], str)
    assert isinstance(value[5], str)
    assert isinstance(value[6], bytes)

    return AccountabilityEvent(
        {
            "chunks": value[0],
            "chunk_id": value[1],
            "event_type": EventType(value[2]).name,
            "rule": Rule(value[3]).name,
            "reporter": value[4],
            "offender": value[5],
            "raw_proof": HexBytes(value[6]).hex(),
            "block": value[7],
            "epoch": value[8],
            "reporting_block": value[9],
            "message_hash": value[10],
        }
    )


class Accountability:
    """Wrapper class for the Accountability contract."""

    contract: Contract

    def __init__(self, web3: Web3):
        abi = ABIManager.load_abi("Accountability")
        address = web3.to_checksum_address(ACCOUNTABILITY_CONTRACT_ADDRESS)
        self.contract = web3.eth.contract(address, abi=abi)

    def get_validator_accusation(
        self, validator_address: ChecksumAddress
    ) -> AccountabilityEvent:
        event_tuple = self.contract.functions.getValidatorAccusation(
            validator_address
        ).call()
        return event_from_tuple(event_tuple)

    def get_validator_faults(
        self, validator_address: ChecksumAddress
    ) -> List[AccountabilityEvent]:
        event_tuples = self.contract.functions.getValidatorFaults(
            validator_address
        ).call()
        return [event_from_tuple(e) for e in event_tuples]
