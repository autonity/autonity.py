# Copyright (C) 2015-2022 Clearmatics Technologies Ltd - All Rights Reserved.

"""
Functions for working with contract ABIs.
"""


from __future__ import annotations
from web3 import Web3
from web3.types import (
    ABI,
    ABIFunctionParams,
    Sequence,
)
from typing import List, Any, Union, Callable


ParamType = Union[str, int, float, bool]
"""
A native type which can be passed as an argument to a ContractFunction
"""

ParamParser = Callable[[str], ParamType]
"""
Function to parse a string to a ParamType
"""


def parse_string(value: str) -> str:
    """
    Identity parser.
    """
    return value


def parse_bool(bool_str: str) -> bool:
    """
    Boolean parser.
    """
    if bool_str in ["False", "false", "0", ""]:
        return False

    return True


def string_to_argument_fn_for_type(arg_type: str) -> ParamParser:
    """
    Return a function which parses a string into a type suitable for
    function arguments.
    """

    # TODO: support complex types

    if "[" in arg_type:
        raise ValueError(f"cannot convert array type '{arg_type}' from string")

    if arg_type.startswith("uint") or arg_type.startswith("int"):
        return int
    if arg_type == "bool":
        return parse_bool
    if arg_type == "address":
        return Web3.toChecksumAddress
    if arg_type.startswith("bytes") or arg_type == "string":
        return parse_string
    if arg_type.startswith("fixed") or arg_type.startswith("ufixed"):
        return float

    raise ValueError(f"cannot convert '{arg_type}' from string")


def argument_parsers_for_params(
    outputs: Sequence[ABIFunctionParams],
) -> List[ParamParser]:
    """
    Given the ABIFunctionParams object representing the output types
    of a specific function, return a list of string-to-paramtype
    converters.
    """

    out_types: List[ParamParser] = []
    for output in outputs:
        out_types.append(string_to_argument_fn_for_type(output["type"]))

    return out_types


def parse_function_arguments(
    abi: ABI, function_name: str, arguments: List[str]
) -> List[Any]:
    """
    Given an ABI, a function name and a list of string parameters,
    parse the parameters to suitable types to call the function on a
    contract with the given ABI.
    """

    for element in abi:

        if element["type"] != "function" or element["name"] != function_name:
            continue

        inputs = element["inputs"]
        parsers = argument_parsers_for_params(inputs)
        if len(parsers) != len(arguments):
            raise ValueError(
                f"function requires {len(parsers)}, received {len(arguments)}"
            )

        return [parse(arg) for parse, arg in zip(parsers, arguments)]

    raise ValueError(f"function {function_name} not found in ABI")
