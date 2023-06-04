from termcolor import colored
import random
from inputimeout import inputimeout, TimeoutOccurred

rhino = "~c`°^)"
rhinolen = len(rhino)
nbcolonnes = 8 #nombre de blocs de 2*rhinolen chars par ligne
nblignes = 32

print("« Allez, vite, il y a une pile de photos assez importante à traiter,")
print("comptes-moi le nombre de rhinos par photo. »")

for i in range(100):
    rhinocount = 0
    rhinotab = [[random.randint(0,1) for c in range(nbcolonnes)] for l in range(nblignes)]
    offsets = [random.randint(0,rhinolen) for i in range(len(rhinotab)*len(rhinotab[0]))]

    for l in range(nblignes):
        for c in range(nbcolonnes):
            if rhinotab[l][c] :
                rhinocount += 1
                print(offsets[l+c]*' '+colored(rhino,"grey")+(rhinolen-offsets[l+c])*' ',end='')
            else :
                print("            ",end='')
        print('')
    print("Combien de rhinocéros comptez-vous dans cette image ?\nVotre réponse :")
    # l'utilisateur a 5 secondes pour répondre
    try:
        user_answer = inputimeout(prompt="> ", timeout=5)
    except:
        print("« Il faut compter plus rapidement, j'ai pas tout le temps du monde ! »")
        exit()
    # vérification de la réponse
    if int(user_answer) == rhinocount :
        print("« Très bien, la suite arrive ! »")
    else:
        print("« Il semble qu'il y ait une erreur dans ton résultat, j'ai recompté et il y avait "+str(rhinocount)+" rhinocéros, essaie de ne pas te tromper pour la prochaine, s'il te plaît... »")
        exit()
# tout s'est bien passé, on donne le flag !
print("« Bien joué ! Avant que tu partes, ta récompense. »\n\nIl vous tend une enveloppe.\n « Ouvres-la une fois qu'il n'y a personne autour de toi. »\nVous faites exactement cela, à l'intérieur se trouve un billet, et une lettre. Dessus il est marqué 404CTF{4h,_l3s_P0uvo1rs_d3_l'iNforM4tiqu3!}")
