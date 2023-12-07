# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model holding Validator information.
"""

from __future__ import annotations

from enum import IntEnum
from typing import NewType, Tuple, TypedDict

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import ChecksumAddress, Wei

from autonity.erc20 import ERC20
from autonity.liquid_newton import LiquidNewton

# pylint: disable=too-many-instance-attributes


NodeAddress = NewType("NodeAddress", ChecksumAddress)
OracleAddress = NewType("OracleAddress", ChecksumAddress)


class ValidatorState(IntEnum):
    """
    The status of a Validator
    """

    ACTIVE = 0
    PAUSED = 1
    JAILED = 2


class ValidatorDescriptor(TypedDict):
    """
    Dictionary representing the description of a Validator
    """

    treasury: ChecksumAddress
    node_address: NodeAddress
    oracle_address: OracleAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    unbonding_stake: int
    unbonding_shares: int
    self_bonded_stake: int
    self_unbonding_stake: int
    self_unbonding_shares: int
    self_unbonding_stake_locked: int
    liquid_contract: ChecksumAddress
    liquid_supply: int
    registration_block: int
    total_slashed: int
    jail_release_block: int
    provable_fault_count: int
    state: ValidatorState


def validator_descriptor_from_tuple(
    value: Tuple[
        ChecksumAddress,
        NodeAddress,
        OracleAddress,
        str,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        ChecksumAddress,
        int,
        int,
        int,
        int,
        int,
        ValidatorState,
    ]
) -> ValidatorDescriptor:
    """
    Create an instance from the tuple returned by Web3 contract calls.
    """
    assert len(value) == 19
    assert isinstance(value[0], str)
    assert isinstance(value[1], str)
    assert isinstance(value[2], str)
    assert isinstance(value[3], str)
    assert isinstance(value[4], int)
    assert isinstance(value[5], int)
    assert isinstance(value[6], int)
    assert isinstance(value[7], int)
    assert isinstance(value[8], int)
    assert isinstance(value[9], int)
    assert isinstance(value[10], int)
    assert isinstance(value[11], int)
    assert isinstance(value[12], str)
    assert isinstance(value[13], int)
    assert isinstance(value[14], int)
    assert isinstance(value[15], int)
    assert isinstance(value[16], int)
    assert isinstance(value[17], int)
    assert isinstance(value[18], int)

    return ValidatorDescriptor(
        {
            "treasury": value[0],
            "node_address": value[1],
            "oracle_address": value[2],
            "enode": value[3],
            "commission_rate": value[4],
            "bonded_stake": value[5],
            "unbonding_stake": value[6],
            "unbonding_shares": value[7],
            "self_bonded_stake": value[8],
            "self_unbonding_stake": value[9],
            "self_unbonding_shares": value[10],
            "self_unbonding_stake_locked": value[11],
            "liquid_contract": value[12],
            "liquid_supply": value[13],
            "registration_block": value[14],
            "total_slashed": value[15],
            "jail_release_block": value[16],
            "provable_fault_count": value[17],
            "state": ValidatorState(value[18]),
        }
    )


class Validator:
    """
    Information held about a Validator.
    """

    treasury: ChecksumAddress
    node_address: NodeAddress
    oracle_address: OracleAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    unbonding_stake: int
    unbonding_shares: int
    self_bonded_stake: int
    self_unbonding_stake: int
    self_unbonding_shares: int
    self_unbonding_stake_locked: int
    lntn_contract: ERC20
    liquid_supply: int
    registration_block: int
    total_slashed: int
    jail_release_block: int
    provable_fault_count: int
    state: ValidatorState

    _liquid_contract: LiquidNewton
    """
    Internally this provides access to the extra functions.  Publicly,
    LNTN is exposed as a plain ERC20 token, via lntn_contract.
    """

    def __init__(self, w3: Web3, vdesc: ValidatorDescriptor):
        self.treasury = vdesc["treasury"]
        self.node_address = vdesc["node_address"]
        self.oracle_address = vdesc["oracle_address"]
        self.enode = vdesc["enode"]
        self.commission_rate = vdesc["commission_rate"]
        self.bonded_stake = vdesc["bonded_stake"]
        self.unbonding_stake = vdesc["unbonding_stake"]
        self.unbonding_shares = vdesc["unbonding_shares"]
        self.self_bonded_stake = vdesc["self_bonded_stake"]
        self.self_unbonding_stake = vdesc["self_unbonding_stake"]
        self.self_unbonding_shares = vdesc["self_unbonding_shares"]
        self.self_unbonding_stake_locked = vdesc["self_unbonding_stake_locked"]
        self._liquid_contract = LiquidNewton(w3, vdesc["liquid_contract"])
        self.lntn_contract = self._liquid_contract
        self.liquid_supply = vdesc["liquid_supply"]
        self.registration_block = vdesc["registration_block"]
        self.total_slashed = vdesc["total_slashed"]
        self.jail_release_block = vdesc["jail_release_block"]
        self.provable_fault_count = vdesc["provable_fault_count"]
        self.state = vdesc["state"]

    def unclaimed_rewards(self, account: ChecksumAddress) -> Wei:
        """
        Query the rewards for this validator, claimable by `account`.
        """
        return self._liquid_contract.unclaimed_rewards(account)

    def claim_rewards(self) -> ContractFunction:
        """
        Create a ContractFunction to claim the rewards due from this validator.
        """
        return self._liquid_contract.claim_rewards()
