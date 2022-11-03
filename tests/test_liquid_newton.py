# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
LiquidNewton token tests
"""

from tests.common import create_test_web3

from autonity import Autonity, Validator

from unittest import TestCase


class TestLiquidNewton(TestCase):
    """
    LiquidNewton token tests
    """

    def test_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)

        # Get some NTN holders
        validator_addrs = autonity.get_validators()
        validators = [
            Validator(w3, autonity.get_validator(val)) for val in validator_addrs
        ]
        holders = [val.treasury for val in validators]

        # Get the LiquidNewton contract for the first validator, and
        # check the unclaimed fees of all validators.
        lnew = validators[0].liquid_contract
        print(f"LNEW({lnew.contract.address}):")
        for account in holders:
            unclaimed_fees = lnew.unclaimed_rewards(account)
            print(f"  {account}: unclaimed fees: {unclaimed_fees}")
