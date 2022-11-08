# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
ERC20 token tests
"""

from tests.common import create_test_web3, ALICE, BOB, CAROL

from autonity.utils.tx import create_contract_function_transaction
from autonity.autonity import Autonity
from autonity.erc20 import ERC20

from web3 import Web3
from web3.types import Wei
from unittest import TestCase


class TestERC20(TestCase):
    """
    ERC20 token tests
    """

    def test_erc20_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)

        # Get some NTN holders
        validator_addrs = autonity.get_validators()
        holders = [autonity.get_validator(val)["treasury"] for val in validator_addrs]
        print(f"holders={holders}")

        # Use the autonity contract as an ERC20 token (Newton)
        token = ERC20(w3, autonity.contract.address)

        name = token.name()
        symbol = token.symbol()
        decimals = token.decimals()
        print(f"Token '{name}' ({symbol}) ({decimals} decimals)")

        supply = token.total_supply()
        self.assertNotEqual(0, supply)

        for holder in holders:
            balance = token.balance_of(holder)
            self.assertTrue(isinstance(balance, int))
            print(f"  {holder}: {balance}")

    def test_erc20_txs(self) -> None:
        """
        Check calls to transaction creation methods.
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)
        token = ERC20(w3, autonity.contract.address)

        alice = Web3.toChecksumAddress(ALICE)
        bob = Web3.toChecksumAddress(BOB)
        carol = Web3.toChecksumAddress(CAROL)

        # Alice to Bob
        transfer_tx = create_contract_function_transaction(
            function=token.transfer(bob, Wei(1)),
            from_addr=alice,
            gas=Wei(10000),
            gas_price=Wei(10000),
        )
        self.assertTrue(transfer_tx)

        # Bob approves Alice to control 1000
        approve_tx = create_contract_function_transaction(
            function=token.approve(alice, Wei(1000)),
            from_addr=bob,
            gas=Wei(50000),
            gas_price=Wei(30000),
        )
        self.assertTrue(approve_tx)

        # Alice uses 500 of the 1000 approved
        transfer_from_tx = create_contract_function_transaction(
            function=token.transfer_from(alice, carol, Wei(500)),
            from_addr=alice,
            gas=Wei(9000),
            gas_price=Wei(5000),
        )
        self.assertTrue(transfer_from_tx)
