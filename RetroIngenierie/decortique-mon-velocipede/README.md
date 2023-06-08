# Décortique mon Vélocipède Mécanique

## Fichiers joints au challenge

- [vm](vm)
- [reverse_my_vm.vmr](reverse_my_vm.vmr)

## Résolution

### Partie 1

On a une VM et un bytecode associé.

On peut commencer par reverse le main de la VM, pour voir qu'elle va initialiser des variables (registres) et des zones mémoires, y charger le fichier passé en argument et chercher une fonction qui s'appelle `main` dans le bytecode.

Les fonctions sont définies comme tel :

```
\x01\x04main\x02
^   ^   ^   ^
|   |   |   |_ magic number fin du nom de la fonction
|   |   |_ nom de la fonction
|   |_ taille du nom de la fonction (max : 255)
|_ magic number début du nom d'une fonction
```

On peut voir qu'une fonction `main` est bien définie dans le bytecode.

Si on regarde son bytecode, elle commence par afficher une phrase qui nous demande une clé.
```
|\x17\x00\x00\x00Please enter the key: \x00:AS$
```

Ensuite, elle lit jusqu'à 256 (0x100) octets de l'entrée utilisateur, et stocke l'adresse de ce qu'elle a lu dans le registre `D`.
```
#B\x00\x01\x00\x00%:DS
```

Puis elle charge une chaîne chiffrée de longueur 176 (0xb0) en mémoire (l'adresse est pointée par le registre de stack `S`) :
```
|\xb0\x00\x00\x00c=!\x11"R\x193\tQ;{;+rlbz-\x0ek\x11\x17\x02\x16Q0Y3Y\x17L\x12U1\n$^\x16\tX\x14BC\x06bVO 4CyG\x14N*\x1e6ByG;r\x10z4By\x035%DFFZB\x03fz6|g~#DZY4~l\x00o}t!O#2ByG\x120mb4BZ\x045rlb\x08\x06\'\x03wL(Ig\x01T\x06sS\x9e\x9d\xcb\xbdC\x14t\x0etb4B:(_\x15\x1e\x03@1Xgh\x1d\x19\x10\x14$\x15&VR\x05\x11\x0ebC\x06bV2#ulY\x14f3+
```

Ensuite on a une boucle de 44 itérations (le registre `A` sert de compteur de boucle)

Celle ci charge 4 octets à l'adresse pointée par `S` et 4 octets à l'adresse `D + E` (`E` alterne entre 0 et 4 pour couvrir 8 octets la clé xor entrée par l'utilisateur)

La VM xor les deux entiers de 4 octets, puis les replace à l'adresse pointée par `S`, augmente `S` de 4 et décrémente `A`.

Après la boucle, elle décale `S` de 256 octets (pour éviter que la stack écrase ce qui a été déchiffré avant) et appelle une fonction du nom de `check_key`.

Comme on a pas de fonction `check_key` dans le bytecode de la VM, on peut supposer qu'elle se trouve dans ce qui est déchiffré en mémoire.

Mais comment trouver la clé xor ? Si on reprend la définition des fonctions évoquée plus haut, la définition de la fonction `check_key` devrait être :
```
\x01\x09check_key\x02
```

Cette définition fait 12 caractères, c'est largement assez pour effectuer une attaque par clair connu et retrouver la clé xor : `b4ByG1rl`

### Partie 2

Maintenant qu'on a la clé on va s'intéresser au bytecode qui a été déchiffré en mémoire et à cette fonction `check_key`.

On peut déchiffrer son byte-code par nous même ou débugger la VM pour le récupérer en mémoire.

Elle commence par afficher une phrase qui nous demande un mot de passe (on peut le constater en exécutant la VM avec la première clé qu'on a obtenu).

```
|\x1a\x00\x00\x00Now, enter the passcode: \x00:AS$
```

À nouveau elle lit jusqu'à 256 (0x100) octets de l'entrée utilisateur, puis pop les 4 premiers octets dans le registre `F`.

```
#B\x00\x01\x00\x00%<F
```

Ensuite elle charge `\n\x00` puis à nouveau une chaine de caractère chiffrée en mémoire (cette fois de taille 24 - 0x18).

Puis elle boucle 6 fois (le registre `A` sert encore de compteur de boucle) en effectuant un xor de la chaîne chiffrée en mémoire avec le registre `F` (on a donc une clé de 4 octets).

Finalement, elle affiche "Congrats! Your flag is: ". La chaîne ne se terminant pas par un null-byte, elle va continuer en passant par la chaîne chiffrée en mémoire (le flag donc) avant de s'arrêter au `\n\x00` chargé précédemment.

Comme il s'agit du flag dont on connait le format, on va pouvoir à nouveau déduire la clé xor : `p4ck`

Ce qui nous donne le flag : `404CTF{P4ck1ng_1s_H3ll!}`
