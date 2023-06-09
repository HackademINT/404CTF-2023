
# Un réseau sans fil en 1844

Logiciel abordé :

- GNU Radio

Figure littéraire :

- Alexandre DUMAS


## Énoncé

En manque de lecture lors de vos interminables journées, vous vous souvenez que votre ami de longue date, au doux nom de Alexandre, est un écrivain particulièrement talentueux.

Sans perdre la moindre seconde, vous informez votre précieux compère qu'il y a urgence : il doit écrire un roman le plus rapidement possible.
Ce malin génie défie les lois du temps en frottant le papier de sa plume aiguisé pour vous offrir sa meilleure création, mais une idée faramineuse lui traversa l'esprit durant la nuit.

C'est vers le petit matin que vous recevez une lettre vous informant de sa fabuleuse, mais non moins surprenante, créativité : un nouveau moyen de communication plus rapide et plus efficace que le courrier.
Il vous explique qu'en transformant son roman en une piste audio, il pourrait vous l'envoyez en utilisant des ondes de **2.4 à 5 GHz**. En réflexion sur un tel dispositif à concevoir pour réceptionner son génie, la piste audio vous est transmise directement avec une note.

Malheur, c'est un audio incompréhensible. Super la camaraderie.

Arriverez - vous tout de même à lire sa préface ?

> Format du flag : 404CTF{xxx}

*Auteur:  `Racoon#8487`*

## Conception

Le challenge permet de comprendre le fonctionnement du wifi, avec la norme 802.11a et 802.11n.
Notre fichier à transmettre est la préface du livre _Les Trois Mousquetaires_. Le graphe sous _GNU Radio_ va décomposer chaque bytes dans une trame portant un en-tête.
Le contenu de la trame est modulé en 16 QAM, l'en-tête en BPSK.
Chaque trame est ensuite encodée sur différentes fréquences orthogonales entre elles.
Pour la norme 802.11a, la largeur de bande est de 20 MHz. Celle ci est décomposé en 64 fréquences, chacune étant espacé de 0.3125 MHz.
Les extrémités ne portent aucune informations : on a 56 sous porteuses. 4 sont des pilliers pour retrouver l'information transmise : [-21, -7, 7, 21]. Sur les 52 restantes, la fréquence centrale n'est pas utilisé (motif de sécurité en cas de repliage du spectre).
On a donc : [-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26]

 > Rq: les nombres sont les indexes

Pour la synchronisation, des symboles sont placés sur les différents indexes : ce sont les *sync_word*. Concrétement, ce sont des vecteurs complexes, où la longueur est identique au nombre de subdivisions, à savoir 64 dans notre cas.

> A titre d'exemple, ici on a :
> [[0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.], [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0] ]

Pour les 4 pilliers, on a le même principe avec une liste fixe : [1,1,-1,1] ou [-1,-1,1,-1].
Pour éviter de simplement recopier le graphe disponible sur le wiki GNU Radio, le protocole utilisé est le 802.11n. On a une largeur de bande de 40 MHz, correspondant à simplement deux bandes côte à côte.

> Pour exemple, les pilotes ne seront plus [-21,-7,7,21] mais [[-21,-7,7,21],[-21,-7,7,21]]

## Solution

On récupère le graphe permettant de recevoir une modulation OFDM. Il représente le protocole 802.11a (il est sur le [github](https://github.com/gnuradio/gnuradio/) de gnuradio). On modifie ensuite les entrées pour pouvoir lire un fichier audio format .raw, la modulation du contenu des trames pour mettre du 16 QAM, et on modifie la largeur de bande pour avoir une bande en 40 MHz.

> Pour plus de précisions, voir le graphe `rx_ofdm.grc` dans Conception

Flag : `404CTF{L35_tr01s_M0usqU3t4ir35_3t_l_0FDm}`

@Racoon
