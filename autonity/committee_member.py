# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Committee member model class
"""

from __future__ import annotations
from dataclasses import dataclass
from web3.types import ChecksumAddress
from typing import TypedDict, Tuple


class CommitteeMemberDict(TypedDict):
    """
    Dictionary representing a member of the consensus committee.
    """

    address: ChecksumAddress
    votingPower: int


@dataclass
class CommitteeMember:
    """
    Model class for a committee member.
    """

    address: ChecksumAddress
    voting_power: int

    @staticmethod
    def from_dict(value: CommitteeMemberDict) -> CommitteeMember:
        """
        From JSON RPC result
        """
        return CommitteeMember(value["address"], value["votingPower"])

    @staticmethod
    def from_tuple(value: Tuple[ChecksumAddress, int]) -> CommitteeMember:
        """
        From Web3 tuple
        """
        assert len(value) == 2
        assert isinstance(value[0], str)
        assert isinstance(value[1], int)
        return CommitteeMember(value[0], value[1])
