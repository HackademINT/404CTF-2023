
## Avez – vous vu les cascades du Hérisson ?

Logiciel abordé :
- GQRX

Figure littéraire :
- [Alexandre DUMAS](https://fr.wikipedia.org/wiki/Alexandre_Dumas)

## Énoncé

Après avoir rencontré votre amie Simone, cette dernière vous propose de découvrir une nouvelle personne. Quoi de mieux qu’un cache-cache pour apprendre à mieux se connaître ?

Lors de votre partie, vous parvenez habilement à trouver Simone, cependant le troisième joueur demeure parfaitement introuvable. Votre cerveau titanesque a eu la bonne idée de faire ce jeu dehors, en pleine nature, pour plus de difficulté. Sublime. Vous voilà perdu au milieu de nulle part.
Toutefois, un bruit vous attire :
> SPLASHHHH... SHHHHH... SPLASHHHH... SHHHHH... _(Le son d'une cascade d'eau qui tombe et qui ruisselle)_ - `ChatGPT`

Cette chute d'eau paraît ordinaire et suspicieuse. Peut - être parviendrez vous à trouver ce charmant flibustier à travers **les cascades du Hérisson** ?

> Vous avez un oeil de lynx, ainsi vous apercevez que la chute d'eau s'écoule à une fréquence de 2 MHz

*Auteur : `Racoon@8487`*

## Conception

Le principe du challenge est de regarder le spectrogramme du signal, ou _waterfall_ en anglais. C'est une représentation temps-fréquence en 3D, où apparaissent le temps, la fréquence et la répartition d'énergie. Souvent dans les logiciels SDR, c'est une image 2D montrant l'énergie en fonction de la fréquence défilant au cours du temps.

Pour établir le graphe sous _GNU Radio_, j'ai d'abord installé le plugin [_Spectrum Painter_](https://github.com/drmpeg/gr-paint)  et j'ai développé un bloc sous GNU pour prendre en argument une image et un flag.
La suite du graphe traite les données pour afficher l'image dans les _waterfall_.

Pour plus de précisions sur les différents blocs: [wiki GNU Radio](https://wiki.gnuradio.org/)

> Le graphe est disponible dans le dossier Conception

## Solution

En utilisant GQRX, on ouvre le fichier en cliquant sur _"Configure I/O devices"_. Dans le champ _"Device string_" on renseigne les différentes informations.

Dans l'onglet _"FFT Settings"_, on ajuste les paramètres pour voir le flag :

- FFT Size : 32768
- Rate : 60 FPS
- Ajustement de _Waterfall dB range_

`404CTF{413x4ndR3_d4n5_Un3_C45c4d35_?}`

@Racoon
