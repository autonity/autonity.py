"""InflationController contract binding and data structures."""

# This module has been generated using pyabigen v0.2.15

import typing
from dataclasses import dataclass

import eth_typing
import web3
from web3.contract import contract


@dataclass
class Params:
    """Port of `struct Params` on the InflationController contract."""

    inflation_rate_initial: int
    inflation_rate_transition: int
    inflation_curve_convexity: int
    inflation_transition_period: int
    inflation_reserve_decay_rate: int


class InflationController:
    """InflationController contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed InflationController contract.
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

    def calculate_supply_delta(
        self,
        _current_supply: int,
        _inflation_reserve: int,
        _last_epoch_time: int,
        _current_epoch_time: int,
    ) -> int:
        """Binding for `calculateSupplyDelta` on the InflationController contract.

        Main function. Calculate NTN inflation.

        Parameters
        ----------
        _current_supply : int
        _inflation_reserve : int
        _last_epoch_time : int
        _current_epoch_time : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.calculateSupplyDelta(
            _current_supply,
            _inflation_reserve,
            _last_epoch_time,
            _current_epoch_time,
        ).call()
        return int(return_value)

    def get_params(
        self,
    ) -> Params:
        """Binding for `getParams` on the InflationController contract.

        Returns
        -------
        Params
            the current parameters of the inflation controller
        """
        return_value = self._contract.functions.getParams().call()
        return Params(
            int(return_value[0]),
            int(return_value[1]),
            int(return_value[2]),
            int(return_value[3]),
            int(return_value[4]),
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "SD59x18",
                            "name": "inflationRateInitial",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationRateTransition",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationCurveConvexity",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationTransitionPeriod",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationReserveDecayRate",
                            "type": "int256",
                        },
                    ],
                    "internalType": "struct InflationController.Params",
                    "name": "_params",
                    "type": "tuple",
                }
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
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
            "inputs": [{"internalType": "int256", "name": "x", "type": "int256"}],
            "name": "PRBMath_SD59x18_Convert_Overflow",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "int256", "name": "x", "type": "int256"}],
            "name": "PRBMath_SD59x18_Convert_Underflow",
            "type": "error",
        },
        {"inputs": [], "name": "PRBMath_SD59x18_Div_InputTooSmall", "type": "error"},
        {
            "inputs": [
                {"internalType": "SD59x18", "name": "x", "type": "int256"},
                {"internalType": "SD59x18", "name": "y", "type": "int256"},
            ],
            "name": "PRBMath_SD59x18_Div_Overflow",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "SD59x18", "name": "x", "type": "int256"}],
            "name": "PRBMath_SD59x18_Exp2_InputTooBig",
            "type": "error",
        },
        {
            "inputs": [{"internalType": "SD59x18", "name": "x", "type": "int256"}],
            "name": "PRBMath_SD59x18_Exp_InputTooBig",
            "type": "error",
        },
        {"inputs": [], "name": "PRBMath_SD59x18_Mul_InputTooSmall", "type": "error"},
        {
            "inputs": [
                {"internalType": "SD59x18", "name": "x", "type": "int256"},
                {"internalType": "SD59x18", "name": "y", "type": "int256"},
            ],
            "name": "PRBMath_SD59x18_Mul_Overflow",
            "type": "error",
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_currentSupply",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "_inflationReserve",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "_lastEpochTime",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "_currentEpochTime",
                    "type": "uint256",
                },
            ],
            "name": "calculateSupplyDelta",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getParams",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "SD59x18",
                            "name": "inflationRateInitial",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationRateTransition",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationCurveConvexity",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationTransitionPeriod",
                            "type": "int256",
                        },
                        {
                            "internalType": "SD59x18",
                            "name": "inflationReserveDecayRate",
                            "type": "int256",
                        },
                    ],
                    "internalType": "struct InflationController.Params",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
