"""Autonity contract binding and data structures."""

# This module has been generated using pyabigen v0.2.9

import enum
import typing

import eth_typing
import hexbytes
import web3
from dataclasses import dataclass
from web3.contract import base_contract, contract

__version__ = "v0.14.0"


class ValidatorState(enum.IntEnum):
    """Port of `enum ValidatorState` on the Autonity contract."""

    ACTIVE = 0
    PAUSED = 1
    JAILED = 2
    JAILBOUND = 3


class UnbondingReleaseState(enum.IntEnum):
    """Port of `enum UnbondingReleaseState` on the Autonity contract."""

    NOT_RELEASED = 0
    RELEASED = 1
    REJECTED = 2
    REVERTED = 3


@dataclass
class Validator:
    """Port of `struct Validator` on the Autonity contract."""

    treasury: eth_typing.ChecksumAddress
    node_address: eth_typing.ChecksumAddress
    oracle_address: eth_typing.ChecksumAddress
    enode: str
    commission_rate: int
    bonded_stake: int
    unbonding_stake: int
    unbonding_shares: int
    self_bonded_stake: int
    self_unbonding_stake: int
    self_unbonding_shares: int
    self_unbonding_stake_locked: int
    liquid_contract: eth_typing.ChecksumAddress
    liquid_supply: int
    registration_block: int
    total_slashed: int
    jail_release_block: int
    provable_fault_count: int
    consensus_key: hexbytes.HexBytes
    state: ValidatorState


@dataclass
class Policy:
    """Port of `struct Policy` on the Autonity contract."""

    treasury_fee: int
    min_base_fee: int
    delegation_rate: int
    unbonding_period: int
    initial_inflation_reserve: int
    treasury_account: eth_typing.ChecksumAddress


@dataclass
class Contracts:
    """Port of `struct Contracts` on the Autonity contract."""

    accountability_contract: eth_typing.ChecksumAddress
    oracle_contract: eth_typing.ChecksumAddress
    acu_contract: eth_typing.ChecksumAddress
    supply_control_contract: eth_typing.ChecksumAddress
    stabilization_contract: eth_typing.ChecksumAddress
    upgrade_manager_contract: eth_typing.ChecksumAddress
    inflation_controller_contract: eth_typing.ChecksumAddress
    non_stakable_vesting_contract: eth_typing.ChecksumAddress


@dataclass
class Protocol:
    """Port of `struct Protocol` on the Autonity contract."""

    operator_account: eth_typing.ChecksumAddress
    epoch_period: int
    block_period: int
    committee_size: int


@dataclass
class Config:
    """Port of `struct Config` on the Autonity contract."""

    policy: Policy
    contracts: Contracts
    protocol: Protocol
    contract_version: int


@dataclass
class CommitteeMember:
    """Port of `struct CommitteeMember` on the Autonity contract."""

    addr: eth_typing.ChecksumAddress
    voting_power: int
    consensus_key: hexbytes.HexBytes


class Autonity:
    """Autonity contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed Autonity contract.
    """

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(
            address=address,
            abi=ABI,
        )

    @property
    def ActivatedValidator(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event ActivatedValidator` on the Autonity contract."""
        return self._contract.events.ActivatedValidator

    @property
    def AppliedUnbondingReverted(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event AppliedUnbondingReverted` on the Autonity contract."""
        return self._contract.events.AppliedUnbondingReverted

    @property
    def Approval(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Approval` on the Autonity contract."""
        return self._contract.events.Approval

    @property
    def BondingRejected(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event BondingRejected` on the Autonity contract."""
        return self._contract.events.BondingRejected

    @property
    def BondingReverted(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event BondingReverted` on the Autonity contract."""
        return self._contract.events.BondingReverted

    @property
    def BurnedStake(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event BurnedStake` on the Autonity contract."""
        return self._contract.events.BurnedStake

    @property
    def CommissionRateChange(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event CommissionRateChange` on the Autonity contract."""
        return self._contract.events.CommissionRateChange

    @property
    def EpochPeriodUpdated(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event EpochPeriodUpdated` on the Autonity contract."""
        return self._contract.events.EpochPeriodUpdated

    @property
    def MinimumBaseFeeUpdated(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event MinimumBaseFeeUpdated` on the Autonity contract."""
        return self._contract.events.MinimumBaseFeeUpdated

    @property
    def MintedStake(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event MintedStake` on the Autonity contract."""
        return self._contract.events.MintedStake

    @property
    def NewBondingRequest(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewBondingRequest` on the Autonity contract.

        This event is emitted when a bonding request to a validator node has been
        registered. This request will only be effective at the end of the current epoch
        however the stake will be put in custody immediately from the delegator's
        account.
        """
        return self._contract.events.NewBondingRequest

    @property
    def NewEpoch(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewEpoch` on the Autonity contract."""
        return self._contract.events.NewEpoch

    @property
    def NewUnbondingRequest(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event NewUnbondingRequest` on the Autonity contract.

        This event is emitted when an unbonding request to a validator node has been
        registered. This request will only be effective after the unbonding period,
        rounded to the next epoch. Please note that because of potential slashing events
        during this delay period, the released amount may or may not be correspond to
        the amount requested.
        """
        return self._contract.events.NewUnbondingRequest

    @property
    def PausedValidator(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event PausedValidator` on the Autonity contract."""
        return self._contract.events.PausedValidator

    @property
    def RegisteredValidator(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event RegisteredValidator` on the Autonity contract."""
        return self._contract.events.RegisteredValidator

    @property
    def ReleasedUnbondingReverted(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event ReleasedUnbondingReverted` on the Autonity contract."""
        return self._contract.events.ReleasedUnbondingReverted

    @property
    def Rewarded(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Rewarded` on the Autonity contract."""
        return self._contract.events.Rewarded

    @property
    def Transfer(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event Transfer` on the Autonity contract."""
        return self._contract.events.Transfer

    @property
    def UnbondingRejected(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event UnbondingRejected` on the Autonity contract."""
        return self._contract.events.UnbondingRejected

    @property
    def UnlockingScheduleFailed(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event UnlockingScheduleFailed` on the Autonity contract."""
        return self._contract.events.UnlockingScheduleFailed

    def commission_rate_precision(
        self,
    ) -> int:
        """Binding for `COMMISSION_RATE_PRECISION` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.COMMISSION_RATE_PRECISION().call()
        return int(return_value)

    def activate_validator(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `activateValidator` on the Autonity contract.

        Re-activate the specified validator.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress
            address to be enabled.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.activateValidator(
            _address,
        )

    def allowance(
        self,
        owner: eth_typing.ChecksumAddress,
        spender: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `allowance` on the Autonity contract.

        Parameters
        ----------
        owner : eth_typing.ChecksumAddress
        spender : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.allowance(
            owner,
            spender,
        ).call()
        return int(return_value)

    def approve(
        self,
        spender: eth_typing.ChecksumAddress,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `approve` on the Autonity contract.

        Parameters
        ----------
        spender : eth_typing.ChecksumAddress
        amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.approve(
            spender,
            amount,
        )

    def atn_total_redistributed(
        self,
    ) -> int:
        """Binding for `atnTotalRedistributed` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.atnTotalRedistributed().call()
        return int(return_value)

    def balance_of(
        self,
        _addr: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `balanceOf` on the Autonity contract.

        Returns the amount of unbonded Newton token held by the account (ERC-20).

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.balanceOf(
            _addr,
        ).call()
        return int(return_value)

    def bond(
        self,
        _validator: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `bond` on the Autonity contract.

        Create a bonding(delegation) request with the caller as delegator. In case the
        caller is a contract, it needs to send some gas so autonity can notify the
        caller about staking operations. In case autonity fails to notify the caller
        (contract), the applied request is reverted.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            address of the validator to delegate stake to.
        _amount : int
            total amount of NTN to bond.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.bond(
            _validator,
            _amount,
        )

    def burn(
        self,
        _addr: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `burn` on the Autonity contract.

        Burn the specified amount of NTN stake token from an account. Restricted to the
        Operator account. This won't burn associated Liquid tokens.

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.burn(
            _addr,
            _amount,
        )

    def change_commission_rate(
        self,
        _validator: eth_typing.ChecksumAddress,
        _rate: int,
    ) -> contract.ContractFunction:
        """Binding for `changeCommissionRate` on the Autonity contract.

        Change commission rate for the specified validator.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            address to be enabled. _rate new commission rate, ranging between 0-10000
            (10000 = 100%).
        _rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.changeCommissionRate(
            _validator,
            _rate,
        )

    def complete_contract_upgrade(
        self,
    ) -> contract.ContractFunction:
        """Binding for `completeContractUpgrade` on the Autonity contract.

        Finalize the contract upgrade. To be called once the storage buffer for the new
        contract are filled using {upgradeContract} The protocol will then update the
        bytecode of the autonity contract at block finalization phase.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.completeContractUpgrade()

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the Autonity contract.

        Returns
        -------
        Config
        """
        return_value = self._contract.functions.config().call()
        return Config(
            Policy(
                int(return_value[0][0]),
                int(return_value[0][1]),
                int(return_value[0][2]),
                int(return_value[0][3]),
                int(return_value[0][4]),
                eth_typing.ChecksumAddress(return_value[0][5]),
            ),
            Contracts(
                eth_typing.ChecksumAddress(return_value[1][0]),
                eth_typing.ChecksumAddress(return_value[1][1]),
                eth_typing.ChecksumAddress(return_value[1][2]),
                eth_typing.ChecksumAddress(return_value[1][3]),
                eth_typing.ChecksumAddress(return_value[1][4]),
                eth_typing.ChecksumAddress(return_value[1][5]),
                eth_typing.ChecksumAddress(return_value[1][6]),
                eth_typing.ChecksumAddress(return_value[1][7]),
            ),
            Protocol(
                eth_typing.ChecksumAddress(return_value[2][0]),
                int(return_value[2][1]),
                int(return_value[2][2]),
                int(return_value[2][3]),
            ),
            int(return_value[3]),
        )

    def decimals(
        self,
    ) -> int:
        """Binding for `decimals` on the Autonity contract.

        Returns
        -------
        int
            the number of decimals the NTN token uses.
        """
        return_value = self._contract.functions.decimals().call()
        return int(return_value)

    def deployer(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `deployer` on the Autonity contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.deployer().call()
        return eth_typing.ChecksumAddress(return_value)

    def epoch_id(
        self,
    ) -> int:
        """Binding for `epochID` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.epochID().call()
        return int(return_value)

    def epoch_reward(
        self,
    ) -> int:
        """Binding for `epochReward` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.epochReward().call()
        return int(return_value)

    def epoch_total_bonded_stake(
        self,
    ) -> int:
        """Binding for `epochTotalBondedStake` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.epochTotalBondedStake().call()
        return int(return_value)

    def get_block_period(
        self,
    ) -> int:
        """Binding for `getBlockPeriod` on the Autonity contract.

        Returns the block period.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getBlockPeriod().call()
        return int(return_value)

    def get_committee(
        self,
    ) -> typing.List[CommitteeMember]:
        """Binding for `getCommittee` on the Autonity contract.

        Returns the block committee.

        Returns
        -------
        typing.List[CommitteeMember]
        """
        return_value = self._contract.functions.getCommittee().call()
        return [
            CommitteeMember(
                eth_typing.ChecksumAddress(elem[0]),
                int(elem[1]),
                hexbytes.HexBytes(elem[2]),
            )
            for elem in return_value
        ]

    def get_committee_enodes(
        self,
    ) -> typing.List[str]:
        """Binding for `getCommitteeEnodes` on the Autonity contract.

        Returns
        -------
        typing.List[str]
            Returns the consensus committee enodes.
        """
        return_value = self._contract.functions.getCommitteeEnodes().call()
        return [str(elem) for elem in return_value]

    def get_epoch_from_block(
        self,
        _block: int,
    ) -> int:
        """Binding for `getEpochFromBlock` on the Autonity contract.

        Returns epoch associated to the block number.

        Parameters
        ----------
        _block : int
            the input block number.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getEpochFromBlock(
            _block,
        ).call()
        return int(return_value)

    def get_epoch_period(
        self,
    ) -> int:
        """Binding for `getEpochPeriod` on the Autonity contract.

        Returns the epoch period.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getEpochPeriod().call()
        return int(return_value)

    def get_last_epoch_block(
        self,
    ) -> int:
        """Binding for `getLastEpochBlock` on the Autonity contract.

        Returns the last epoch's end block height.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getLastEpochBlock().call()
        return int(return_value)

    def get_max_committee_size(
        self,
    ) -> int:
        """Binding for `getMaxCommitteeSize` on the Autonity contract.

        Returns
        -------
        int
            Returns the maximum size of the consensus committee.
        """
        return_value = self._contract.functions.getMaxCommitteeSize().call()
        return int(return_value)

    def get_minimum_base_fee(
        self,
    ) -> int:
        """Binding for `getMinimumBaseFee` on the Autonity contract.

        Returns
        -------
        int
            Returns the minimum gas price.
        """
        return_value = self._contract.functions.getMinimumBaseFee().call()
        return int(return_value)

    def get_new_contract(
        self,
    ) -> typing.Tuple[hexbytes.HexBytes, str]:
        """Binding for `getNewContract` on the Autonity contract.

        Getter to retrieve a new Autonity contract bytecode and ABI when an upgrade is
        initiated.

        Returns
        -------
        hexbytes.HexBytes
            `bytecode` the new contract bytecode.
        str
            `contractAbi` the new contract ABI.
        """
        return_value = self._contract.functions.getNewContract().call()
        return (
            hexbytes.HexBytes(return_value[0]),
            str(return_value[1]),
        )

    def get_operator(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getOperator` on the Autonity contract.

        Returns the current operator account.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getOperator().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_oracle(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getOracle` on the Autonity contract.

        Returns the current Oracle account.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getOracle().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_proposer(
        self,
        height: int,
        round: int,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getProposer` on the Autonity contract.

        getProposer returns the address of the proposer for the given height and round.
        The proposer is selected from the committee via weighted random sampling, with
        selection probability determined by the voting power of each committee member.
        The selection mechanism is deterministic and will always select the same
        address, given the same height, round and contract state.

        Parameters
        ----------
        height : int
        round : int

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getProposer(
            height,
            round,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def get_reverting_amount(
        self,
        _unbonding_id: int,
    ) -> int:
        """Binding for `getRevertingAmount` on the Autonity contract.

        Returns the amount of LNTN or NTN bonded when the released unbonding was
        reverted

        Parameters
        ----------
        _unbonding_id : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getRevertingAmount(
            _unbonding_id,
        ).call()
        return int(return_value)

    def get_treasury_account(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getTreasuryAccount` on the Autonity contract.

        Returns the current treasury account.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getTreasuryAccount().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_treasury_fee(
        self,
    ) -> int:
        """Binding for `getTreasuryFee` on the Autonity contract.

        Returns the current treasury fee.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getTreasuryFee().call()
        return int(return_value)

    def get_unbonding_period(
        self,
    ) -> int:
        """Binding for `getUnbondingPeriod` on the Autonity contract.

        Returns the un-bonding period.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getUnbondingPeriod().call()
        return int(return_value)

    def get_unbonding_release_state(
        self,
        _unbonding_id: int,
    ) -> UnbondingReleaseState:
        """Binding for `getUnbondingReleaseState` on the Autonity contract.

        Returns the release state of the unbonding request

        Parameters
        ----------
        _unbonding_id : int

        Returns
        -------
        UnbondingReleaseState
        """
        return_value = self._contract.functions.getUnbondingReleaseState(
            _unbonding_id,
        ).call()
        return UnbondingReleaseState(return_value)

    def get_validator(
        self,
        _addr: eth_typing.ChecksumAddress,
    ) -> Validator:
        """Binding for `getValidator` on the Autonity contract.

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress

        Returns
        -------
        Validator
            Returns a user object with the `_account` parameter. The returned data
            object might be empty if there is no user associated.
        """
        return_value = self._contract.functions.getValidator(
            _addr,
        ).call()
        return Validator(
            eth_typing.ChecksumAddress(return_value[0]),
            eth_typing.ChecksumAddress(return_value[1]),
            eth_typing.ChecksumAddress(return_value[2]),
            str(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
            int(return_value[8]),
            int(return_value[9]),
            int(return_value[10]),
            int(return_value[11]),
            eth_typing.ChecksumAddress(return_value[12]),
            int(return_value[13]),
            int(return_value[14]),
            int(return_value[15]),
            int(return_value[16]),
            int(return_value[17]),
            hexbytes.HexBytes(return_value[18]),
            ValidatorState(return_value[19]),
        )

    def get_validators(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """Binding for `getValidators` on the Autonity contract.

        Returns the current list of validators.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
        """
        return_value = self._contract.functions.getValidators().call()
        return [eth_typing.ChecksumAddress(elem) for elem in return_value]

    def get_version(
        self,
    ) -> int:
        """Binding for `getVersion` on the Autonity contract.

        Returns the current contract version.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getVersion().call()
        return int(return_value)

    def inflation_reserve(
        self,
    ) -> int:
        """Binding for `inflationReserve` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.inflationReserve().call()
        return int(return_value)

    def last_epoch_block(
        self,
    ) -> int:
        """Binding for `lastEpochBlock` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lastEpochBlock().call()
        return int(return_value)

    def last_epoch_time(
        self,
    ) -> int:
        """Binding for `lastEpochTime` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.lastEpochTime().call()
        return int(return_value)

    def max_bond_applied_gas(
        self,
    ) -> int:
        """Binding for `maxBondAppliedGas` on the Autonity contract.

        max allowed gas for notifying delegator (contract) about staking operations

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxBondAppliedGas().call()
        return int(return_value)

    def max_rewards_distribution_gas(
        self,
    ) -> int:
        """Binding for `maxRewardsDistributionGas` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxRewardsDistributionGas().call()
        return int(return_value)

    def max_unbond_applied_gas(
        self,
    ) -> int:
        """Binding for `maxUnbondAppliedGas` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxUnbondAppliedGas().call()
        return int(return_value)

    def max_unbond_released_gas(
        self,
    ) -> int:
        """Binding for `maxUnbondReleasedGas` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.maxUnbondReleasedGas().call()
        return int(return_value)

    def mint(
        self,
        _addr: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `mint` on the Autonity contract.

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.mint(
            _addr,
            _amount,
        )

    def name(
        self,
    ) -> str:
        """Binding for `name` on the Autonity contract.

        Returns
        -------
        str
            the name of the stake token.
        """
        return_value = self._contract.functions.name().call()
        return str(return_value)

    def pause_validator(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `pauseValidator` on the Autonity contract.

        Pause the validator and stop it accepting delegations.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress
            address to be disabled.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.pauseValidator(
            _address,
        )

    def receive_atn(
        self,
    ) -> contract.ContractFunction:
        """Binding for `receiveATN` on the Autonity contract.

        can be used to send AUT to the contract

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.receiveATN()

    def register_validator(
        self,
        _enode: str,
        _oracle_address: eth_typing.ChecksumAddress,
        _consensus_key: hexbytes.HexBytes,
        _signatures: hexbytes.HexBytes,
    ) -> contract.ContractFunction:
        """Binding for `registerValidator` on the Autonity contract.

        Register a new validator in the system.  The validator might be selected to be
        part of consensus. This validator will have assigned to its treasury account the
        caller of this function. A new token "Liquid Stake" is deployed at this phase.

        Parameters
        ----------
        _enode : str
            enode identifying the validator node.
        _oracle_address : eth_typing.ChecksumAddress
        _consensus_key : hexbytes.HexBytes
        _signatures : hexbytes.HexBytes
            is a combination of two ecdsa signatures, and a bls signature as the
            ownership proof of the validator key appended sequentially. The 1st two
            ecdsa signatures are in below order: 1. a message containing treasury
            account and signed by validator account private key . 2. a message
            containing treasury account and signed by Oracle account private key .

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.registerValidator(
            _enode,
            _oracle_address,
            _consensus_key,
            _signatures,
        )

    def reset_contract_upgrade(
        self,
    ) -> contract.ContractFunction:
        """Binding for `resetContractUpgrade` on the Autonity contract.

        Reset internal storage contract-upgrade buffers in case of issue.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.resetContractUpgrade()

    def set_accountability_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setAccountabilityContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setAccountabilityContract(
            _address,
        )

    def set_acu_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setAcuContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setAcuContract(
            _address,
        )

    def set_committee_size(
        self,
        _size: int,
    ) -> contract.ContractFunction:
        """Binding for `setCommitteeSize` on the Autonity contract.

        Parameters
        ----------
        _size : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setCommitteeSize(
            _size,
        )

    def set_epoch_period(
        self,
        _period: int,
    ) -> contract.ContractFunction:
        """Binding for `setEpochPeriod` on the Autonity contract.

        Parameters
        ----------
        _period : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setEpochPeriod(
            _period,
        )

    def set_inflation_controller_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setInflationControllerContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setInflationControllerContract(
            _address,
        )

    def set_max_bond_applied_gas(
        self,
        _gas: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxBondAppliedGas` on the Autonity contract.

        sets the value of max allowed gas for notifying delegator about staking
        operations NOTE: before updating, please check if the updated value works. It
        can be checked by updatting the hardcoded value of requiredGasBond and then
        compiling the contracts and running the tests in stakable_vesting_test.go

        Parameters
        ----------
        _gas : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxBondAppliedGas(
            _gas,
        )

    def set_max_rewards_distribution_gas(
        self,
        _gas: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxRewardsDistributionGas` on the Autonity contract.

        Parameters
        ----------
        _gas : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxRewardsDistributionGas(
            _gas,
        )

    def set_max_unbond_applied_gas(
        self,
        _gas: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxUnbondAppliedGas` on the Autonity contract.

        Parameters
        ----------
        _gas : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxUnbondAppliedGas(
            _gas,
        )

    def set_max_unbond_released_gas(
        self,
        _gas: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxUnbondReleasedGas` on the Autonity contract.

        Parameters
        ----------
        _gas : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxUnbondReleasedGas(
            _gas,
        )

    def set_minimum_base_fee(
        self,
        _price: int,
    ) -> contract.ContractFunction:
        """Binding for `setMinimumBaseFee` on the Autonity contract.

        Set the minimum gas price. Restricted to the operator account.

        Parameters
        ----------
        _price : int
            Positive integer.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMinimumBaseFee(
            _price,
        )

    def set_non_stakable_vesting_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setNonStakableVestingContract` on the Autonity contract.

        Set the Non-stakable Vesting contract address.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setNonStakableVestingContract(
            _address,
        )

    def set_operator_account(
        self,
        _account: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setOperatorAccount` on the Autonity contract.

        Parameters
        ----------
        _account : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setOperatorAccount(
            _account,
        )

    def set_oracle_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setOracleContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setOracleContract(
            _address,
        )

    def set_stabilization_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setStabilizationContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setStabilizationContract(
            _address,
        )

    def set_staking_gas_price(
        self,
        _price: int,
    ) -> contract.ContractFunction:
        """Binding for `setStakingGasPrice` on the Autonity contract.

        Set gas price for notification on staking operation

        Parameters
        ----------
        _price : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setStakingGasPrice(
            _price,
        )

    def set_supply_control_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setSupplyControlContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSupplyControlContract(
            _address,
        )

    def set_treasury_account(
        self,
        _account: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setTreasuryAccount` on the Autonity contract.

        Parameters
        ----------
        _account : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setTreasuryAccount(
            _account,
        )

    def set_treasury_fee(
        self,
        _treasury_fee: int,
    ) -> contract.ContractFunction:
        """Binding for `setTreasuryFee` on the Autonity contract.

        Parameters
        ----------
        _treasury_fee : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setTreasuryFee(
            _treasury_fee,
        )

    def set_unbonding_period(
        self,
        _period: int,
    ) -> contract.ContractFunction:
        """Binding for `setUnbondingPeriod` on the Autonity contract.

        Parameters
        ----------
        _period : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setUnbondingPeriod(
            _period,
        )

    def set_upgrade_manager_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setUpgradeManagerContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setUpgradeManagerContract(
            _address,
        )

    def staking_gas_price(
        self,
    ) -> int:
        """Binding for `stakingGasPrice` on the Autonity contract.

        the gas price to notify the delegator (only if contract) about the staking
        operation at epoch end

        Returns
        -------
        int
        """
        return_value = self._contract.functions.stakingGasPrice().call()
        return int(return_value)

    def symbol(
        self,
    ) -> str:
        """Binding for `symbol` on the Autonity contract.

        Returns
        -------
        str
            the Stake token's symbol.
        """
        return_value = self._contract.functions.symbol().call()
        return str(return_value)

    def total_supply(
        self,
    ) -> int:
        """Binding for `totalSupply` on the Autonity contract.

        Returns the total amount of stake token issued.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.totalSupply().call()
        return int(return_value)

    def transfer(
        self,
        _recipient: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transfer` on the Autonity contract.

        Moves `amount` NTN stake tokens from the caller's account to `recipient`.

        Parameters
        ----------
        _recipient : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transfer(
            _recipient,
            _amount,
        )

    def transfer_from(
        self,
        _sender: eth_typing.ChecksumAddress,
        _recipient: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `transferFrom` on the Autonity contract.

        Parameters
        ----------
        _sender : eth_typing.ChecksumAddress
        _recipient : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.transferFrom(
            _sender,
            _recipient,
            _amount,
        )

    def unbond(
        self,
        _validator: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `unbond` on the Autonity contract.

        Create an unbonding request with the caller as delegator. In case the caller is
        a contract, it needs to send some gas so autonity can notify the caller about
        staking operations. In case autonity fails to notify the caller (contract), the
        applied request is reverted.

        Parameters
        ----------
        _validator : eth_typing.ChecksumAddress
            address of the validator to unbond stake to.
        _amount : int
            total amount of LNTN (or NTN if self delegated) to unbond.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.unbond(
            _validator,
            _amount,
        )

    def update_enode(
        self,
        _node_address: eth_typing.ChecksumAddress,
        _enode: str,
    ) -> contract.ContractFunction:
        """Binding for `updateEnode` on the Autonity contract.

        Update enode of a registered validator. This function updates the network
        connection information (IP or/and port) of a registered validator. you cannot
        change the validator's address (pubkey part of the enode)

        Parameters
        ----------
        _node_address : eth_typing.ChecksumAddress
        _enode : str
            new enode to be updated

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.updateEnode(
            _node_address,
            _enode,
        )

    def upgrade_contract(
        self,
        _bytecode: hexbytes.HexBytes,
        _abi: str,
    ) -> contract.ContractFunction:
        """Binding for `upgradeContract` on the Autonity contract.

        Append to the contract storage buffer the new contract bytecode and abi. Should
        be called as many times as required.

        Parameters
        ----------
        _bytecode : hexbytes.HexBytes
        _abi : str

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.upgradeContract(
            _bytecode,
            _abi,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "address payable",
                            "name": "treasury",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "nodeAddress",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "oracleAddress",
                            "type": "address",
                        },
                        {"internalType": "string", "name": "enode", "type": "string"},
                        {
                            "internalType": "uint256",
                            "name": "commissionRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfBondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStakeLocked",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract Liquid",
                            "name": "liquidContract",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "registrationBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSlashed",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "jailReleaseBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "provableFaultCount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                        {
                            "internalType": "enum ValidatorState",
                            "name": "state",
                            "type": "uint8",
                        },
                    ],
                    "internalType": "struct Autonity.Validator[]",
                    "name": "_validators",
                    "type": "tuple[]",
                },
                {
                    "components": [
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "treasuryFee",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "minBaseFee",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "delegationRate",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "unbondingPeriod",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "initialInflationReserve",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "address payable",
                                    "name": "treasuryAccount",
                                    "type": "address",
                                },
                            ],
                            "internalType": "struct Autonity.Policy",
                            "name": "policy",
                            "type": "tuple",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "contract IAccountability",
                                    "name": "accountabilityContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IOracle",
                                    "name": "oracleContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IACU",
                                    "name": "acuContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract ISupplyControl",
                                    "name": "supplyControlContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IStabilization",
                                    "name": "stabilizationContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract UpgradeManager",
                                    "name": "upgradeManagerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IInflationController",
                                    "name": "inflationControllerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract INonStakableVestingVault",
                                    "name": "nonStakableVestingContract",
                                    "type": "address",
                                },
                            ],
                            "internalType": "struct Autonity.Contracts",
                            "name": "contracts",
                            "type": "tuple",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "address",
                                    "name": "operatorAccount",
                                    "type": "address",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "epochPeriod",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "blockPeriod",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "committeeSize",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct Autonity.Protocol",
                            "name": "protocol",
                            "type": "tuple",
                        },
                        {
                            "internalType": "uint256",
                            "name": "contractVersion",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Autonity.Config",
                    "name": "_config",
                    "type": "tuple",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "treasury",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "effectiveBlock",
                    "type": "uint256",
                },
            ],
            "name": "ActivatedValidator",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "selfBonded",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "AppliedUnbondingReverted",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "enum ValidatorState",
                    "name": "state",
                    "type": "uint8",
                },
            ],
            "name": "BondingRejected",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "BondingReverted",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "BurnedStake",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "rate",
                    "type": "uint256",
                },
            ],
            "name": "CommissionRateChange",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "period",
                    "type": "uint256",
                }
            ],
            "name": "EpochPeriodUpdated",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "gasPrice",
                    "type": "uint256",
                }
            ],
            "name": "MinimumBaseFeeUpdated",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "MintedStake",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "selfBonded",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "NewBondingRequest",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "epoch",
                    "type": "uint256",
                }
            ],
            "name": "NewEpoch",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "selfBonded",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "NewUnbondingRequest",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "treasury",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "effectiveBlock",
                    "type": "uint256",
                },
            ],
            "name": "PausedValidator",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "treasury",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "oracleAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "enode",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "liquidContract",
                    "type": "address",
                },
            ],
            "name": "RegisteredValidator",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "selfBonded",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "ReleasedUnbondingReverted",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "atnAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "ntnAmount",
                    "type": "uint256",
                },
            ],
            "name": "Rewarded",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Transfer",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "delegator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "selfBonded",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "UnbondingRejected",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "epochTime",
                    "type": "uint256",
                }
            ],
            "name": "UnlockingScheduleFailed",
            "type": "event",
        },
        {"stateMutability": "payable", "type": "fallback"},
        {
            "inputs": [],
            "name": "COMMISSION_RATE_PRECISION",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_address", "type": "address"}
            ],
            "name": "activateValidator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "spender", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "atnTotalRedistributed",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_addr", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "bond",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_addr", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "burn",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_rate", "type": "uint256"},
            ],
            "name": "changeCommissionRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "completeContractUpgrade",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "computeCommittee",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "config",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "treasuryFee",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minBaseFee",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "delegationRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingPeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "initialInflationReserve",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address payable",
                            "name": "treasuryAccount",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct Autonity.Policy",
                    "name": "policy",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "contract IAccountability",
                            "name": "accountabilityContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IOracle",
                            "name": "oracleContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IACU",
                            "name": "acuContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract ISupplyControl",
                            "name": "supplyControlContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IStabilization",
                            "name": "stabilizationContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract UpgradeManager",
                            "name": "upgradeManagerContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IInflationController",
                            "name": "inflationControllerContract",
                            "type": "address",
                        },
                        {
                            "internalType": "contract INonStakableVestingVault",
                            "name": "nonStakableVestingContract",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct Autonity.Contracts",
                    "name": "contracts",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "operatorAccount",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "epochPeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "blockPeriod",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "committeeSize",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Autonity.Protocol",
                    "name": "protocol",
                    "type": "tuple",
                },
                {
                    "internalType": "uint256",
                    "name": "contractVersion",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "deployer",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "epochID",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "epochReward",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "epochTotalBondedStake",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "finalize",
            "outputs": [
                {"internalType": "bool", "name": "", "type": "bool"},
                {
                    "components": [
                        {"internalType": "address", "name": "addr", "type": "address"},
                        {
                            "internalType": "uint256",
                            "name": "votingPower",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                    ],
                    "internalType": "struct Autonity.CommitteeMember[]",
                    "name": "",
                    "type": "tuple[]",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "finalizeInitialization",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getBlockPeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCommittee",
            "outputs": [
                {
                    "components": [
                        {"internalType": "address", "name": "addr", "type": "address"},
                        {
                            "internalType": "uint256",
                            "name": "votingPower",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                    ],
                    "internalType": "struct Autonity.CommitteeMember[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCommitteeEnodes",
            "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_block", "type": "uint256"}
            ],
            "name": "getEpochFromBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getEpochPeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getLastEpochBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getMaxCommitteeSize",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getMinimumBaseFee",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getNewContract",
            "outputs": [
                {"internalType": "bytes", "name": "", "type": "bytes"},
                {"internalType": "string", "name": "", "type": "string"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOperator",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOracle",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "height", "type": "uint256"},
                {"internalType": "uint256", "name": "round", "type": "uint256"},
            ],
            "name": "getProposer",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_unbondingID", "type": "uint256"}
            ],
            "name": "getRevertingAmount",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTreasuryAccount",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTreasuryFee",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getUnbondingPeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_unbondingID", "type": "uint256"}
            ],
            "name": "getUnbondingReleaseState",
            "outputs": [
                {
                    "internalType": "enum Autonity.UnbondingReleaseState",
                    "name": "",
                    "type": "uint8",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_addr", "type": "address"}],
            "name": "getValidator",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address payable",
                            "name": "treasury",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "nodeAddress",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "oracleAddress",
                            "type": "address",
                        },
                        {"internalType": "string", "name": "enode", "type": "string"},
                        {
                            "internalType": "uint256",
                            "name": "commissionRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfBondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStakeLocked",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract Liquid",
                            "name": "liquidContract",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "registrationBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSlashed",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "jailReleaseBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "provableFaultCount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                        {
                            "internalType": "enum ValidatorState",
                            "name": "state",
                            "type": "uint8",
                        },
                    ],
                    "internalType": "struct Autonity.Validator",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getValidators",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getVersion",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "inflationReserve",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastEpochBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastEpochTime",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "maxBondAppliedGas",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "maxRewardsDistributionGas",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "maxUnbondAppliedGas",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "maxUnbondReleasedGas",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_addr", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_address", "type": "address"}
            ],
            "name": "pauseValidator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "receiveATN",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "_enode", "type": "string"},
                {
                    "internalType": "address",
                    "name": "_oracleAddress",
                    "type": "address",
                },
                {"internalType": "bytes", "name": "_consensusKey", "type": "bytes"},
                {"internalType": "bytes", "name": "_signatures", "type": "bytes"},
            ],
            "name": "registerValidator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "resetContractUpgrade",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IAccountability",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setAccountabilityContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IACU", "name": "_address", "type": "address"}
            ],
            "name": "setAcuContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_size", "type": "uint256"}],
            "name": "setCommitteeSize",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_period", "type": "uint256"}
            ],
            "name": "setEpochPeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IInflationController",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setInflationControllerContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_gas", "type": "uint256"}],
            "name": "setMaxBondAppliedGas",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_gas", "type": "uint256"}],
            "name": "setMaxRewardsDistributionGas",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_gas", "type": "uint256"}],
            "name": "setMaxUnbondAppliedGas",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "_gas", "type": "uint256"}],
            "name": "setMaxUnbondReleasedGas",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_price", "type": "uint256"}
            ],
            "name": "setMinimumBaseFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract INonStakableVestingVault",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setNonStakableVestingContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"}
            ],
            "name": "setOperatorAccount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address payable",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setOracleContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IStabilization",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setStabilizationContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_price", "type": "uint256"}
            ],
            "name": "setStakingGasPrice",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract ISupplyControl",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setSupplyControlContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address payable",
                    "name": "_account",
                    "type": "address",
                }
            ],
            "name": "setTreasuryAccount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_treasuryFee", "type": "uint256"}
            ],
            "name": "setTreasuryFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_period", "type": "uint256"}
            ],
            "name": "setUnbondingPeriod",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract UpgradeManager",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setUpgradeManagerContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "stakingGasPrice",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_recipient", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_sender", "type": "address"},
                {"internalType": "address", "name": "_recipient", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "unbond",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"},
                {"internalType": "string", "name": "_enode", "type": "string"},
            ],
            "name": "updateEnode",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "address payable",
                            "name": "treasury",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "nodeAddress",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "oracleAddress",
                            "type": "address",
                        },
                        {"internalType": "string", "name": "enode", "type": "string"},
                        {
                            "internalType": "uint256",
                            "name": "commissionRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfBondedStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStake",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingShares",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "selfUnbondingStakeLocked",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract Liquid",
                            "name": "liquidContract",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "registrationBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSlashed",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "jailReleaseBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "provableFaultCount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                        {
                            "internalType": "enum ValidatorState",
                            "name": "state",
                            "type": "uint8",
                        },
                    ],
                    "internalType": "struct Autonity.Validator",
                    "name": "_val",
                    "type": "tuple",
                }
            ],
            "name": "updateValidatorAndTransferSlashedFunds",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes", "name": "_bytecode", "type": "bytes"},
                {"internalType": "string", "name": "_abi", "type": "string"},
            ],
            "name": "upgradeContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ],
)
