// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

contract MySecretVault {
    string private mySecretPassword;
    address private owner;

    mapping(address => bool) private isPasswordGiven;
    uint256 private passwordGivenCount;

    constructor(string memory _secretString) {
        mySecretPassword = _secretString;
        owner = msg.sender;
    }

    function givePassword(
        string memory _fistDoor,
        string memory _secondDoor
    ) public returns (string memory) {
        require(
            keccak256(abi.encodePacked(_fistDoor)) ==
                keccak256(abi.encodePacked("La peau")),
            "Quel est le premier mot magique ?"
        );
        require(
            keccak256(abi.encodePacked(_secondDoor)) ==
                keccak256(abi.encodePacked("de chagrin")),
            "Quel est le second mot magique ?"
        );
        isPasswordGiven[msg.sender] = true;
        passwordGivenCount++;
        return mySecretPassword;
    }

    function checkPasswordGiven(address _address) public view returns (bool) {
        require(msg.sender == owner, "Chenapan !");
        return isPasswordGiven[_address];
    }

    function getPasswordGivenCount() public view returns (uint256) {
        require(msg.sender == owner, "Sacripant !");
        return passwordGivenCount;
    }
}
