const Web3 = require("web3");
const web3 = new Web3("https://blockchain.challenges.404ctf.fr/");

const JeuABI = [
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_start",
        type: "uint256",
      },
    ],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    inputs: [],
    name: "a",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "c",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_next",
        type: "uint256",
      },
    ],
    name: "guess",
    outputs: [
      {
        internalType: "bool",
        name: "",
        type: "bool",
      },
    ],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [],
    name: "isSolved",
    outputs: [
      {
        internalType: "bool",
        name: "",
        type: "bool",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "m",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
];

const contractAddress = "<L'adresse donnée>";


const jeu = new web3.eth.Contract(JeuABI, contractAddress);

let state;
let next;
web3.eth.getStorageAt(contractAddress, 4).then((res) => {
  state = Number(res);
  console.log(state);
  next = (12345 * state + 1103515245) % 0x7fffffff;
  console.log(next);
  jeu.methods
    .guess(next)
    .send({ from: senderAddress })
    .then((res) => {
      console.log(res);
    });
});
