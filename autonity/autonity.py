# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the Autonity Web3.py external module
"""

from __future__ import annotations

from autonity.config import Config, config_from_tuple
from autonity.validator import (
    validator_description_from_tuple,
    ValidatorDescription,
    ValidatorAddress,
)
from autonity.committee_member import CommitteeMember, committee_member_from_tuple
from autonity.erc20 import ERC20
from autonity.abi_manager import ABIManager

from web3 import Web3
from web3.contract import ContractFunction
from web3.types import ChecksumAddress, Wei
from typing import Sequence, TypedDict, Tuple, cast

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-arguments

AUTONITY_CONTRACT_VERSION = 2
"""
The version of the Autonity contract which this library is aligned
with.
"""


# TODO: use the tendermint RPC call for this?
AUTONITY_CONTRACT_ADDRESS = "0xBd770416a3345F91E4B34576cb804a576fa48EB1"


class Staking(TypedDict):
    """
    Queued staking operations
    """

    delegator: ChecksumAddress
    delegatee: ChecksumAddress
    amount: int
    start_block: int


def staking_from_tuple(value: Tuple[str, str, int, int]) -> Staking:
    """
    Create Staking object from a Web3 tuple.
    """
    assert len(value) == 4
    assert isinstance(value[0], str)
    assert isinstance(value[1], str)
    assert isinstance(value[2], int)
    assert isinstance(value[3], int)
    return Staking(
        {
            "delegator": cast(ChecksumAddress, value[0]),
            "delegatee": cast(ChecksumAddress, value[1]),
            "amount": value[2],
            "start_block": value[3],
        }
    )


class Autonity(ERC20):
    """
    Web3 module representing Autonity-specific API.
    """

    def __init__(self, web3: Web3, disable_version_checks: bool = False):
        super().__init__(
            web3,
            web3.toChecksumAddress(AUTONITY_CONTRACT_ADDRESS),
            ABIManager.load_abi("Autonity"),
        )

        # Check the contract version
        if not disable_version_checks:
            config = self.config()
            assert AUTONITY_CONTRACT_VERSION == config["contract_version"], (
                f"Autonity contract version mismatch (chain: {config['contract_version']}, "
                f"local: {AUTONITY_CONTRACT_VERSION})"
            )

    @staticmethod
    def address() -> ChecksumAddress:
        """
        Return the deterministic address of the Autonity contract.
        """
        return Web3.toChecksumAddress(AUTONITY_CONTRACT_ADDRESS)

    def commission_rate_precision(self) -> int:
        """
        See `COMMISSION_RATE_PRECISION` on the Autonity contract.
        """
        return self.contract.functions.COMMISSION_RATE_PRECISION().call()

    def config(self) -> Config:
        """
        See `config` on the Autonity contract.
        """
        return config_from_tuple(self.contract.functions.config().call())

    def epoch_id(self) -> int:
        """
        See `epochID` on the Autonity contract.
        """
        return self.contract.functions.epochID().call()

    def last_epoch_block(self) -> int:
        """
        See `lastEpochBlock` on the Autonity contract.
        """
        return self.contract.functions.lastEpochBlock().call()

    def epoch_total_bonded_stake(self) -> int:
        """
        See `epochTotalBondedStake` on the Autonity contract.
        """
        return self.contract.functions.epochTotalBondedStake().call()

    def total_redistributed(self) -> int:
        """
        See `totalRedistributed` on the Autonity contract.
        """
        return self.contract.functions.totalRedistributed().call()

    def epoch_reward(self) -> int:
        """
        See `epochReward` on the Autonity contract.
        """
        return self.contract.functions.epochReward().call()

    def tail_bonding_id(self) -> int:
        """
        See `tailBondingID` on the Autonity contract.
        """
        return self.contract.functions.tailBondingID().call()

    def head_bonding_id(self) -> int:
        """
        See `headBondingID` on the Autonity contract.
        """
        return self.contract.functions.headBondingID().call()

    def tail_unbonding_id(self) -> int:
        """
        See `tailUnbondingID` on the Autonity contract.
        """
        return self.contract.functions.tailUnbondingID().call()

    def head_unbonding_id(self) -> int:
        """
        See `headUnbondingID` on the Autonity contract.
        """
        return self.contract.functions.headUnbondingID().call()

    def deployer(self) -> ChecksumAddress:
        """
        See `deployer` on the Autonity contract.
        """
        return self.contract.functions.deployer().call()

    def get_last_epoch_block(self) -> int:
        """
        See `getLastEpochBlock` on the Autonity contract.
        """
        return self.contract.functions.getLastEpochBlock().call()

    def get_version(self) -> int:
        """
        See `getVersion` on the Autonity contract.
        """
        return self.contract.functions.getVersion().call()

    def get_committee(self) -> Sequence[CommitteeMember]:
        """
        See `getCommittee` on the Autonity contract.
        """
        cms = self.contract.functions.getCommittee().call()
        return [committee_member_from_tuple(cm) for cm in cms]

    def get_validators(self) -> Sequence[ChecksumAddress]:
        """
        See `getValidators` on the Autonity contract.
        """
        return self.contract.functions.getValidators().call()

    def get_validator(self, addr: ChecksumAddress) -> ValidatorDescription:
        """
        See `getValidator` on the Autonity contract.  To interact with
        validators, construct a `Validator` object from the returned
        ValidatorDescription.
        """
        assert isinstance(addr, str)
        value = self.contract.functions.getValidator(addr).call()
        return validator_description_from_tuple(value)

    def get_max_committee_size(self) -> int:
        """
        See `getMaxCommitteeSize` on the Autonity contract.
        """
        return self.contract.functions.getMaxCommitteeSize().call()

    def get_committee_enodes(self) -> Sequence[str]:
        """
        See `getCommitteeEnodes` on the Autonity contract.
        """
        return self.contract.functions.getCommitteeEnodes().call()

    def get_minimum_base_fee(self) -> int:
        """
        See `getMinimumBaseFee` on the Autonity contract.
        """
        return self.contract.functions.getMinimumBaseFee().call()

    def get_operator(self) -> ChecksumAddress:
        """
        See `getOperator` on the Autonity contract.
        """
        return self.contract.functions.getOperator().call()

    def get_proposer(self, height: int, round_idx: int) -> ChecksumAddress:
        """
        See `getProposer` on the Autonity contract.
        """
        return self.contract.functions.getProposer(height, round_idx).call()

    def get_bonding_req(self, start_id: int, last_id: int) -> Sequence[Staking]:
        """
        See `getBondingReq` on the Autonity contract.
        """
        result = self.contract.functions.getBondingReq(start_id, last_id).call()
        assert isinstance(result, list)
        return [staking_from_tuple(staking) for staking in result]

    def get_unbonding_req(self, start_id: int, last_id: int) -> Sequence[Staking]:
        """
        See `getUnbondingReq` on the Autonity contract.
        """
        result = self.contract.functions.getUnbondingReq(start_id, last_id).call()
        assert isinstance(result, list)
        return [staking_from_tuple(staking) for staking in result]

    def bond(
        self,
        validator_addr: ValidatorAddress,
        amount: Wei,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `bond` method.  See `bond` on the
        Autonity contract.
        """
        return self.contract.functions.bond(validator_addr, amount)

    def unbond(
        self,
        validator_addr: ValidatorAddress,
        amount: int,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `unbond` method.  See `unbond` on
        the Autonity contract.
        """
        return self.contract.functions.unbond(validator_addr, amount)

    def register_validator(
        self,
        enode: str,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `registerValidator` method.  See
        `registerValidator` on the Autonity contract.
        """
        return self.contract.functions.registerValidator(enode)

    def pause_validator(
        self,
        validator_addr: ValidatorAddress,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `pauseValidator` method.  See
        `pauseValidator` on the Autonity contract.
        """
        return self.contract.functions.pauseValidator(validator_addr)

    def activate_validator(
        self,
        validator_addr: ValidatorAddress,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `activateValidator` method.  See
        `activateValidator` on the Autonity contract.
        """
        return self.contract.functions.activateValidator(validator_addr)

    def change_commissionrate(
        self,
        validator: ValidatorAddress,
        rate: int,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `changeCommissionRate` method.  See
        `changeCommissionRate` on the Autonity contract.
        """
        return self.contract.functions.changeCommissionRate(validator, rate)

    # TODO: events

    # event MintedStake(address addr, uint256 amount);
    # event BurnedStake(address addr, uint256 amount);
    # event CommissionRateChange(address validator, uint256 rate);
    # event RegisteredValidator(
    #   address treasury, address addr, string enode, address liquidContract);
    # event PausedValidator(address treasury, address addr, uint256 effectiveBlock);
    # event Rewarded(address addr, uint256 amount);
