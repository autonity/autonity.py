"""Essential protocol parameters exposed as Python variables for convenience."""

from typing import cast

from eth_typing import ChecksumAddress

AUTONITY_CONTRACT_ADDRESS = cast(
    ChecksumAddress, "0xBd770416a3345F91E4B34576cb804a576fa48EB1"
)
AUTONITY_CONTRACT_VERSION = 1

NATIVE_TOKEN_SYMBOL = "ATN"
NATIVE_TOKEN_DECIMALS = 18
