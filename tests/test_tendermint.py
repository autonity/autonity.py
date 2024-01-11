# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Tendermint module tests
"""

from unittest import TestCase

from autonity import Tendermint
from tests.common import create_test_web3


class TestTenderming(TestCase):
    """
    Tendermint module tests
    """

    def _test_tendermint_module(self) -> None:
        """
        test tendermint module
        """
        w3 = create_test_web3()
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
