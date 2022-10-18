# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
LiquidNewton token tests
"""

from autonity.liquid_newton import LiquidNewton
from autonity import create_web3
from autonity.validator import Validator

from unittest import TestCase
from web3.types import ChecksumAddress
from typing import List, cast


class TestLiquidNewton(TestCase):
    """
    LiquidNewton token tests
    """

    def test_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_web3()
        aut = w3.aut  # pylint: disable=no-member

        # Get some NTN holders
        autonity = aut.autonity_contract()
        validator_addrs = cast(
            List[ChecksumAddress], autonity.functions.getValidators().call()
        )
        validators = cast(
            List[Validator],
            [
                Validator.from_tuple(autonity.functions.getValidator(v_addr).call())
                for v_addr in validator_addrs
            ],
        )

        # Get the LiquidNewton contract for the first validator, and
        # check the unclaimed fees of all validators.

        lnew = LiquidNewton(w3, validators[0].liquid_contract)
        print(f"LNEW({validators[0].addr}):")
        for validator in validators:
            account = validator.treasury
            unclaimed_fees = lnew.unclaimed_rewards(account)
            print(f"  {account}: unclaimed fees: {unclaimed_fees}")
