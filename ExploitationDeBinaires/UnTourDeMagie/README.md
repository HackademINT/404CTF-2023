# Un tour de magie

## Enoncé

En fouillant le café du regard, vous remarquez le Capitaine Némo, assis dans un coin, en train d'examiner une curieuse boîte. Il vous explique alors qu'en tant qu'homme de science, ils souhaite comprendre comment fonctionne la boîte qu'il manipule.

Le créateur de la boîte prétend qu'elle permet de déterminer si une personne possède des pouvoirs magiques ou non, mais le Capitaine ne croit pas un mot de ces sottises. Vous disposez de la boîte ainsi que de son plan de fabrication. Aidez-le à percer ce mystère et faites en sorte que la boîte reconnaisse vos pouvoirs magiques.

Auteur : [mh4ckt3mh4ckt1c4s#0705](https://www.mh4ckt3mh4ckt1c4s.xyz/)

## Solution

Nous sommes en face d'un binaire Wasm dont nous disposons le code source. Outre le fait qu'il s'agit d'un binaire Wasm, il s'agit d'un chall de pwn assez classique. Il existe plusieurs moyens de l'exploiter, dont une est présente dans le fichier `exploit.py` fourni dans ce dossier. 

Ce code source est exploitable à cause du fonctionnement de la mémoire de Wasm qui consiste en une zone continue et sans permissions (lecture, écriture, exécution) que l'on peut retrouver dans un binaire classique ELF par exemple. Cette absence de séparation entre les zones mémoire et l'absence de permissions permettent dans un binaire Wasm de réécrire le contenu de la heap depuis la stack, chose irréalisable dans un binaire ELF.

## Ressources

Voici l'article qui a été ma source d'inspiration pour ce challenge :

- https://www.usenix.org/system/files/sec20-lehmann.pdf

Et en complément un autre article intéressant sur la compréhension de la sécurité mémoire dans Wasm : 

- https://arxiv.org/ftp/arxiv/papers/2111/2111.01421.pdf
