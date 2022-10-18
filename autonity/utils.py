# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Utility functions
"""


from web3.contract import ContractFunction
from web3.types import ChecksumAddress, TxParams, Wei, Nonce


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
    call_tx_params = function.build_transaction(tx_params)
    call_tx_params["gas"] = gas or function.web3.eth.estimate_gas(call_tx_params)
    return call_tx_params
