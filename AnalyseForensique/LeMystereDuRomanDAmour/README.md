# Le Mystère du roman d'amour

## Enoncé

En train de faire les cent pas dans un couloir du café se trouve Joseph Rouletabille. Il est préoccupé par un mystère des plus intrigants : une de ses amies, qui écrit régulièrement des livres passionnants, a perdu le contenu de son dernier roman !! Elle a voulu ouvrir son oeuvre et son éditeur a crashé... Il semblerait qu'un petit malin a voulu lui faire une blague et a modifié ses fichiers. Elle n'a pu retrouver qu'un seul fichier étrange, que Joseph vous demande de l'aider à l'analyser afin de retrouver son précieux contenu et de comprendre ce qu'il s'est passé.

Vous devez retrouver :

- le PID du processus crashé
- le chemin complet vers le fichier en question (espaces autorisés) : la forme exacte trouvée dans le challenge et la forme étendue commençant par un / permettent toutes les deux de valider le challenge
- le nom de l'amie de Rouletabille
- le nom de la machine
- le contenu TEXTUEL du brouillon de son livre (si vous avez autre chose que du texte, continuez à chercher : vous devez trouver un contenu texte qui ressemble clairement au début d'un roman). Une fois ce contenu trouvé, il sera clairement indiqué quelle partie utiliser pour soumettre le flag (il s'agira d'une chaîne de caractères en leet)

Le flag est la suite de ces éléments mis bout à bout, et séparés par un tiret du 6 (-), le tout enveloppé par `404CTF{...}`.

Un exemple de flag valide :

`404CTF{1234-/ceci/est/un/Chemin avec/ des espaces1337/fichier.ext-gertrude-monPcPerso-W0w_Tr0P_1337_C3_T3xt3}`

Format du flag : `404CTF{PidDuProcessusCrashé-chemin/vers le/fichier-nomUser-nomDeLaMachine-contenuDuFichier}`

Auteur : [mh4ckt3mh4ckt1c4s#0705](https://www.mh4ckt3mh4ckt1c4s.xyz/)

## Solution

En analysant le fichier fourni, on commence par utiliser la commande `file` qui nous donne les informations suivantes : 

```bash
 $ file fichier-etrange.swp
fichier-etrange.swp: Vim swap file, version 7.4, pid 168, user jaqueline, host aime_ecrire, file ~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt
```

On récupère déjà la plupart des informations, stockées directement dans les métadonnées du fichier swap de Vim. Il ne reste alors plus qu'à retrouver son contenu.

Pour ce faire, on peut utiliser la commande `vim -r fichier-etrange.swp`. Cela nous donnera un prompt nous confirmant que le fichier a bien été restoré. On peut ensuite sauvegarder le fihcier restoré avec la commande `:w restored.bin`.

Une fois le fichier restoré, on l'analyse à nouveau avec la commande `file` : 

```bash
 $ file restored.bin
restored.bin: PNG image data, 1932 x 1932, 8-bit/color RGBA, non-interlaced
```

On s'aperçoit qu'on est en présence d'une image et on peut donc renommer ce fichier restored.png et l'examiner.

On obtient une illustration de livre sur un carré blanc. L'énoncé nous indique qu'on cherche un fichier avec du contenu textuel, donc on continue à creuser et on vérifie si l'image ne contient pas de contenu caché avec [Apéri'Solve](https://aperisolve.fr/). Les résultats de ce site nous font découvrir un QR code caché qu'on peut scanner pour obtenir le contenu textuel recherché.
