import random
import time
import os

# Flag
flag = "404CTF{:T]cdeikm_)W_doprsu_nt_;adei}"

# Les 4 règles, cf le document règles.md
rules = [
    "Règle 0 : Aucune modification",
    "Règle 1 : Inverser les lettres",
    """Règle 2 :
- Si le mot à un nombre de lettres pair, échanger la 1ere et la 2e partie du mot obtenu
- Sinon, enlever toutes les lettres du mot correspondant à la lettre centrale""",
    """Règle 3 :
_Si le mot a 3 lettres ou plus_ :

- Si la 3e lettre du mot obtenu est une consonne, "décaler" les voyelles vers la gauche dans le mot original, puis réappliquer les règles 1 et 2.
- Sinon : la même chose mais les décaler vers la droite.

> Ex de décalage : _poteau => petauo_ // _drapeau => drupaea_""",
    R"""Règle 4 :
- Pour `n` allant de 0 à la fin du mot, si le caractère `c` à la position `n` du mot est une consonne (majuscule ou minuscule), insérer en position `n+1` le caractère de code ASCII `a = ((vp + s) % 95) + 32`, où `vp` est le code ASCII de la voyelle précédant la consonne `c` dans l'alphabet (si `c = 'F'`, `vp = 'E'`), et `s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))`, où `a{i}` est le code ASCII de la `i`-ième lettre du mot, `Id(x)` vaut `1` si `x` est vrai, `0` sinon, et `l{i}` la `i`-ième lettre du mot. _Attention à bien appliquer cette règle aussi sur les caractères insérés au mot._

> Ex : _futur => f&ut\ur@_

- Enfin, trier le mot par ordre décroissant d'occurrences des caractères, puis par ordre croissant en code ASCII pour les égalités

> Ex de tri : _patate => aattep_""",
]

# Variables globales
max_time_in_seconds = 5

# Réponse pour chaque règle appliquées sur le mot cosette
cosetteIter = ["cosette", "ettesoc", "ttsoc", "ottsc", "PPtt!15QRUWcos"]


# Teste si le mot cosette pour la règle rule correspond à ce qui est attendu
def testCosette(rule, answer):
    if answer != cosetteIter[rule]:
        print("Malheureusement ce n'est pas le résultat attendu, rappel :")
        print(rules[rule])
        print("Solution : {" + cosetteIter[rule] + "}")
        return False
    return True


# Première partie du chall, fait tester à l'utilisateur le mot cosette en donnant les règles une par une
def cosette():
    print("Commençons. Je te propose de démarrer en transformant mon nom.")
    print("Tout d'abord retourne mon nom sans modifications.")
    print(rules[0])
    print("Entrée : {cosette}")
    answer = input(">> ")
    if not testCosette(0, answer):
        return False
    print("Je vois que tu as compris. La première règle de ce langage est très simple.")
    print(rules[1])
    print("Entrée : {cosette}")
    answer = input(">> ")
    if not testCosette(1, answer):
        return False
    print("Oui c'est bien. Maintenant la deuxième règle est un peu plus difficile.")
    print(rules[2])
    print("Entrée : {cosette}")
    answer = input(">> ")
    if not testCosette(2, answer):
        return False
    print("Tu t'en sors très bien ! Continuons avec la troisième règle.")
    print(rules[3])
    print("Entrée : {cosette}")
    answer = input(">> ")
    if not testCosette(3, answer):
        return False
    print("Nous avons presque fini, la quatrième règle est la plus complexe.")
    print(rules[4])
    print("Entrée : {cosette}")
    answer = input(">> ")
    if not testCosette(4, answer):
        return False
    return True


# Retourne l'entrée et la sortie attendue d'un chapitre aléatoirement choisi
def getRandomFileContent():
    l = os.listdir("./input/")
    n = random.randint(0, len(l))
    with open("./input/" + l[n]) as fi:
        with open("./output/" + l[n]) as fo:
            return [fi.read(), fo.read()]


# Deuxième partie, donne un chapitre formaté à l'utilisateur et teste sa réponse et s'il a répondu dans le temps imparti.
def chapter():
    print(
        "Bravo ! Maintenant je vais te donner un chapitre dont j'ai besoin de la traduction complète."
    )
    print(
        "Chaque mot est écrit en minuscule sans accents ni caractères spéciaux et sont séparés par un espace. Tu as "
        + str(max_time_in_seconds)
        + " secondes pour répondre."
    )
    io = getRandomFileContent()
    print("Entrée : {" + io[0] + "}")
    start = time.time()
    answer = input(">> ")
    end = time.time()
    if end - start > max_time_in_seconds:
        print(
            "Tu as été trop lent... Essaye d'améliorer ton programme et reviens me voir."
        )
        return False
    if io[1] != answer:
        print("Tu as fait une erreur, relis bien les règles.")
        return False
    print("Merci ! C'est exactement ce qu'il me fallait !")
    print("Voici ta récompense : " + flag)
    return True


if cosette():
    chapter()
exit(0)
