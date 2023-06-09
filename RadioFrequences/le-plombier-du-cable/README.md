
# Le plombier du câble

Logiciels abordés :

- GQRX
- TempestSDR

Figures littéraires :

- Simone DE BEAUVOIR
- Alexandre DUMAS

## Énoncé

Après les aventures tumultueues de notre cher compagnon, vous retrouvez Simone et Alexandre au café _Le bon café_.
Le bougre avait effectivement disparu : il était en voyage à Paris, pour voir les pièces de théatre jouées par la Comédie Française. Son amour pour le théatre apparu dans ces jeunes années, où il écrivit un drame historique : _[Henri III et sa cour](https://fr.wikipedia.org/wiki/Henri_III_et_sa_cour)_.

Nos resplendissant compagnons, autour de leur quatrième pause café de la douce matinée, ont l'air bien nerveux, mais toutefois portent un air remplis de fourberie. Ils ont enfin eu l'éclair de génie pour espionner l'infâme *collègue* : un plan aux aspects loufoque, mais qui attire vivement votre attention.
Simone DE BEAUVOIR est une figure d'intelligence. Son père lui disait qu'elle aurait pu faire Polytechnique si elle était un homme.
Elle vous explique le détail de l'affaire : pénétrer dans la plus grande légalité chez notre victime, déployer l'antenne et écouter. Mais vu votre talent pour le moins inexistant en matière de discrétion, votre mission sera juste de traiter le signal.

C'est ainsi, lors de la soirée du 3ème martis du mois Kankin, dans le petit logement coquet de notre énergumène, situé rue du Transistor, dans une petite ville de France, d'une superfice de 135,7 hectars, que nos deux héroiques figures représentant le combat contre la mesquinerie, Alexandre et Simone, déployèrent leur antenne directive de 10 cm, dans l'objectif d'intercepter les communications afin que VOUS les traitiez pour découvrir la sombre, tenance et inéluctible vérité.

*Auteur : Racoon@8487 & Astate@3107*


## Conception

**Premier temps : mise en place du dispositif**

Pour ce faire, un ordinnateur portable est connecté en HDMI à un vidéo-projecteur.
Sur un autre ordinateur, un HackRF est branché avec une antenne pour détecter les fréquences sortantes du câble HDMI.
Un premier balayage est effectué sur GQRX pour obtenir la fréquence optimale du câble.
Ensuite, avec le logiciel TempestSDR, on peut visualiser ces ondes et reformer l'image en noir et blanc afin de reproduire l'écran en direct. On affine les paramètres pour lire au mieux le texte affiché à l'écran.

**Deuxième temps : création du flag**

Ici, on met en scène Jean-Paul SAT. On a écrit une lettre possédant un QR Code à scanner pour obtenir le flag. Après avoir vérifié que le texte est assez lisible sur TempestSDR, on passe sous GQRX pour enregistrer les données brutes.
Une série de réglage est effectué sur ce logiciel pour obtenir un fichier qui est ensuite lu sur TempestSDR afin de voir la lisibilité.
La capture est une partie de Tétris venant du challenge de Hardware _[Des tétrominos qui choient](https://gitlab.hackademint.org/404-ctf/2023/des-tetrominos-qui-choient)_, puis la lettre est affiché un instant pour voir le QR Code.


- ``Hackrf`` : Cf [ici](https://greatscottgadgets.com/hackrf/). Il possède un oscillateur externe TCXO 0.5 PPM.
- ``TempestSDR`` : [lien du GitHub](https://github.com/martinmarinov/TempestSDR)


## Solution

On dispose d'une capture audio et d'une lettre. Cette dernière présente les différentes informations techniques, dont l'écran et la fréquence d'échantillonnage. On en déduit de l'écran que l'affichage utilisé est de 1920x1080, en 60 Hz.
On parle également d'une communication intercepté, on peut donc pensez qu'il s'agit d'une capture du câble HDMI. Les différentes recherches sur le sujet permettent de trouver le logiciel TempestSDR, où l'ont peut lire le fichier. Après quelques configurations, on trouve la vidéo de l'écran, ainsi que le QR code qui apparaît.

Flag : `404CTF{4rR3tE_De_m_e$pi0Nn3R}`

@Racoon & @Astate
