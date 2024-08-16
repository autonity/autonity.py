# Generated by pyabigen 0.2.0

import typing

import eth_typing
import web3
from plum import dispatch
from web3.contract import contract

__version__ = "v0.14.0"

ADDRESS = typing.cast(
    eth_typing.ChecksumAddress, "0x29b2440db4A256B0c1E6d3B4CDcaA68E2440A08f"
)


class Config(typing.NamedTuple):
    """See `struct Config` on the Stabilization contract."""

    borrow_interest_rate: int
    liquidation_ratio: int
    min_collateralization_ratio: int
    min_debt_requirement: int
    target_price: int


class Stabilization:
    """Stabilization contract wrapper."""

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
    ):
        self._contract = w3.eth.contract(
            address=ADDRESS,
            abi=abi,
        )

    def scale(
        self,
    ) -> int:
        """See `SCALE` on the Stabilization contract."""
        return_value = self._contract.functions.SCALE().call()
        return int(return_value)

    def scale_factor(
        self,
    ) -> int:
        """See `SCALE_FACTOR` on the Stabilization contract."""
        return_value = self._contract.functions.SCALE_FACTOR().call()
        return int(return_value)

    def seconds_in_year(
        self,
    ) -> int:
        """See `SECONDS_IN_YEAR` on the Stabilization contract."""
        return_value = self._contract.functions.SECONDS_IN_YEAR().call()
        return int(return_value)

    def accounts(
        self,
    ) -> typing.List[eth_typing.ChecksumAddress]:
        """See `accounts` on the Stabilization contract."""
        return_value = self._contract.functions.accounts().call()
        return [eth_typing.ChecksumAddress(elem) for elem in return_value]

    def borrow(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """See `borrow` on the Stabilization contract."""
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
        """See `borrowLimit` on the Stabilization contract."""
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
        """See `cdps` on the Stabilization contract."""
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
        """See `collateralPrice` on the Stabilization contract."""
        return_value = self._contract.functions.collateralPrice().call()
        return int(return_value)

    def config(
        self,
    ) -> Config:
        """See `config` on the Stabilization contract."""
        return_value = self._contract.functions.config().call()
        return Config(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
        )

    @dispatch  # type: ignore
    def debt_amount(  # noqa: F811
        self,
        account: eth_typing.ChecksumAddress,
        timestamp: int,
    ) -> int:
        """See `debtAmount` on the Stabilization contract."""
        return_value = self._contract.functions.debtAmount(
            account,
            timestamp,
        ).call()
        return int(return_value)

    @dispatch  # type: ignore
    def debt_amount(  # noqa: F811
        self,
        account: eth_typing.ChecksumAddress,
    ) -> int:
        """See `debtAmount` on the Stabilization contract."""
        return_value = self._contract.functions.debtAmount(
            account,
        ).call()
        return int(return_value)

    def deposit(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """See `deposit` on the Stabilization contract."""
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
        """See `interestDue` on the Stabilization contract."""
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
        """See `isLiquidatable` on the Stabilization contract."""
        return_value = self._contract.functions.isLiquidatable(
            account,
        ).call()
        return bool(return_value)

    def liquidate(
        self,
        account: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """See `liquidate` on the Stabilization contract."""
        return self._contract.functions.liquidate(
            account,
        )

    def minimum_collateral(
        self,
        principal: int,
        price: int,
        mcr: int,
    ) -> int:
        """See `minimumCollateral` on the Stabilization contract."""
        return_value = self._contract.functions.minimumCollateral(
            principal,
            price,
            mcr,
        ).call()
        return int(return_value)

    def repay(
        self,
    ) -> contract.ContractFunction:
        """See `repay` on the Stabilization contract."""
        return self._contract.functions.repay()

    def set_liquidation_ratio(
        self,
        ratio: int,
    ) -> contract.ContractFunction:
        """See `setLiquidationRatio` on the Stabilization contract."""
        return self._contract.functions.setLiquidationRatio(
            ratio,
        )

    def set_min_collateralization_ratio(
        self,
        ratio: int,
    ) -> contract.ContractFunction:
        """See `setMinCollateralizationRatio` on the Stabilization contract."""
        return self._contract.functions.setMinCollateralizationRatio(
            ratio,
        )

    def set_min_debt_requirement(
        self,
        amount: int,
    ) -> contract.ContractFunction:
        """See `setMinDebtRequirement` on the Stabilization contract."""
        return self._contract.functions.setMinDebtRequirement(
            amount,
        )

    def set_supply_control(
        self,
        supply_control: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """See `setSupplyControl` on the Stabilization contract."""
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
        """See `underCollateralized` on the Stabilization contract."""
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
        """See `withdraw` on the Stabilization contract."""
        return self._contract.functions.withdraw(
            amount,
        )


abi = [
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
    {"inputs": [], "name": "InsufficientAllowance", "type": "error"},
    {"inputs": [], "name": "InsufficientCollateral", "type": "error"},
    {"inputs": [], "name": "InsufficientPayment", "type": "error"},
    {"inputs": [], "name": "InvalidAmount", "type": "error"},
    {"inputs": [], "name": "InvalidDebtPosition", "type": "error"},
    {"inputs": [], "name": "InvalidParameter", "type": "error"},
    {"inputs": [], "name": "InvalidPrice", "type": "error"},
    {"inputs": [], "name": "Liquidatable", "type": "error"},
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
    {"inputs": [], "name": "TransferFailed", "type": "error"},
    {"inputs": [], "name": "Unauthorized", "type": "error"},
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
    {"inputs": [], "name": "ZeroValue", "type": "error"},
    {
        "inputs": [],
        "name": "accounts",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
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
        "outputs": [{"internalType": "uint256", "name": "price", "type": "uint256"}],
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
            {"internalType": "uint256", "name": "liquidationRatio", "type": "uint256"},
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
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "debtAmount",
        "outputs": [{"internalType": "uint256", "name": "debt", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
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
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "isLiquidatable",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
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
        "name": "repay",
        "outputs": [],
        "stateMutability": "payable",
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
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "setMinDebtRequirement",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "operator", "type": "address"}],
        "name": "setOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "oracle", "type": "address"}],
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
            {"internalType": "uint256", "name": "liquidationRatio", "type": "uint256"},
        ],
        "name": "underCollateralized",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]