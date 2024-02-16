# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Committee member model class
"""

from __future__ import annotations

from typing import Tuple, TypedDict

from eth_typing import ChecksumAddress
from hexbytes import HexBytes


class CommitteeMember(TypedDict):
    """
    Dictionary representing a member of the consensus committee.
    """

    address: ChecksumAddress
    voting_power: int
    consensus_key: str


def committee_member_from_tuple(
    value: Tuple[ChecksumAddress, int, bytes]
) -> CommitteeMember:
    """
    From Web3 tuple
    """
    assert len(value) == 3
    assert isinstance(value[0], str)
    assert isinstance(value[1], int)
    assert isinstance(value[2], bytes)
    return CommitteeMember(
        {
            "address": value[0],
            "voting_power": value[1],
            "consensus_key": HexBytes(value[2]).hex(),
        }
    )
