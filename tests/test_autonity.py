# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Autonity contract tests
"""

from tests.common import create_test_web3

from autonity.autonity import Autonity

from web3.types import Wei
from unittest import TestCase


class TestAutonity(TestCase):
    """
    Autonity contract tests
    """

    def test_autonity_queries(self) -> None:
        """
        Test all query functions.
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)

        self.assertIsInstance(autonity.commission_rate_precision(), int)
        config = autonity.config()
        self.assertIsInstance(config, dict)
        print(f"Autonity config: {config}")

        self.assertIsInstance(autonity.epoch_id(), int)
        self.assertIsInstance(autonity.last_epoch_block(), int)
        self.assertIsInstance(autonity.epoch_total_bonded_stake(), int)
        self.assertIsInstance(autonity.total_redistributed(), int)
        self.assertIsInstance(autonity.epoch_reward(), int)

        self.assertIsInstance(autonity.tail_bonding_id(), int)
        self.assertIsInstance(autonity.head_bonding_id(), int)
        self.assertIsInstance(autonity.tail_unbonding_id(), int)
        self.assertIsInstance(autonity.head_unbonding_id(), int)

        self.assertIsInstance(autonity.deployer(), str)

        self.assertIsInstance(autonity.get_last_epoch_block(), int)
        self.assertIsInstance(autonity.get_version(), int)
        committee = autonity.get_committee()
        self.assertIsInstance(committee, list)
        self.assertIsInstance(committee[0], dict)
        validators = autonity.get_validators()
        self.assertIsInstance(validators, list)
        self.assertIsInstance(validators[0], str)
        self.assertIsInstance(autonity.get_validator(validators[0]), dict)

        self.assertIsInstance(autonity.get_max_committee_size(), int)
        committee_enodes = autonity.get_committee_enodes()
        self.assertIsInstance(committee_enodes, list)
        self.assertIsInstance(committee_enodes[0], str)
        self.assertIsInstance(autonity.get_minimum_base_fee(), int)
        self.assertIsInstance(autonity.get_operator(), str)
        self.assertIsInstance(autonity.get_proposer(1, 1), str)
        self.assertIsInstance(autonity.get_bonding_req(0, 100), list)
        self.assertIsInstance(autonity.get_unbonding_req(0, 100), list)

    def test_autonity_txs(self) -> None:
        """
        Test all tx functions.  For now, simply call the methods to ensure
        they use contract ABI crreectly.
        """

        w3 = create_test_web3()
        autonity = Autonity(w3)

        validators = autonity.get_validators()
        validator_addr = validators[0]
        enode = "adsf"

        autonity.bond(validator_addr, Wei(1))
        autonity.unbond(validator_addr, Wei(1))
        autonity.register_validator(enode)
        autonity.pause_validator(validator_addr)
        autonity.activate_validator(validator_addr)
        autonity.set_minimum_base_fee(Wei(1))
        autonity.set_committee_size(3)
        autonity.set_unbonding_period(10)
        autonity.set_epoch_period(10)
        autonity.set_operator_account(validator_addr)
        # autonity. set_block_period(12)
        autonity.set_treasury_account(validator_addr)
        autonity.set_treasury_fee(100000)
        autonity.mint(validator_addr, Wei(7))
        autonity.burn(validator_addr, Wei(7))
