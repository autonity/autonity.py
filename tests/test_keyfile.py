# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Keyfile tests
"""

from autonity.utils.keyfile import (
    PrivateKey,
    create_keyfile_from_private_key,
    get_address_from_keyfile,
    decrypt_keyfile,
)

from web3 import Web3
from unittest import TestCase


class TestKeyfile(TestCase):
    """
    Keyfile tests
    """

    def test_keyfile_generation(self) -> None:
        """
        Test basic enc / dec
        """
        # test pk = 00...01  (32 bytes)
        private_key = PrivateKey(bytes([0] * 31 + [1]))
        password = "pw"
        enc_keyfile = create_keyfile_from_private_key(private_key, password)

        # Check address extraction
        self.assertTrue(Web3.is_checksum_address(get_address_from_keyfile(enc_keyfile)))

        # attempt to decrypt
        private_key_dec = decrypt_keyfile(enc_keyfile, password)
        self.assertEqual(private_key, private_key_dec)
