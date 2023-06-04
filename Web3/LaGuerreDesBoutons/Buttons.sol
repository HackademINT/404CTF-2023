// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

interface Event {
    event Transfer(address indexed from, address indexed to, uint256 value);

    event Approval(
        address indexed owner,
        address indexed spender,
        uint256 value
    );
}

contract Buttons is Event {
    mapping(address => uint256) private _balances;

    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 private _totalButtons;

    string private _name;
    string private _symbol;

    bool public isFlag;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply
    ) {
        _name = name_;
        _symbol = symbol_;
        _mint(
            address(0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5),
            initialSupply
        );
        _mint(
            address(0x779f05969a12c992A91C1C096C29A17db1143F24),
            initialSupply
        );
        _mint(
            address(0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5),
            initialSupply
        );
        _mint(
            address(0x388C818CA8B9251b393131C08a736A67ccB19297),
            initialSupply
        );
        _mint(
            address(0x690B9A9E9aa1C9dB991C7721a92d351Db4FaC990),
            initialSupply
        );
        isFlag = false;
    }

    function name() public view returns (string memory) {
        return _name;
    }

    function symbol() public view returns (string memory) {
        return _symbol;
    }

    function decimals() public pure returns (uint8) {
        return 18;
    }

    function totalButtons() public view returns (uint256) {
        return _totalButtons;
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function _msgSender() internal view returns (address) {
        return msg.sender;
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        address owner = _msgSender();
        _transfer(owner, to, amount);
        return true;
    }

    function allowance(
        address owner,
        address spender
    ) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, amount);
        return true;
    }

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public returns (bool) {
        address spender = _msgSender();
        uint256 currentAllowance = allowance(from, spender);
        if (currentAllowance != type(uint256).max) {
            require(currentAllowance >= amount, "Allocation insuffisante");
            unchecked {
                _approve(from, spender, currentAllowance - amount);
            }
        }
        _transfer(from, to, amount);
        return true;
    }

    function increaseAllowance(
        address spender,
        uint256 addedValue
    ) public returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, allowance(owner, spender) + addedValue);
        return true;
    }

    function decreaseAllowance(
        address spender,
        uint256 subtractedValue
    ) public returns (bool) {
        address owner = _msgSender();
        uint256 currentAllowance = allowance(owner, spender);
        require(
            currentAllowance >= subtractedValue,
            "Allocation en dessous de 0 impossible"
        );
        unchecked {
            _approve(owner, spender, currentAllowance - subtractedValue);
        }

        return true;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require(
            from != address(0),
            "Transfert depuis l'adresse nulle impossible"
        );
        require(to != address(0), "Trasnfert vers l'adresse nulle impossible");

        uint256 fromBalance = _balances[from];
        require(
            fromBalance >= amount,
            "Transfert impossible : montant trop important"
        );
        unchecked {
            _balances[from] = fromBalance - amount;
            _balances[to] += amount;
        }

        emit Transfer(from, to, amount);
    }

    function _mint(address account, uint256 amount) internal {
        require(
            account != address(0),
            "Minage vers l'adresse nulle impossible"
        );

        _totalButtons += amount;
        unchecked {
            _balances[account] += amount;
        }
        emit Transfer(address(0), account, amount);
    }

    function _burn(address account, uint256 amount) internal {
        require(
            account != address(0),
            "Brulage depuis l'adresse nulle impossible"
        );

        uint256 accountBalance = _balances[account];
        require(
            accountBalance >= amount,
            "Brulage impossible : montant trop important"
        );
        unchecked {
            _balances[account] = accountBalance - amount;
            _totalButtons -= amount;
        }

        emit Transfer(account, address(0), amount);
    }

    function burn(uint256 amount) public {
        _burn(_msgSender(), amount);
    }

    function burnFrom(address account, uint256 amount) public {
        uint256 currentAllowance = _allowances[_msgSender()][account];
        if (currentAllowance != type(uint256).max) {
            require(currentAllowance >= amount, "Allocation insuffisante");
            unchecked {
                _approve(account, _msgSender(), currentAllowance - amount);
            }
        }
        _burn(account, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(
            owner != address(0),
            "Approbation depuis l'adresse nulle impossible"
        );
        require(
            spender != address(0),
            "Approbation vers l'adresse nulle impossible"
        );

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function flag() public {
        require(
            balanceOf(_msgSender()) >= 5 ether,
            "La guerre des boutons n'est pas finie"
        );
        isFlag = true;
    }
}
