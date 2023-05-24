// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

/**
 * @title TestTypes
 * @dev Implements a contract to test the different types of parameters
 */
contract TestTypes {
    struct Dummy {
        address from; // if true, that person already voted
        address to; // person delegated to
        uint256 amount; // index of the voted proposal
    }

    function test_array(string[] calldata x) public pure returns (uint) {
        return x.length;
    }

    function test_tuple(Dummy calldata x) public pure returns (address) {
        return x.from;
    }

    function test_string(
        string calldata x
    ) public pure returns (string memory) {
        return x;
    }

    function test_int(int x) public pure returns (int) {
        return x;
    }

    function test_bool(bool x) public pure returns (bool) {
        return x;
    }

    function test_address(address x) public pure returns (address) {
        return x;
    }

    function test_bytes(bytes calldata x) public pure returns (bytes memory) {
        return x;
    }

    function test_combine(
        string[] calldata x,
        Dummy calldata y,
        address z,
        uint256 w
    ) public pure returns (uint, address, address, uint256) {
        return (x.length, y.from, z, w);
    }
}
