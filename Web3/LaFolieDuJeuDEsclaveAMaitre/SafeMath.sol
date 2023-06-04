// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract SafeMath {
    uint256 c;

    function mul(uint256 a, uint256 b) public returns (uint256) {
        if (a == 0) {
            return 0;
        }
        c = a * b;
        assert(c / a == b);
        return c;
    }

    function div(uint256 a, uint256 b) public returns (uint256) {
        c = a / b;
        return c;
    }

    function sub(uint256 a, uint256 b) public returns (uint256) {
        assert(b <= a);
        c = a - b;
        return c;
    }

    function add(uint256 a, uint256 b) public returns (uint256) {
        c = a + b;
        assert(c >= a);
        return c;
    }
}
