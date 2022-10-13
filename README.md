
# Introduction

[Autonity](https://autnoity.org) is a protocol that provides smart contract and settlement infrastructure specialized for developing new risk markets.  It is a fork of the [Ethereum protocol](https://ethereum.org/).

This package provides the `tendermint` and `aut` extensions to [Web3.py](https://github.com/ethereum/web3.py), for convenient interaction with the Autonity network.

# Installation

```console
pip install autonity
```

# Usage

The convenience function `create_web3` can be used to easily create a
Web3 object with the appropriate extensions enabled:

```python
from web3 import HTTPProvider
from autonity import create_web3

w3 = create_web3(HTTPProvider("https://rpc1.<NETWORK>.autonity.org:8545/"))
```

Where`<NETWORK>` is the name of the Autonity Network being connected to. For example, `https://rpc1.bakerloo.autonity.org:8545/` to connect to the public endpoint on the Bakerloo Testnet.

Alternatively the caller can attach these modules manually:

```python
from web3 import Web3, HTTPProvider
from autonity import Tendermint, Autonity

w3 = Web3(
    HTTPProvider("https://rpc1.bakerloo.autonity.org:8545/"),
    external_modules={
        "aut": Autonity,
        "tendermint": Tendermint,
    })
```

These modules can then be used as any other extension.

For example, the *Autonity contract* (a special contract providing much of Autonity-specific functionality [docs.autonity.org, Autonity Contract Interface](https://docs.autonity.org/reference/api/aut/)), can be accessed as any other [web3.py contract object](https://web3py.readthedocs.io/en/latest/contracts.html#contracts) as follows.

```python
aut_contract = web3.aut.autonity_contract()

# Get the total supply of Newton
ntn_supply = autonity_contract.functions.totalSupply().call()
```

To query the autonity-specific RPC interface:

```python
# Get the current enodes belonging to the consensus committee
committee_enodes = web3.tendermint.get_committee_enodes()
```

# Development

```console
# Install for development in a virtual env
$ make install

# Execute all code checks
$ make check
```
