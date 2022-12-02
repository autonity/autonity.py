# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Web3 utility functions
"""

from autonity.tendermint import Tendermint

import re
from web3 import Web3
from web3.providers import BaseProvider
from web3.module import Module
from typing import Dict, Sequence, Union, Optional, Type, Any, cast


class Web3WithAutonity(Web3):
    """
    Web3.py class with Autonity-related modules. Used to inform the
    static type checker of the existence and types of the modules.
    """

    tendermint: Tendermint


def web3_provider_for_endpoint(endpoint: str) -> BaseProvider:
    """
    Given an rpc endpoint, return an appropriate provider (https, ws,
    or IPC). If identifier isn't a valid format of one of these three
    types, throws an exception.
    """
    regex_http = re.compile(r"^(?:http)s?://")
    if re.match(regex_http, endpoint) is not None:
        return Web3.HTTPProvider(endpoint)

    regex_ws = re.compile(r"^(?:ws)s?://")
    if re.match(regex_ws, endpoint) is not None:
        return Web3.WebsocketProvider(endpoint)

    regex_ipc = re.compile("([^ !$`&*()+]|(\\[ !$`&*()+]))+\\.ipc")
    if re.match(regex_ipc, endpoint) is not None:
        return Web3.IPCProvider(endpoint)

    raise ValueError(f"cannot determine provider for: {endpoint}")


def create_web3(
    provider: Optional[BaseProvider] = None,
    external_modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
    ignore_chain_id: bool = True,
    **kwArgs: Any,
) -> Web3WithAutonity:
    """
    Convenience function to create a Web3 instance with the Autonity
    external modules attached.  Returns a Web3WithAut type, for static
    type checking.
    """

    external_modules = external_modules or {}
    external_modules["tendermint"] = Tendermint
    w3 = Web3(
        provider,
        external_modules={
            "tendermint": Tendermint,
        },
        **kwArgs,
    )

    # Check the chain ID and ensure it conforms to the Autonity
    # standard.
    if not ignore_chain_id:
        chain_id = w3.eth.chain_id
        _ = parse_autonity_chain_id(chain_id)

    return cast(Web3WithAutonity, w3)


def create_web3_for_endpoint(
    endpoint: str, ignore_chain_id: bool = True, **kwArgs: Any
) -> Web3WithAutonity:
    """
    Convenience function to create a Web3 object for a specific
    endpoint URL.
    """
    return create_web3(
        web3_provider_for_endpoint(endpoint, **kwArgs), ignore_chain_id=ignore_chain_id
    )


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
