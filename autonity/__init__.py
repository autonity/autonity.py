# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Top-level autonity module containing the Web3.py external modules
and helper functions.
"""

from web3 import Web3, HTTPProvider
from web3.providers import BaseProvider
from web3.module import Module
from typing import Dict, Sequence, Union, Optional, Type, Any, cast

from autonity.aut import Aut
from autonity.tendermint import Tendermint


DEFAULT_URI = "https://rpc1.piccadilly.autonity.org:8545/"


class Web3WithAut(Web3):
    """
    Web3.py class with Autonity-related modules. Used to inform the static type
    checker of the existence and types of the modules.
    """

    aut: Aut
    tendermint: Tendermint


def create_web3(
    provider: Optional[BaseProvider] = None,
    external_modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
    **kwArgs: Any,
) -> Web3WithAut:
    """
    Convenience function to create a Web3 instance with the Autonity
    external modules attached.  Returns a Web3WithAut type, for static
    type checking.
    """

    provider = provider or HTTPProvider(DEFAULT_URI)
    external_modules = external_modules or {}
    external_modules["aut"] = Aut
    external_modules["tendermint"] = Tendermint
    w3 = Web3(
        provider,
        external_modules={
            "aut": Aut,
            "tendermint": Tendermint,
        },
        **kwArgs,
    )

    # Check the chain ID
    chain_id = w3.eth.chain_id
    chain_id_str = parse_autonity_chain_id(chain_id)
    print(f"Connected to {chain_id_str}")

    return cast(Web3WithAut, w3)


def parse_autonity_chain_id(chain_id: int) -> str:
    """
    Parse a chain ID according to the Autonity scheme and return a
    human-readable version.  Raise an exception if the chain ID is not
    recognised.
    """

    # As a decimal: '65xxyyyy' where 'xx' = network type and 'yyyy' =
    # identifier.

    digits = str(chain_id)
    if len(digits) != 8 or digits[:2] != "65":
        raise ValueError("chain ID does not match the Autonity scheme")

    net_type = digits[2:4]
    net_id = digits[4:]

    return f"Autonity (type: {net_type}, id: {net_id})"
