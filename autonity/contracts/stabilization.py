"""Stabilization contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract


@dataclass
class Config:
    """Port of `struct Config` on the IStabilization contract."""

    borrow_interest_rate: int
    announcement_window: int
    liquidation_ratio: int
    min_collateralization_ratio: int
    min_debt_requirement: int
    target_price: int
    default_ntnatn_price: int
    default_ntnusd_price: int
    default_acuusd_price: int


@dataclass
class CDP:
    """Port of `struct CDP` on the IStabilization contract."""

    timestamp: int
    collateral: int
    principal: int
    interest: int
    last_aggregated_interest_exponent: int


@dataclass
class LastUpdated:
    """Port of `struct LastUpdated` on the IStabilization contract."""

    borrow_interest_rate_timestamp: int
    announcement_window_timestamp: int
    liquidation_ratio_timestamp: int
    min_collateralization_ratio_timestamp: int


class Stabilization:
    """Stabilization contract binding.

    A CDP-based stabilization mechanism for the Auton.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed Stabilization contract.
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
    def AnnouncementWindowUpdateAnnounced(self) -> contract.ContractEvent:
        """Binding for `event AnnouncementWindowUpdateAnnounced` on the Stabilization contract.

        Announcement that the announcement window is going to be updated
        """
        return self._contract.events.AnnouncementWindowUpdateAnnounced

    @property
    def Borrow(self) -> contract.ContractEvent:
        """Binding for `event Borrow` on the Stabilization contract.

        Auton was borrowed from a CDP
        """
        return self._contract.events.Borrow

    @property
    def CDPRestrictionsRemoved(self) -> contract.ContractEvent:
        """Binding for `event CDPRestrictionsRemoved` on the Stabilization contract.

        Transition out of the initial CDP restrictions
        """
        return self._contract.events.CDPRestrictionsRemoved

    @property
    def ConfigUpdateAddress(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateAddress` on the Stabilization contract.

        Emitted after updating config parameter of type address
        """
        return self._contract.events.ConfigUpdateAddress

    @property
    def ConfigUpdateBool(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateBool` on the Stabilization contract.

        Emitted after updating config parameter of type boolean
        """
        return self._contract.events.ConfigUpdateBool

    @property
    def ConfigUpdateUint(self) -> contract.ContractEvent:
        """Binding for `event ConfigUpdateUint` on the Stabilization contract.

        Emitted after updating config parameter of type uint
        """
        return self._contract.events.ConfigUpdateUint

    @property
    def Deposit(self) -> contract.ContractEvent:
        """Binding for `event Deposit` on the Stabilization contract.

        Collateral Token was deposited into a CDP
        """
        return self._contract.events.Deposit

    @property
    def InterestRateUpdateAnnounced(self) -> contract.ContractEvent:
        """Binding for `event InterestRateUpdateAnnounced` on the Stabilization contract.

        It is announced that borrow interest rate is going to be updated.
        """
        return self._contract.events.InterestRateUpdateAnnounced

    @property
    def Liquidate(self) -> contract.ContractEvent:
        """Binding for `event Liquidate` on the Stabilization contract.

        A CDP was liquidated
        """
        return self._contract.events.Liquidate

    @property
    def LiquidationRatioUpdateAnnounced(self) -> contract.ContractEvent:
        """Binding for `event LiquidationRatioUpdateAnnounced` on the Stabilization contract.

        Announcement that the liquidation ratio is going to be updated
        """
        return self._contract.events.LiquidationRatioUpdateAnnounced

    @property
    def MinCollateralizationRatioUpdateAnnounced(self) -> contract.ContractEvent:
        """Binding for `event MinCollateralizationRatioUpdateAnnounced` on the Stabilization contract.

        Announcement that the min collateralization ratio is going to be updated
        """
        return self._contract.events.MinCollateralizationRatioUpdateAnnounced

    @property
    def Repay(self) -> contract.ContractEvent:
        """Binding for `event Repay` on the Stabilization contract.

        Auton debt was paid into a CDP
        """
        return self._contract.events.Repay

    @property
    def Withdraw(self) -> contract.ContractEvent:
        """Binding for `event Withdraw` on the Stabilization contract.

        Collateral Token was withdrawn from a CDP
        """
        return self._contract.events.Withdraw

    def accounts(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """Binding for `accounts` on the Stabilization contract.

        Retrieve all the accounts that have opened a CDP.

        Returns
        -------
        typing.List[eth_typing.ChecksumAddress]
            Array of CDP account addresses
        """
        return_value = self._contract.functions.accounts().call()
        return [
            eth_typing.ChecksumAddress(return_value_elem)
            for return_value_elem in return_value
        ]

    def acu_price(
        self,
    ) -> int:
        """Binding for `acuPrice` on the Stabilization contract.

        Price the ACU value in USD. Retrieves the ACU value from the ACU Contract and
        converts it to have StabilizationMath.SCALE_FACTOR precision.

        Returns
        -------
        int
            Price of ACU value
        """
        return_value = self._contract.functions.acuPrice().call()
        return int(return_value)

    def borrow(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `borrow` on the Stabilization contract.

        Borrow Auton against the CDP Collateral. The CDP must not be liquidatable, the
        `amount` must not exceed the borrow limit, the debt after borrowing must satisfy
        the minimum debt requirement.

        Parameters
        ----------
        amount : int
            Auton to borrow

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.borrow(
            amount,
        )

    def borrow_limit(
        self,
        collateral: int,
        collateral_price_acu: int,
        target_price_acu: int,
        mcr: int,
    ) -> int:
        """Binding for `borrowLimit` on the Stabilization contract.

        Parameters
        ----------
        collateral : int
        collateral_price_acu : int
        target_price_acu : int
        mcr : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.borrowLimit(
            collateral,
            collateral_price_acu,
            target_price_acu,
            mcr,
        ).call()
        return int(return_value)

    def cdps(
        self,
        owner: eth_typing.ChecksumAddress,
    ) -> CDP:
        """Binding for `cdps` on the Stabilization contract.

        Retrieve the CDP for an account address.

        Parameters
        ----------
        owner : eth_typing.ChecksumAddress
            The CDP account address

        Returns
        -------
        CDP
            The CDP object
        """
        return_value = self._contract.functions.cdps(
            owner,
        ).call()
        return CDP(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
        )

    def collateral_price(
        self,
    ) -> int:
        """Binding for `collateralPrice` on the Stabilization contract.

        Price the Collateral Token in Auton. Retrieves the Collateral Token price from
        the Oracle Contract and converts it to Auton.

        Returns
        -------
        int
            Price of Collateral Token
        """
        return_value = self._contract.functions.collateralPrice().call()
        return int(return_value)

    def collateral_price_acu(
        self,
    ) -> int:
        """Binding for `collateralPriceACU` on the Stabilization contract.

        Price the Collateral Token in ACU Retrieves the Collateral Token price from the
        Oracle Contract in USD and converts it to ACU

        Returns
        -------
        int
            price Price of Collateral Token in ACU
        """
        return_value = self._contract.functions.collateralPriceACU().call()
        return int(return_value)

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the Stabilization contract.

        Retrieve the current Stabilization configuration.

        Returns
        -------
        Config
            The Stabilization configuration
        """
        return_value = self._contract.functions.config().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
            int(return_value[5]),
            int(return_value[6]),
            int(return_value[7]),
            int(return_value[8]),
        )

    def debt_amount(
        self,
        account: eth_typing.ChecksumAddress,
    ) -> int:
        """Binding for `debtAmount` on the Stabilization contract.

        Calculate the current debt amount outstanding for a CDP.

        Parameters
        ----------
        account : eth_typing.ChecksumAddress
            The CDP account address

        Returns
        -------
        int
            The debt amount
        """
        return_value = self._contract.functions.debtAmount(
            account,
        ).call()
        return int(return_value)

    def debt_amount_at_time(
        self,
        account: eth_typing.ChecksumAddress,
        timestamp: int,
    ) -> int:
        """Binding for `debtAmountAtTime` on the Stabilization contract.

        Calculate the debt amount outstanding for a CDP at the given timestamp. The
        timestamp must be equal or later than the time of the CDP last borrow or
        repayment.

        Parameters
        ----------
        account : eth_typing.ChecksumAddress
            The CDP account address
        timestamp : int
            The timestamp to value the debt

        Returns
        -------
        int
            The debt amount
        """
        return_value = self._contract.functions.debtAmountAtTime(
            account,
            timestamp,
        ).call()
        return int(return_value)

    def deposit(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `deposit` on the Stabilization contract.

        Deposit Collateral Token using the ERC20 allowance mechanism. Before calling
        this function, the CDP owner must approve the Stabilization contract to spend
        Collateral Token on their behalf for the full amount to be deposited.

        Parameters
        ----------
        amount : int
            Units of Collateral Token to deposit (non-zero)

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.deposit(
            amount,
        )

    def get_aggregated_interest_exponent(
        self,
    ) -> int:
        """Binding for `getAggregatedInterestExponent` on the Stabilization contract.

        Get aggregated interest exponent which is the summation of all interest rate
        multiplied by their respective time window (in years).

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getAggregatedInterestExponent().call()
        return int(return_value)

    def get_announcement_window(
        self,
    ) -> int:
        """Binding for `getAnnouncementWindow` on the Stabilization contract.

        Get the announcement window in seconds.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getAnnouncementWindow().call()
        return int(return_value)

    def get_current_rate(
        self,
    ) -> int:
        """Binding for `getCurrentRate` on the Stabilization contract.

        Get the active current rate.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getCurrentRate().call()
        return int(return_value)

    def get_current_rate_active_timestamp(
        self,
    ) -> int:
        """Binding for `getCurrentRateActiveTimestamp` on the Stabilization contract.

        Get the timestamp since when the current rate is active.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getCurrentRateActiveTimestamp().call()
        return int(return_value)

    def get_pending_announcement_window_info(
        self,
    ) -> typing.Tuple[int, int]:
        """Binding for `getPendingAnnouncementWindowInfo` on the Stabilization contract.

        Get the pending announcement window and since when it will be active.

        Returns
        -------
        int
            uint256 The pending announcement window
        int
            uint256 The timestamp since the pending announcement window will be active
        """
        return_value = (
            self._contract.functions.getPendingAnnouncementWindowInfo().call()
        )
        return (
            int(return_value[0]),
            int(return_value[1]),
        )

    def get_pending_interest_rate_info(
        self,
    ) -> typing.Tuple[int, int]:
        """Binding for `getPendingInterestRateInfo` on the Stabilization contract.

        Get the pending borrow interest rate and since when it will be active.

        Returns
        -------
        int
            uint256 The pending rate
        int
            uint256 The timestamp since it will be active
        """
        return_value = self._contract.functions.getPendingInterestRateInfo().call()
        return (
            int(return_value[0]),
            int(return_value[1]),
        )

    def get_pending_liquidation_ratio_info(
        self,
    ) -> typing.Tuple[int, int]:
        """Binding for `getPendingLiquidationRatioInfo` on the Stabilization contract.

        Get the pending liquidation ratio and since when it will be active.

        Returns
        -------
        int
            uint256 The pending liquidation ratio
        int
            uint256 The timestamp since the pending liquidation ratio will be active
        """
        return_value = self._contract.functions.getPendingLiquidationRatioInfo().call()
        return (
            int(return_value[0]),
            int(return_value[1]),
        )

    def get_pending_min_collateralization_ratio_info(
        self,
    ) -> typing.Tuple[int, int]:
        """Binding for `getPendingMinCollateralizationRatioInfo` on the Stabilization contract.

        Get the pending min collateralization ratio and since when it will be active.

        Returns
        -------
        int
            uint256 The pending min collateralization ratio
        int
            uint256 The timestamp since the pending min collateralization ratio will be
            active
        """
        return_value = (
            self._contract.functions.getPendingMinCollateralizationRatioInfo().call()
        )
        return (
            int(return_value[0]),
            int(return_value[1]),
        )

    def interest_due(
        self,
        debt: int,
        rate_exponent: int,
    ) -> int:
        """Binding for `interestDue` on the Stabilization contract.

        Parameters
        ----------
        debt : int
        rate_exponent : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.interestDue(
            debt,
            rate_exponent,
        ).call()
        return int(return_value)

    def interest_exponent(
        self,
        interest_rate: int,
        start_timestamp: int,
        end_timestamp: int,
    ) -> int:
        """Binding for `interestExponent` on the Stabilization contract.

        Parameters
        ----------
        interest_rate : int
        start_timestamp : int
        end_timestamp : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.interestExponent(
            interest_rate,
            start_timestamp,
            end_timestamp,
        ).call()
        return int(return_value)

    def is_liquidatable(
        self,
        account: eth_typing.ChecksumAddress,
    ) -> bool:
        """Binding for `isLiquidatable` on the Stabilization contract.

        Determine if the CDP is currently liquidatable.

        Parameters
        ----------
        account : eth_typing.ChecksumAddress
            The CDP account address

        Returns
        -------
        bool
            Whether the CDP is liquidatable
        """
        return_value = self._contract.functions.isLiquidatable(
            account,
        ).call()
        return bool(return_value)

    def last_updated(
        self,
    ) -> LastUpdated:
        """Binding for `lastUpdated` on the Stabilization contract.

        Get the last updated timestamp of the updatable config parameters

        Returns
        -------
        LastUpdated
            LastUpdated The last updated timestamps
        """
        return_value = self._contract.functions.lastUpdated().call()
        return LastUpdated(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
        )

    def liquidation_ratio(
        self,
    ) -> int:
        """Binding for `liquidationRatio` on the Stabilization contract.

        Get the liquidation ratio.

        Returns
        -------
        int
            uint256 The liquidation ratio
        """
        return_value = self._contract.functions.liquidationRatio().call()
        return int(return_value)

    def max_borrow(
        self,
        collateral: int,
    ) -> int:
        """Binding for `maxBorrow` on the Stabilization contract.

        Calculate the maximum amount that can be borrowed against the collateral. Note
        that this takes into account the minimum collateralization ratio or the max
        borrow limit, whichever is lower will determine the max borrow

        Parameters
        ----------
        collateral : int
            The amount of Collateral Token

        Returns
        -------
        int
            The maximum borrow amount
        """
        return_value = self._contract.functions.maxBorrow(
            collateral,
        ).call()
        return int(return_value)

    def min_collateralization_ratio(
        self,
    ) -> int:
        """Binding for `minCollateralizationRatio` on the Stabilization contract.

        Get the min collateralization ratio.

        Returns
        -------
        int
            uint256 The pending min collateralization ratio
        """
        return_value = self._contract.functions.minCollateralizationRatio().call()
        return int(return_value)

    def minimum_collateral(
        self,
        principal: int,
        collateral_price_acu: int,
        target_price_acu: int,
        mcr: int,
    ) -> int:
        """Binding for `minimumCollateral` on the Stabilization contract.

        Parameters
        ----------
        principal : int
        collateral_price_acu : int
        target_price_acu : int
        mcr : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.minimumCollateral(
            principal,
            collateral_price_acu,
            target_price_acu,
            mcr,
        ).call()
        return int(return_value)

    def remove_cdp_restrictions(
        self,
    ) -> contract.ContractFunction:
        """Binding for `removeCDPRestrictions` on the Stabilization contract.

        Transition out of the restricted state.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeCDPRestrictions()

    def repay(
        self,
    ) -> contract.ContractFunction:
        """Binding for `repay` on the Stabilization contract.

        Make a payment towards CDP debt. The transaction value is the payment amount.
        The debt after payment must satisfy the minimum debt requirement. The payment
        first covers the outstanding interest debt before the principal debt.

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.repay()

    def set_atn_supply_operator(
        self,
        atn_supply_operator: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setAtnSupplyOperator` on the Stabilization contract.

        Set the _atnSupplyOperator address.

        Parameters
        ----------
        atn_supply_operator : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setAtnSupplyOperator(
            atn_supply_operator,
        )

    def set_default_acuusd_price(
        self,
        default_acuusd_price: int,
    ) -> contract.ContractFunction:
        """Binding for `setDefaultACUUSDPrice` on the Stabilization contract.

        Set the default ACU-USD price for use when fixed prices are enabled.

        Parameters
        ----------
        default_acuusd_price : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setDefaultACUUSDPrice(
            default_acuusd_price,
        )

    def set_default_ntnatn_price(
        self,
        default_ntnatn_price: int,
    ) -> contract.ContractFunction:
        """Binding for `setDefaultNTNATNPrice` on the Stabilization contract.

        Set the default NTN-ATN price for use when fixed prices are enabled.

        Parameters
        ----------
        default_ntnatn_price : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setDefaultNTNATNPrice(
            default_ntnatn_price,
        )

    def set_default_ntnusd_price(
        self,
        default_ntnusd_price: int,
    ) -> contract.ContractFunction:
        """Binding for `setDefaultNTNUSDPrice` on the Stabilization contract.

        Set the default NTN-USD price for use when fixed prices are enabled.

        Parameters
        ----------
        default_ntnusd_price : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setDefaultNTNUSDPrice(
            default_ntnusd_price,
        )

    def set_min_debt_requirement(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `setMinDebtRequirement` on the Stabilization contract.

        Set the minimum debt requirement.

        Parameters
        ----------
        amount : int
            The minimum debt amount

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMinDebtRequirement(
            amount,
        )

    def under_collateralized(
        self,
        collateral: int,
        price: int,
        debt: int,
        liquidation_ratio: int,
    ) -> bool:
        """Binding for `underCollateralized` on the Stabilization contract.

        Parameters
        ----------
        collateral : int
        price : int
        debt : int
        liquidation_ratio : int

        Returns
        -------
        bool
        """
        return_value = self._contract.functions.underCollateralized(
            collateral,
            price,
            debt,
            liquidation_ratio,
        ).call()
        return bool(return_value)

    def update_announcement_window(
        self,
        window: int,
    ) -> contract.ContractFunction:
        """Binding for `updateAnnouncementWindow` on the Stabilization contract.

        Updates the announcement window. The new window `window` will take affect after
        the `config.announcementWindow` (in seconds). It requires that there is no
        announcement window in pending.

        Parameters
        ----------
        window : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.updateAnnouncementWindow(
            window,
        )

    def update_borrow_interest_rate(
        self,
        new_interest_rate: int,
    ) -> contract.ContractFunction:
        """Binding for `updateBorrowInterestRate` on the Stabilization contract.

        Updates the borrow interest rate. The new rate `newInterestRate` will take
        affect after the `config.announcementWindow` (in seconds).

        Parameters
        ----------
        new_interest_rate : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.updateBorrowInterestRate(
            new_interest_rate,
        )

    def update_ratios(
        self,
        new_liquidation_ratio: int,
        new_min_collateralization_ratio: int,
    ) -> contract.ContractFunction:
        """Binding for `updateRatios` on the Stabilization contract.

        Updates min collateralization ratio and liquidation ratio.

        Parameters
        ----------
        new_liquidation_ratio : int
        new_min_collateralization_ratio : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.updateRatios(
            new_liquidation_ratio,
            new_min_collateralization_ratio,
        )

    def use_fixed_genesis_prices(
        self,
        use_fixed: bool,
    ) -> contract.ContractFunction:
        """Binding for `useFixedGenesisPrices` on the Stabilization contract.

        Toggle the use of the fixed genesis price state.

        Parameters
        ----------
        use_fixed : bool

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.useFixedGenesisPrices(
            use_fixed,
        )

    def withdraw(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """Binding for `withdraw` on the Stabilization contract.

        Request a withdrawal of Collateral Token. The CDP must not be liquidatable and
        the withdrawal must not reduce the remaining Collateral Token amount below the
        minimum collateral amount.

        Parameters
        ----------
        amount : int
            Units of Collateral Token to withdraw

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.withdraw(
            amount,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "borrowInterestRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "announcementWindow",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidationRatio",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minCollateralizationRatio",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minDebtRequirement",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "targetPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultNTNATNPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultNTNUSDPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultACUUSDPrice",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IStabilization.Config",
                    "name": "config_",
                    "type": "tuple",
                },
                {"internalType": "address", "name": "autonity", "type": "address"},
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "address", "name": "oracle", "type": "address"},
                {"internalType": "address", "name": "supplyControl", "type": "address"},
                {"internalType": "address", "name": "auctioneer", "type": "address"},
                {"internalType": "address", "name": "acu", "type": "address"},
                {
                    "internalType": "contract IERC20",
                    "name": "collateralToken",
                    "type": "address",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {"inputs": [], "name": "AnnouncementWindowPending", "type": "error"},
        {"inputs": [], "name": "InsufficientAllowance", "type": "error"},
        {"inputs": [], "name": "InsufficientCollateral", "type": "error"},
        {"inputs": [], "name": "InsufficientPayment", "type": "error"},
        {"inputs": [], "name": "InvalidAmount", "type": "error"},
        {"inputs": [], "name": "InvalidDebtPosition", "type": "error"},
        {
            "inputs": [{"internalType": "string", "name": "message", "type": "string"}],
            "name": "InvalidParameter",
            "type": "error",
        },
        {"inputs": [], "name": "InvalidPrice", "type": "error"},
        {"inputs": [], "name": "Liquidatable", "type": "error"},
        {"inputs": [], "name": "NoDebtPosition", "type": "error"},
        {"inputs": [], "name": "NotLiquidatable", "type": "error"},
        {"inputs": [], "name": "NotRestricted", "type": "error"},
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "PRBMath_MulDiv18_Overflow",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "UD60x18", "name": "x", "type": "uint256"}],
            "name": "PRBMath_UD60x18_Exp2_InputTooBig",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "UD60x18", "name": "x", "type": "uint256"}],
            "name": "PRBMath_UD60x18_Exp_InputTooBig",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "string", "name": "symbol", "type": "string"}],
            "name": "PriceUnavailable",
            "type": "error",
        },
        {"inputs": [], "name": "TransferFailed", "type": "error"},
        {"inputs": [], "name": "Unauthorized", "type": "error"},
        {"inputs": [], "name": "ZeroValue", "type": "error"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newAnnouncementWindow",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "activeSince",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "pendingWindowOverridden",
                    "type": "bool",
                },
            ],
            "name": "AnnouncementWindowUpdateAnnounced",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "account",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Borrow",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [],
            "name": "CDPRestrictionsRemoved",
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
                    "indexed": True,
                    "internalType": "address",
                    "name": "account",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Deposit",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newRate",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "activeSince",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "pendingRateOverridden",
                    "type": "bool",
                },
            ],
            "name": "InterestRateUpdateAnnounced",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "account",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "liquidator",
                    "type": "address",
                },
            ],
            "name": "Liquidate",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newRatio",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "activeSince",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "pendingRatioOverridden",
                    "type": "bool",
                },
            ],
            "name": "LiquidationRatioUpdateAnnounced",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "newRatio",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "activeSince",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "pendingRatioOverridden",
                    "type": "bool",
                },
            ],
            "name": "MinCollateralizationRatioUpdateAnnounced",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "account",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Repay",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "account",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Withdraw",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "accounts",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "acuPrice",
            "outputs": [
                {"internalType": "uint256", "name": "price", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "borrow",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "collateral", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "collateralPriceACU",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "targetPriceACU",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "mcr", "type": "uint256"},
            ],
            "name": "borrowLimit",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "owner", "type": "address"}],
            "name": "cdps",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "timestamp",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "collateral",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "principal",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "interest",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lastAggregatedInterestExponent",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IStabilization.CDP",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "collateralPrice",
            "outputs": [
                {"internalType": "uint256", "name": "price", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "collateralPriceACU",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
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
                            "name": "borrowInterestRate",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "announcementWindow",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidationRatio",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minCollateralizationRatio",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minDebtRequirement",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "targetPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultNTNATNPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultNTNUSDPrice",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "defaultACUUSDPrice",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IStabilization.Config",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"}
            ],
            "name": "debtAmount",
            "outputs": [{"internalType": "uint256", "name": "debt", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"},
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            ],
            "name": "debtAmountAtTime",
            "outputs": [{"internalType": "uint256", "name": "debt", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "deposit",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAggregatedInterestExponent",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAnnouncementWindow",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCurrentRate",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getCurrentRateActiveTimestamp",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPendingAnnouncementWindowInfo",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPendingInterestRateInfo",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPendingLiquidationRatioInfo",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPendingMinCollateralizationRatioInfo",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "debt", "type": "uint256"},
                {"internalType": "uint256", "name": "rateExponent", "type": "uint256"},
            ],
            "name": "interestDue",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "interestRate", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "startTimestamp",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "endTimestamp", "type": "uint256"},
            ],
            "name": "interestExponent",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"}
            ],
            "name": "isLiquidatable",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastUpdated",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "borrowInterestRateTimestamp",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "announcementWindowTimestamp",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "liquidationRatioTimestamp",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minCollateralizationRatioTimestamp",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IStabilization.LastUpdated",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "collateralSold",
                    "type": "uint256",
                },
                {"internalType": "address", "name": "bidder", "type": "address"},
            ],
            "name": "liquidate",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "liquidationRatio",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "collateral", "type": "uint256"}
            ],
            "name": "maxBorrow",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "minCollateralizationRatio",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "principal", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "collateralPriceACU",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "targetPriceACU",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "mcr", "type": "uint256"},
            ],
            "name": "minimumCollateral",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "removeCDPRestrictions",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "repay",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "acu", "type": "address"}],
            "name": "setACU",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "atnSupplyOperator",
                    "type": "address",
                }
            ],
            "name": "setAtnSupplyOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "auctioneer", "type": "address"}
            ],
            "name": "setAuctioneer",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "defaultACUUSDPrice",
                    "type": "uint256",
                }
            ],
            "name": "setDefaultACUUSDPrice",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "defaultNTNATNPrice",
                    "type": "uint256",
                }
            ],
            "name": "setDefaultNTNATNPrice",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "defaultNTNUSDPrice",
                    "type": "uint256",
                }
            ],
            "name": "setDefaultNTNUSDPrice",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "setMinDebtRequirement",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "operator", "type": "address"}
            ],
            "name": "setOperator",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "oracle", "type": "address"}
            ],
            "name": "setOracle",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "supplyControl", "type": "address"}
            ],
            "name": "setSupplyControl",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "collateral", "type": "uint256"},
                {"internalType": "uint256", "name": "price", "type": "uint256"},
                {"internalType": "uint256", "name": "debt", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "liquidationRatio",
                    "type": "uint256",
                },
            ],
            "name": "underCollateralized",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "window", "type": "uint256"}
            ],
            "name": "updateAnnouncementWindow",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "newInterestRate",
                    "type": "uint256",
                }
            ],
            "name": "updateBorrowInterestRate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "newLiquidationRatio",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "newMinCollateralizationRatio",
                    "type": "uint256",
                },
            ],
            "name": "updateRatios",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "useFixed", "type": "bool"}],
            "name": "useFixedGenesisPrices",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "withdraw",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
