# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Python module holding the Autonity Web3.py external module
"""

from __future__ import annotations

import os
from enum import IntEnum
from typing import Sequence, Tuple, TypedDict, cast

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.types import Wei

from autonity.abi_manager import ABIManager
from autonity.committee_member import CommitteeMember, committee_member_from_tuple
from autonity.config import Config, config_from_tuple
from autonity.erc20 import ERC20
from autonity.validator import (
    NodeAddress,
    OracleAddress,
    ValidatorDescriptor,
    validator_descriptor_from_tuple,
)

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-arguments

AUTONITY_CONTRACT_ADDRESS = "0xBd770416a3345F91E4B34576cb804a576fa48EB1"
"""
The default autonity contract address.
see https://docs.autonity.org/concepts/architecture/#autonity-protocol-contract
"""


def get_autonity_contract_version() -> str:
    """
    Returns the version of the Autonity contract which this library is aligned with,
    and that is bundled with the library.
    """
    version_path = os.path.join(os.path.dirname(__file__), "abi", "autonity-commit.txt")
    if not os.path.exists(version_path):
        return "N/A"
    with open(version_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def get_autonity_contract_abi_path() -> str:
    """
    Returns the Autonity contract ABI path bundled with the library.
    This can be used in to load the ABI from a 3rd party app or library
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "abi", "Autonity.abi")
    )


class UnbondingReleaseState(IntEnum):
    NOT_RELEASED = 0
    RELEASED = 1
    REJECTED = 2
    REVERTED = 3


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

    def __init__(self, web3: Web3):
        super().__init__(
            web3,
            web3.to_checksum_address(AUTONITY_CONTRACT_ADDRESS),
            ABIManager.load_abi("Autonity"),
        )

        # TODO: What contract version checks can be performed here?

    @staticmethod
    def address() -> ChecksumAddress:
        """
        Return the deterministic address of the Autonity contract.
        """
        return Web3.to_checksum_address(AUTONITY_CONTRACT_ADDRESS)

    def commission_rate_precision(self) -> int:
        """
        See `COMMISSION_RATE_PRECISION` on the Autonity contract.
        """
        return self.contract.functions.COMMISSION_RATE_PRECISION().call()

    def max_bond_applied_gas(self) -> int:
        """
        See `maxBondAppliedGas` on the Autonity contract.
        """
        return self.contract.functions.maxBondAppliedGas().call()

    def max_unbond_applied_gas(self) -> int:
        """
        See `maxUnbondAppliedGas` on the Autonity contract.
        """
        return self.contract.functions.maxUnbondAppliedGas().call()

    def max_unbond_released_gas(self) -> int:
        """
        See `maxUnbondReleasedGas` on the Autonity contract.
        """
        return self.contract.functions.maxUnbondReleasedGas().call()

    def max_rewards_distribution_gas(self) -> int:
        """
        See `maxRewardsDistributionGas` on the Autonity contract.
        """
        return self.contract.functions.maxRewardsDistributionGas().call()

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

    def last_epoch_time(self) -> int:
        """
        See `lastEpochTime` on the Autonity contract.
        """
        return self.contract.functions.lastEpochTime().call()

    def epoch_total_bonded_stake(self) -> int:
        """
        See `epochTotalBondedStake` on the Autonity contract.
        """
        return self.contract.functions.epochTotalBondedStake().call()

    def atn_total_redistributed(self) -> int:
        """
        See `atnTotalRedistributed` on the Autonity contract.
        """
        return self.contract.functions.atnTotalRedistributed().call()

    def epoch_reward(self) -> int:
        """
        See `epochReward` on the Autonity contract.
        """
        return self.contract.functions.epochReward().call()

    def staking_gas_price(self) -> int:
        """
        See `stakingGasPrice` on the Autonity contract.
        """
        return self.contract.functions.stakingGasPrice().call()

    def inflation_reserve(self) -> int:
        """
        See `inflationReserve` on the Autonity contract.
        """
        return self.contract.functions.inflationReserve().call()

    def deployer(self) -> ChecksumAddress:
        """
        See `deployer` on the Autonity contract.
        """
        return self.contract.functions.deployer().call()

    def get_epoch_period(self) -> int:
        """
        See `getEpochPeriod` on the Autonity contract.
        """
        return self.contract.functions.getEpochPeriod().call()

    def get_block_period(self) -> int:
        """
        See `getBlockPeriod` on the Autonity contract.
        """
        return self.contract.functions.getBlockPeriod().call()

    def get_unbonding_period(self) -> int:
        """
        See `getUnbondingPeriod` on the Autonity contract.
        """
        return self.contract.functions.getUnbondingPeriod().call()

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

    def get_validators(self) -> Sequence[NodeAddress]:
        """
        See `getValidators` on the Autonity contract.
        """
        return self.contract.functions.getValidators().call()

    def get_treasury_account(self) -> ChecksumAddress:
        """
        See `getTreasuryAccount` on the Autonity contract.
        """
        return self.contract.functions.getTreasuryAccount().call()

    def get_treasury_fee(self) -> int:
        """
        See `getTreasuryFee` on the Autonity contract.
        """
        return self.contract.functions.getTreasuryFee().call()

    def get_validator(self, addr: ChecksumAddress) -> ValidatorDescriptor:
        """
        See `getValidator` on the Autonity contract.  To interact with
        validators, construct a `Validator` object from the returned
        ValidatorDescription.
        """
        assert isinstance(addr, str)
        value = self.contract.functions.getValidator(addr).call()
        return validator_descriptor_from_tuple(value)

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

    def get_oracle(self) -> ChecksumAddress:
        """
        See `getOracle` on the Autonity contract.
        """
        return self.contract.functions.getOracle().call()

    def get_proposer(self, height: int, round_idx: int) -> ChecksumAddress:
        """
        See `getProposer` on the Autonity contract.
        """
        return self.contract.functions.getProposer(height, round_idx).call()

    def get_unbonding_release_state(self, unbonding_id: int) -> int:
        """
        See `getUnbondingReleaseState` on the Autonity contract.
        """
        return UnbondingReleaseState(
            self.contract.functions.getUnbondingReleaseState().call()
        )

    def get_reverting_amount(self, unbonding_id: int) -> int:
        """
        See `getRevertingAmount` on the Autonity contract.
        """
        return self.contract.functions.getRevertingAmount(unbonding_id).call()

    def get_epoch_from_block(self, block: int) -> int:
        """
        See `getEpochFromBlock` on the Autonity contract.
        """
        return self.contract.functions.getEpochFromBlock(block).call()

    def bond(
        self,
        validator_addr: NodeAddress,
        amount: int,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `bond` method.  See `bond` on the
        Autonity contract.
        """
        return self.contract.functions.bond(validator_addr, amount)

    def unbond(
        self,
        validator_addr: NodeAddress,
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
        oracle: OracleAddress,
        consensus_key: HexBytes,
        proof: HexBytes,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `registerValidator` method.  See
        `registerValidator` on the Autonity contract.
        """
        return self.contract.functions.registerValidator(
            enode, oracle, consensus_key, proof
        )

    def pause_validator(
        self,
        validator_addr: NodeAddress,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `pauseValidator` method.  See
        `pauseValidator` on the Autonity contract.
        """
        return self.contract.functions.pauseValidator(validator_addr)

    def activate_validator(
        self,
        validator_addr: NodeAddress,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `activateValidator` method.  See
        `activateValidator` on the Autonity contract.
        """
        return self.contract.functions.activateValidator(validator_addr)

    def update_enode(self, validator: NodeAddress, enode: str) -> ContractFunction:
        """
        Update enode of a registered validator.
        """
        return self.contract.functions.updateEnode(validator, enode)

    # Functions below here are operatorOnly

    def set_max_bond_applied_gas(self, gas: int) -> ContractFunction:
        """
        Set the maximum bond applied gas. Restricted to the operator account.
        See `setMaxBondAppliedGas` on the Autonity contract.
        """
        return self.contract.functions.setMaxBondAppliedGas(gas)

    def set_max_unbond_applied_gas(self, gas: int) -> ContractFunction:
        """
        Set the maximum unbond applied gas. Restricted to the operator account.
        See `setMaxUnbondAppliedGas` on the Autonity contract.
        """
        return self.contract.functions.setMaxUnbondAppliedGas(gas)

    def set_max_unbond_released_gas(self, gas: int) -> ContractFunction:
        """
        Set the maximum unbond released gas. Restricted to the operator account.
        See `setMaxUnbondReleasedGas` on the Autonity contract.
        """
        return self.contract.functions.setMaxUnbondReleasedGas(gas)

    def set_max_rewards_distribution_gas(self, gas: int) -> ContractFunction:
        """
        Set the maximum rewards distrbution gas. Restricted to the operator account.
        See `setMaxRewardsDistributionGas` on the Autonity contract.
        """
        return self.contract.functions.setMaxRewardsDistributionGas(gas)

    def set_staking_gas_price(self, price: int) -> ContractFunction:
        """
        Set the gas price for notification on staking operation. Restricted to the
        operator account. See `setStakingGasPrice` on the Autonity contract.
        """
        return self.contract.functions.setStakingGasPrice(price)

    def set_minimum_base_fee(self, base_fee: Wei) -> ContractFunction:
        """
        Set the minimum gas price. Restricted to the operator account.
        See `setMinimumBaseFee` on the Autonity contract.
        """
        return self.contract.functions.setMinimumBaseFee(base_fee)

    def set_committee_size(self, committee_size: int) -> ContractFunction:
        """
        Set the maximum size of the consensus committee. Restricted to the
        Operator account.  See `setCommitteeSize` on Autonity contract.
        """
        return self.contract.functions.setCommitteeSize(committee_size)

    def set_unbonding_period(self, period: int) -> ContractFunction:
        """
        Set the unbonding period. Restricted to the Operator account.  See
        `setUnbondingPeriod` on Autonity contract.
        """
        return self.contract.functions.setUnbondingPeriod(period)

    def set_epoch_period(self, period: int) -> ContractFunction:
        """
        Set the epoch period. Restricted to the Operator account.  See
        `setEpochPeriod` on Autonity contract.
        """
        return self.contract.functions.setEpochPeriod(period)

    def set_operator_account(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the Operator account. Restricted to the Operator account.  See
        `setOperatorAccount` on Autonity contract.
        """
        return self.contract.functions.setOperatorAccount(address)

    # def set_block_period(period: int) -> ContractFunction:
    #     """
    #     Currently not supported.  Set the block period. Restricted to the
    #     Operator account.
    #     """
    #     return self.contract.setBlockPeriod(period)

    def set_treasury_account(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the global treasury account. Restricted to the Operator
        account.  See `setTreasuryAccount` on Autonity contract.
        """
        return self.contract.functions.setTreasuryAccount(address)

    def set_treasury_fee(self, treasury_fee: int) -> ContractFunction:
        """
        Set the treasury fee. Restricted to the Operator account.  See
        `setTreasuryFee` on Autonity contract.
        """
        return self.contract.functions.setTreasuryFee(treasury_fee)

    def set_accountability_contract(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the accountability contract address. Restricted to the Operator
        account.  See `setAccountabilityContract` on Autonity contract.
        """
        return self.contract.functions.setAccountabilityContract(address)

    def set_oracle_contract(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the oracle contract address. Restricted to the Operator
        account.  See `setOracleContract` on Autonity contract.
        """
        return self.contract.functions.setOracleContract(address)

    def set_acu_contract(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the acu contract address. Restricted to the Operator
        account.  See `setAcuContract` on Autonity contract.
        """
        return self.contract.functions.setAcuContract(address)

    def set_supply_control_contract(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the supply control contract address. Restricted to the Operator
        account.  See `setSupplyControlContract` on Autonity contract.
        """
        return self.contract.functions.setSupplyControlContract(address)

    def set_stabilization_contract(self, address: ChecksumAddress) -> ContractFunction:
        """
        Set the stabilization contract address. Restricted to the Operator
        account.  See `setStabilizationContract` on Autonity contract.
        """
        return self.contract.functions.setStabilizationContract(address)

    def set_inflation_controller_contract(
        self, address: ChecksumAddress
    ) -> ContractFunction:
        """
        Set the inflation controller contract address. Restricted to the Operator
        account.  See `setStabilizationContract` on Autonity contract.
        """
        return self.contract.functions.setInflationControllerContract(address)

    def set_upgrade_manager_contract(
        self, address: ChecksumAddress
    ) -> ContractFunction:
        """
        Set the upgrade manager contract address. Restricted to the Operator account.
        See `setUpgradeManagerContract` on Autonity contract.
        """
        return self.contract.functions.setStabilizationContract(address)

    def set_non_stakable_vesting_contract(
        self, address: ChecksumAddress
    ) -> ContractFunction:
        """
        Set the non stakable vesting contract address. Restricted to the Operator
        account. See `setNonStakableVestingContract` on Autonity contract.
        """
        return self.contract.functions.setNonStakableVestingContract(address)

    def mint(self, address: ChecksumAddress, amount: int) -> ContractFunction:
        """
        Mint new stake token (NTN) and add it to the recipient
        balance. Restricted to the Operator account.  See `mint` on
        Autonity contract.
        """
        return self.contract.functions.mint(address, amount)

    def burn(self, address: ChecksumAddress, amount: int) -> ContractFunction:
        """
        Burn the specified amount of NTN stake token from an
        account. Restricted to the Operator account.  This won't burn
        associated Liquid tokens.  See `burn` on Autonity contract.
        """
        return self.contract.functions.burn(address, amount)

    def change_commission_rate(
        self,
        validator: NodeAddress,
        rate: int,
    ) -> ContractFunction:
        """
        Create a TxParams calling the `changeCommissionRate` method.  See
        `changeCommissionRate` on the Autonity contract.
        """
        return self.contract.functions.changeCommissionRate(validator, rate)

    # TODO: events
    # event ActivatedValidator(address indexed treasury, address indexed addr, uint256 effectiveBlock);
    # event AppliedUnbondingReverted(address indexed validator, address indexed delegator, bool selfBonded, uint256 amount);
    # event BondingRejected(address indexed validator, address indexed delegator, uint256 amount, ValidatorState state);
    # event BondingReverted(address indexed validator, address indexed delegator, uint256 amount);
    # event BurnedStake(address addr, uint256 amount);
    # event CommissionRateChange(address validator, uint256 rate);
    # event EpochPeriodUpdated(uint256 period);
    # event MinimumBaseFeeUpdated(uint256 gasPrice);
    # event MintedStake(address addr, uint256 amount);
    # event NewBondingRequest(address indexed validator, address indexed delegator, bool selfBonded, uint256 amount);
    # event NewEpoch(uint256 epoch);
    # event NewUnbondingRequest(address indexed validator, address indexed delegator, bool selfBonded, uint256 amount);
    # event PausedValidator(address indexed treasury, address indexed addr, uint256 effectiveBlock);
    # event RegisteredValidator(address treasury, address addr, address oracleAddress, string enode, address liquidContract);
    # event ReleasedUnbondingReverted(address indexed validator, address indexed delegator, bool selfBonded, uint256 amount);
    # event Rewarded(address indexed addr, uint256 atnAmount, uint256 ntnAmount);
    # event UnbondingRejected(address indexed validator, address indexed delegator, bool selfBonded, uint256 amount);
    # event UnlockingScheduleFailed(uint256 epochTime);
