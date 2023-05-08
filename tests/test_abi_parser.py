"""
Tests for abi_parser.py
"""

from autonity.abi_parser import find_abi_function, parse_arguments, parse_return_value
from autonity.abi_manager import ABIManager

from web3 import Web3
from web3.types import ABI
from unittest import TestCase
from typing import Dict, cast


MOCK_ABI = cast(
    ABI,
    [
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
                        {"internalType": "address", "name": "addr", "type": "address"},
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
                            "name": "totalSlashed",
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
                            "internalType": "enum Autonity.ValidatorState",
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
        }
    ],
)

MOCK_RETURN_VALUE = (
    "0x75474aC55768fAb6fE092191eea8016b955072F5",
    "0x32F3493Ef14c28419a98Ff20dE8A033cf9e6aB97",
    "enode://d4dc137f987e17155a69b31e566494c16edafd228912483cc519a48ce85864781"
    "faccc38141cc0eb1df8cdb28b9b3ccd10e1c298bac78ac43bbe5804021c1152@34.142.71.5:30303",
    1000,
    10000000000000000000000,
    0,
    "0xf4D9599aFd90B5038b18e3B551Bc21a97ed21c37",
    10000000000000000000000,
    0,
    0,
)

MOCK_EXPECTED_PARSED_RETURN_VALUE: Dict = {
    "treasury": "0x75474aC55768fAb6fE092191eea8016b955072F5",
    "addr": "0x32F3493Ef14c28419a98Ff20dE8A033cf9e6aB97",
    "enode": "enode://d4dc137f987e17155a69b31e566494c16edafd228912483cc519a48ce85864781"
    "faccc38141cc0eb1df8cdb28b9b3ccd10e1c298bac78ac43bbe5804021c1152@34.142.71.5:30303",
    "commissionRate": 1000,
    "bondedStake": 10000000000000000000000,
    "totalSlashed": 0,
    "liquidContract": "0xf4D9599aFd90B5038b18e3B551Bc21a97ed21c37",
    "liquidSupply": 10000000000000000000000,
    "registrationBlock": 0,
    "state": 0,
}


class TestABIParser(TestCase):
    """
    Test the ABI parsing functionality.
    """

    def test_arg_encoding(self) -> None:
        """
        Test argument encoding.
        """

        abi = ABIManager.load_abi("IERC20")
        abi_function = find_abi_function(abi, "approve")
        arguments = parse_arguments(
            abi_function, ["0x2b5ad5c4795c026514f8317c7a215e218dccd6cf", "100"]
        )
        self.assertEqual(
            [
                Web3.to_checksum_address("0x2b5ad5c4795c026514f8317c7a215e218dccd6cf"),
                100,
            ],
            arguments,
        )

        # TODO: use mock ABIs to test other types

    def test_return_value_decoding(self) -> None:
        """
        Test return value decoding.
        """

        abi_function = find_abi_function(MOCK_ABI, "getValidator")
        retval = parse_return_value(abi_function, MOCK_RETURN_VALUE)
        self.assertEqual(MOCK_EXPECTED_PARSED_RETURN_VALUE, retval)

        # TODO: test more sophisticated cases
