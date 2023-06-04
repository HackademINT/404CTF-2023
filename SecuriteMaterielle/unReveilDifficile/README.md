# Un réveil difficile  
  
## Énoncé  
  
Pour changer de l'électronique, Jean-Paul Sat vous propose de tester un exercice d'écriture. Le principe est le suivant : chaque premier mot de la phrase doit être la minute pendant laquelle la phrase est écrite. Ainsi, ce zigoto qu'est Jean-Paul Sat a posé un réveil digital tout ce qu'il y a de plus classique sur la table.  
Du fait des cinq cafés que vous avez pris pour faire passer le temps pendant que cet aliéné vous expliquait le fonctionnement de chaque type de bascule existant, à peine avez vous démarré l'exercice que vous sentez une envie pressante.  
Après avoir satisfait votre besoin pressant, vous vous rendez compte assez vite que votre réveil, qui marchait jusqu'alors très bien, affiche désormais n'importe quoi. À la recherche d'une explication, vous tentez d'interpeler un individu assis à la table d'en face, qui a l'air de remarquer votre malheureux désarroi. Il retourne cependant aussitôt à sa tâche sans vous accorder plus d'une seconde de son attention.  
C'est alors que cet individu névrosé qu'est Jean-Paul Sat entre en trombe.  
« Alors, sympa, non ? Je suis sûr qu'on va bien s'entendre ! Fais afficher `Un_c` à ton réveil et on pourra sans aucun doute continuer à bien s'amuser, toi et moi. »  
À peine avez-vous le temps d'emmagaziner l'information, qu'il a déjà disparu de votre champ de vision. Vous vous retrouvez presque sans foi, face à votre réveil cassé et votre écrit, fini à moitié.  
  
***  
  
**Format** : `404CTF{le_message_que_vous_avez_trouvé}`
Pour les caractères ambigüs, on considèrera par ordre d'importance le chiffre, la majuscule, puis en dernier la minuscule.
  
Auteur : `Jauttaro Coudjau#0911`

<p class="space">&nbsp;</p>
  
### Fichier
`réveil.circ`  
  
## Résolution  
  
- Identification du contenu de la blackbox (un XOR, effectué avec des NAND)  
- Indentification du pattern de parsing de la ROM par les MUX  
OU  
- On regarde directement en sortie du MUX ce qui en sort en rajoutant une probe  
- Input la clé du XOR dans l'input en connaissant le chiffré afin de faire afficher `Un_c` (i.e. `5e8a048c` en hexa) aux quatres 7 segments  
- Appuyer sur la clock pour voir le flag dérouler sur les 7 segments  
  
## Description des fichiers  
  
`réveil.circ` : Le fichier contenant le chall, à ouvrir avec logisim.  
`flagInject` et son code source `flagInject.cpp` compilé avec `make flagInject` grâce au `Makefile` réorganise un flag donné sous une forme affichable par un 7 segments (une partie de LUT code 7 segments/char est fournie dans `PartialLUT.txt`) pour le placer dans le bon ordre dans la ROM 1 (celle du haut) et la ROM 2 (celle du bas (surprenant, non ?))  
Il génère deux fichiers rom1.txt et rom2.txt qui peuvent directement être chargés dans les bonnes ROM dans Logisim
