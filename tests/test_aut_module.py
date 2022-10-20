# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Autonity module tests
"""

from autonity import create_web3, Aut
from autonity.validator import Validator

from unittest import TestCase
from web3.contract import Contract
from web3.types import Address
from typing import List, cast


class TestAutonityModule(TestCase):
    """
    Autonity module tests
    """

    def test_autonity_contract(self) -> None:
        """
        test autonity module
        """

        w3 = create_web3()
        assert hasattr(w3, "aut")
        aut = w3.aut  # pylint: disable=no-member
        assert isinstance(aut, Aut)

        autonity = aut.autonity_contract()
        self.assertTrue(autonity)
        self.assertTrue(autonity.functions)
        self.assertTrue(autonity.functions.totalSupply)
        self.assertTrue(autonity.functions.getValidators)
        self.assertTrue(isinstance(autonity, Contract))

        validators: List[Address] = cast(
            List[Address], autonity.functions.getValidators().call()
        )
        print(f"validators={validators}")
        self.assertTrue(isinstance(validators[0], str))

        validator_0 = Validator.from_tuple(
            w3, autonity.functions.getValidator(validators[0]).call()
        )
        print(f"validator_0={validator_0}")
        print(f"type(validator_0)={type(validator_0)}")
