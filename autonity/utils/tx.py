# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Transaction utility functions
"""

from autonity.utils.keyfile import (
    EncryptedKeyData,
    PrivateKey,
    decrypt_keyfile,
)

from eth_account.account import Account, SignedTransaction  # type: ignore
from web3 import Web3
from web3.contract import ContractFunction
from web3.types import ChecksumAddress, TxParams, TxReceipt, Wei, Nonce, HexBytes
from typing import Optional

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
    if gas:
        tx_params["gas"] = gas
    call_tx_params = function.buildTransaction(tx_params)
    return call_tx_params


def sign_tx_with_private_key(
    tx: TxParams, private_key: PrivateKey
) -> SignedTransaction:
    """
    For cases where the private key has already been decrypted.  (In
    general, for signing single transactions `sign_tx` is
    recommended.)
    """
    return Account.sign_transaction(  # pylint: disable=no-value-for-parameter
        tx, private_key
    )


def sign_tx(
    tx: TxParams, key_data: EncryptedKeyData, key_passphrase: str
) -> SignedTransaction:
    """
    Sign a transaction using the data from an encrypted keyfile and
    password.
    """
    private_key = decrypt_keyfile(key_data, key_passphrase)
    return sign_tx_with_private_key(tx, private_key)


def send_tx(w3: Web3, tx_signed: SignedTransaction) -> HexBytes:
    """
    Send raw signed tx bytes provided by 'tx_raw' to an RPC server
    to be validated and included in the blockchain.
    """
    raw_tx = tx_signed.rawTransaction
    tx_hash = w3.eth.send_raw_transaction(raw_tx)
    return tx_hash


def wait_for_tx(w3: Web3, tx_hash: HexBytes, timeout: Optional[float]) -> TxReceipt:
    """
    Wait for a specific transaction.  Returns the receipts.

    This simply wraps Web3.eth.wait_for_transaction_receipt, but uses
    stricter types (accepts only a HexBytes object).
    """
    if timeout is None:
        return w3.eth.wait_for_transaction_receipt(tx_hash)

    return w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
