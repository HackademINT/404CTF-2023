# Solution du challenge Des mots, des mots, des mots

Pour lancer la solution, il faut compiler avec la commande `g++ main.cpp wordShuffle.cpp -o main`.

- *Si un entier est passé en argument, alors le programme se connecte en mode normal pour résoudre le challenge.
- Si aucun argument n'est mis alors le programme passe en mode "mot à mot", dans ce cas le programme prend un mot de l'entrée standard et répond à la sortie standard.
- Si 2 chemins vers des dossiers sont passés en arguments, alors il transformera tous les fichiers textes trouvés dans le dossier source (1er paramètre) et les traitera tous un par un pour les mettre dans le dossier sortie (2e paramètre) pour générer la solution.
