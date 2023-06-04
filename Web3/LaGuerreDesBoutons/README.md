# La guerre des boutons

## Énoncé

<div style="margin-bottom: 1em;"><i>Disclaimer : Vous ne devez, en <b>aucun</b> cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement -La trésorerie</i></div>

Dans le café littéraire, l'atmosphère est empreinte de calme et de sérénité. Les étagères regorgent de livres, de revues
et de magazines, tandis que les clients s'installent confortablement dans des fauteuils moelleux pour savourer leurs
boissons chaudes et leurs lectures.

Dans le café littéraire, l'atmosphère est empreinte de calme et de sérénité. Les étagères regorgent de livres, de revues
et de magazines, tandis que les clients s'installent confortablement dans des fauteuils moelleux pour savourer leurs
boissons chaudes et leurs lectures.

Il vous regarde avec détermination et vous demande si vous voulez bien l'aider dans cette mission périlleuse. Allez-vous
relever le défi lancé par Lebrac et l'aider à récupérer ses boutons et à prendre sa revanche sur les Velrans ?

Auteur: `Soremo`

## Niveau du challenge

Challenge de niveau moyen.

## Résolution

Vous disposez [du code source du smart contract](Buttons.sol).

Après un peu de recherche, notamment en comparant au standard du token ERC20 proposé
par [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol),
vous vous rendez compte qu'il y a une vulnérabilité dans la fonction `burnFrom`.

La fonction `burnFrom` ne vérifie pas correctement l'allowances à l'entrée de la
fonction : `uint256 currentAllowance = _allowances[_msgSender()][account];`. En partant de ce constat, il est possible
de vider n'importe quel compte de ses tokens en appelant successivement `burnFrom` puis `transferFrom`.

En répétant l'opération pour chaque compte non vide successivement, vous pouvez récupérer tous les tokens du contrat.

Voir le [script de résolution](solution.py).
