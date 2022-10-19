# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Autonity contract tests
"""

from autonity import create_web3
from autonity.autonity import Autonity, Config
from autonity.tendermint import CommitteeMember

from unittest import TestCase


class TestAutonity(TestCase):
    """
    Autonity contract tests
    """

    def test_autonity_queries(self) -> None:

        w3 = create_web3()
        autonity = Autonity(w3)

        self.assertIsInstance(autonity.commission_rate_precision(), int)
        self.assertIsInstance(autonity.config(), Config)
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
        self.assertIsInstance(committee[0], CommitteeMember)
        validators = autonity.get_validators()
        self.assertIsInstance(validators, list)
        self.assertIsInstance(validators[0], str)
