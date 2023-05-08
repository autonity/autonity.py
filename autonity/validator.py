# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model holding Validator information.
"""

from __future__ import annotations

from autonity.liquid_newton import LiquidNewton
from autonity.erc20 import ERC20

from enum import IntEnum
from web3 import Web3
from web3.types import ChecksumAddress, Wei
from web3.contract.contract import ContractFunction
from typing import TypedDict, NewType, Tuple

# pylint: disable=too-many-instance-attributes


ValidatorAddress = NewType("ValidatorAddress", ChecksumAddress)


class ValidatorState(IntEnum):
    """
    The status of a Validator
    """

    ACTIVE = 0
    PAUSED = 1


class ValidatorDescriptor(TypedDict):
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


def validator_descriptor_from_tuple(
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
) -> ValidatorDescriptor:
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

    return ValidatorDescriptor(
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


class Validator:
    """
    Information held about a Validator.
    """

    treasury: ChecksumAddress
    address: ValidatorAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    total_slashed: int
    lnew_contract: ERC20
    liquid_supply: int
    registration_block: int
    state: ValidatorState

    _liquid_contract: LiquidNewton
    """
    Internally this provides access to the extra functions.  Publicly,
    LNEW is exposed as a plain ERC20 token, via lnew_contract.
    """

    def __init__(self, w3: Web3, vdesc: ValidatorDescriptor):
        self.treasury = vdesc["treasury"]
        self.address = vdesc["addr"]
        self.enode = vdesc["enode"]
        self.commission_rate = vdesc["commission_rate"]
        self.bonded_stake = vdesc["bonded_stake"]
        self.total_slashed = vdesc["total_slashed"]
        self._liquid_contract = LiquidNewton(w3, vdesc["liquid_contract"])
        self.lnew_contract = self._liquid_contract
        self.liquid_supply = vdesc["liquid_supply"]
        self.registration_block = vdesc["registration_block"]
        self.state = vdesc["state"]

    def unclaimed_rewards(self, account: ChecksumAddress) -> Wei:
        """
        Query the rewards for this validator, claimable by `account`.
        """
        return self._liquid_contract.unclaimed_rewards(account)

    def claim_rewards(self) -> ContractFunction:
        """
        Create a ContractFunction to claim the rewards due to th call, from this validator.
        """
        return self._liquid_contract.claim_rewards()
