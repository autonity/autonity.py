# mypy: ignore-errors
# This is a test file, skipping type checking in it.
"""
Tests for abi_parser.py
"""

import os
from json.decoder import JSONDecodeError
from typing import Dict, cast
from unittest import TestCase

from web3 import Web3
from web3.types import ABI

from autonity.abi_manager import load_abi_file
from autonity.abi_parser import find_abi_function, parse_arguments, parse_return_value

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

    # pylint: disable=line-too-long
    def test_arg_encoding(self) -> None:
        """
        Test argument encoding.
        """
        tests = [
            {
                "name": "OK: test for address",
                "function": "test_address",
                "inputs": ["0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"],
                "expected": [
                    Web3.to_checksum_address(
                        "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"
                    )
                ],
            },
            {
                "name": "OK: for boolean input (1)",
                "function": "test_bool",
                "inputs": ["true"],
                "expected": [True],
            },
            {
                "name": "OK: for boolean input (2)",
                "function": "test_bool",
                "inputs": ["1"],
                "expected": [True],
            },
            {
                "name": "OK: for boolean input (3)",
                "function": "test_bool",
                "inputs": ["True"],
                "expected": [True],
            },
            {
                "name": "OK: for boolean input (4)",
                "function": "test_bool",
                "inputs": ["non empty string"],
                "expected": [True],
            },
            {
                "name": "OK: for boolean input (5)",
                "function": "test_bool",
                "inputs": ["   "],
                "expected": [True],
            },  # whitespace is considered True
            {
                "name": "OK: for boolean input (6)",
                "function": "test_bool",
                "inputs": ["false"],
                "expected": [False],
            },
            {
                "name": "OK: for boolean input (7)",
                "function": "test_bool",
                "inputs": ["0"],
                "expected": [False],
            },
            {
                "name": "OK: for boolean input (8)",
                "function": "test_bool",
                "inputs": ["False"],
                "expected": [False],
            },
            {
                "name": "OK: for boolean input (9)",
                "function": "test_bool",
                "inputs": [""],
                "expected": [False],
            },
            {
                "name": "OK: for array input",
                "function": "test_array",
                "inputs": ["[1,2,3,4,5]"],
                "expected": [[1, 2, 3, 4, 5]],
            },
            {
                "name": "OK: for tuple input",
                "function": "test_tuple",
                "inputs": [
                    '["0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c","0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c",10]'
                ],
                "expected": [
                    [
                        Web3.to_checksum_address(
                            "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"
                        ),
                        Web3.to_checksum_address(
                            "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"
                        ),
                        10,
                    ]
                ],
            },
            {
                "name": "OK: test for multiple input types",
                "function": "test_combine",
                "inputs": [
                    '["0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c","0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c",10]',
                    '["a","b","c","d"]',
                    "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c",
                    "10000",
                ],
                "expected": [
                    [
                        Web3.to_checksum_address(
                            "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"
                        ),
                        Web3.to_checksum_address(
                            "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c"
                        ),
                        10,
                    ],
                    ["a", "b", "c", "d"],
                    "0x1e9Ee7293bc304A10a0b33D0FCCBDFF78463bE5c",
                    10000,
                ],
            },
            {
                "name": "ERR: test invalid json",
                "function": "test_array",
                "inputs": ["1,2,3,4,5"],
                "error": JSONDecodeError,
            },
        ]
        # execute tests
        abi = load_abi_file(
            os.path.join(os.path.dirname(__file__), "abi", "TestTypes.abi")
        )
        for test in tests:
            abi_function = find_abi_function(abi, test["function"])
            # check for error
            if test.get("error") is not None:
                self.assertRaises(
                    JSONDecodeError, parse_arguments, abi_function, test["inputs"]
                )
                continue
            arguments = parse_arguments(abi_function, test["inputs"])
            self.assertEqual(test["expected"], arguments)

    def test_return_value_decoding(self) -> None:
        """
        Test return value decoding.
        """

        abi_function = find_abi_function(MOCK_ABI, "getValidator")
        retval = parse_return_value(abi_function, MOCK_RETURN_VALUE)
        self.assertEqual(MOCK_EXPECTED_PARSED_RETURN_VALUE, retval)

        # TODO: test more sophisticated cases
