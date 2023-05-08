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

The project uses [hatch](https://hatch.pypa.io/latest/install/#pipx) as build tool.

## Test and linting

For linting use the command:

```console 
make lint
```

To run the test with coverage report use the command:
```
make coverage
```

## Updating the contract ABIs

The script `script/update_abi` generates the contract ABIs using `solc`. Keys are ordered via the `jq` tool, in order to produce deterministic output, and the results written to the `autonity/abi` directory.  Further, it also records the version of solc and the commit used in files in the same directory.

The autonity contract version being compiled is set in the `update_abi` script, to build a different version, it is necessary to set the variable
`AUTONITY_NODE_COMMIT` with the desired git commit hash.

After executing the script against a new version of the code, the diffs can be reviewed to determine which methods have been modified, removed or added.

To run the script use

```console
make update-abi
```

## Reporting a Vulnerability

**Please do not file a public ticket** mentioning the vulnerability.

Instead, please send an email to <security@autonity.org> to report a security issue.

The following PGP key may be used to communicate sensitive information to developers:

Fingerprint: `6006 CCC3 DD11 7885 1A23 4290 7486 F832 6320 219E`

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
VtiVUMzKBEpmz4LdeSy73Qfr
=12PL
-----END PGP PUBLIC KEY BLOCK-----
```
