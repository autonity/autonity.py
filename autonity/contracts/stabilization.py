"""Stabilization contract binding and data structures."""

# This module has been generated using pyabigen v0.2.11

import typing
from dataclasses import dataclass

import eth_typing
import web3
from plum import dispatch
from web3.contract import contract

__version__ = "v1.0.2-alpha"


@dataclass
class Config:
    """Port of `struct Config` on the Stabilization contract."""

    borrow_interest_rate: int
    liquidation_ratio: int
    min_collateralization_ratio: int
    min_debt_requirement: int
    target_price: int


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
    def Borrow(self) -> contract.ContractEvent:
        """Binding for `event Borrow` on the Stabilization contract.

        Auton was borrowed from a CDP
        """
        return self._contract.events.Borrow

    @property
    def Deposit(self) -> contract.ContractEvent:
        """Binding for `event Deposit` on the Stabilization contract.

        Collateral Token was deposited into a CDP
        """
        return self._contract.events.Deposit

    @property
    def Liquidate(self) -> contract.ContractEvent:
        """Binding for `event Liquidate` on the Stabilization contract.

        A CDP was liquidated
        """
        return self._contract.events.Liquidate

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

    def scale(
        self,
    ) -> int:
        """Binding for `SCALE` on the Stabilization contract.

        The decimal places in fixed-point integer representation.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.SCALE().call()
        return int(return_value)

    def scale_factor(
        self,
    ) -> int:
        """Binding for `SCALE_FACTOR` on the Stabilization contract.

        The multiplier for scaling numbers to the required scale.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.SCALE_FACTOR().call()
        return int(return_value)

    def seconds_in_year(
        self,
    ) -> int:
        """Binding for `SECONDS_IN_YEAR` on the Stabilization contract.

        A year is assumed to have 365 days for interest rate calculations.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.SECONDS_IN_YEAR().call()
        return int(return_value)

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
        price: int,
        target_price: int,
        mcr: int,
    ) -> int:
        """Binding for `borrowLimit` on the Stabilization contract.

        Calculate the maximum amount of Amount that can be borrowed for the given amount
        of Collateral Token.

        Parameters
        ----------
        collateral : int
            Amount of Collateral Token backing the debt
        price : int
            The price of Collateral Token in Auton
        target_price : int
        mcr : int
            The minimum collateralization ratio

        Returns
        -------
        int
            The maximum Auton that can be borrowed
        """
        return_value = self._contract.functions.borrowLimit(
            collateral,
            price,
            target_price,
            mcr,
        ).call()
        return int(return_value)

    def cdps(
        self,
        key0: eth_typing.ChecksumAddress,
    ) -> typing.Tuple[int, int, int, int]:
        """Binding for `cdps` on the Stabilization contract.

        A mapping to retrieve the CDP for an account address.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress

        Returns
        -------
        int
        int
        int
        int
        """
        return_value = self._contract.functions.cdps(
            key0,
        ).call()
        return (
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
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

    def config(
        self,
    ) -> Config:
        """Binding for `config` on the Stabilization contract.

        The Config object that stores Stabilization Contract parameters.

        Returns
        -------
        Config
        """
        return_value = self._contract.functions.config().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
        )

    @dispatch  # type: ignore
    def debt_amount(  # type: ignore # noqa: F811
        self,
        account: eth_typing.ChecksumAddress,
        timestamp: int,
    ) -> int:
        """Binding for `debtAmount` on the Stabilization contract.

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
        return_value = self._contract.functions.debtAmount(
            account,
            timestamp,
        ).call()
        return int(return_value)

    @dispatch  # type: ignore
    def debt_amount(  # type: ignore # noqa: F811
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

    def interest_due(
        self,
        debt: int,
        rate: int,
        time_borrow: int,
        time_due: int,
    ) -> int:
        """Binding for `interestDue` on the Stabilization contract.

        Calculate the interest due for a given amount of debt.

        Parameters
        ----------
        debt : int
            The debt amount
        rate : int
            The borrow interest rate
        time_borrow : int
        time_due : int

        Returns
        -------
        int
            @dev Makes use of the prb-math library for natural exponentiation.
        """
        return_value = self._contract.functions.interestDue(
            debt,
            rate,
            time_borrow,
            time_due,
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

    def liquidate(
        self,
        account: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `liquidate` on the Stabilization contract.

        Liquidate a CDP that is undercollateralized. The liquidator must pay all the CDP
        debt outstanding. As a reward, the liquidator will receive the collateral that
        is held in the CDP. The transaction value is the payment amount. After covering
        the CDP's debt, any surplus is refunded to the liquidator.

        Parameters
        ----------
        account : eth_typing.ChecksumAddress
            The CDP account address to liquidate

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.liquidate(
            account,
        )

    def minimum_collateral(
        self,
        principal: int,
        price: int,
        mcr: int,
    ) -> int:
        """Binding for `minimumCollateral` on the Stabilization contract.

        Calculate the minimum amount of Collateral Token that must be deposited in the
        CDP in order to borrow the given amount of Autons.

        Parameters
        ----------
        principal : int
            Auton amount to borrow
        price : int
            The price of Collateral Token in Auton
        mcr : int
            The minimum collateralization ratio

        Returns
        -------
        int
            The minimum Collateral Token amount required
        """
        return_value = self._contract.functions.minimumCollateral(
            principal,
            price,
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

    def set_liquidation_ratio(
        self,
        ratio: int,
    ) -> contract.ContractFunction:
        """Binding for `setLiquidationRatio` on the Stabilization contract.

        Set the liquidation ratio. Must be less than the minimum collateralization
        ratio.

        Parameters
        ----------
        ratio : int
            The liquidation ratio

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setLiquidationRatio(
            ratio,
        )

    def set_min_collateralization_ratio(
        self,
        ratio: int,
    ) -> contract.ContractFunction:
        """Binding for `setMinCollateralizationRatio` on the Stabilization contract.

        Set the minimum collateralization ratio. Must be positive and greater than the
        liquidation ratio.

        Parameters
        ----------
        ratio : int
            The minimum collateralization ratio

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setMinCollateralizationRatio(
            ratio,
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

    def set_supply_control(
        self,
        supply_control: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setSupplyControl` on the Stabilization contract.

        Set the SupplyControl Contract address.

        Parameters
        ----------
        supply_control : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setSupplyControl(
            supply_control,
        )

    def under_collateralized(
        self,
        collateral: int,
        price: int,
        debt: int,
        liquidation_ratio: int,
    ) -> bool:
        """Binding for `underCollateralized` on the Stabilization contract.

        Determine if a debt position is undercollateralized.

        Parameters
        ----------
        collateral : int
            The collateral amount
        price : int
            The price of Collateral Token in Auton
        debt : int
            The debt amount
        liquidation_ratio : int

        Returns
        -------
        bool
            Whether the position is liquidatable
        """
        return_value = self._contract.functions.underCollateralized(
            collateral,
            price,
            debt,
            liquidation_ratio,
        ).call()
        return bool(return_value)

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
                    ],
                    "internalType": "struct Stabilization.Config",
                    "name": "config_",
                    "type": "tuple",
                },
                {"internalType": "address", "name": "autonity", "type": "address"},
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "address", "name": "oracle", "type": "address"},
                {"internalType": "address", "name": "supplyControl", "type": "address"},
                {
                    "internalType": "contract IERC20",
                    "name": "collateralToken",
                    "type": "address",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {"inputs": [], "name": "InsufficientAllowance", "type": "error"},
        {"inputs": [], "name": "InsufficientCollateral", "type": "error"},
        {"inputs": [], "name": "InsufficientPayment", "type": "error"},
        {"inputs": [], "name": "InvalidAmount", "type": "error"},
        {"inputs": [], "name": "InvalidDebtPosition", "type": "error"},
        {"inputs": [], "name": "InvalidParameter", "type": "error"},
        {"inputs": [], "name": "InvalidPrice", "type": "error"},
        {"inputs": [], "name": "Liquidatable", "type": "error"},
        {"inputs": [], "name": "NoDebtPosition", "type": "error"},
        {"inputs": [], "name": "NotLiquidatable", "type": "error"},
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "PRBMath_MulDiv18_Overflow",
            "type": "error",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
                {"internalType": "uint256", "name": "denominator", "type": "uint256"},
            ],
            "name": "PRBMath_MulDiv_Overflow",
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
        {"inputs": [], "name": "PriceUnavailable", "type": "error"},
        {"inputs": [], "name": "TransferFailed", "type": "error"},
        {"inputs": [], "name": "Unauthorized", "type": "error"},
        {"inputs": [], "name": "ZeroValue", "type": "error"},
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
            "name": "SCALE",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SCALE_FACTOR",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SECONDS_IN_YEAR",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "accounts",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
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
                {"internalType": "uint256", "name": "price", "type": "uint256"},
                {"internalType": "uint256", "name": "targetPrice", "type": "uint256"},
                {"internalType": "uint256", "name": "mcr", "type": "uint256"},
            ],
            "name": "borrowLimit",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "cdps",
            "outputs": [
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
                {"internalType": "uint256", "name": "collateral", "type": "uint256"},
                {"internalType": "uint256", "name": "principal", "type": "uint256"},
                {"internalType": "uint256", "name": "interest", "type": "uint256"},
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
            "name": "config",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "borrowInterestRate",
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
                {"internalType": "uint256", "name": "targetPrice", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"},
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            ],
            "name": "debtAmount",
            "outputs": [{"internalType": "uint256", "name": "debt", "type": "uint256"}],
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
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "deposit",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "debt", "type": "uint256"},
                {"internalType": "uint256", "name": "rate", "type": "uint256"},
                {"internalType": "uint256", "name": "timeBorrow", "type": "uint256"},
                {"internalType": "uint256", "name": "timeDue", "type": "uint256"},
            ],
            "name": "interestDue",
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
            "inputs": [
                {"internalType": "address", "name": "account", "type": "address"}
            ],
            "name": "liquidate",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "principal", "type": "uint256"},
                {"internalType": "uint256", "name": "price", "type": "uint256"},
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
            "inputs": [{"internalType": "uint256", "name": "ratio", "type": "uint256"}],
            "name": "setLiquidationRatio",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "ratio", "type": "uint256"}],
            "name": "setMinCollateralizationRatio",
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
                {"internalType": "uint256", "name": "amount", "type": "uint256"}
            ],
            "name": "withdraw",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
