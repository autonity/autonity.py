# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Keyfile tests
"""

from autonity.utils.keyfile import (
    PrivateKey,
    keyfile_create_from_private_key,
    keyfile_decrypt_private_key,
)

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
        enc_keyfile = keyfile_create_from_private_key(private_key, password)

        # attempt to decrypt
        private_key_dec = keyfile_decrypt_private_key(enc_keyfile, password)
        self.assertEqual(private_key, private_key_dec)
