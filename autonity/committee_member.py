# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Committee member model class
"""

from __future__ import annotations
from web3.types import ChecksumAddress
from typing import TypedDict, Tuple


class CommitteeMember(TypedDict):
    """
    Dictionary representing a member of the consensus committee.
    """

    address: ChecksumAddress
    voting_power: int


def committee_member_from_tuple(value: Tuple[ChecksumAddress, int]) -> CommitteeMember:
    """
    From Web3 tuple
    """
    assert len(value) == 2
    assert isinstance(value[0], str)
    assert isinstance(value[1], int)
    return CommitteeMember({"address": value[0], "voting_power": value[1]})
