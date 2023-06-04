// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Memo is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    address public owner;
    string youGotThis = "https://shorturl.ac/mysecretpassword";

    constructor() ERC721("MonMemo", "MEMO") {
        owner = msg.sender;
    }

    function createToken() public returns (uint) {
        require(_tokenIds.current() < 10000, "La limite de NFT est atteinte");
        uint256 newItemId = _tokenIds.current();
        string
            memory tokenURI = "/ipfs/bafybeia5g2umnaq5x5bt5drt2jodpsvfiauv5mowjv6mu7q5tmqufmo47i/metadata.json";
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        _tokenIds.increment();
        return newItemId;
    }
}
