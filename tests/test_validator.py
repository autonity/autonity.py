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
        lntn = validator.lntn_contract
        lntn_symbol = lntn.symbol() or "LNTN"
        print(
            f"Validator: {validator.node_address}, {lntn_symbol}: "
            f"{lntn.name()} @{lntn.contract.address}"
        )
        for account in holders:
            lntn_balance = lntn.balance_of(account)
            unclaimed_atn, _ = validator.unclaimed_rewards(account)
            print(
                f"  {account}: "
                f"balance={lntn_balance} {lntn_symbol}, unclaimed fees={unclaimed_atn}"
            )
