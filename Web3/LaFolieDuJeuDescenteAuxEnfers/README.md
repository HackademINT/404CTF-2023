# La folie du jeu : Descente aux enfers

## Introduction

Ce challenge de Web3 facile a pour but de présenter deux concepts simples de la blockchain en général. D'abord, tout ce qui est stocké dans la blockchain est accessible. Le fait qu'une variable soit privée n'est qu'une courtoisie de solidity.

Ensuite, l'aléatoire dans la blockchain est très difficilement implémentable, car tout résultat est soumis à un consensus, et doit donc être prédictible. Pour avoir du vrai aléatoire, il faut demander à un oracle (problème de confiance) ou implémenter des protocoles assez complexes.

## Fichiers
 - **Jeu.sol** est le smart contrat à valider
 - **solve.js** est un script js qui permet de solve

## Énoncé

<div style="margin-bottom: 1em;"><i>Disclaimer : Vous ne devez, en <b>aucun</b> cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement -La trésorerie</i></div>

<div style="margin-bottom: 1em;"><i>Narrativement, ce challenge vient avant "La folie du jeu : D'esclave à maître" cependant il n'est pas nécessaire de faire celui-ci pour faire le second.
Nous vous conseillons néanmoins de lire l'énoncé de ce challenge pour comprendre le contexte.</i></div>

Alors que vous étiez assis à une table du café Le Procope, vos pensées furent interrompues par l'apparition de la magnifique Marguerite Gauthier. Son regard était aussi pénétrant que ses courbes gracieuses, et son air empreint d'un charme envoûtant ne laissait aucun doute quant à sa nature exceptionnelle.

<p class="space">&nbsp;</p>

Elle s'approcha de vous avec grâce, ses pas silencieux comme une promesse d'aventure. Elle vous confia alors les affres qui tourmentaient son âme : c'était à cause d'elle qu'Armand Duval était pris dans une spirale d'addiction aux jeux d'argent qui le détruisait.

<p class="space">&nbsp;</p>

Ce n'était pas n'importe quels jeux d'argent qui retenaient Armand prisonnier de leurs charmes sournois. Non, il s'était épris des loteries établies sur la blockchain Ethereum, ces jeux impitoyables où l'espoir et le désespoir se côtoyaient sans relâche, tels des amants inséparables.
Ainsi, les dés étaient jetés, et la danse avec le destin commençait. Vous alliez donc vous plonger dans cet univers énigmatique de la blockchain Ethereum, où les paris étaient éternels et les gains fugaces. Pour Marguerite, vous braveriez les tourments, manipuleriez les nombres et les probabilités avec habileté, cherchant à renverser le cours du destin et à redonner à Armand Duval une chance de s'échapper des griffes implacables du jeu.

<p class="space">&nbsp;</p>

Les tasses de café fumaient encore devant vous, tandis que vous vous prépariez à affronter les défis à venir. Marguerite vous observait avec un mélange d'inquiétude et d'espoir dans ses yeux. Vous aviez maintenant un objectif commun : sauver l'âme tourmentée d'Armand et lui offrir une nouvelle vie.

***

<p class="space">&nbsp;</p>
<p class="space">&nbsp;</p>


Gagnez à la roulette décrite dans le contrat ci-joint :

<div class="author">OwlyDuck#4819</div>
<p class="space">&nbsp;</p>


## Résolution

La première étape consiste à trouver le storage correspondant à la variable **currentState** qui doit se trouver à l'adresse 4, étant en 4e position. On peut utiliser la méthode **getStorageAt**.

Ensuite on calcule la next instance, toutes les variables sont connues.

`next = ( 12345*state + 1103515245 ) % 0x7fffffff`

Ensuite on fait un appel au smart contract en mettant en argument next, et c'est gagné !

Vous pouvez voir un exemple de script de résolution [ici](solve.js).

`Flag : 404CTF{r4Nd0Mn3ss_1S_NOt_s0_345y}` 
