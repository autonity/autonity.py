"""Example exercise: find the validators with the 3 lowest commission rates on
Autonity Piccadilly Testnet and delegate 100 NTN to each.
"""

import os
from typing import cast

from autonity import networks
from autonity.factories import Autonity
from autonity.contracts.autonity import ValidatorState
from web3 import Web3
from web3.middleware import Middleware, SignAndSendRawMiddlewareBuilder


# Use the RPC provider pre-configured for the Autonity Piccadilly Testnet
w3 = Web3(networks.piccadilly.http_provider)

# Load account and set it as the default sender
account = w3.eth.account.from_key(os.environ["PRIVATE_KEY"])
w3.eth.default_account = account.address

# Also set it as the default signer
signer_middleware = cast(Middleware, SignAndSendRawMiddlewareBuilder.build(account))
w3.middleware_onion.add(signer_middleware)

# Create binding around the Autonity contract
autonity = Autonity(w3)

# Get the addresses of all registered validators
validator_addresses = autonity.get_validators()

# Get validator data as instances of `autonity.contracts.autonity.Validator`
validators = [autonity.get_validator(address) for address in validator_addresses]

# Only consider active validators
active_validators = [
    validator for validator in validators if validator.state is ValidatorState.ACTIVE
]

# Identify the targets by sorting validators by commission rate and taking the first 3
target_validators = sorted(
    active_validators, key=lambda validator: validator.commission_rate
)[:3]

# Convert 100 NTN to ton (the equivalent of wei)
amount = 100 * (10 ** autonity.decimals())

for validator in target_validators:
    # Delegate stake to the target validator
    print(validator.node_address, validator.commission_rate)
    tx = autonity.bond(validator.node_address, amount).transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx)

    # Make sure a new bonding request has been created by inspecting the event
    logs = autonity.NewBondingRequest().process_receipt(receipt)
    print(logs[0].args)
