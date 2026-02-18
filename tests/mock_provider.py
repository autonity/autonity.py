from collections.abc import Mapping
from typing import cast

from eth_abi import encode
from eth_typing import ChecksumAddress
from eth_utils import function_signature_to_4byte_selector
from web3 import Web3
from web3.providers.base import BaseProvider

from autonity.constants import AUTONITY_CONTRACT_ADDRESS
from autonity.contracts import (
    accountability,
    acu,
    auctioneer,
    autonity,
    inflation_controller,
    liquid_logic,
    omission_accountability,
    oracle,
    stabilization,
    supply_control,
    upgrade_manager,
)


def make_address(index: int) -> ChecksumAddress:
    return Web3.to_checksum_address(f"0x{index:040x}")


CONTRACT_ADDRESSES: dict[str, ChecksumAddress] = {
    "autonity": AUTONITY_CONTRACT_ADDRESS,
    "accountability": make_address(1),
    "oracle": make_address(2),
    "acu": make_address(3),
    "supply_control": make_address(4),
    "stabilization": make_address(5),
    "upgrade_manager": make_address(6),
    "inflation_controller": make_address(7),
    "omission_accountability": make_address(8),
    "auctioneer": make_address(9),
    "liquid_logic": make_address(10),
}


def _canonical_abi_type(item: Mapping[str, object]) -> str:
    abi_type = cast(str, item["type"])
    if not abi_type.startswith("tuple"):
        return abi_type

    suffix = abi_type[5:]
    components = cast(list[dict[str, object]], item.get("components", []))
    inner_types = ",".join(_canonical_abi_type(component) for component in components)
    return f"({inner_types}){suffix}"


def _default_abi_value(item: Mapping[str, object]) -> object:
    abi_type = cast(str, item["type"])

    if abi_type.endswith("]"):
        base_type, _, suffix = abi_type.rpartition("[")
        length_text = suffix[:-1]

        base_item = dict(item)
        base_item["type"] = base_type
        base_value = _default_abi_value(base_item)

        if length_text == "":
            return []
        return [base_value for _ in range(int(length_text))]

    if abi_type.startswith("tuple"):
        components = cast(list[dict[str, object]], item.get("components", []))
        return tuple(_default_abi_value(component) for component in components)

    if abi_type.startswith(("uint", "int")):
        return 0
    if abi_type == "bool":
        return False
    if abi_type == "address":
        return make_address(0)
    if abi_type == "string":
        return ""
    if abi_type == "bytes":
        return b""
    if abi_type.startswith("bytes"):
        return b"\x00" * int(abi_type[5:])

    raise ValueError(f"Unsupported ABI type: {abi_type}")


def _build_selector_map(abi: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    selector_map: dict[str, dict[str, object]] = {}

    for item in abi:
        if item.get("type") != "function":
            continue

        inputs = cast(list[dict[str, object]], item.get("inputs", []))
        input_types = ",".join(_canonical_abi_type(param) for param in inputs)
        signature = f"{item['name']}({input_types})"
        selector = "0x" + function_signature_to_4byte_selector(signature).hex()
        selector_map[selector] = item

    return selector_map


class MockProvider(BaseProvider):
    def __init__(self) -> None:
        super().__init__()
        self._selector_map_by_address = {
            CONTRACT_ADDRESSES["autonity"].lower(): _build_selector_map(autonity.ABI),
            CONTRACT_ADDRESSES["accountability"].lower(): _build_selector_map(
                accountability.ABI
            ),
            CONTRACT_ADDRESSES["oracle"].lower(): _build_selector_map(oracle.ABI),
            CONTRACT_ADDRESSES["acu"].lower(): _build_selector_map(acu.ABI),
            CONTRACT_ADDRESSES["supply_control"].lower(): _build_selector_map(
                supply_control.ABI
            ),
            CONTRACT_ADDRESSES["stabilization"].lower(): _build_selector_map(
                stabilization.ABI
            ),
            CONTRACT_ADDRESSES["upgrade_manager"].lower(): _build_selector_map(
                upgrade_manager.ABI
            ),
            CONTRACT_ADDRESSES["inflation_controller"].lower(): _build_selector_map(
                inflation_controller.ABI
            ),
            CONTRACT_ADDRESSES["omission_accountability"].lower(): _build_selector_map(
                omission_accountability.ABI
            ),
            CONTRACT_ADDRESSES["auctioneer"].lower(): _build_selector_map(
                auctioneer.ABI
            ),
            CONTRACT_ADDRESSES["liquid_logic"].lower(): _build_selector_map(
                liquid_logic.ABI
            ),
        }

    def make_request(self, method: str, params: object) -> dict[str, object]:
        if method == "eth_call":
            request_params = cast(list[dict[str, str]], params)
            tx = request_params[0]
            to_address = tx["to"].lower()
            call_data = tx.get("data", "0x")
            selector = call_data[:10]

            selector_map = self._selector_map_by_address[to_address]
            function_abi = selector_map[selector]
            outputs = cast(list[dict[str, object]], function_abi.get("outputs", []))

            output_types = [_canonical_abi_type(output) for output in outputs]
            output_values = [_default_abi_value(output) for output in outputs]
            encoded = "0x" + encode(output_types, output_values).hex()

            return {"jsonrpc": "2.0", "id": 1, "result": encoded}

        if method == "eth_chainId":
            return {"jsonrpc": "2.0", "id": 1, "result": "0x1"}
        if method == "web3_clientVersion":
            return {
                "jsonrpc": "2.0",
                "id": 1,
                "result": "Autonity/v6.0.0/linux",
            }
        if method == "eth_getTransactionCount":
            return {"jsonrpc": "2.0", "id": 1, "result": "0x0"}
        if method == "eth_estimateGas":
            return {"jsonrpc": "2.0", "id": 1, "result": "0x5208"}
        if method == "eth_gasPrice":
            return {"jsonrpc": "2.0", "id": 1, "result": "0x1"}
        if method == "eth_maxPriorityFeePerGas":
            return {"jsonrpc": "2.0", "id": 1, "result": "0x1"}
        if method == "eth_getBlockByNumber":
            return {
                "jsonrpc": "2.0",
                "id": 1,
                "result": {"number": "0x1", "baseFeePerGas": "0x1"},
            }

        raise RuntimeError(f"Unexpected RPC method: {method}")
