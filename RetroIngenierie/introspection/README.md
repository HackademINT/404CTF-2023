## Introspection

Challenge de reverse de dificulté `Moyen` pour le 404 CTF 2023.

# Flag

Le flag est `404CTF{5t3althy_f1Le$-4nD_aUt0matIon}` avec le format 404CTF{MotDePasse}

# Principe

Il s'agit d'un packer qui utilise `memfd_create`, dans un packer qui utilise `memfd_create` etc...
Chaque programme unpacké l'est dans un nouveau processus.
Il y a un anti-debug à base de `PTRACE`.

# Build

Vous pouvez utiliser le fichier `build.py` pour reconstruire l'image. Vous aurez besoin de `Jinja2`.
Le nombre de couches peut être changé avec la variable `N`.
Vous pouvez desactiver le rickroll en mettant `rickroll=False` dans le dernier render Template.
Le payload final est le fichier `stage0.c`, qui peut tout à fait être changé suivant vos besoins.

Le dossier `stages` sert à stocker les fichiers temporaires, qui se font supprimer petit à petit, pour des considérations d'espace disque.