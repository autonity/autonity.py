# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for Autonity contract configuration
"""

from __future__ import annotations

from dataclasses import dataclass
from web3.types import ChecksumAddress
from typing import Tuple


@dataclass
class Config:
    """
    Autonity configuration.
    """

    operator_account: ChecksumAddress
    treasury_account: ChecksumAddress
    treasury_fee: int
    min_basefee: int
    delegation_rate: int
    epoch_period: int
    unbonding_period: int
    committee_size: int
    contract_version: int
    block_period: int

    @staticmethod
    def from_tuple(
        value: Tuple[
            ChecksumAddress, ChecksumAddress, int, int, int, int, int, int, int, int
        ]
    ) -> Config:
        """
        Create from a Web3 tuple.
        """
        assert isinstance(value[0], str)
        assert isinstance(value[1], str)
        assert isinstance(value[2], int)
        assert isinstance(value[3], int)
        assert isinstance(value[4], int)
        assert isinstance(value[5], int)
        assert isinstance(value[6], int)
        assert isinstance(value[7], int)
        assert isinstance(value[8], int)
        assert isinstance(value[9], int)
        return Config(*value)