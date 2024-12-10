"""Subpackage containing modules for protocol contracts.

Each module consists of the contract binding class, the contract ABI, and ports of
Solidity structures and enumerations.
"""

import warnings

# Suppress warnings raised by `plum` about not being able to resolve types
# from `eth_typing`; the dispatch works as expected
warnings.filterwarnings("ignore", message="Could not resolve the type hint")
warnings.filterwarnings("ignore", message="Could not determine whether .+ is faithful")
