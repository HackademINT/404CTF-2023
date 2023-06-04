// SPDX-License-Identifier: MIT
pragma solidity 0.7.6;

contract Bank {
    mapping(address => uint256) private _balances;
    mapping(address => uint256) public _rewardPoints;
    mapping(address => uint256) private _lastExchangeTime;
    bool private lock;
    bool public isFlag;
    uint256 public _bankGold;

    constructor() payable {
        _bankGold = msg.value;
        lock = false;
        isFlag = false;
    }

    function depositGold() external payable {
        _balances[msg.sender] += msg.value;
        _rewardPoints[msg.sender] += msg.value / (1 gwei);
        _bankGold += msg.value;
    }

    receive() external payable {
        _bankGold += msg.value;
    }

    fallback() external payable {
        _bankGold += msg.value;
    }

    modifier noSpaceForThieves() {
        require(!lock, "La banque est securisee");
        lock = true;
        _;
        lock = false;
    }

    function withdrawGold(uint256 amount) external noSpaceForThieves {
        require(_balances[msg.sender] >= amount, "Votre solde est insuffisant");
        _rewardPoints[msg.sender] -= amount / (1 wei);
        _bankGold -= amount;
        _balances[msg.sender] -= amount;
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Erreur lors de l'envoi de l'ethereum.");
    }

    function withdrawAllGold() external noSpaceForThieves {
        require(_balances[msg.sender] > 0, "Votre solde est insuffisant");
        uint256 amount = _balances[msg.sender];
        _rewardPoints[msg.sender] = 0;
        _bankGold -= amount;
        _balances[msg.sender] = 0;
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Erreur lors de l'envoi de l'ethereum.");
    }

    function enterVault(string memory action) external {
        require(
            lock,
            "Le coffre-fort est ferme pour votre securite, revenez avec du personnel de la banque"
        );
        require(
            _bankGold < address(this).balance,
            "Mais ou est passe l'or ??? Revenez plus tard le temps que nous investiguions"
        );
        if (
            keccak256(abi.encodePacked(action)) ==
            keccak256(abi.encodePacked("Voler le butin et fuir"))
        ) {
            require(
                _rewardPoints[msg.sender] == type(uint256).max,
                "Seuls les clients de confiance peuvent penetrer dans la derniere salle du coffre-fort"
            );
            _balances[msg.sender] = _bankGold;
        }
        if (
            keccak256(abi.encodePacked(action)) ==
            keccak256(abi.encodePacked("Echanger les points de fidelite"))
        ) {
            require(
                _rewardPoints[msg.sender] > 0,
                "Vous n'avez pas de points a echanger"
            );
            require(
                block.timestamp >= _lastExchangeTime[msg.sender] + 7 days,
                "Les points sont echangeables une fois par semaine"
            );
            _rewardPoints[msg.sender] = 0;
            uint256 amount = 100;
            _balances[msg.sender] += amount;
            _lastExchangeTime[msg.sender] = block.timestamp;
        }
    }

    function flag() external {
        require(_balances[msg.sender] >= _bankGold, "Vous etes trop pauvre");
        isFlag = true;
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }
}
