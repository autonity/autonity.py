"""Autonity contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import enum
import typing
from dataclasses import dataclass

import eth_typing
import hexbytes
import web3
from web3.contract import contract

__version__ = "v1.1.2"


class ValidatorState(enum.IntEnum):
    """Port of `enum ValidatorState` on the IAutonity contract."""

    ACTIVE = 0
    PAUSED = 1
    JAILED = 2
    JAILBOUND = 3
    JAILED_FOR_INACTIVITY = 4
    JAILBOUND_FOR_INACTIVITY = 5


@dataclass
class Validator:
    """Port of `struct Validator` on the IAutonity contract."""

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
    liquid_state_contract: eth_typing.ChecksumAddress
    liquid_supply: int
    registration_block: int
    total_slashed: int
    jail_release_block: int
    consensus_key: hexbytes.HexBytes
    state: ValidatorState
    conversion_ratio: int


@dataclass
class Policy:
    """Port of `struct Policy` on the IAutonity contract."""

    treasury_fee: int
    min_base_fee: int
    delegation_rate: int
    unbonding_period: int
    initial_inflation_reserve: int
    withholding_threshold: int
    proposer_reward_rate: int
    oracle_reward_rate: int
    withheld_rewards_pool: eth_typing.ChecksumAddress
    treasury_account: eth_typing.ChecksumAddress
    base_fee_change_denominator: int
    elasticity_multiplier: int


@dataclass
class Contracts:
    """Port of `struct Contracts` on the IAutonity contract."""

    accountability_contract: eth_typing.ChecksumAddress
    oracle_contract: eth_typing.ChecksumAddress
    acu_contract: eth_typing.ChecksumAddress
    supply_control_contract: eth_typing.ChecksumAddress
    stabilization_contract: eth_typing.ChecksumAddress
    upgrade_manager_contract: eth_typing.ChecksumAddress
    inflation_controller_contract: eth_typing.ChecksumAddress
    omission_accountability_contract: eth_typing.ChecksumAddress
    auctioneer_contract: eth_typing.ChecksumAddress


@dataclass
class Protocol:
    """Port of `struct Protocol` on the IAutonity contract."""

    operator_account: eth_typing.ChecksumAddress
    epoch_period: int
    block_period: int
    committee_size: int
    max_schedule_duration: int
    gas_limit: int
    gas_limit_bound_divisor: int
    clustering_threshold: int


@dataclass
class Config:
    """Port of `struct Config` on the IAutonity contract."""

    policy: Policy
    contracts: Contracts
    protocol: Protocol
    contract_version: int


@dataclass
class BondingRequest:
    """Port of `struct BondingRequest` on the IAutonity contract."""

    delegator: eth_typing.ChecksumAddress
    delegatee: eth_typing.ChecksumAddress
    amount: int
    request_block: int


@dataclass
class Accountability:
    """Port of `struct Accountability` on the IAutonity contract."""

    range: int
    delta: int
    grace_period: int


@dataclass
class Eip1559:
    """Port of `struct Eip1559` on the IAutonity contract."""

    min_base_fee: int
    base_fee_change_denominator: int
    elasticity_multiplier: int
    gas_limit_bound_divisor: int


@dataclass
class ClientAwareConfig:
    """Port of `struct ClientAwareConfig` on the IAutonity contract."""

    epoch_period: int
    block_period: int
    gas_limit: int
    clustering_threshold: int
    accountability: Accountability
    eip1559: Eip1559


@dataclass
class CommitteeMember:
    """Port of `struct CommitteeMember` on the IAutonity contract."""

    addr: eth_typing.ChecksumAddress
    voting_power: int
    consensus_key: hexbytes.HexBytes


@dataclass
class EpochInfo:
    """Port of `struct EpochInfo` on the IAutonity contract."""

    committee: typing.List[CommitteeMember]
    previous_epoch_block: int
    epoch_block: int
    next_epoch_block: int
    omission_delta: int
    eip1559: Eip1559


@dataclass
class Schedule:
    """Port of `struct Schedule` on the IScheduleController contract."""

    total_amount: int
    unlocked_amount: int
    start: int
    total_duration: int
    last_unlock_time: int


@dataclass
class UnbondingRequest:
    """Port of `struct UnbondingRequest` on the IAutonity contract."""

    delegator: eth_typing.ChecksumAddress
    delegatee: eth_typing.ChecksumAddress
    amount: int
    unbonding_share: int
    request_block: int
    unlocked: bool
    released: bool
    self_delegation: bool


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
    def ActivatedValidator(self) -> contract.ContractEvent:
        """Binding for `event ActivatedValidator` on the Autonity contract.

        emitted when a validator is activated, validator starts accepting delegation and
        becomes eligible  for committee inclusion
        """
        return self._contract.events.ActivatedValidator

    @property
    def Approval(self) -> contract.ContractEvent:
        """Binding for `event Approval` on the Autonity contract."""
        return self._contract.events.Approval

    @property
    def BondingApproval(self) -> contract.ContractEvent:
        """Binding for `event BondingApproval` on the Autonity contract.

        Emitted when the bonding-allowance (NTN) of a `_caller` for an `_owner` is set
        by a call to `approveBonding`. `_value` is the new `bondingAllowance` (NTN).
        """
        return self._contract.events.BondingApproval

    @property
    def BondingRejected(self) -> contract.ContractEvent:
        """Binding for `event BondingRejected` on the Autonity contract.

        This event is emitted when a registered bonding request to a validator is
        rejected
        """
        return self._contract.events.BondingRejected

    @property
    def BurnedStake(self) -> contract.ContractEvent:
        """Binding for `event BurnedStake` on the Autonity contract."""
        return self._contract.events.BurnedStake

    @property
    def CallFailed(self) -> contract.ContractEvent:
        """Binding for `event CallFailed` on the Autonity contract.

        This event is emitted when a call to an address fails in a protocol function
        (like finalize()).
        """
        return self._contract.events.CallFailed

    @property
    def CommissionRateChange(self) -> contract.ContractEvent:
        """Binding for `event CommissionRateChange` on the Autonity contract.

        Emitted after registering a commission rate change request has been submitted
        for the validator
        """
        return self._contract.events.CommissionRateChange

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the Autonity contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the Autonity contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateInt(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateInt` on the Autonity contract.

        Emitted after updating config parameter of type int
        """
        return self._contract.events.ConfigUpdateInt

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the Autonity contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def Eip1559ParamsUpdate(self) -> contract.ContractEvent:
        """Binding for `event Eip1559ParamsUpdate` on the Autonity contract.

        Event emitted after EIP-1559 parameters are updated
        """
        return self._contract.events.Eip1559ParamsUpdate

    @property
    def EnodeUpdate(self) -> contract.ContractEvent:
        """Binding for `event EnodeUpdate` on the Autonity contract.

        Emitted after updating a enode address of a validator
        """
        return self._contract.events.EnodeUpdate

    @property
    def EpochPeriodUpdated(self) -> contract.ContractEvent:
        """Binding for `event EpochPeriodUpdated` on the Autonity contract.

        emitted when epoch period is updated
        """
        return self._contract.events.EpochPeriodUpdated

    @property
    def MintedStake(self) -> contract.ContractEvent:
        """Binding for `event MintedStake` on the Autonity contract."""
        return self._contract.events.MintedStake

    @property
    def NewBondingRequest(self) -> contract.ContractEvent:
        """Binding for `event NewBondingRequest` on the Autonity contract.

        This event is emitted when a bonding request to a validator node has been
        registered. This request will only be effective at the end of the current epoch
        however the stake will be put in custody immediately from the delegator's
        account.
        """
        return self._contract.events.NewBondingRequest

    @property
    def NewEpoch(self) -> contract.ContractEvent:
        """Binding for `event NewEpoch` on the Autonity contract.

        emitted when a newEpoch begins
        """
        return self._contract.events.NewEpoch

    @property
    def NewSchedule(self) -> contract.ContractEvent:
        """Binding for `event NewSchedule` on the Autonity contract."""
        return self._contract.events.NewSchedule

    @property
    def NewUnbondingRequest(self) -> contract.ContractEvent:
        """Binding for `event NewUnbondingRequest` on the Autonity contract.

        This event is emitted when an unbonding request to a validator node has been
        registered. This request will only be effective after the unbonding period,
        rounded to the next epoch. Please note that because of potential slashing events
        during this delay period, the released amount may or may not be correspond to
        the amount requested.
        """
        return self._contract.events.NewUnbondingRequest

    @property
    def PausedValidator(self) -> contract.ContractEvent:
        """Binding for `event PausedValidator` on the Autonity contract.

        emitted when a validator is paused, validator stops accepting delegation and
        becomes ineligible  for committee inclusion
        """
        return self._contract.events.PausedValidator

    @property
    def RegisteredValidator(self) -> contract.ContractEvent:
        """Binding for `event RegisteredValidator` on the Autonity contract.

        emitted when a new validator is registered
        """
        return self._contract.events.RegisteredValidator

    @property
    def Rewarded(self) -> contract.ContractEvent:
        """Binding for `event Rewarded` on the Autonity contract.

        emitted when a validator is rewarded for taking part in block consensus  for
        committee inclusion
        """
        return self._contract.events.Rewarded

    @property
    def Transfer(self) -> contract.ContractEvent:
        """Binding for `event Transfer` on the Autonity contract."""
        return self._contract.events.Transfer

    def standard_decimals(
        self,
    ) -> int:
        """Binding for `STANDARD_DECIMALS` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.STANDARD_DECIMALS().call()
        return int(return_value)

    def standard_scale_factor(
        self,
    ) -> int:
        """Binding for `STANDARD_SCALE_FACTOR` on the Autonity contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.STANDARD_SCALE_FACTOR().call()
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

    def approve_bonding(
        self,
        _caller: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `approveBonding` on the Autonity contract.

        Sets `_amount` as the bonding-allowance (NTN) of `_caller` over the caller's
        tokens. Returns a boolean value indicating whether the operation succeeded.
        Emits an {BondingApproval} event.

        Parameters
        ----------
        _caller : eth_typing.ChecksumAddress
        _amount : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.approveBonding(
            _caller,
            _amount,
        )

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

        Create a bonding(delegation) request with the caller as delegator.

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

    def bond_from(
        self,
        _account: eth_typing.ChecksumAddress,
        _validator: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `bondFrom` on the Autonity contract.

        Create a bonding(delegation) request with the `_account` as delegator. The
        caller needs to have required bonding-allowance (NTN) from the `_account`.

        Parameters
        ----------
        _account : eth_typing.ChecksumAddress
            address of the delegator.
        _validator : eth_typing.ChecksumAddress
            address of the validator to delegate stake to.
        _amount : int
            total amount of NTN to bond.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.bondFrom(
            _account,
            _validator,
            _amount,
        )

    def bonding_allowance(
        self,
        _owner: eth_typing.ChecksumAddress,
        _caller: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `bondingAllowance` on the Autonity contract.

        Returns the remaining number of NTN that `_caller` will be allowed to bond on
        behalf of `_owner` through `bondFrom`. This is zero by default.

        Parameters
        ----------
        _owner : eth_typing.ChecksumAddress
        _caller : eth_typing.ChecksumAddress

        Returns
        -------
        int
        """
        return_value = self._contract.functions.bondingAllowance(
            _owner,
            _caller,
        ).call()
        return int(return_value)

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

    def circulating_supply(
        self,
    ) -> int:
        """Binding for `circulatingSupply` on the Autonity contract.

        Returns the amount of tokens circulating in the network.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.circulatingSupply().call()
        return int(return_value)

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

    def create_schedule(
        self,
        _schedule_vault: eth_typing.ChecksumAddress,
        _amount: int,
        _start_time: int,
        _total_duration: int,
    ) -> contract.ContractFunction:
        """Binding for `createSchedule` on the Autonity contract.

        Creates a new schedule.

        Parameters
        ----------
        _schedule_vault : eth_typing.ChecksumAddress
        _amount : int
            total amount of the schedule
        _start_time : int
        _total_duration : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.createSchedule(
            _schedule_vault,
            _amount,
            _start_time,
            _total_duration,
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

    def get_bonding_request_by_id(
        self,
        _id: int,
    ) -> BondingRequest:
        """Binding for `getBondingRequestByID` on the Autonity contract.

        Returns the bonding request corresponding to bonding ID.

        Parameters
        ----------
        _id : int

        Returns
        -------
        BondingRequest
        """
        return_value = self._contract.functions.getBondingRequestByID(
            _id,
        ).call()
        return BondingRequest(
            eth_typing.ChecksumAddress(return_value[0]),
            eth_typing.ChecksumAddress(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
        )

    def get_client_config(
        self,
    ) -> ClientAwareConfig:
        """Binding for `getClientConfig` on the Autonity contract.

        Returns the current client aware config

        Returns
        -------
        ClientAwareConfig
        """
        return_value = self._contract.functions.getClientConfig().call()
        return ClientAwareConfig(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            Accountability(
                int(return_value[4][0]),
                int(return_value[4][1]),
                int(return_value[4][2]),
            ),
            Eip1559(
                int(return_value[5][0]),
                int(return_value[5][1]),
                int(return_value[5][2]),
                int(return_value[5][3]),
            ),
        )

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
                eth_typing.ChecksumAddress(return_value_elem[0]),
                int(return_value_elem[1]),
                hexbytes.HexBytes(return_value_elem[2]),
            )
            for return_value_elem in return_value
        ]

    def get_committee_enodes(
        self,
    ) -> typing.List[str]:
        """Binding for `getCommitteeEnodes` on the Autonity contract.

        Returns the consensus committee enodes.

        Returns
        -------
        typing.List[str]
        """
        return_value = self._contract.functions.getCommitteeEnodes().call()
        return [str(return_value_elem) for return_value_elem in return_value]

    def get_config(
        self,
    ) -> Config:
        """Binding for `getConfig` on the Autonity contract.

        Returns the current contract config

        Returns
        -------
        Config
        """
        return_value = self._contract.functions.getConfig().call()
        return Config(
            Policy(
                int(return_value[0][0]),
                int(return_value[0][1]),
                int(return_value[0][2]),
                int(return_value[0][3]),
                int(return_value[0][4]),
                int(return_value[0][5]),
                int(return_value[0][6]),
                int(return_value[0][7]),
                eth_typing.ChecksumAddress(return_value[0][8]),
                eth_typing.ChecksumAddress(return_value[0][9]),
                int(return_value[0][10]),
                int(return_value[0][11]),
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
                eth_typing.ChecksumAddress(return_value[1][8]),
            ),
            Protocol(
                eth_typing.ChecksumAddress(return_value[2][0]),
                int(return_value[2][1]),
                int(return_value[2][2]),
                int(return_value[2][3]),
                int(return_value[2][4]),
                int(return_value[2][5]),
                int(return_value[2][6]),
                int(return_value[2][7]),
            ),
            int(return_value[3]),
        )

    def get_current_committee_size(
        self,
    ) -> int:
        """Binding for `getCurrentCommitteeSize` on the Autonity contract.

        Returns the current size of the consensus committee.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getCurrentCommitteeSize().call()
        return int(return_value)

    def get_current_epoch_period(
        self,
    ) -> int:
        """Binding for `getCurrentEpochPeriod` on the Autonity contract.

        Returns the epoch period of the current epoch

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getCurrentEpochPeriod().call()
        return int(return_value)

    def get_epoch_by_height(
        self,
        _height: int,
    ) -> EpochInfo:
        """Binding for `getEpochByHeight` on the Autonity contract.

        Returns the epoch info of the height.

        Parameters
        ----------
        _height : int

        Returns
        -------
        EpochInfo
        """
        return_value = self._contract.functions.getEpochByHeight(
            _height,
        ).call()
        return EpochInfo(
            [
                CommitteeMember(
                    eth_typing.ChecksumAddress(return_value0_elem[0]),
                    int(return_value0_elem[1]),
                    hexbytes.HexBytes(return_value0_elem[2]),
                )
                for return_value0_elem in return_value[0]
            ],
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            Eip1559(
                int(return_value[5][0]),
                int(return_value[5][1]),
                int(return_value[5][2]),
                int(return_value[5][3]),
            ),
        )

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

    def get_epoch_id(
        self,
    ) -> int:
        """Binding for `getEpochID` on the Autonity contract.

        Returns the current epoch ID

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getEpochID().call()
        return int(return_value)

    def get_epoch_info(
        self,
    ) -> EpochInfo:
        """Binding for `getEpochInfo` on the Autonity contract.

        Returns the current epoch info of the chain.

        Returns
        -------
        EpochInfo
        """
        return_value = self._contract.functions.getEpochInfo().call()
        return EpochInfo(
            [
                CommitteeMember(
                    eth_typing.ChecksumAddress(return_value0_elem[0]),
                    int(return_value0_elem[1]),
                    hexbytes.HexBytes(return_value0_elem[2]),
                )
                for return_value0_elem in return_value[0]
            ],
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            Eip1559(
                int(return_value[5][0]),
                int(return_value[5][1]),
                int(return_value[5][2]),
                int(return_value[5][3]),
            ),
        )

    def get_epoch_period(
        self,
    ) -> int:
        """Binding for `getEpochPeriod` on the Autonity contract.

        Returns the epoch period. If there will be an update at epoch end, the new epoch
        period is returned

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getEpochPeriod().call()
        return int(return_value)

    def get_epoch_total_bonded_stake(
        self,
    ) -> int:
        """Binding for `getEpochTotalBondedStake` on the Autonity contract.

        Returns the current epoch total bonded stake

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getEpochTotalBondedStake().call()
        return int(return_value)

    def get_inflation_reserve(
        self,
    ) -> int:
        """Binding for `getInflationReserve` on the Autonity contract.

        Returns the current inflation reserve

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getInflationReserve().call()
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

    def get_last_epoch_time(
        self,
    ) -> int:
        """Binding for `getLastEpochTime` on the Autonity contract.

        Returns the last epoch's end block timestamp

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getLastEpochTime().call()
        return int(return_value)

    def get_liquid_logic_contract(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getLiquidLogicContract` on the Autonity contract.

        Returns the liquid logic contract

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getLiquidLogicContract().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_max_committee_size(
        self,
    ) -> int:
        """Binding for `getMaxCommitteeSize` on the Autonity contract.

        Returns the maximum size of the consensus committee.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getMaxCommitteeSize().call()
        return int(return_value)

    def get_max_schedule_duration(
        self,
    ) -> int:
        """Binding for `getMaxScheduleDuration` on the Autonity contract.

        Returns the max allowed duration of any schedule or contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getMaxScheduleDuration().call()
        return int(return_value)

    def get_minimum_base_fee(
        self,
    ) -> int:
        """Binding for `getMinimumBaseFee` on the Autonity contract.

        Returns the minimum gas price.

        Returns
        -------
        int
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

    def get_next_epoch_block(
        self,
    ) -> int:
        """Binding for `getNextEpochBlock` on the Autonity contract.

        Returns the next epoch block.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getNextEpochBlock().call()
        return int(return_value)

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

    def get_schedule(
        self,
        _vault: eth_typing.ChecksumAddress,
        _id: int,
    ) -> Schedule:
        """Binding for `getSchedule` on the Autonity contract.

        Returns the schedule at index = `_id` in the `vaultSchedules[_vault]` array.

        Parameters
        ----------
        _vault : eth_typing.ChecksumAddress
            address of the vault for the schedule
        _id : int
            index of the schedule

        Returns
        -------
        Schedule
        """
        return_value = self._contract.functions.getSchedule(
            _vault,
            _id,
        ).call()
        return Schedule(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
        )

    def get_slasher(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getSlasher` on the Autonity contract.

        Returns the slasher contract address

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getSlasher().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_total_schedules(
        self,
        _vault: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `getTotalSchedules` on the Autonity contract.

        Returns total number of schedules for the vault at address `_vault`.

        Parameters
        ----------
        _vault : eth_typing.ChecksumAddress
            address of the vault for the schedules

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getTotalSchedules(
            _vault,
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

    def get_unbonding_request_by_id(
        self,
        _id: int,
    ) -> UnbondingRequest:
        """Binding for `getUnbondingRequestByID` on the Autonity contract.

        Returns the unbonding request corresponding to unbonding ID.

        Parameters
        ----------
        _id : int

        Returns
        -------
        UnbondingRequest
        """
        return_value = self._contract.functions.getUnbondingRequestByID(
            _id,
        ).call()
        return UnbondingRequest(
            eth_typing.ChecksumAddress(return_value[0]),
            eth_typing.ChecksumAddress(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            bool(return_value[5]),
            bool(return_value[6]),
            bool(return_value[7]),
        )

    def get_unbonding_share(
        self,
        _unbonding_id: int,
    ) -> int:
        """Binding for `getUnbondingShare` on the Autonity contract.

        Returns the unbonding share after the unbonding request is applied at epoch end.

        Parameters
        ----------
        _unbonding_id : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getUnbondingShare(
            _unbonding_id,
        ).call()
        return int(return_value)

    def get_validator(
        self,
        _addr: eth_typing.ChecksumAddress,
    ) -> Validator:
        """Binding for `getValidator` on the Autonity contract.

        Returns the validator object associated with `_addr`.

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress

        Returns
        -------
        Validator
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
            hexbytes.HexBytes(return_value[17]),
            ValidatorState(return_value[18]),
            int(return_value[19]),
        )

    def get_validator_state(
        self,
        _addr: eth_typing.ChecksumAddress,
    ) -> ValidatorState:
        """Binding for `getValidatorState` on the Autonity contract.

        Returns the state of the validator associated with `_addr`.

        Parameters
        ----------
        _addr : eth_typing.ChecksumAddress

        Returns
        -------
        ValidatorState
        """
        return_value = self._contract.functions.getValidatorState(
            _addr,
        ).call()
        return ValidatorState(return_value)

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
        return [
            eth_typing.ChecksumAddress(return_value_elem)
            for return_value_elem in return_value
        ]

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

    def is_unbonding_released(
        self,
        _unbonding_id: int,
    ) -> bool:
        """Binding for `isUnbondingReleased` on the Autonity contract.

        Returns `true` if unbonding is released and `false` otherwise.

        Parameters
        ----------
        _unbonding_id : int

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.isUnbondingReleased(
            _unbonding_id,
        ).call()
        return bool(return_value)

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

    def set_auctioneer_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setAuctioneerContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setAuctioneerContract(
            _address,
        )

    def set_clustering_threshold(
        self,
        _threshold: int,
    ) -> contract.ContractFunction:
        """Binding for `setClusteringThreshold` on the Autonity contract.

        Parameters
        ----------
        _threshold : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setClusteringThreshold(
            _threshold,
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

    def set_eip1559_params(
        self,
        _params: Eip1559,
    ) -> contract.ContractFunction:
        """Binding for `setEip1559Params` on the Autonity contract.

        Set the eip1559 parameters for the next epoch. Restricted to the operator
        account.

        Parameters
        ----------
        _params : Eip1559
            , eip1559 parameters: minBaseFee, gasLimitBoundDivisor, elasticityMultiplier
            and baseFeeChangeDenominator

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setEip1559Params(
            (
                _params.min_base_fee,
                _params.base_fee_change_denominator,
                _params.elasticity_multiplier,
                _params.gas_limit_bound_divisor,
            ),
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

    def set_gas_limit(
        self,
        _gas_limit: int,
    ) -> contract.ContractFunction:
        """Binding for `setGasLimit` on the Autonity contract.

        Sets the gas limit. Restricted to the operator account.

        Parameters
        ----------
        _gas_limit : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setGasLimit(
            _gas_limit,
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

    def set_liquid_logic_contract(
        self,
        _contract: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setLiquidLogicContract` on the Autonity contract.

        Set address of the liquid logic contact.

        Parameters
        ----------
        _contract : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setLiquidLogicContract(
            _contract,
        )

    def set_max_schedule_duration(
        self,
        _new_max_duration: int,
    ) -> contract.ContractFunction:
        """Binding for `setMaxScheduleDuration` on the Autonity contract.

        Sets the max allowed duration of any schedule or contract.

        Parameters
        ----------
        _new_max_duration : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMaxScheduleDuration(
            _new_max_duration,
        )

    def set_omission_accountability_contract(
        self,
        _address: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setOmissionAccountabilityContract` on the Autonity contract.

        Parameters
        ----------
        _address : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setOmissionAccountabilityContract(
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

    def set_oracle_reward_rate(
        self,
        _oracle_reward_rate: int,
    ) -> contract.ContractFunction:
        """Binding for `setOracleRewardRate` on the Autonity contract.

        Sets the oracle reward rate for the policy configuration.

        Parameters
        ----------
        _oracle_reward_rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setOracleRewardRate(
            _oracle_reward_rate,
        )

    def set_proposer_reward_rate(
        self,
        _proposer_reward_rate: int,
    ) -> contract.ContractFunction:
        """Binding for `setProposerRewardRate` on the Autonity contract.

        Sets the proposer reward rate for the policy configuration.

        Parameters
        ----------
        _proposer_reward_rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setProposerRewardRate(
            _proposer_reward_rate,
        )

    def set_slasher(
        self,
        _slasher: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setSlasher` on the Autonity contract.

        Parameters
        ----------
        _slasher : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSlasher(
            _slasher,
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

        Sets the unbonding period for the policy configuration.

        Parameters
        ----------
        _period : int
            The new unbonding period, in blocks.

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

    def set_withheld_rewards_pool(
        self,
        _pool: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setWithheldRewardsPool` on the Autonity contract.

        Sets the address of the pool to which withheld rewards will be sent.

        Parameters
        ----------
        _pool : eth_typing.ChecksumAddress
            The address of the withheld rewards pool.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setWithheldRewardsPool(
            _pool,
        )

    def set_withholding_threshold(
        self,
        _withholding_threshold: int,
    ) -> contract.ContractFunction:
        """Binding for `setWithholdingThreshold` on the Autonity contract.

        Sets the withholding threshold for the policy configuration.

        Parameters
        ----------
        _withholding_threshold : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setWithholdingThreshold(
            _withholding_threshold,
        )

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

        Create an unbonding request with the caller as delegator.

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

    def unbond_from(
        self,
        _account: eth_typing.ChecksumAddress,
        _validator: eth_typing.ChecksumAddress,
        _amount: int,
    ) -> contract.ContractFunction:
        """Binding for `unbondFrom` on the Autonity contract.

        Create an unbonding request with the `_account` as delegator. The caller needs
        to have required unbonding-allowance to unbond LNTN from the `_account`.

        Parameters
        ----------
        _account : eth_typing.ChecksumAddress
            address of the delegator.
        _validator : eth_typing.ChecksumAddress
            address of the validator to unbond stake to.
        _amount : int
            total amount of LNTN (or NTN if self delegated) to unbond.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.unbondFrom(
            _account,
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
                            "internalType": "contract ILiquid",
                            "name": "liquidStateContract",
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
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                        {
                            "internalType": "enum IAutonity.ValidatorState",
                            "name": "state",
                            "type": "uint8",
                        },
                        {
                            "internalType": "uint256",
                            "name": "conversionRatio",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.Validator[]",
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
                                    "internalType": "uint256",
                                    "name": "withholdingThreshold",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "proposerRewardRate",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "oracleRewardRate",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "address payable",
                                    "name": "withheldRewardsPool",
                                    "type": "address",
                                },
                                {
                                    "internalType": "address payable",
                                    "name": "treasuryAccount",
                                    "type": "address",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "baseFeeChangeDenominator",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "elasticityMultiplier",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Policy",
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
                                    "internalType": "contract IUpgradeManager",
                                    "name": "upgradeManagerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IInflationController",
                                    "name": "inflationControllerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IOmissionAccountability",
                                    "name": "omissionAccountabilityContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IAuctioneer",
                                    "name": "auctioneerContract",
                                    "type": "address",
                                },
                            ],
                            "internalType": "struct IAutonity.Contracts",
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
                                {
                                    "internalType": "uint256",
                                    "name": "maxScheduleDuration",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimit",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimitBoundDivisor",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "clusteringThreshold",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Protocol",
                            "name": "protocol",
                            "type": "tuple",
                        },
                        {
                            "internalType": "uint256",
                            "name": "contractVersion",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.Config",
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
                    "name": "_owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "_caller",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_value",
                    "type": "uint256",
                },
            ],
            "name": "BondingApproval",
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
                    "internalType": "enum IAutonity.ValidatorState",
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
                    "indexed": False,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "methodSignature",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "bytes",
                    "name": "returnData",
                    "type": "bytes",
                },
            ],
            "name": "CallFailed",
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
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "oldValue",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "newValue",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateAddress",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "oldValue",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "newValue",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateBool",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "oldValue",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "newValue",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateInt",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "name",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "oldValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newValue",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliesAtHeight",
                    "type": "uint256",
                },
            ],
            "name": "ConfigUpdateUint",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minBaseFee",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseFeeChangeDenominator",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "elasticityMultiplier",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "gasLimitBoundDivisor",
                            "type": "uint256",
                        },
                    ],
                    "indexed": False,
                    "internalType": "struct IAutonity.Eip1559",
                    "name": "oldParams",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minBaseFee",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseFeeChangeDenominator",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "elasticityMultiplier",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "gasLimitBoundDivisor",
                            "type": "uint256",
                        },
                    ],
                    "indexed": False,
                    "internalType": "struct IAutonity.Eip1559",
                    "name": "newParams",
                    "type": "tuple",
                },
            ],
            "name": "Eip1559ParamsUpdate",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "validator",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "oldEnode",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "newEnode",
                    "type": "string",
                },
            ],
            "name": "EnodeUpdate",
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
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "appliedAtBlock",
                    "type": "uint256",
                },
            ],
            "name": "EpochPeriodUpdated",
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
                    "indexed": True,
                    "internalType": "address",
                    "name": "caller",
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
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "headBondingID",
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
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "inflationReserve",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "stakeCirculating",
                    "type": "uint256",
                },
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
                    "name": "scheduleVault",
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
                    "internalType": "uint256",
                    "name": "start",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "totalDuration",
                    "type": "uint256",
                },
            ],
            "name": "NewSchedule",
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
                    "indexed": True,
                    "internalType": "address",
                    "name": "caller",
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
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "headUnbondingID",
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
                    "name": "liquidStateContract",
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
                    "name": "addr",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "atnSelfAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "atnDelegatedAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "ntnSelfAmount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "ntnDelegatedAmount",
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
        {"stateMutability": "payable", "type": "fallback"},
        {
            "inputs": [],
            "name": "STANDARD_DECIMALS",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "STANDARD_SCALE_FACTOR",
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
            "inputs": [
                {"internalType": "address", "name": "_caller", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approveBonding",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_selfBond", "type": "uint256"},
                {"internalType": "uint256", "name": "_delegated", "type": "uint256"},
            ],
            "name": "autobond",
            "outputs": [],
            "stateMutability": "nonpayable",
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
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "bondFrom",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_owner", "type": "address"},
                {"internalType": "address", "name": "_caller", "type": "address"},
            ],
            "name": "bondingAllowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
            "name": "circulatingSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_scheduleVault",
                    "type": "address",
                },
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
                {"internalType": "uint256", "name": "_startTime", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "_totalDuration",
                    "type": "uint256",
                },
            ],
            "name": "createSchedule",
            "outputs": [],
            "stateMutability": "nonpayable",
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
            "name": "finalize",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "bool",
                            "name": "contractUpgradeReady",
                            "type": "bool",
                        },
                        {"internalType": "bool", "name": "epochEnded", "type": "bool"},
                        {
                            "components": [
                                {
                                    "components": [
                                        {
                                            "internalType": "address",
                                            "name": "addr",
                                            "type": "address",
                                        },
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
                                    "internalType": "struct IAutonity.CommitteeMember[]",
                                    "name": "committee",
                                    "type": "tuple[]",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "previousEpochBlock",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "epochBlock",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "nextEpochBlock",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "omissionDelta",
                                    "type": "uint256",
                                },
                                {
                                    "components": [
                                        {
                                            "internalType": "uint256",
                                            "name": "minBaseFee",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "baseFeeChangeDenominator",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "elasticityMultiplier",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "gasLimitBoundDivisor",
                                            "type": "uint256",
                                        },
                                    ],
                                    "internalType": "struct IAutonity.Eip1559",
                                    "name": "eip1559",
                                    "type": "tuple",
                                },
                            ],
                            "internalType": "struct IAutonity.EpochInfo",
                            "name": "epoch",
                            "type": "tuple",
                        },
                        {
                            "components": [
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
                                    "name": "gasLimit",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "clusteringThreshold",
                                    "type": "uint256",
                                },
                                {
                                    "components": [
                                        {
                                            "internalType": "uint256",
                                            "name": "range",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "delta",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "gracePeriod",
                                            "type": "uint256",
                                        },
                                    ],
                                    "internalType": "struct IAutonity.Accountability",
                                    "name": "accountability",
                                    "type": "tuple",
                                },
                                {
                                    "components": [
                                        {
                                            "internalType": "uint256",
                                            "name": "minBaseFee",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "baseFeeChangeDenominator",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "elasticityMultiplier",
                                            "type": "uint256",
                                        },
                                        {
                                            "internalType": "uint256",
                                            "name": "gasLimitBoundDivisor",
                                            "type": "uint256",
                                        },
                                    ],
                                    "internalType": "struct IAutonity.Eip1559",
                                    "name": "eip1559",
                                    "type": "tuple",
                                },
                            ],
                            "internalType": "struct IAutonity.ClientAwareConfig",
                            "name": "config",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Autonity.FinalizeResult",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_omissionDelta", "type": "uint256"}
            ],
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
            "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
            "name": "getBondingRequestByID",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address payable",
                            "name": "delegator",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "delegatee",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "requestBlock",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.BondingRequest",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getClientConfig",
            "outputs": [
                {
                    "components": [
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
                            "name": "gasLimit",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "clusteringThreshold",
                            "type": "uint256",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "range",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "delta",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gracePeriod",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Accountability",
                            "name": "accountability",
                            "type": "tuple",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "minBaseFee",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "baseFeeChangeDenominator",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "elasticityMultiplier",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimitBoundDivisor",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Eip1559",
                            "name": "eip1559",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IAutonity.ClientAwareConfig",
                    "name": "",
                    "type": "tuple",
                }
            ],
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
                    "internalType": "struct IAutonity.CommitteeMember[]",
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
            "inputs": [],
            "name": "getConfig",
            "outputs": [
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
                                    "internalType": "uint256",
                                    "name": "withholdingThreshold",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "proposerRewardRate",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "oracleRewardRate",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "address payable",
                                    "name": "withheldRewardsPool",
                                    "type": "address",
                                },
                                {
                                    "internalType": "address payable",
                                    "name": "treasuryAccount",
                                    "type": "address",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "baseFeeChangeDenominator",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "elasticityMultiplier",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Policy",
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
                                    "internalType": "contract IUpgradeManager",
                                    "name": "upgradeManagerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IInflationController",
                                    "name": "inflationControllerContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IOmissionAccountability",
                                    "name": "omissionAccountabilityContract",
                                    "type": "address",
                                },
                                {
                                    "internalType": "contract IAuctioneer",
                                    "name": "auctioneerContract",
                                    "type": "address",
                                },
                            ],
                            "internalType": "struct IAutonity.Contracts",
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
                                {
                                    "internalType": "uint256",
                                    "name": "maxScheduleDuration",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimit",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimitBoundDivisor",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "clusteringThreshold",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Protocol",
                            "name": "protocol",
                            "type": "tuple",
                        },
                        {
                            "internalType": "uint256",
                            "name": "contractVersion",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.Config",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCurrentCommitteeSize",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCurrentEpochPeriod",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_height", "type": "uint256"}
            ],
            "name": "getEpochByHeight",
            "outputs": [
                {
                    "components": [
                        {
                            "components": [
                                {
                                    "internalType": "address",
                                    "name": "addr",
                                    "type": "address",
                                },
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
                            "internalType": "struct IAutonity.CommitteeMember[]",
                            "name": "committee",
                            "type": "tuple[]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "previousEpochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "epochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "nextEpochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "omissionDelta",
                            "type": "uint256",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "minBaseFee",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "baseFeeChangeDenominator",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "elasticityMultiplier",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimitBoundDivisor",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Eip1559",
                            "name": "eip1559",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IAutonity.EpochInfo",
                    "name": "",
                    "type": "tuple",
                }
            ],
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
            "name": "getEpochID",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getEpochInfo",
            "outputs": [
                {
                    "components": [
                        {
                            "components": [
                                {
                                    "internalType": "address",
                                    "name": "addr",
                                    "type": "address",
                                },
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
                            "internalType": "struct IAutonity.CommitteeMember[]",
                            "name": "committee",
                            "type": "tuple[]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "previousEpochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "epochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "nextEpochBlock",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "omissionDelta",
                            "type": "uint256",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "uint256",
                                    "name": "minBaseFee",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "baseFeeChangeDenominator",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "elasticityMultiplier",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "gasLimitBoundDivisor",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct IAutonity.Eip1559",
                            "name": "eip1559",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IAutonity.EpochInfo",
                    "name": "",
                    "type": "tuple",
                }
            ],
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
            "name": "getEpochTotalBondedStake",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getInflationReserve",
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
            "name": "getLastEpochTime",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getLiquidLogicContract",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
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
            "name": "getMaxScheduleDuration",
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
            "name": "getNextEpochBlock",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
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
                {"internalType": "address", "name": "_vault", "type": "address"},
                {"internalType": "uint256", "name": "_id", "type": "uint256"},
            ],
            "name": "getSchedule",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "totalAmount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unlockedAmount",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "start", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "totalDuration",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lastUnlockTime",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IScheduleController.Schedule",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getSlasher",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_vault", "type": "address"}
            ],
            "name": "getTotalSchedules",
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
            "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
            "name": "getUnbondingRequestByID",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address payable",
                            "name": "delegator",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "delegatee",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "unbondingShare",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "requestBlock",
                            "type": "uint256",
                        },
                        {"internalType": "bool", "name": "unlocked", "type": "bool"},
                        {"internalType": "bool", "name": "released", "type": "bool"},
                        {
                            "internalType": "bool",
                            "name": "selfDelegation",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IAutonity.UnbondingRequest",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_unbondingID", "type": "uint256"}
            ],
            "name": "getUnbondingShare",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
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
                            "internalType": "contract ILiquid",
                            "name": "liquidStateContract",
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
                            "internalType": "bytes",
                            "name": "consensusKey",
                            "type": "bytes",
                        },
                        {
                            "internalType": "enum IAutonity.ValidatorState",
                            "name": "state",
                            "type": "uint8",
                        },
                        {
                            "internalType": "uint256",
                            "name": "conversionRatio",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.Validator",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "_addr", "type": "address"}],
            "name": "getValidatorState",
            "outputs": [
                {
                    "internalType": "enum IAutonity.ValidatorState",
                    "name": "",
                    "type": "uint8",
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
            "inputs": [
                {"internalType": "uint256", "name": "_unbondingID", "type": "uint256"}
            ],
            "name": "isUnbondingReleased",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"},
                {"internalType": "uint256", "name": "_jailtime", "type": "uint256"},
                {
                    "internalType": "enum IAutonity.ValidatorState",
                    "name": "_newJailedState",
                    "type": "uint8",
                },
            ],
            "name": "jail",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"},
                {
                    "internalType": "enum IAutonity.ValidatorState",
                    "name": "_newJailboundState",
                    "type": "uint8",
                },
            ],
            "name": "jailbound",
            "outputs": [],
            "stateMutability": "nonpayable",
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
                {"internalType": "address", "name": "_address", "type": "address"}
            ],
            "name": "setAcuContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_address", "type": "address"}
            ],
            "name": "setAuctioneerContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "_threshold", "type": "uint256"}
            ],
            "name": "setClusteringThreshold",
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
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minBaseFee",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "baseFeeChangeDenominator",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "elasticityMultiplier",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "gasLimitBoundDivisor",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IAutonity.Eip1559",
                    "name": "_params",
                    "type": "tuple",
                }
            ],
            "name": "setEip1559Params",
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
                {"internalType": "uint256", "name": "_gasLimit", "type": "uint256"}
            ],
            "name": "setGasLimit",
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
            "inputs": [
                {"internalType": "address", "name": "_contract", "type": "address"}
            ],
            "name": "setLiquidLogicContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_newMaxDuration",
                    "type": "uint256",
                }
            ],
            "name": "setMaxScheduleDuration",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IOmissionAccountability",
                    "name": "_address",
                    "type": "address",
                }
            ],
            "name": "setOmissionAccountabilityContract",
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
                    "internalType": "uint256",
                    "name": "_oracleRewardRate",
                    "type": "uint256",
                }
            ],
            "name": "setOracleRewardRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_proposerRewardRate",
                    "type": "uint256",
                }
            ],
            "name": "setProposerRewardRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_slasher", "type": "address"}
            ],
            "name": "setSlasher",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_address", "type": "address"}
            ],
            "name": "setStabilizationContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_address", "type": "address"}
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
            "inputs": [
                {"internalType": "address payable", "name": "_pool", "type": "address"}
            ],
            "name": "setWithheldRewardsPool",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_withholdingThreshold",
                    "type": "uint256",
                }
            ],
            "name": "setWithholdingThreshold",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"},
                {"internalType": "uint256", "name": "_slashingRate", "type": "uint256"},
            ],
            "name": "slash",
            "outputs": [
                {"internalType": "uint256", "name": "slashingAmount", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_nodeAddress", "type": "address"},
                {"internalType": "uint256", "name": "_slashingRate", "type": "uint256"},
                {"internalType": "uint256", "name": "_jailtime", "type": "uint256"},
                {
                    "internalType": "enum IAutonity.ValidatorState",
                    "name": "_newJailedState",
                    "type": "uint8",
                },
                {
                    "internalType": "enum IAutonity.ValidatorState",
                    "name": "_newJailboundState",
                    "type": "uint8",
                },
            ],
            "name": "slashAndJail",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "slashingAmount",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "jailReleaseBlock",
                    "type": "uint256",
                },
                {"internalType": "bool", "name": "isJailbound", "type": "bool"},
            ],
            "stateMutability": "nonpayable",
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
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_account", "type": "address"},
                {"internalType": "address", "name": "_validator", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "unbondFrom",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
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
