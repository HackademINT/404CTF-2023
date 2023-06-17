// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract Jeu {
    bool public isSolved = false;
    uint public m = 0x7fffffff;
    uint public a = 12345;
    uint public c = 1103515245;

    uint private currentState;

    constructor(uint _start) {
        currentState = _start;
    }

    function guess(uint _next) public returns (bool) {
        currentState = (a * currentState + c) % m;
        isSolved = (_next == currentState) || isSolved;
        return isSolved;
    }
}
