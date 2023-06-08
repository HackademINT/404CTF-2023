# À la fin de l'envoi, je signe!

## Énoncé

Alors que vous étiez entrain de vous diriger vers la sortie du café, vous entendez subitement du bruit venir d'un petit attroupement formé autour d'une table.
Un homme, debout, semble visiblement agaçé par quelque chose.  
« C'est inadmissible ! Comment je peux me défendre maintenant ? Si je répond à leurs critiques, ils me traiteront de troll !  
— Calme-toi Pierre, tu sais bien que ça nous gène tout autant que toi.  
— C'est une insulte, c'est un affront, que dis-je, c'est une hérésie !  
— T'en fait toujours trop, souris celle dont vous vous souvenez qu'elle s'appelle Marthe.  
— Qu'est-ce qu'il se passe ? Demandez-vous en vous rapprochant de la conversation.  
— Salutations à vous, vous répondis Pierre en vous saluant avec son chapeau. Nous sommes dans une situation terrible ! Nous possédions un système de signature très avancé au sein du groupe qui nous permettait de signer des messages au noms du groupe. Malheureusement, l'ancien administrateur du système est parti, et nous n'avons plus le contrôle dessus. J'ai l'habitude de me défende contre toute sorte de viles critiques quant aux ouvrages que je produis, mais maintenant que je ne peux plus signer mes réponses, je vais perdre toute crédibilité ! Pauvre de moi !  
— Je peux essayer de regarder ce système si vous voulez.  
— Vous pensez pouvoir reprendre la main dessus ? Si vous y arriviez, vous aurez ma reconnaissance éternelle !  
— Ça vaut le coup d'essayer ! Répondez vous en souriant, amusé par la grandiloquence du bonhomme. »

``Auteur: bluesheet#8813``

## Explications sur Winternitz
Ce challenge traite du schéma de signature à usage unique Winternitz. Ce schéma utilise des chaînes de hashs, de la façon suivante :  
Imaginons que je veuille signer un message `m` composé d'un bloc de 4 bits (`0 <= m <= 15`). Je me fais une clé privée `Kpriv=H(random)`, et je calcule `Kpub = H(H(H(H...(H(Kpriv))))) = H^16(Kpriv)`, avec 16 (=2^block_size) fois l'application de `H` un algo de hachage. Pour signer `m` (`0 <= m <= 15`), je calcule `s = H^m(Kpriv)` (impossible a forger car il est impossible de remonter la chaîne de hashs depuis Kpub). Cette signature est facile à vérifier, en calculant `H^(16-m)(s) == Kpub ?`. Si oui, c'est que le signataire était en possession de Kpriv.  
Attention toutefois, une fois qu'une signature a été générée, il est facile pour un attaquant de signer un message `m'` plus grand que `m` (en appliquant simplement la fonction de hashage `m' - m` fois)

Pour appliquer ce schéma de signature à un message plus long, il suffit de répéter l'opération sur chaque bloc (c'est plus facile que de simplement augmenter la taille de bloc, qui augmenterait exponentiellement le nombre d'opérations de hachage à effectuer). Ainsi, la clé privée est un tableau `[Kpriv_0, Kpriv_1, Kpriv_2, ...]` et la clé publique `[Kpub_0, Kpub_1, Kpub_2, ...]`, chaque sous-clé étant responsable de la signature d'un bloc comme vu plus haut.

Pour palier au problème évoqué plus haut sur la capacité d'un attaquant à signer un message "plus grand", une checksum est ajoutée. Celle-ci fonctionne "à l'envers", de sorte que la checksum associée à un "petit message" soit grande, et celle d'un "grand message" soit petite, afin que signer un "plus grand" message nécessite de remonter la chaîne de hashs pour la partie relative à la checksum. En pratique, il suffit d'additionner les compléments à 2^block_size-1 pour chaque bloc.  
Par exemple, pour une block_size de 4 et un message m = 0x5da (blocs [5, 13, 10]), les compléments à 15 sont [10, 2, 5], et la checksum est donc 17 (0x11). On ajoute donc celle-ci au message, et on signe [5, 13, 10, 1, 1]. On se convainc facilement que pour signer un message plus grand (par exemple 0x6db), on va forcément faire baisser les compléments, et donc baisser la checksum. Il n'est donc pas possible d'avoir deux couples (message, checksum) dont l'un est supérieur en chaque bloc à un autre.

Toutefois, cette signature reste à usage quasi-unique, parce qu'à partir du moment où un attaquant a vu passer deux couples (petit message, grande checksum) et (grand message, petite checksum), il peut avancer les chaînes de hashs des deux côté et signer quasiment n'importe quel message.

## Le challenge

Ici, tout est presque bien implémenté, à un détail près : la checksum est trop petite, et donc cyclique. Il est donc possible, à partir d'un message pas trop grand (le message envoyé par le serveur), de signer un mesage plus grand, et de faire baisser la checksum de sorte que le modulo la fasse re-boucler et qu'elle re-devienne grande, c'est ce qui est fait dans le script (immonde, j'en conviens). Dans le script, je vais jusqu'à lui faire retrouver la valeur qu'elle avait dans le message d'origine, mais ça n'est pas nécessaire. En effet, il suffit d'obtenir une valeur de la checksum plus grande, puis d'avancer la chaîne de hashs.


