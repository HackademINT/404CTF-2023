# L'Inondation  
  
## Énoncé  
  
Vous prenez une collation accolé au bar du Procope, et remarquez au bout d'une dizaine de minutes un post-it, sur lequel votre nom est écrit, et en dessous une inscription : « Salut, le nouveau, viens à ma rencontre, porte de derrière ».  
Curieux, vous sortez du café par cette porte et tombez nez à nez avec un jeune homme.  
  
 « Bonjour, pouquoi ce post-it ?  

— Salut ! Excellente question. Dernièrement, un évènement étrange a bouleversé ma ville : elle a été prise d'une épidémie de gens se transformant en rhinocéros. Alors que ce n'était jusqu'hier qu'une dizaine de gens qui étaient touchés, j'ai vu ce matin un troupeau de ce qui semblait être plusieurs centaines de rhinocéros passer sous ma fenêtre. J'ai aussitôt saisi mon appareil photo et photographié régulièrement le troupeau pour avoir une estimation du nombre de rhinocéros, mais il y en a bien trop pour compter tout ça à moi seul ou même à deux.  
  
— Certes, et où voulez-vous donc en venir ?  
  
— Voyez-vous, j'ai entendu parler de vos talent dans les nouvelles technologies par le biais d'un ami qui fréquente ce café. J'imagine qu'un ordinateur saura compter bien plus vite que nous deux, ça vous dirait de m'aider ? D'ailleurs, on ne s'est toujours pas présentés. Moi, c'est Béranger. »  
  
***  
  
Auteur : `Jauttaro Coudjau#0911`  

### Connexion  
`nc cody.hackademint.org 31981`  
  
## Résolution  
  
- on se connecte au challenge en tcp à l'adrese `challenges.404ctf.fr:31420` à l'aide de notre langage de programmation préféré  
OU  
- on exécute localement `LInondation.py` avec python 3 après avoir installé les dépendances requises avec pip (`pip install inputimeout termcolor` si vous êtes sous arch linux, par exemple. Il vous faudra sans doute utiliser pip3 autrement)  
  
- mettre en place des routines de lecture du stdout pour prendre l'énoncé  
- à l'aide des donnée récupérées, compter le nombre de sprites de rhinocéros (i.e. la chaîne : ``~c`°^)``) présents  
- on rentre le nombre de rhinocéros compté dans le stdin et confirmer l'envoi des données.  
- recommencer avec succès 100 fois, moment auquel le flag nous sera donné !  
- il faudra alors afficher le flag  
  
C'est essentiellement ce que fait `solve.py` un exemple de programme de résolution utilisant la librairie python `nclib`.  
