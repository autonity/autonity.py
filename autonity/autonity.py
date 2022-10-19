# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the Autonity Web3.py external module
"""

from __future__ import annotations

from autonity.tendermint import CommitteeMember
from autonity.erc20 import ERC20
from autonity.abi_manager import ABIManager

from dataclasses import dataclass
from web3 import Web3
from web3.types import ChecksumAddress
from typing import Sequence, Tuple

# TODO: use the tendermint RPC call for this?
AUTONITY_CONTRACT_ADDRESS = "0xBd770416a3345F91E4B34576cb804a576fa48EB1"


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
        Create from web3 tuple
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
        return Config(
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6],
            value[7],
            value[8],
            value[9],
        )


class Autonity(ERC20):
    """
    Web3 module representing Autonity-specific API.
    """

    def __init__(self, web3: Web3):
        super().__init__(
            web3,
            web3.toChecksumAddress(AUTONITY_CONTRACT_ADDRESS),
            ABIManager.load_abi("Autonity"),
        )

    def commission_rate_precision(self) -> int:
        """See `COMMISSION_RATE_PRECISION` on Autonity contract."""
        return self.contract.functions.COMMISSION_RATE_PRECISION().call()

    def config(self) -> Config:
        """See `config` on Autonity contract."""
        return Config.from_tuple(self.contract.functions.config().call())

    def epoch_id(self) -> int:
        """See `epochID` on Autonity contract."""
        return self.contract.functions.epochID().call()

    def last_epoch_block(self) -> int:
        """See `lastEpochBlock` on Autonity contract."""
        return self.contract.functions.lastEpochBlock().call()

    def epoch_total_bonded_stake(self) -> int:
        """See `epochTotalBondedStake` on Autonity contract."""
        return self.contract.functions.epochTotalBondedStake().call()

    def total_redistributed(self) -> int:
        """See `totalRedistributed` on Autonity contract."""
        return self.contract.functions.totalRedistributed().call()

    def epoch_reward(self) -> int:
        """See `epochReward` on Autonity contract."""
        return self.contract.functions.epochReward().call()

    def tail_bonding_id(self) -> int:
        """See `tailBondingID` on Autonity contract."""
        return self.contract.functions.tailBondingID().call()

    def head_bonding_id(self) -> int:
        """See `headBondingID` on Autonity contract."""
        return self.contract.functions.headBondingID().call()

    def tail_unbonding_id(self) -> int:
        """See `tailUnbondingID` on Autonity contract."""
        return self.contract.functions.tailUnbondingID().call()

    def head_unbonding_id(self) -> int:
        """See `headUnbondingID` on Autonity contract."""
        return self.contract.functions.headUnbondingID().call()

    def deployer(self) -> ChecksumAddress:
        """See `deployer` on Autonity contract."""
        return self.contract.functions.deployer().call()

    def get_last_epoch_block(self) -> int:
        """See `getLastEpochBlock` on Autonity contract."""
        return self.contract.functions.getLastEpochBlock().call()

    def get_version(self) -> int:
        """See `getVersion` on Autonity contract."""
        return self.contract.functions.getVersion().call()

    def get_committee(self) -> Sequence[CommitteeMember]:
        """See `getCommittee` on Autonity contract."""
        cms = self.contract.functions.getCommittee().call()
        return [CommitteeMember.from_tuple(cm) for cm in cms]

    def get_validators(self) -> Sequence[ChecksumAddress]:
        """See `getValidators` on Autonity contract."""
        return self.contract.functions.getValidators().call()

    # function getValidator(address _addr) external view returns (Validator memory) {
    # function getMaxCommitteeSize() external view returns (uint256) {
    # function getCommitteeEnodes() external view returns (string[] memory) {
    # function getMinimumBaseFee() external view returns (uint256) {
    # function getOperator() external view returns (address) {

    # function getProposer(uint256 height, uint256 round) external view returns (address)
    # function getBondingReq(uint256 startId, uint256 lastId) external view returns (Staking[] memory) {
    # function getUnbondingReq(uint256 startId, uint256 lastId) external view returns (Staking[] memory) {

    # function bond(address _validator, uint256 _amount) public {
    # function unbond(address _validator, uint256 _amount) public {

    # function registerValidator(string memory _enode, bytes memory _proof) public {
    # function pauseValidator(address _address) public {
    # function activateValidator(address _address) public {
    # function changeCommissionRate(address _validator, uint256 _rate) public {


# def autonity_contract(self) -> Contract:
#     """
#     Returns the Autonity contract. See docs.autonity.org for details of the
#     methods available.
#     """
#     if not self._autonity_contract:
#         if not hasattr(self._w3, "tendermint"):
#             self._w3.attach_modules({"tendermint": Tendermint})

#         tendermint = cast(Tendermint, self._w3.tendermint)  # type: ignore
#         abi = tendermint.get_contract_abi()
#         eth = self._w3.eth
#         autonity_contract_addr = self._w3.toChecksumAddress(
#             AUTONITY_CONTRACT_ADDRESS
#         )
#         self._autonity_contract = eth.contract(autonity_contract_addr, abi=abi)

#     assert self._autonity_contract
#     return self._autonity_contract

# event MintedStake(address addr, uint256 amount);
# event BurnedStake(address addr, uint256 amount);
# event CommissionRateChange(address validator, uint256 rate);
# event RegisteredValidator(address treasury, address addr, string enode, address liquidContract);
# event PausedValidator(address treasury, address addr, uint256 effectiveBlock);
# event Rewarded(address addr, uint256 amount);
