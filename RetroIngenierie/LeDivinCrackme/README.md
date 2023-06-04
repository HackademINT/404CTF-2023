# Le divin crackme

## Ennoncé

Jean-Jacques Rousseau vous prend à part :
"Je t'ai déjà raconté la fois où j'ai rencontré le Marquis de Sade ? Non ? Tu en as de la chance... Mes amis m'avaient organisé un rendez-vous avec lui en ville et avant même de lui parler, il me paraissait étrange. Quoique l'air bien à l'aise, les premiers mots qu'il prononça furent '_Me feriez vous le plaisir d'être mon partenaire de jeu ?_' Malgré sa demande, j'avais comme l'impression de ne pas vraiment avoir le choix et, en effet, avant de pouvoir lui répondre il poursuivit '_Voici ce que nous allons entreprendre : Vous trouvez mon mot de passe et vous voilà libre. Autrement, je ne réponds plus de rien._'. Pendant que j'essayais de le trouver, il continua en me présentant ses points de vue sur les institutions, et, bien que je partage ses opinions sur la nécessité d'accepter l'humain le plus naturel, laissant la corruption des mœurs installée par les institutions, je restais critique face à ses aspects les plus libertins...
Il serait malvenu de te raconter ce qui se passa par la suite considérant mon échec, mais je suis curieux, aurait tu réussi, toi ? Essaye donc, tu ne risques rien en ce qu'il me concerne ! Pour vérifier que tu ne m'as pas répondu au hasard, j'aimerais que tu me précises avec quel programme le binaire a été compilé ainsi que la fonction utilisée pour tester le mot de passe, le flag est donc :
**404CTF{compilateur:fonction:mot_de_passe}**

## Résolution

Il y a un grand nombre de manière de résoudre ce challenge.

- Pour trouver le compilateur, la manière la plus rapide est de remarquer qu'en faisant un `strings`, la string `gcc` apparaît très tôt. gcc étant un compilateur, on se doute que la string est pas là par hasard. Pour être un peu plus certain de ce qu'on raconte (et plus rigoureux), on peut utiliser un outil comme `DIE` (`Detect It Easy`) qui donne beaucoup d'infos sur le binaire et notamment avec quoi il a été compilé... Du coup, compilateur : `gcc`
- Pour trouver la fonction, ça demande d'un peu plus comprendre ce qu'il se passe. Pour ça, vous pouvez utiliser votre déassembleur favoris (`objdump`, `radare2`...) mais bon sur un binaire comme celui-là, vous êtes sûrement bien mieux à utiliser un décompilateur (encore une fois, votre favoris parmis des trucs comme `Ghidra` ou `Ida`)... Alors là, bien sûr, vous voyez que la vérification se passe dans main, mais bon à ce titre là la vérification se passe aussi dans l'entry, d'où le fait qu'on cherchait une fonction plus spécifique que `main`. Du coup en allant voir la fonction `main`, on observe pleins de trucs, notamment qu'il check une longueur et trois strings avec l'entrée utilisateur. Le fait que si l'un de ces checks ne réussis pas alors l'utilisateur est renvoyé vers un message d'erreur nous donne la puce à l'oreille qu'en au fait qu'il vérifie un mot de passe... Et ça avec les fonction de vérifications de strings, les `strncmp`
- Pour le mot de passe, faut reconstituer la string complète avec les trois tests. Pour ça faut comprendre ce que fait vraiment `strncmp`, à savoir vérifier les n premiers caractères d'une string par rapport à une autre. Le truc c'est qu'en fait les trois parties du mot de passes sont vérifiés dans le désordre, du coup faut pas oublier de remettre en ordre avec les différents décalages utilisés. Le mot de passe est donc `L4_pH1l0so`+`Ph13_d4N5_`+`l3_Cr4cKm3`

## Flag

404CTF{gcc:strncmp:L4_pH1l0soPh13_d4N5_l3_Cr4cKm3}
