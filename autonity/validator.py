# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model holding Validator information.
"""

from __future__ import annotations

from autonity.liquid_newton import LiquidNewton

from enum import IntEnum
from dataclasses import dataclass
from web3 import Web3
from web3.types import ChecksumAddress
from typing import TypedDict, NewType, Tuple


ValidatorAddress = NewType("ValidatorAddress", ChecksumAddress)


class ValidatorState(IntEnum):
    """
    The status of a Validator
    """

    ACTIVE = 0
    PAUSED = 1


class ValidatorDescription(TypedDict):
    """
    Dictionary representing the description of a Validator
    """

    treasury: ChecksumAddress
    addr: ValidatorAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    total_slashed: int
    liquid_contract: ChecksumAddress
    liquid_supply: int
    registration_block: int
    state: ValidatorState


def validator_description_from_tuple(
    value: Tuple[
        ChecksumAddress,
        ValidatorAddress,
        str,
        int,
        int,
        int,
        ChecksumAddress,
        int,
        int,
        ValidatorState,
    ]
) -> ValidatorDescription:

    """
    Create an instance from the tuple returned by Web3 contract calls.
    """
    assert len(value) == 10
    assert isinstance(value[0], str)
    assert isinstance(value[1], str)
    assert isinstance(value[2], str)
    assert isinstance(value[3], int)
    assert isinstance(value[4], int)
    assert isinstance(value[5], int)
    assert isinstance(value[6], str)
    assert isinstance(value[7], int)
    assert isinstance(value[8], int)
    assert isinstance(value[9], int)

    return ValidatorDescription(
        {
            "treasury": value[0],
            "addr": value[1],
            "enode": value[2],
            "commission_rate": value[3],
            "bonded_stake": value[4],
            "total_slashed": value[5],
            "liquid_contract": value[6],
            "liquid_supply": value[7],
            "registration_block": value[8],
            "state": ValidatorState(value[9]),
        }
    )


@dataclass
class Validator:
    """
    Information held about a Validator.
    """

    treasury: ChecksumAddress
    addr: ValidatorAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    total_slashed: int
    liquid_contract: LiquidNewton
    liquid_supply: int
    registration_block: int
    state: ValidatorState

    def __init__(self, w3: Web3, vdesc: ValidatorDescription):
        self.treasury = vdesc["treasury"]
        self.addr = vdesc["addr"]
        self.enode = vdesc["enode"]
        self.commission_rate = vdesc["commission_rate"]
        self.bonded_stake = vdesc["bonded_stake"]
        self.total_slashed = vdesc["total_slashed"]
        self.liquid_contract = LiquidNewton(w3, vdesc["liquid_contract"])
        self.liquid_supply = vdesc["liquid_supply"]
        self.registration_block = vdesc["registration_block"]
        self.state = vdesc["state"]
