# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Model holding Validator information.
"""

from __future__ import annotations
from enum import IntEnum
from dataclasses import dataclass
from web3.types import ChecksumAddress
from typing import Tuple


class ValidatorState(IntEnum):
    """
    The status of a Validator
    """

    ACTIVE = 0
    PAUSED = 1


@dataclass
class Validator:
    """
    Information held about a Validator.
    """

    treasury: ChecksumAddress
    addr: ChecksumAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    total_slashed: int
    liquid_contract: ChecksumAddress  # TODO: address -> Contract -> ValidatorContract
    liquid_supply: int
    registration_block: int
    state: ValidatorState

    @staticmethod
    def from_tuple(
        value: Tuple[
            ChecksumAddress,
            ChecksumAddress,
            str,
            int,
            int,
            int,
            ChecksumAddress,
            int,
            int,
            ValidatorState,
        ]
    ) -> Validator:
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

        return Validator(
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6],
            value[7],
            value[8],
            ValidatorState(value[9]),
        )
