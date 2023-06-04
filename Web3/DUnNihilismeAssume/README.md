# D'un nihilisme assumé

## Énoncé

<div style="margin-bottom: 1em;"><i>Disclaimer : Vous ne devez, en <b>aucun</b> cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement -La trésorerie</i></div>

Georges Randal fait son apparition au café littéraire, et il ne passe pas inaperçu. Orphelin et ruiné par son oncle indélicat, il a vécu dans la pauvreté après la mort de ses parents. Des rumeurs circulent selon lesquelles il serait un voleur, tellement que — même vous — le connaissez. Malgré tout, vous avez toujours voulu lui donner une chance.

Alors qu'il est parti chercher un café, vous remarquez un croquis posé sur la table devant lui, qui semble être le plan de vol d'une banque. Vous décidez de le confronter à ce sujet. Bien qu'il avoue ses intentions, il reste déterminé à mettre son projet à éxécution.

Vous êtes maintenant confronté à un choix difficile. Allez-vous l'aider à réussir son vol ou essayer de prévenir la banque du plan de Georges?

Auteur: `Soremo`

## Niveau du challenge

Challenge de niveau difficile.

## Résolution

Vous disposez du [code source du smart contract](Bank.sol). Le but est de contourner 3 protections grâce à certaines vulnérabilités.
Dans l'ordre il faut :
- Transférer de l'ether sur le contrat sans appeller une fonction de fallback du contrat (fallback, receive). Pour cela, il faut invoquer la fonction selfdestruct [depuis un autre contrat](SelfDestruct.sol).
- Faire un underflow sur le nombre de crédits fidélité pour pouvoir devenir un client de confiance immédiatement.
- Faire une reentrancy attack sur la fonction withdrawGold pour passer lock à True.

Voir [le smart contract de l'attaquant](AttackBank.sol) et [le smart contract d'auto-destruction](SelfDestruct.sol) pour la mise en place technique de la solution.
