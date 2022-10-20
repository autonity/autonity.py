# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Utility functions
"""


from autonity.tendermint import Tendermint

from eth_keyfile import create_keyfile_json, decode_keyfile_json  # type: ignore
import json
from web3 import Web3, HTTPProvider
from web3.providers import BaseProvider
from web3.module import Module
from web3.contract import ContractFunction
from web3.types import ChecksumAddress, TxParams, Wei, Nonce
from typing import Dict, Sequence, Union, Optional, NewType, Type, Any, cast

# pylint: disable=too-many-arguments


DEFAULT_URI = "https://rpc1.piccadilly.autonity.org:8545/"


class Web3WithAutonity(Web3):
    """
    Web3.py class with Autonity-related modules. Used to inform the
    static type checker of the existence and types of the modules.
    """

    tendermint: Tendermint


def create_web3(
    provider: Optional[BaseProvider] = None,
    external_modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
    **kwArgs: Any,
) -> Web3WithAutonity:
    """
    Convenience function to create a Web3 instance with the Autonity
    external modules attached.  Returns a Web3WithAut type, for static
    type checking.
    """

    provider = provider or HTTPProvider(DEFAULT_URI)
    external_modules = external_modules or {}
    external_modules["tendermint"] = Tendermint
    w3 = Web3(
        provider,
        external_modules={
            "tendermint": Tendermint,
        },
        **kwArgs,
    )

    # Check the chain ID
    chain_id = w3.eth.chain_id
    chain_id_str = parse_autonity_chain_id(chain_id)
    print(f"Connected to {chain_id_str}")

    return cast(Web3WithAutonity, w3)


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


def unsigned_tx_from_contract_call(
    function: ContractFunction,
    from_addr: ChecksumAddress,
    value: Wei = Wei(0),
    gas: Wei = Wei(0),
    gas_price: Wei = Wei(0),
    nonce: Nonce = Nonce(0),
) -> TxParams:
    """
    Given a contract call and other parameters, create an unsigned
    transaction (Web3 TxParams object).
    """
    tx_params: TxParams = {"from": from_addr}
    if value:
        tx_params["value"] = value

    w3 = function.web3
    tx_params["gasPrice"] = gas_price or w3.eth.gas_price
    tx_params["nonce"] = nonce or w3.eth.get_transaction_count(from_addr)
    call_tx_params = function.build_transaction(tx_params)
    call_tx_params["gas"] = gas or function.web3.eth.estimate_gas(call_tx_params)
    return call_tx_params


EncryptedKeyFile = NewType("EncryptedKeyFile", Dict[str, Any])

PrivateKey = NewType("PrivateKey", bytes)


def keyfile_load(filename: str) -> EncryptedKeyFile:
    """
    Load a keyfile.
    """
    with open(filename, "r", encoding="utf8") as keyfile_f:
        return cast(EncryptedKeyFile, json.load(keyfile_f))


def keyfile_create_from_private_key(
    private_key: PrivateKey, password: str
) -> EncryptedKeyFile:
    """
    Create a keyfile (with encrypted private key) from a private key.
    """
    assert len(private_key) == 32
    return create_keyfile_json(private_key, password.encode("utf8"))


def keyfile_decrypt_private_key(
    encrypted_key: EncryptedKeyFile, password: str
) -> PrivateKey:
    """
    Decrypt the private key from a keyfile.
    """
    pk = decode_keyfile_json(encrypted_key, password.encode("utf8"))
    assert isinstance(pk, bytes)
    return cast(PrivateKey, pk)
