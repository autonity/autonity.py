# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Common test functions
"""


from autonity.utils.web3 import Web3WithAutonity, create_web3_for_endpoint


DEFAULT_URI = "https://rpc1.piccadilly.autonity.org:8545/"


def create_test_web3() -> Web3WithAutonity:
    """
    Create a Web3 for testing purposes.
    """
    return create_web3_for_endpoint(DEFAULT_URI)
