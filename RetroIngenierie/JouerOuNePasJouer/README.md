# Jouer ou ne pas jouer ?

## Énoncé
Assis au comptoir du Procope, Roger Caillois, votre voisin de café, vous interpelle. Il s'agite, remarquant une certaine machine en votre possession vous permettant de jouer n'importe où, n'importe quand. Il déclare :

« Le jeu est une activité libre, incertaine, avec des limites précises de temps et de lieu, il a ses règles et il est sans conséquence pour la vie réelle. »

Le jeu est-il vraiment sans conséquence ? Vous tâchez de le découvrir.

Vous vous empressez de sortir cet engin défiant les règles de la philosophie, mais patatras — vous n'arrivez pas à charger votre sauvegarde. Roger a-t-il raison ? Avez-vous osé jouer dans un lieu qui n'était pas propice au jeu, et ceci était votre punition ?

Vous voulez lui prouver le contraire, et pour cela, une seule solution : muni d'un outil douteux, vous devez récupérer votre sauvegarde et jouer.

***

Récupérez les 4 valeurs "??????" précédant celles données, en déduire la seed et ensuite obtenir le format du flag.

**Format** : 404CTF{...}


## Conception

Le challenge consiste à reverse un fichier .nro, un exécutable Switch, puis à reverse sead::Random, un PRNG d'origine utilisé dans les jeux Nintendo (et notamment dans les sauvegardes de Splatoon 2 et 3 sur Switch). L'algorithme d'origine a été adapté pour utiliser un uint64 pour la seed au lieu d'un u32 pour éviter toute tentative de bruteforce.

Le .nro contient l'algorithme et affiche à son lancement:
```
???????????????????????
???????????????????????
???????????????????????
???????????????????????
u64_1
u64_2
u64_3
u64_4
```
Les 4 u64 hardcodés à la fin ont été générés par l'algorithme. Il faut trouver les 4 u64 précédents (c'est-à-dire le tableau d'état interne du PRNG).

Un message donnant le format du flag peut être déchiffré (AES-256-CBC) avec une clé se trouvant uniquement avec ces 4 u64 mais trouver le seed est nécessaire pour flag.

Le fichier .nro peut être lancé directement par l'émulateur Ryujinx (peut-être Yuzu, non testé) sans avoir à fournir de clé, et tout est FOSS. Le .nro devrait également marcher sur console sans problème.

Compilation par GCC fourni par devkitPro, -Ofast, symboles strip.

## Solution

- Utiliser Ghidra ou IDA avec un plugin permettant de load les exécutables Switch (.nro).

- Trouver la fonction main (en regardant les strings par exemple) et reverse l'algorithme de PRNG jusqu'à trouver la seed.

- Déchiffrer le message donnant le flag en lançant le NRO dans un émulateur et en rentrant la seed lorsque demandé.

Voir le dossier solution/ pour un exemple d'algorithme reverse.

Solution rédigée avec l'aide de https://github.com/kinnay.

Flag: 404CTF{Un3_s33d_s34d-17734365728342759975} (Une seed sead)
