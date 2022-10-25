# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Transaction utility functions
"""

from eth_account.account import Account, SignedTransaction  # type: ignore
from web3.contract import ContractFunction
from web3.types import ChecksumAddress, TxParams, Wei, Nonce
from typing import Dict, Any

# pylint: disable=too-many-arguments


def unsigned_tx_from_contract_call(
    function: ContractFunction,
    from_addr: ChecksumAddress,
    value: Wei = Wei(0),
    gas: Wei = Wei(0),
    gas_price: Wei = Wei(0),
    nonce: Nonce = Nonce(0),
) -> TxParams:
    """
    Given a contract call and other parameters, create an unsigned
    transaction (Web3 TxParams object).
    """
    tx_params: TxParams = {"from": from_addr}
    if value:
        tx_params["value"] = value

    w3 = function.web3
    tx_params["gasPrice"] = gas_price or w3.eth.gas_price
    tx_params["nonce"] = nonce or w3.eth.get_transaction_count(from_addr)
    call_tx_params = function.buildTransaction(tx_params)
    call_tx_params["gas"] = gas or function.web3.eth.estimate_gas(call_tx_params)
    return call_tx_params


def sign_tx(
    tx: TxParams, keyfile_data: Dict[Any, Any], keyfile_passphrase: str
) -> SignedTransaction:
    """
    Sign a transaction using the data from an encrypted keyfile and
    password.  Returns a SignedTx.
    """
    private_key = Account.decrypt(keyfile_data, keyfile_passphrase)  # type: ignore
    return Account.sign_transaction(  # pylint: disable=no-value-for-parameter
        tx, private_key
    )
