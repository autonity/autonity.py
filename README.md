# Introduction

[Autonity](https://autonity.org) is a protocol that provides smart contract and settlement infrastructure specialized for developing new risk markets.  It is a fork of the [Ethereum protocol](https://ethereum.org/).  See the [Autonity documentation](https://docs.autonity.org) for further information.

This package provides typed wrappers around the Autonity-specific extensions of Ethereum, using the [Web3.py](https://github.com/ethereum/web3.py) framework, for convenient and statically checked interactions with the Autonity network.

# Installation

```console
pip install git+https://github.com/autonity/autonity.py
```

# Usage

The primary utility of this library is the typed wrappers around the Autonity protocol contract, which provides access to Autonity-specific functionality.

```python
from autonity.utils.web3 import create_web3_for_endpoint
from autonity import Autonity, Validator

w3 = create_web3_for_endpoint("<RPC_ENDPOINT>")

# Create the typed wrapper around the Autonity contract.
autonity = Autonity(w3)

# Get total supply of Newton
ntn_supply = autonity.total_supply()

# Get the current validator list
validator_ids = autonity.get_validators()

# Get descriptor for the 0-th validator.  Print LNEW contract address.
validator_desc_0 = autonity.get_validator(validator_ids[0])
print(f"LNEW contract addr: {validator_desc_0.liquid_contract}")

# Typed validator Liquid Newton contract.  Query unclaimed fees for <ADDRESS>.
validator_0 = Validator(w3, validator_desc_0)
unclaimed_rewards = validator_0.unclaimed_rewards("<ADDRESS>")
print(f"unclaimed rewards: {unclaimed_rewards}")
```

Where`<RPC_ENDPOINT>` is the name of the Autonity network being connected to. See https://docs.autonity.org/networks/ for information about specific networks.

# Development

## Setup

```console
# Install for development in a virtual env
$ make install

# Execute all code checks
$ make check
```

## Updating the contract ABIs

The simple script `script/update_abi` generates the contract ABIs using `solc` from the path, assuming the autonity souce code is installed in a default location (see the script for details).  Keys are ordered via the `jq` tool, in order to produce deterministic output, and the results written to the `autonity/abi` directory.  Further, it also records the version of solc and the commit used in files in the same directory.

After executing the script against a new version of the code, the diffs can be reviewed to determine which methods have been modified, removed or added.
