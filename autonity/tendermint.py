# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module containing the Tendermint Web3 external module.
"""

from __future__ import annotations
from dataclasses import dataclass
import json
from web3.types import ABI, RPCEndpoint, ChecksumAddress
from web3.module import Module
from web3.method import Method
from typing import Sequence, TypedDict, Tuple, Any, cast


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


class Tendermint(Module):
    """
    A custom Web3.module.Module that enables a JSON-RPC method call to
    `tendermint_getContractABI`.
    """

    def _getCommittee_munger(  # pylint: disable=invalid-name
        self, block_height: int
    ) -> Tuple[str]:
        return (("0x" + str(block_height)),)

    def _getCommitteeAtHash_munger(  # pylint: disable=invalid-name
        self, block_hash: bytes
    ) -> Tuple[str]:
        return (self.web3.toHex(block_hash),)

    _getCommittee: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getCommittee"),
        mungers=[_getCommittee_munger],
    )

    _getCommitteeAtHash: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getCommitteeAtHash"),
        mungers=[_getCommitteeAtHash_munger],
    )

    _getContractABI: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getContractABI")
    )

    _getContractAddress: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getContractAddress")
    )

    _getCoreState: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getCoreState")
    )

    _getCommitteeEnodes: Method = Method(
        json_rpc_method=RPCEndpoint("tendermint_getCommitteeEnodes")
    )

    def get_committee(self, block_height: int) -> Sequence[CommitteeMember]:
        """
        Return the committee at the given block height.
        """
        result = self._getCommittee(block_height)
        assert isinstance(result, list)
        return [CommitteeMember.from_dict(cm) for cm in result]

    def get_committee_at_hash(self, block_hash: bytes) -> Sequence[CommitteeMember]:
        """
        Return the committee at the given block hash.
        """
        result = self._getCommitteeAtHash(block_hash)
        print(f"result={result}")
        assert isinstance(result, list)
        committee_members = cast(Sequence[CommitteeMember], result)
        assert isinstance(result[0].address, str)
        assert isinstance(result[0].votingPower, int)
        return committee_members

    def get_contract_abi(self) -> ABI:
        """
        Returns the ABI of the Autonity contract.
        """
        abi_str = self._getContractABI()
        abi = json.loads(abi_str)
        assert isinstance(abi, list), f"ABI type {type(abi)})"
        return abi

    def get_contract_address(self) -> str:
        """
        Returns the address of the Autonity contract.
        """
        addr = self._getContractAddress()
        assert isinstance(addr, str)
        return self.web3.toChecksumAddress(addr)

    def get_core_state(self) -> Any:
        """
        Returns the core state of attached node.
        """
        core_state = self._getCoreState()
        print(f"core_state={core_state}")
        return core_state

    def get_committee_enodes(self) -> Sequence[str]:
        """
        Returns the set of enodes in the current consensus committee.
        """
        committee_enodes = self._getCommitteeEnodes()
        print(f"core_state={committee_enodes}")
        return committee_enodes
