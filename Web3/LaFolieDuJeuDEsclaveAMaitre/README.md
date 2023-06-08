# La folie du jeu : D'esclave à maître

## Énoncé

<div style="margin-bottom: 1em;"><i>Disclaimer : Vous ne devez, en <b>aucun</b> cas, utiliser vos fonds personnels pour résoudre les challenges de web3. Il n'est pas nécessaire de posséder des cryptomonnaies pour lancer les challenges, intéragir avec ou les valider. (Il est aussi inutile de soudoyer les concepteurs des challenges) Cordialement -La trésorerie</i></div>

<div style="margin-bottom: 1em;"><i>Narrativement, ce challenge vient après "La folie du jeu : descente aux enfers" cependant il n'est pas nécessaire de faire le premier pour faire celui-ci.</i></div>

Alors que vous aviez remporté la première bataille contre les jeux de hasard aux côtés d'Armand, la guerre était loin d'être terminée. Marguerite Gauthier vous apprend que les victoires d'Armand Duval à la roulette ne sont qu'une goutte d'eau dans l'océan de ses dettes, accumulées dans des parties de poker clandestines et d'autres jeux illégaux.

Le sort d'Armand est entre vos mains, et vous ne pouvez abandonner maintenant. Marguerite vous implore de trouver une solution définitive à ce fléau qui dévore la vie de son amant.

Vous comprenez que l'heure est venue de jouer votre va-tout, de parier sur votre intelligence et votre ruse pour sauver la situation. Vous avez entendu parler d'un jeu en ligne sur la blockchain Ethereum, qui permet aux joueurs de devenir maîtres de leur destinée. Un jeu où les défis sont ardus, mais les récompenses inestimables. Il s'agit de "CoinFlip", une plateforme révolutionnaire qui offre la possibilité de doubler vos gains à chaque tour, mais qui peut aussi vous faire tout perdre en un instant.

Vous décidez d'entrer dans l'arène du "CoinFlip", prêt à affronter tous les défis et à maîtriser le jeu pour sauver la vie d'Armand Duval. Mais ce jeu n'est pas pour les âmes sensibles, et les enjeux sont énormes.

C'est dans cette arène impitoyable que vous devez prouver votre valeur, votre perspicacité, votre intelligence et votre chance. Vous devez braver les obstacles, contourner les pièges, et vous élever au-dessus de la concurrence. Vous devez vous frayer un chemin vers le sommet. En devenant propriétaire de CoinFlip, vous pouvez ensuite choisir de sauver Armand Duval, ou de le laisser sombrer dans les abysses de la dette.

La route sera semée d'embûches et de dangers, mais vous êtes prêt à tout pour réussir. Marguerite vous observe avec une lueur d'espoir dans les yeux, car elle sait que si quelqu'un peut réussir cette mission impossible, c'est bien vous. Le destin d'Armand Duval est entre vos mains, vous ne pouvez pas échouer.

Auteur: `Soremo`

## Niveau du challenge

Challenge de niveau moyen.

## Résolution

Vous disposez du [code source du smart contract CoinFlip](CoinFlip.sol) ainsi que de [SafeMath](SafeMath.sol), contrat utilisé par CoinFlip pour effectuer semble-t-il des opérations mathématiques sécurisées.

Le but ici va être d'exploiter le fait que delegatecall change le state du contrat appelant et non pas du contrat de destination. Comme le contrat de destination n'est pas stateless on peut réécrire la variable owner (grâce à la variable de transition `uint256 c` dans [SafeMath](SafeMath.sol)) et devenir propriétaire du contrat CoinFlip.


Voir [le smart contract de l'attaquant](AttackCoinFlip.sol) pour la mise en place technique de la solution.

