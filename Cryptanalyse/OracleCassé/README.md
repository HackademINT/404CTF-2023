# Oracle Cassé

## Énoncé

*Cette description fait référence à un challenge de l'édition précédente qu'il n'est absolument pas nécessaire de connaître pour faire ce challenge.*

**Communiqué de la direction du 404CTF**

Nous souhaitons prendre la parole pour vous dire que nous avons compris vos plaintes concernant les oracles de l'édition précédente. Nous comprenons que ces derniers ont été jugés injustes et trop difficiles à deviner, et c'est pourquoi nous avions décidé de les retirer. C'est pourquoi nous avons décidé de refaire un nouvel oracle, avec les toutes dernières technologies d'optimisation à notre disposition. Afin de nous excuser pour la gène occasionnée, nous offrons aux 1000 premiers arrivés un cadeau à récupérer directement dans l'oracle. Par souci de transparence, nous vous fournirons cette fois-ci le code de fonctionnement exact de cet oracle.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.  
*Colette, directrice du Matin et du 404CTF*

``Auteur: Alternatif#7526``

## Fichier

oracle.py

## Writeup

Lorsque l'on essaye de décoder le cadeau proposé par le service distant en utilisant l'oracle, on se rend compte que celui-ci n'est pas bien déchiffré. Il doit donc y avoir un problème avec l'oracle. En effet, on comparant le déchiffrement effectué par l'oracle avec un déchiffrement RSA classique qui utilise ces paramètres (cf https://medium.com/asecuritysite-when-bob-met-alice/so-what-are-dq-dp-and-invq-used-for-in-rsa-32e365e45e81), on se rend compte que l'on a une erreur: on a ``u = pow(p, -1, q)`` au lieu de ``u = pow(q, -1, p)``. Ceci explique que le déchiffrement ne fonctionne pas. De là il est possible de se rendre compte, soit en jouant un peu avec l'oracle, soit en développant l'équation modifiée de déchiffrement, que l'oracle déchiffre correctement les "petits" messages (et pour être plus précis, les messages inférieurs à q). Cette observation nous permet donc de faire une attaque par dichotomie pour identifier ce facteur, en envoyant le chiffré de nombres (ie pow(nombre, e, n) en python) et en observant si le résultat de l'oracle est ce nombre (auquel cas il est plus petit que q) ou autre chose (plus grand que q). Dès que l'on a récupérer q, on peut déchiffrer à la main le GIFT et récuprérer le flag.


