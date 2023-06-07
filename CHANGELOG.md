## 1.0.1 (2023-06-07)

### Docs

- update installation instructions in readme

## v1.0.0 (2023-05-26)

### Feat

- support parsing json encoded input for tuple and arrays
- expose bundled autonity contract version and path
- add ABI for autonity contract v0.10.1
- update web3 dependency to v6 series
- add support for python v3.11

## v0.1.0 (2023-01-24)

### Feat

- util functions for formatting token quantities.  with tests.
- add get_address_from_private_key util function
- update web3.py to 5.31.3.  support python 3.10
- add operatorOnly calls on Autonity contract
- option to disable chain_id checks
- expose LNEW as pure ERC20, and reward claiming calls on Validator objects
- support falling back to web3 computation of gas-price
- use correct versions of contract ABIs, from autonity v0.9.0
- support passing gas, gas_price, nonce etc to erc20 methods (to avoid querying node)
- tx wait functionality
- send_tx util function
- add sign_tx util function
- keyfile handling
- use piccadilly network by default
- util function to create Tx from contract call

### Chore
- switch to solc 0.8.12
- sort ABI keys alphabetically
- make update_abi script geenrate prettified json
