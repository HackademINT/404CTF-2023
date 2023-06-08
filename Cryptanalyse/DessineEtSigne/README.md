# Dessine et Signe

## Énoncé

Au cours d'une de vos sessions au sein du café littéraire, vous tombez par hasard sur un atelier de dessin, qui vient visiblement de se terminer. Vous comptemplez les participants qui rangent leurs affaires, quand une voix vous interpelle:  
« Bonjour! Les cours de dessin vous intéressent?  
Un jeune couple s'est rapproché de vous. Les deux ressortent visiblement du cours.  
— Moi c'est Camille, et lui Salim. Enchantée de faire votre connaissance !  
— Le plaisir est partagé ! Répondez-vous. Je ne savais pas qu'il y avait ce genre de cours ici, mais cela pourait effectivement m'intéresser. Enfin, si vous acceptez les débutants.   
Salim se mit à rigoler, et montra les nombreuses tâches de peinture qui sillonaient ses habits.  
— Si je suis accepté, croyez-moi que tout le monde peut l'être! Et puis, c'est l'occasion d'apprendre de la grande Ewilan donc autant en profiter! Dit-il en montrant de la tête Camille.  
— Wow! répondîtes-vous, surpris. Ewilan était en effet une peintre très connue.  
— Tu sais que tu n'es pas obligé de dévoiler mon identité d'artiste à l'intégralité des personnes que l'on rencontre lui répondit Camille / Ewilan en le foudroyant du regard.  
— Je ne fais que vendre le cours du mieux possible, dit Salim avec un faux air ingénu.  
Camille se mit à sourire. Ces deux-là forment un très beau couple, et leur bonne humeur est contagieuse.  
— C'est vrai que ça donne envie, même si je viens de la cybersécurité à la base.  
— Ohhhh vous venez de la cybersécu? C'est rigolo, c'est ma passion également! Répondit Ewilan.  
— Le hasard fait bien les choses.  
— D'ailleurs je me suis amusée à faire un petit serveur personnel avec un système de signature que j'ai refait entièrement seule. Ça vous intéresserais de me donner votre avis dessus? Vous aurez le droit à un cours particulier de dessin en échange!  
— Eh! Pourquoi même moi j'ai pas le droit à ça? Protesta Salim.  
— Parce que tu m'as jamais demandé, peut-être?  
— C'est pas faux.  
— Et bien pas de problèmes, je vais regarder ça.  
— Merci beaucoup! Et au plaisir de vous revoir aux cours de dessin! »

``Auteur: Alternatif#7526``

## Fichiers

ECDSA.py
serv.py

## Writeup

Dans ce challenge, on est confronté à une implémentation maison de l'ECDSA ainsi qu'à un oracle de chiffrement et de vérification de signatures. On est également limité en termes de nombres signatures que l'on peut envoyer à l'oracle. Ceci a surement du mettre la puce à l'oreille aux habitués de crypto en CTF quant à la vulnérabilité à exploiter. L'objectif est d'accéder à la partie debug du service, qui nécessite pour y accéder de connaitre la clé secrète de la session en cours.

En regardant de plus près l'implémentation de l'ECDSA utilisée ici, on se rend compte qu'elle utilise un système de nonce déterministes (ie les nonces ne sont pas tirés au hasard et sont complètement déterminés par le message à signer). Cela est en général une bonne idée, puisque cela permet d'éviter que des problèmes surviennent lors de la génération aléatoire du nonce. En effet, si un biais existe sur la génération du nonce (par exemple les 50 premiers bits sont tous fixés à 0) alors il suffit de quelques signatures pour pouvoir récupérer la clé! (cf https://blog.trailofbits.com/2020/06/11/ecdsa-handle-with-care/). Les nonces déterministes permettent normalement de se prévenir de cette attaque, sauf que il y a un gros problème ici lors de la génération du nonce.

Au sein de la fonction compute_nonce, qui utilise une clé annexe d2, on voit que, successivement,
- On hash le message concaténé à la clé d1
- On enlève les 6 derniers bytes
- On calcule un rajout qui se base sur différent bytes du nonce_temporaire
- On xor ce rajout avec la clé d2 
- On rajoute les 6 premiers bytes de ce rajout au nonce, qu'on renvoie ensuite.
Intéressons-nous à cette ligne : ``add_on += bytes(tmp_nonce[tmp_nonce[-i] % len(tmp_nonce)])``
Ce que cette ligne semble faire, c'est de récupérer la valeur d'un des byte du nonce. Cette valeur étant un entier au vu de comment les bytes sont gérés en python, on le reconvertit en bytes puis on l'ajoute MAIS la fonction bytes() ne fonctionne pas comme ça. En effet, Si n est un entier bytes(n) == b"\x00"\*n. Pour faire la transformation attendue, il faut faire bytes([n])!

add_on est donc toujours une chaine de null bytes. Elle est ensuite xorée à une clé secrète, qui ne change pas pour toute la durée de la session, puis remplace les 6 derniers bytes du nonce. Ainsi, les 6 derniers bytes (ie 48 bits) du nonce sont toujours les mêmes. On tient notre biais! On peut donc récupérer le secret d1 en exploitant la technique développée dans le blog ci-dessus: https://blog.trailofbits.com/2020/06/11/ecdsa-handle-with-care/.


