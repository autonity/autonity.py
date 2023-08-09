# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
LiquidNewton token tests
"""

from unittest import TestCase

from autonity import Autonity, Validator
from tests.common import create_test_web3


class TestValidator(TestCase):
    """
    Test the Validator contract.
    """

    def test_queries(self) -> None:
        """
        Basic queries on the Newton token
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)

        # Get some NTN holders
        validator_addrs = autonity.get_validators()
        validator_descs = [autonity.get_validator(val) for val in validator_addrs]
        validators = [Validator(w3, vdesc) for vdesc in validator_descs]
        holders = [val.treasury for val in validators]

        validator = validators[0]
        lnew = validator.lnew_contract
        lnew_symbol = lnew.symbol() or "LNEW"
        print(
            f"Validator: {validator.node_address}, {lnew_symbol}: "
            f"{lnew.name()} @{lnew.contract.address}"
        )
        for account in holders:
            lnew_balance = lnew.balance_of(account)
            unclaimed = validator.unclaimed_rewards(account)
            print(
                f"  {account}: "
                f"balance={lnew_balance} {lnew_symbol}, unclaimed fees={unclaimed}"
            )
