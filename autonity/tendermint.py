# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

import json
from web3.types import ABI, RPCEndpoint, Address
from web3.module import Module
from web3.method import Method
from typing import Sequence, TypedDict, Tuple, Any, cast


class CommitteeMember(TypedDict):
    address: Address
    votingPower: int


class Tendermint(Module):
    """
    A custom Web3.module.Module that enables a JSON-RPC method call to
    `tendermint_getContractABI`.
    """

    def _getCommittee_munger(self, block_height: int) -> Tuple[str]:
        return (("0x" + str(block_height)),)

    def _getCommitteeAtHash_munger(self, block_hash: bytes) -> Tuple[str]:
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
        result = self._getCommittee(block_height)
        assert isinstance(result, list)
        committee_members = cast(Sequence[CommitteeMember], result)
        assert isinstance(result[0].address, str)
        assert isinstance(result[0].votingPower, int)
        return committee_members

    def get_committee_at_hash(self, block_hash: bytes) -> Sequence[CommitteeMember]:
        result = self._getCommitteeAtHash(block_hash)
        print(f"result={result}")
        assert isinstance(result, list)
        committee_members = cast(Sequence[CommitteeMember], result)
        assert isinstance(result[0].address, str)
        assert isinstance(result[0].votingPower, int)
        return committee_members

    def get_contract_abi(self) -> ABI:
        abi_str = self._getContractABI()
        abi = json.loads(abi_str)
        assert isinstance(abi, list), f"ABI type {type(abi)})"
        return abi

    def get_contract_address(self) -> str:
        addr = self._getContractAddress()
        assert isinstance(addr, str)
        return self.web3.toChecksumAddress(addr)

    def get_core_state(self) -> Any:
        core_state = self._getCoreState()
        print(f"core_state={core_state}")
        return core_state

    def get_committee_enodes(self) -> Sequence[str]:
        committee_enodes = self._getCommitteeEnodes()
        print(f"core_state={committee_enodes}")
        return committee_enodes
