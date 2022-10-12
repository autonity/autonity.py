# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

from web3 import Web3, HTTPProvider
from web3.providers import BaseProvider
from web3.module import Module
from typing import Dict, Sequence, Union, Optional, Type, Any, cast

from autonity.autonity import Autonity
from autonity.tendermint import Tendermint


DEFAULT_URI = "https://rpc1.bakerloo.autonity.org:8545/"


class Web3WithAut(Web3):
    """
    Web3.py class with Autonity-related modules. Used to inform the static type
    checker of the existence and types of the modules.
    """

    aut: Autonity
    tendermint: Tendermint


def create_web3(
    provider: Optional[BaseProvider] = None,
    external_modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
    **kwArgs: Any
) -> Web3WithAut:
    provider = provider or HTTPProvider(DEFAULT_URI)
    external_modules = external_modules or {}
    external_modules["aut"] = Autonity
    external_modules["tendermint"] = Tendermint
    w3 = Web3(
        provider,
        external_modules={
            "aut": Autonity,
            "tendermint": Tendermint,
        },
        **kwArgs
    )
    return cast(Web3WithAut, w3)
