// SPDX-License-Identifier: MIT

import "./Bank.sol";
pragma solidity 0.7.6;

contract SelfDestruct {
    address bank;

    constructor(address _bank) payable {
        bank = _bank;
    }

    function autoDestruction() public {
        selfdestruct(payable(bank));
    }
}
