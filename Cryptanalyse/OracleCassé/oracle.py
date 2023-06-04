#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long
from secret import GIFT

p, q = getPrime(1024), getPrime(1024)
n = p * q
e = 0x10001
d = pow(e, -1, (p-1) * (q-1))
ct = pow(bytes_to_long(GIFT), e, n)


dP = d % (p-1)
dQ = d % (q-1)
u = pow(p, -1, q)


def oracle(c):
    m1 = pow(c, dP, p)
    m2 = pow(c, dQ, q)
    h = u * (m1-m2) % p
    mrec = (m2 + h * q) % n
    return mrec


def intro():
    print("Bienvenue dans notre nouveau service d'oracle!")
    print("Le service de l'année précédente nous a causé de nombreaux problèmes, il ne fonctionnait pas comme attendu et était inefficace.")
    print("C'est pourquoi nous avons décidé de tout reprendre à zéro! Cette fois un seul oracle est présent, et il a été optimisé pour être le plus efficace possible!")
    print("Pour fêter le lancement de ce nouveau service, nous offrons un cadeau aux mille premiers utilisateurs.")
    print("...........................................................................................................................................................")
    print("Félicitations! Vous faîtes parti des mille premiers! Voici votre bon-cadeau à utiliser dans l'oracle!:")
    print(ct)


def main():
    intro()
    print(f"Initialisation de l'oracle n°{hex(n)} terminée. Bonne utilisation!")
    while True:
        try:
            print(oracle(int(input("Que voulez vous envoyer à l'oracle?\n"))))
        except:
            print("Erreur critique, le service va s'arrêter.")
            break


if __name__ == '__main__':
    main()
