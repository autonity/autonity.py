# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Models for the LiquidNewton contract for a given validator.  Note
that this contract also exposes functionality for claiming fees.
"""

from autonity.erc20 import ERC20


class LiquidNewton(ERC20):
    """
    The LiquidNewton contract.
    """
