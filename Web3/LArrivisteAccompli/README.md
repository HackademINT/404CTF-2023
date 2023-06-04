# L'arriviste accompli

## Énoncé

<div style="margin-bottom: 1em;"><i>Disclaimer : Vous ne devez, en <b>aucun</b> cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement -La trésorerie</i></div>

En quelques heures à peine, votre acuité d'esprit vous a permis de distinguer les clients réguliers de l'établissement,
dont Eugène de Rastignac, personnage ambitieux qui semble préparer quelque chose de conséquent. Il semble également être
attentif à votre présence, depuis que vous avez marqué les esprits au café. Mais voilà qu'en un tour de main, il vous
approche avec avec une grande habileté pour vous soumettre une proposition des plus alléchantes.

D'après lui, Vautrin, épaulé de sa bande de fidèles, mettrait sur pied un système pyramidal destiné à affermir son
emprise. Eugène vous convie ainsi à vous joindre à lui pour faire tomber cette organisation. Pour votre contribution à
la réussite de cette entreprise, vous bénéficieriez de toutes les retombées financières accompagnant la chute de
l'organisation, tandis que les honneurs de la victoire reviendraient à votre complice.

Collaborez donc avec Eugène pour éradiquer ce système pyramidal.

Auteur: `Soremo`

## Niveau du challenge

Challenge de niveau moyen.

## Résolution

Vous disposez [du code source du smart contract](Pyramid.sol).

Après quelques recherches, on peut voir que la fonction `transferFrom` appelle la fonction `transferTokens`.
Cette dernière appelle la fonction `sell` quand l'adresse de destination des tokens est le contrat lui-même.

Le problème est que la fonction sell part du principe que les tokens à vendre viennent de `msg.sender`, ce qui n'est pas
le cas quand `transferFrom` est appelé. Ce faisant, un underflow est possible, permettant à `msg.sender` d'acquérir le
nombre maximum de tokens possible (2^256 - 1).

Voir le [script de résolution](solution.py).
