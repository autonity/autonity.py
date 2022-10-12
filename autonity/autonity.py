# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

from autonity.tendermint import Tendermint

from web3 import Web3
from web3.module import Module
from web3.contract import Contract
from typing import Optional, cast

# TODO: use the tendermint RPC call for this?
AUTONITY_CONTRACT_ADDRESS = "0xBd770416a3345F91E4B34576cb804a576fa48EB1"


class Autonity(Module):
    """
    Web3 module representing Autonity-specific API.
    """

    _w3: Web3
    _autonity_contract: Optional[Contract]

    def __init__(self, w3: Web3):
        super().__init__(w3)
        self._w3 = self.web3
        self._autonity_contract = None

        # TODO: check chain id?

    def autonity_contract(self) -> Contract:
        """
        Returns the Autonity contract. See docs.autonity.org for details of the
        methods available.
        """
        if not self._autonity_contract:
            if not hasattr(self._w3, "tendermint"):
                self._w3.attach_modules({"tendermint": Tendermint})

            tendermint = cast(Tendermint, self._w3.tendermint)  # type: ignore
            abi = tendermint.get_contract_abi()
            eth = self._w3.eth
            autonity_contract_addr = self._w3.toChecksumAddress(
                AUTONITY_CONTRACT_ADDRESS
            )
            self._autonity_contract = eth.contract(autonity_contract_addr, abi=abi)

        assert self._autonity_contract
        return self._autonity_contract
