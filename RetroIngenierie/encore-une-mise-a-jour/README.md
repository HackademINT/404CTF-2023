# Encore une mise à jour !

Challenge de reverse python 3.11 qui se base sur la spécialisation de bytecode apparue dans cette version.

# Flag

`404CTF{H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8}` avec le format 404CTF{MotDePasse}

# Fichiers

`encore-une-mise-a-jour.py` contient le fichier du challenge tel que donné aux participants.

`chall.py` est un fichier équivalent, avec les noms originaux des variables.

`solve.py` contient un script de solution.

# Principe

Il s'agit d'un ensemble d'équations pour chaque triplet de lettres du mot de passe.
A première vue, il n'y a pas assez d'équations pour avoir un solution unique.
Pour chaque triplet il y a une droite de solutions (2 équations indépendantes pour 2 inconnues) (Ce n'est pas vraiment une droite, puisqu'ici on travaille uniquement avec des entiers modulo 256 (voir 127)).

En réalité, puisque la fonction de check est lancée 20 fois, un certains nombre d'opérations sont spécialisées. (plus de détails [ici](https://peps.python.org/pep-0659/)).
Ainsi la variable `secret` change au milieu de l'éxécution, et un autre ensemble d'équations est vérifié.
Une autre droite de solutions peut être déduite pour chaque triplet. A l'intersection, une solution unique est possible.

Attention, puisque la variable `secret` change avec le bytecode de la fonction `check`, il est impossible de la modifer, ou encode d'attacher un debugger, sans modifier le comportement du programme.

# Solution

Il s'agit d'un script z3 basique, pour trouver la solution unique.
Si vous commentez le second bloc d'équations, le script vous affichera l'ensemble des solutions possibles au premier ensemble d'équation.