# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Common test functions
"""

import os
from autonity.utils.web3 import Web3WithAutonity, create_web3_for_endpoint


ALICE = "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf"
"""
Dummy address
"""

BOB = "0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF"
"""
Dummy address
"""

CAROL = "0x6813Eb9362372EEF6200f3b1dbC3f819671cBA69"
"""
Dummy address
"""


DEFAULT_URI = os.getenv("TEST_RPC_URI", "https://rpc1.piccadilly.autonity.org/")


def create_test_web3() -> Web3WithAutonity:
    """
    Create a Web3 for testing purposes.
    """
    return create_web3_for_endpoint(DEFAULT_URI)
