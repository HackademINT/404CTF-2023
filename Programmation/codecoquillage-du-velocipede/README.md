# Codecoquillage du Vélocipède Mécanique

## Fichiers joints au challenge

- [vm](vm)
- [shellcode_my_vm_redacted.vmr](shellcode_my_vm_redacted.vmr)

## Docker à déployer

Cf [Dockerfile](Dockerfile)

Fichiers déployés
- [vm](vm)
- [shellcode_my_vm.vmr](shellcode_my_vm.vmr)
- [Eont3ih4](Eont3ih4) *(contient le flag)*

## Résolution

### Analyse du bytecode

La fonction `main` appelle 3 fonctions consécutivement :
- `ask_code`
- `shellcode`
- `read_flag`

La fonction `ask_code` se contente de lire une entrée utilisateur. La taille de l'entrée est de 1000 donc on pourrait vouloir faire un stack overflow comme dans le challenge "Débordement du Vélocipède Mécanique" pour `ret` sur `read_flag` directement mais on verra un peu plus loin que ça ne nous avance pas trop.

La fonction `shellcode` n'est pas présente dans le binaire. Si on la "crée" dans notre input, elle sera alors présente en mémoire (sur la stack de la VM) et pourra donc être exécutée.

La fonction `read_flag` commence par vérifier deux conditions, dont le pseudo code peut être écrit comme ceci :
```py
if (reg_A + reg_B) - 840983 != 0:
    fail()

reg_C = reg_B
reg_B = 0
for _ in range(reg_C):
    reg_B += reg_A

if reg_B - 3657663292 != 0:
    fail()
```

La deuxième condition peut être simplifiée de la manière suivante :
```py
if (reg_A * reg_B) - 3657663292 != 0:
    fail()
```

(ouais je pensais avoir mis une instruction pour la multiplication mais apparemment non, du coup on fait avec ce qu'on a, boucle et additions)

On a donc deux équations et deux inconnues, on pourra en déduire les valeurs attendues pour `reg_A` et `reg_B`.

Si ces deux conditions sont validées, alors le résultat de la multiplication est utilisé pour déchiffrer avec XOR une chaîne de caractères qui est utilisée comme nom de fichier. Puis 37 caractères sont lus depuis ce fichier.

Donc même si on faisait un débordement, les valeurs de `reg_A` et `reg_B` auraient été incorrectes et le programme ne nous aurait pas affiché le flag.

De plus, si on essaie d'utiliser directement la valeur `3657663292` pour XOR avec le nom du fichier chargé en mémoire, on obtiendrait `FAKENAME`. On ne peut donc pas simplement pas copier-coller la partie de la VM qui lis un fichier dans notre shellcode, en remplaçant le nom du fichier trouvé, puisque le nom est différent sur la remote (mais ça fonctionnerait en local avec un fichier qui s'appelle "FAKENAME").

### Écriture du shellcode

Pour commencer, on doit créer dans notre code une fonction qui s'appelle shellcode. Si on en revient à la définition des fonctions dans la VM :

```
\x01\x04main\x02
^   ^   ^   ^
|   |   |   |_ magic number fin du nom de la fonction
|   |   |_ nom de la fonction
|   |_ taille du nom de la fonction (max : 255)
|_ magic number début du nom d'une fonction
```

On doit donc commencer notre shellcode par `\x01\x09shellcode\x02`. Il doit également se finir par un ret `)` pour revenir à `main` et continuer l'exécution et passer à la fonction `read_flag`. Alternativement, on pourrait aussi faire un call de la fonction `read_flag` puis un exit comme ceci : `(\x09read_flag^AA.` (`^AA` c'est pour mettre `reg_A` à 0 et avoir un joli code de retour 0 quand on exit).

Si on exécute simplement nos 2 instructions de shellcode précédentes, on aurait en sortie : "Conditions not met, not showing flag.". Maintenant, on va chercher à faire en sorte que les conditions de `read_flag` soient valides.

Si on résout le systèmes d'équations qu'on a identifié plus tôt, on obtient :

```
A = 836611
B = 4372
```

(ou l'inverse, ça n'a pas vraiment d'importance si ce n'est le nombre de tours de boucle pour la multiplication)

Donc on pourrait vouloir faire un shellcode qui ferait simplement ça :

```as
fn shellcode:
mov reg_A, 836611
mov reg_B, 4372
ret
```

Cependant, les entiers sont codés sur 4 octets, donc au minimum pour B (et sûrement pour A) on aurait des null bytes dans le shellcode. Et d'expérience, envoyer des null bytes à un programme qui te demande ton entrée utilisateur, ça marche pas vraiment bien (et ici se vérifie assez bien aussi). Il faut pas non plus qu'on ait de retour à la ligne (`0x0A`) sinon le programme va probablement arrêter de lire avant qu'on ait tout envoyé, mais c'est déjà moins probable.

Pour pallier au problème des null-bytes, on peut préparer un entier avec 4 octets non-nuls (j'ai choisi totalement arbitrairement `0x42424242`) dans le registre `reg_C`, charger les valeurs xorées dans A et B, et les xorer à nouveau avec C pour qu'ils retrouvent la valeur attendue.

Ça nous donne le pseudo-code équivalent suivant :
```as
fn shellcode:
mov reg_C, 0x42424242
mov reg_A, (836611 ^ 0x42424242)
xor reg_A, reg_C
mov reg_B, (4372 ^ 0x42424242)
xor reg_B, reg_C
ret
```

Par précaution on peut aussi vérifier que dans toutes les valeurs qu'on charge il n'y a pas l'octet `0x0A`. Ici, pas de problème.

J'ai donc fait un petit programme Python qui permet d'écrire le bytecode associé, et de l'afficher dans la sortie standard (pour pouvoir pipe le résultat dans le programme ou la remote) :

```py
# solve.py
import sys

def generate_bc():
    code =  b"\x01\x09shellcode\x02"
    code += b"#C" + (0x42424242).to_bytes(4, byteorder="little")
    code += b"#A" + (836611 ^ 0x42424242).to_bytes(4, byteorder="little")
    code += b"^AC"
    code += b"#B" + (4372 ^ 0x42424242).to_bytes(4, byteorder="little")
    code += b"^BC"
    code += b')'

    return code

sys.stdout.buffer.write(generate_bc() + b'\n')
```

Et on peut exécuter ce script sur la remote :

```
$ python3 solve.py | nc challenges.404ctf.fr [PORT]
Please enter your shellcode: 404CTF{Y0u_C4n_Wr1t3_PR0graM5_:pog:}
```