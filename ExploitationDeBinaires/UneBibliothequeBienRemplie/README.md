# Une bibliothèque bien remplie

## Enoncé

Impressionné par vos talents, le Capitaine Némo vous laisse accéder à sa bibliothèque privée. Comme vous venez d'arriver, vous n'avez pas accès à grand-chose... Mais peut-être trouverez-vous un moyen d'élargir vos horizons de lecture ?

Vous devez trouver un moyen de lire le contenu du poème stocké dans le fichier `flag.txt`.

Auteur : [mh4ckt3mh4ckt1c4s#0705](https://www.mh4ckt3mh4ckt1c4s.xyz/)

## Solution

Nous sommes en face d'un binaire Wasm. Outre le fait qu'il s'agit d'un binaire Wasm, il s'agit d'un chall de
pwn assez classique. Il existe plusieurs moyens de l'exploiter, dont une est présente dans le fichier `exploit.py` fourni dans ce dossier.

Ce code source est exploitable à cause du fonctionnement de la mémoire de Wasm qui consiste en une zone continue et sans permissions (lecture, é
criture, exécution) que l'on peut retrouver dans un binaire classique ELF par exemple. Cette absence de séparation entre les zones mémoire et l'
absence de permissions permettent dans un binaire Wasm de réécrire le contenu de la variable `FILENAME` (cf le fichier `main.c` qui correspond au code source), qui est pourtant déclarée comme étant constante.Cet exploit serait irréalisable dans un binaire ELF car la zone mémoire dans laquelle la variable `FILENAME` serait stockée serait marquée en lecture seule (zone `rodata`). L'absence de permissions de mémoire dans Wasm rend l'exploit possible.
. 

## Ressources

Voici l'article qui a été ma source d'inspiration pour ce challenge :

- https://www.usenix.org/system/files/sec20-lehmann.pdf

Et en complément un autre article intéressant sur la compréhension de la sécurité mémoire dans Wasm :

- https://arxiv.org/ftp/arxiv/papers/2111/2111.01421.pdf
