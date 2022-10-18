# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Autonity module tests
"""


from autonity import create_web3, Autonity, Tendermint
from autonity.validator import Validator

from unittest import TestCase
from web3.contract import Contract
from web3.types import Address
from typing import List, cast


class TestAutonityModule(TestCase):
    """
    Autonity module tests
    """

    def _test_tendermint_module(self) -> None:
        """
        test tendermint module
        """
        w3 = create_web3()
        assert hasattr(w3, "tendermint")
        # tendermint = cast(Tendermint, w3.tendermint)  # pylint: disable=no-member
        tendermint = w3.tendermint
        assert isinstance(tendermint, Tendermint)

        commitee_1 = tendermint.get_committee(1)
        assert isinstance(commitee_1, list)

        block_1 = w3.eth.get_block(1, False)
        commitee_block_1 = tendermint.get_committee_at_hash(block_1["hash"])
        assert commitee_1 == commitee_block_1

        contract_abi = tendermint.get_contract_abi()
        assert isinstance(contract_abi, list)

        contract_address = tendermint.get_contract_address()
        assert isinstance(contract_address, str)

        # TODO: test this once the RPC call works
        # core_state = tendermint.get_core_state()

        committee_enodes = tendermint.get_committee_enodes()
        assert isinstance(committee_enodes, list)
        assert isinstance(committee_enodes[0], str)

    def test_autonity_contract(self) -> None:
        """
        test autonity module
        """

        w3 = create_web3()
        assert hasattr(w3, "aut")
        aut = w3.aut  # pylint: disable=no-member
        assert isinstance(aut, Autonity)

        autonity = aut.autonity_contract()
        # print(f"autonity = {autonity}")
        # print(f"autonity.abi = {autonity.abi}")
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
            autonity.functions.getValidator(validators[0]).call()
        )
        print(f"validator_0={validator_0}")
        print(f"type(validator_0)={type(validator_0)}")
