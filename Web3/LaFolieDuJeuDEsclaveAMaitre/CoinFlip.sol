// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

import "./SafeMath.sol";

contract CoinFlip {
    address public safeMathLibrary;
    address public owner;
    uint256 public contractBalance;
    bool public isFlag = false;

    mapping(address => uint256) public playerBalance;

    event BetResult(bool result, uint256 amount);

    constructor(address _safeMathLibrary) payable {
        safeMathLibrary = _safeMathLibrary;
        contractBalance = msg.value;
        owner = address(0x0);
    }

    function getTokens() public payable {
        require(msg.value > 0, "Echangez de l'ether contre des tokens");
        playerBalance[msg.sender] += msg.value;
    }

    function withdrawAll() public {
        require(
            playerBalance[msg.sender] > 0,
            "Vous n'avez aucun token a retirer"
        );
        playerBalance[msg.sender] = 0;
        payable(msg.sender).transfer(playerBalance[msg.sender]);
    }

    function flipCoin(bool _guess, uint256 randomHelper) public {
        require(playerBalance[msg.sender] > 0, "Placez un pari");
        require(
            playerBalance[msg.sender] * 2 <= contractBalance,
            "Votre pari ne doit pas depasser une certaine limite"
        );

        uint256 random = (uint256(uint160(msg.sender)) +
            playerBalance[msg.sender]);
        (bool success, bytes memory resultRandom) = safeMathLibrary
            .delegatecall(
                abi.encodeWithSignature(
                    "sub(uint256,uint256)",
                    random,
                    randomHelper
                )
            );
        require(success, "Erreur dans l'initialisation de l'aleatoire");
        random = abi.decode(resultRandom, (uint256)) % 2;
        bool result = (random == 0 ? false : true);

        if (_guess == result) {
            (bool successPos, bytes memory resPos) = safeMathLibrary
                .delegatecall(
                    abi.encodeWithSignature(
                        "mul(uint256,uint256)",
                        playerBalance[msg.sender],
                        2
                    )
                );
            require(successPos, "Erreur dans le calcul des gains");

            (bool successSub, bytes memory resultSub) = safeMathLibrary
                .delegatecall(
                    abi.encodeWithSignature(
                        "sub(uint256,uint256)",
                        contractBalance,
                        playerBalance[msg.sender]
                    )
                );
            require(successSub, "Erreur dans le changement de la balance");
            playerBalance[msg.sender] = abi.decode(resPos, (uint256));
            contractBalance = abi.decode(resultSub, (uint256));
            emit BetResult(true, playerBalance[msg.sender]);
        } else {
            (bool successAdd, bytes memory resAdd) = safeMathLibrary
                .delegatecall(
                    abi.encodeWithSignature(
                        "add(uint256,uint256)",
                        contractBalance,
                        playerBalance[msg.sender]
                    )
                );
            require(successAdd, "Erreur dans le changement de la balance");
            contractBalance = abi.decode(resAdd, (uint256));
            playerBalance[msg.sender] = 0;
            emit BetResult(false, 0);
        }
    }

    function withdrawOwner() public {
        require(
            msg.sender == owner,
            "Seul le proprietaire peut retirer les fonds"
        );
        contractBalance = 0;
        payable(msg.sender).transfer(contractBalance);
    }

    function flag() public {
        require(msg.sender == owner, "Vous devez etre proprietaire");
        isFlag = true;
    }
}
