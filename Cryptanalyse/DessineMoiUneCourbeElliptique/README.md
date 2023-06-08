# Dessine-moi une courbe elliptique

## Énoncé 

*Au cours d'une de vos explorations dans le café, vous surprenez la conversation suivante*

Oh ! Ce jour, je m'en souviens parfaitement, comme si c'était hier. À cette époque, je passais mes journées à mon bureau chez moi, avec comme seule occupation de dessiner les illustrations qui m'étaient commandées par les journaux du coin. Je ne m'en rendais pas compte à ce moment, mais cela faisait bien 6 ans que je vivais cette vie monacale sans réelle interaction humaine. Le temps passe vite quand on n'a rien à faire de ses journées. Mais ce jour-là, c'était différent. Je m'apprêtais à commencer ma journée de travail, un peu stressé parce que j'avais des illustrations que je devais absolument finir aujourd'hui. Alors que je venais de m'installer devant ma planche à dessin, quelle ne fut pas ma surprise d'entendre une voix venir de derrière-moi : 
« S'il-te plaît, dessine moi une courbe elliptique. » 
Je me suis retourné immédiatement. Un petit bonhomme se tenait derrière moi, dans mon appartement, habillé de façon tout à fait incongrue. Il portait une sorte de tenue de mousquetaire céleste ? Même aujourd'hui je ne sais toujours pas comment la décrire.  

« Quoi ?  

— S'il-te plaît, dessine moi une courbe elliptique. »

Devant cette situation ubuesque, mon cerveau a lâché, a abandonné. Je ne cherchais plus à comprendre et je me contentais de répondre:  

« Je ne sais pas ce que c'est.  

— Ce n'est pas grave, je suis sûr que tu pourras en dessiner une belle! Répondit l'enfant en rigolant. »

Machinalement, je pris mon crayon, et je dessinai à main levée une courbe, sans réfléchir. Après quelques instants, je me suis retourné, et j'ai montré le résultat à l'enfant, qui secoua immédiatement la tête.  

« Non, regarde: cette courbe à un déterminant nul, je ne veux pas d'une courbe malade ! »

À ce moment, je ne cherchais plus à comprendre ce qu'il se passait. J'ai donc fait la seule chose que je pouvais faire, j'en ai redessiné une. Cette fois, l'enfant était très heureux.  

« Elle est magnifique ! Je suis sûr qu'elle sera très heureuse toute seule. »

Et là, sous mes yeux ébahis, la courbe pris vie depuis mon dessin, et s'envola dans la pièce. Elle se mit à tourner partout, avant de disparaître. J'étais bouche bée, enfin encore plus qu'avant.  

« Ah, elle avait envie de bouger visiblement !  

— Où est-elle partie ?  

— Je ne sais pas. Mais c'est toi qui l'a dessinée ! Tu ne devrais pas avoir de mal à la retrouver. En plus je crois qu'elle t'a laissé un petit souvenir, dit-il en pointant le sol, où une série de chiffres étaient effectivement dessinés sur le parquet.  

— Merci encore ! Sur ce, je dois partir. Au revoir ! »

Avant que je puisse ouvrir la bouche, il disparût.  
Je ne sais toujours pas ce qu'il s'est passé ce jour-là, mais je retrouverais cette courbe un jour !

*Peut-être pourriez-vous l'aider ?*

``Auteur: Alternatif#7526``

## Fichiers

challenge.py
data.txt

## Principe

Le challenge consiste à retrouver les paramètres a et b d'une courbe elliptique définie sur un corp  à partir de deux points aléatoires de cette courbe. Ces paramètres sont utilisés ensuite pour générer une clé AES qui a servie à chiffrer le flag. Toutes les valeurs importantes sont données dans le data.txt

Pour récupérer ces valeurs, il faut repartir de l'équation d'une courbe elliptique ``y^2 = x^3 + a * x + b`` (à vrai dire une courbe elliptique peut avoir une équation avec plus de paramètres, mais lorsque seuls deux paramètres sont donnés au constructeur de courbes elliptiques de sage celui-ci génère une courbe de cette forme, appelée équation de Weierstrass, qui est le forme la plus classique de courbe elliptique).

On possède les coordonnées de deux points P1 = (x1, y1) et P2 = (x2, y2) sur cette courbe, il vérifient donc l'équation ci-dessus. On a donc:
``y1^2 = x1^3 + a * x1 + b``
``y2^2 = x2^3 + a * x2 + b``

Il y a plusieures façons de résoudre à partir de là, mais la plus ismple consiste certainement à soustraire ces deux équations pour faire disparaitre une des deux inconnues:

``y1^2 - y2^2 = x1^3 - x2^3 + a * (x1 - x2) ``
``(y1^2 - y2^2 - (x1^3 - x2^3)) / (x1 - x2) = a ``

On obtient donc une équation pour a. Attention cependant à ne pas oublier que l'on travaille dans un corps GF(p)! On ne travaille donc qu'avec des nombres entiers, et la division consiste plutot en la multiplication par l'inverse modulaire.

Il suffit ensuite de prendre une des deux équations pour retrouver b, comme a est connu.

