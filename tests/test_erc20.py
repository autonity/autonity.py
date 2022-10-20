# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
ERC20 token tests
"""

from autonity.autonity import Autonity
from autonity.erc20 import ERC20
from autonity.utils.web3 import create_web3

from unittest import TestCase


class TestERC20(TestCase):
    """
    ERC20 token tests
    """

    def test_erc20_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_web3()
        autonity = Autonity(w3)

        # Get some NTN holders
        validator_addrs = autonity.get_validators()
        holders = [autonity.get_validator(val).treasury for val in validator_addrs]
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
