"""
Tests for abi_parser.py
"""

from autonity.abi_parser import parse_function_arguments
from autonity.abi_manager import ABIManager

from web3 import Web3
from unittest import TestCase


class TestABIParser(TestCase):
    """
    Test the ABI parsing functionality.
    """

    def test_arg_encoding(self) -> None:
        """
        Test argument encoding.
        """

        abi = ABIManager.load_abi("IERC20")
        arguments = parse_function_arguments(
            abi, "approve", ["0x2b5ad5c4795c026514f8317c7a215e218dccd6cf", "100"]
        )
        self.assertEqual(
            [Web3.toChecksumAddress("0x2b5ad5c4795c026514f8317c7a215e218dccd6cf"), 100],
            arguments,
        )

        # TODO: use mock ABIs to test other types
