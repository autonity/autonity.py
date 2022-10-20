# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Keyfile utility functions
"""


from eth_keyfile import create_keyfile_json, decode_keyfile_json  # type: ignore
import json
from typing import Dict, NewType, Any, cast


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
    private_key = decode_keyfile_json(encrypted_key, password.encode("utf8"))
    assert isinstance(private_key, bytes)
    return cast(PrivateKey, private_key)
