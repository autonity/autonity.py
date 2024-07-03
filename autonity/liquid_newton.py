# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Deprecated module left for backwards compatibility.
"""

import warnings

from web3 import Web3
from web3.types import ChecksumAddress

from .liquid import Liquid


class LiquidNewton(Liquid):
    def __init__(self, web3: Web3, address: ChecksumAddress):
        warnings.warn(
            "The liquid_newton.LiquidNewton class has been renamed to liquid.Liquid "
            "and will be removed in a future release",
            DeprecationWarning,
        )
        super().__init__(web3, address)
