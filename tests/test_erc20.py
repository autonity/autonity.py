# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
ERC20 token tests
"""

from autonity import create_web3
from autonity.validator import Validator
from autonity.erc20 import ERC20

from unittest import TestCase
from web3.types import ChecksumAddress
from typing import List, cast


class TestERC20(TestCase):
    """
    ERC20 token tests
    """

    def test_erc20_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_web3()
        aut = w3.aut  # pylint: disable=no-member

        # Get some NTN holders
        autonity = aut.autonity_contract()
        validator_addrs: List[ChecksumAddress] = cast(
            List[ChecksumAddress], autonity.functions.getValidators().call()
        )

        def get_treasury_addr(v_addr: ChecksumAddress) -> ChecksumAddress:
            val = Validator.from_tuple(autonity.functions.getValidator(v_addr).call())
            return val.treasury

        holders = [get_treasury_addr(addr) for addr in validator_addrs]
        print(f"holders={holders}")

        token = ERC20(w3, autonity.address)

        supply = token.total_supply()
        self.assertNotEqual(0, supply)

        for holder in holders:
            balance = token.balance_of(holder)
            self.assertTrue(isinstance(balance, int))
            print(f"  {holder}: {balance}")
