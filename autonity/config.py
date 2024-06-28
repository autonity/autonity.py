# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for Autonity contract configuration
"""

from __future__ import annotations

from typing import Tuple, TypedDict

from web3.types import ChecksumAddress


class Contracts(TypedDict):
    accountability_contract: ChecksumAddress
    oracle_contract: ChecksumAddress
    acu_contract: ChecksumAddress
    supply_control_contract: ChecksumAddress
    stabilization_contract: ChecksumAddress
    upgrade_manager_contract: ChecksumAddress
    inflation_controller_contract: ChecksumAddress
    non_stakable_vesting_contract: ChecksumAddress


class Policy(TypedDict):
    treasury_fee: int
    min_basefee: int
    delegation_rate: int
    unbonding_period: int
    initial_inflation_reserve: int
    treasury_account: ChecksumAddress


class Protocol(TypedDict):
    operator_account: ChecksumAddress
    epoch_period: int
    block_period: int
    committee_size: int


class Config(TypedDict):
    """
    Autonity configuration.
    """

    policy: Policy
    contracts: Contracts
    protocol: Protocol
    contract_version: int


def config_from_tuple(
    value: Tuple[
        Tuple[int, int, int, int, int, ChecksumAddress],
        Tuple[
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
            ChecksumAddress,
        ],
        Tuple[ChecksumAddress, int, int, int],
        int,
    ]
) -> Config:
    """
    Create from a Web3 tuple.
    """
    assert isinstance(value[0][0], int)
    assert isinstance(value[0][1], int)
    assert isinstance(value[0][2], int)
    assert isinstance(value[0][3], int)
    assert isinstance(value[0][4], int)
    assert isinstance(value[0][5], str)
    assert isinstance(value[1][0], str)
    assert isinstance(value[1][1], str)
    assert isinstance(value[1][2], str)
    assert isinstance(value[1][3], str)
    assert isinstance(value[1][4], str)
    assert isinstance(value[1][5], str)
    assert isinstance(value[1][6], str)
    assert isinstance(value[1][7], str)
    assert isinstance(value[2][0], str)
    assert isinstance(value[2][1], int)
    assert isinstance(value[2][2], int)
    assert isinstance(value[2][3], int)
    assert isinstance(value[3], int)
    return Config(
        {
            "policy": Policy(
                {
                    "treasury_fee": value[0][0],
                    "min_basefee": value[0][1],
                    "delegation_rate": value[0][2],
                    "unbonding_period": value[0][3],
                    "initial_inflation_reserve": value[0][4],
                    "treasury_account": value[0][5],
                }
            ),
            "contracts": Contracts(
                {
                    "accountability_contract": value[1][0],
                    "oracle_contract": value[1][1],
                    "acu_contract": value[1][2],
                    "supply_control_contract": value[1][3],
                    "stabilization_contract": value[1][4],
                    "upgrade_manager_contract": value[1][5],
                    "inflation_controller_contract": value[1][6],
                    "non_stakable_vesting_contract": value[1][7],
                }
            ),
            "protocol": Protocol(
                {
                    "operator_account": value[2][0],
                    "epoch_period": value[2][1],
                    "block_period": value[2][2],
                    "committee_size": value[2][3],
                }
            ),
            "contract_version": value[3],
        }
    )
