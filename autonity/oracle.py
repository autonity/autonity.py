# Copyright (C) 2015-2023 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the Oracle Web3.py external module
"""

from __future__ import annotations

from autonity.abi_manager import ABIManager

import os

from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import ChecksumAddress, Wei
from typing import Sequence, TypedDict, Tuple

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-arguments

CONTRACT_ADDRESS = "0xBd770416a3345F91E4B34576cb804a576fa48EB1"
"""
The default Oracle contract address.
"""


def get_contract_version() -> str:
    """
    Returns the version of the Autonity contract which this library is aligned with,
    and that is bundled with the library.
    """
    version_path = os.path.join(os.path.dirname(__file__), "abi", "autonity-commit.txt")
    if not os.path.exists(version_path):
        return "N/A"
    with open(version_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def get_contract_abi_path() -> str:
    """
    Returns the Autonity contract ABI path bundled with the library.
    This can be used in to load the ABI from a 3rd party app or library
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "abi", "Oracle.abi")
    )


class RoundData(TypedDict):
    round: int
    price: Wei
    timestamp: int
    status: int


class Oracle(object):
    """
    Web3 module representing Oracle-specific API.
    """

    def __init__(self, web3: Web3):
        super().__init__(
            web3,
            web3.to_checksum_address(CONTRACT_ADDRESS),
            ABIManager.load_abi("Autonity"),
        )

    @staticmethod
    def address() -> ChecksumAddress:
        """
        Return the deterministic address of the Oracle contract.
        """
        return Web3.to_checksum_address(CONTRACT_ADDRESS)

    def finalize(self) -> ContractFunction:
        """
        Generated from Oracle ABI
        See `finalize` on the Oracle contract.
        Called once per VotePeriod part of the state finalisation function.
        Mutability: nonpayable
        """
        return self.contract.functions.finalize()

    def get_precision(self) -> int:
        """
        Generated from Oracle ABI
        See `getPrecision` on the Oracle contract.
        Precision to be used with price reports
        Mutability: pure
        """
        return self.contract.functions.getPrecision().call()

    def get_round(self) -> int:
        """
        Generated from Oracle ABI
        See `getRound` on the Oracle contract.
        Retrieve the current round ID.
        Mutability: view
        """
        return self.contract.functions.getRound().call()

    def get_round_data(self, _round: int, _symbol: str) -> RoundData:
        """
        Generated from Oracle ABI
        See `getRoundData` on the Oracle contract.
        Return price data for a specific round.
        Mutability: view
        """
        return self.contract.functions.getRoundData(_round, _symbol).call()

    def get_symbols(self) -> Sequence[str]:
        """
        Generated from Oracle ABI
        See `getSymbols` on the Oracle contract.
        Retrieve the lists of symbols to be voted on. Need to be called by the Oracle Server as part of the init.
        Mutability: view
        """
        return self.contract.functions.getSymbols().call()

    def get_vote_period(self) -> int:
        """
        Generated from Oracle ABI
        See `getVotePeriod` on the Oracle contract.
        vote period to be used for price voting and aggregation
        Mutability: view
        """
        return self.contract.functions.getVotePeriod().call()

    def get_voters(self) -> Sequence[ChecksumAddress]:
        """
        Generated from Oracle ABI
        See `getVoters` on the Oracle contract.
        Retrieve the current voters in the committee.
        Mutability: view
        """
        return self.contract.functions.getVoters().call()

    def last_round_block(self) -> int:
        """
        Generated from Oracle ABI
        See `lastRoundBlock` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.lastRoundBlock().call()

    def last_voter_update_round(self) -> int:
        """
        Generated from Oracle ABI
        See `lastVoterUpdateRound` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.lastVoterUpdateRound().call()

    def latest_round_data(self, _symbol: str) -> RoundData:
        """
        Generated from Oracle ABI
        See `latestRoundData` on the Oracle contract.
        Return latest available price data.
        Mutability: view
        """
        return self.contract.functions.latestRoundData(_symbol).call()

    def new_symbols(self, _uint256: int) -> str:
        """
        Generated from Oracle ABI
        See `newSymbols` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.newSymbols(_uint256).call()

    def reports(self, _string: str, _address: ChecksumAddress) -> int:
        """
        Generated from Oracle ABI
        See `reports` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.reports(_string, _address).call()

    def round(self) -> int:
        """
        Generated from Oracle ABI
        See `round` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.round().call()

    def set_operator(self, _operator: ChecksumAddress) -> ContractFunction:
        """
        Generated from Oracle ABI
        See `setOperator` on the Oracle contract.

        Mutability: nonpayable
        """
        return self.contract.functions.setOperator(_operator)

    def set_symbols(self, _symbols: Sequence[str]) -> ContractFunction:
        """
        Generated from Oracle ABI
        See `setSymbols` on the Oracle contract.
        Update the symbols to be requested. Only effective at the next round. Restricted to the operator account.
        Mutability: nonpayable
        """
        return self.contract.functions.setSymbols(_symbols)

    def set_voters(self, _newVoters: Sequence[ChecksumAddress]) -> ContractFunction:
        """
        Generated from Oracle ABI
        See `setVoters` on the Oracle contract.

        Mutability: nonpayable
        """
        return self.contract.functions.setVoters(_newVoters)

    def symbol_updated_round(self) -> int:
        """
        Generated from Oracle ABI
        See `symbolUpdatedRound` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.symbolUpdatedRound().call()

    def symbols(self, _uint256: int) -> str:
        """
        Generated from Oracle ABI
        See `symbols` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.symbols(_uint256).call()

    def vote(self, _commit: int, _reports: Sequence[int], _salt: int) -> ContractFunction:
        """
        Generated from Oracle ABI
        See `vote` on the Oracle contract.
        Vote for the current period. In order to save gas, if (reports[i] == INVALID_PRICE)g the symbols. if the validator leave consensus committee then his vote is discarded. if a validator joins the consensus committee then his first vote is not taken into account. Only allowed to vote once per round.
        Mutability: nonpayable
        """
        return self.contract.functions.vote(_commit, _reports, _salt)

    def vote_period(self) -> int:
        """
        Generated from Oracle ABI
        See `votePeriod` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.votePeriod().call()

    def voting_info(self, _address: ChecksumAddress) -> Tuple[int, int, bool]:
        """
        Generated from Oracle ABI
        See `votingInfo` on the Oracle contract.

        Mutability: view
        """
        return self.contract.functions.votingInfo(_address).call()
