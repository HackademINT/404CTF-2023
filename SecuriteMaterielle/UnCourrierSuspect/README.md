# Un courier suspect  
  
## Énoncé  

Vous commencez à profiter de la vue offerte par ce café pittoresque ainsi que de vos premières gorgées de café quand vous sentez une présence derrière vous.  
«  Bienvenue, novice. Moi c'est Jean Paul Sartre, mais on m'appelle plutôt Jean Paul Sat par ici. »  
À peine avez vous eu le temps de vous retourner, que cet individu vous met dans les mains une platine sur laquelle figure un circuit. Il vous tend également une petite feuille, qui parle d'un "test de remise à niveau".  
« Et voici les instructions. »  
  
Il vous regarde avec insistance.  
  
***  
  
Auteur : `Jauttaro Coudjau#0911`  

### Fichier  
`bienvenue.circ`

## Résolution  
  
- Ouvrir `bienvenue.circ` avec Logisim (la version utilisée pour la création est `2.7.1-7`)  
- Double cliquer sur le sous circuit `partie_1` -> on a la première partie du flag  
- Se rendre dans le sous circuit `partie_2` et cliquer sur la clock jusqu'à obtenir une suite de nombres hexadécimaux de 16 bytes.  
- Se rendre dans le sous circuit `partie_3` et suivre les instructions pour récupérer la deuxième partie du flag. On aurait aussi pu utiliser un site, par exemple [cyberchef](https://cyberchef.org/), pour convertir l'hexadécimal en ASCII.  
- Se rendre dans le sous circuit `partie_4` puis dans la blackbox pour réaliser que l'output du [multiplexeur](https://fr.wikipedia.org/wiki/Multiplexeur) est [AND](https://fr.wikipedia.org/wiki/Fonction_ET) avec 0x00 ce qui fait que le bloc renverra toujours 0x00.  
- Éditer le contenu de la blackbox `partie_4_blackbox` pour pouvoir afficher l'output du multiplexeur.  
- Revenir dans la partie 3 pour encoder en ASCII la 3ème et dernière partie du flag.  
