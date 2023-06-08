
# Navi

Logiciel abordé :
- Audacity

Figure littéraire :
- [Simone DE BEAUVOIR](https://fr.wikipedia.org/wiki/Simone_de_Beauvoir)

## Énoncé

En arrivant en ville, une pause vous est grandement nécessaire après votre long voyage. Heureusement, non loin de là se trouve un café littéraire : parfait pour vous détendre et vous changer les idées.

En vous installant à une table, sirotant tranquillement une boisson, vous entendez le bruit monté avec les nombreuses personnes à l’intérieur. C'est à ce moment qu'une femme vient se poser en face de vous. En la regardant, vous reconnaissez une très chère amie : Simone DE BEAUVOIR.
Vous vous étiez rencontré lors des comités de lecture des éditions Gallimard, et ce fut alors le début d'une grande relation.
Pendant votre discussion absolument passionnante, la radio du café diffuse une musique d'un certain Daniel BALAVOINE pour le moins intriguante. Votre amie Simone remarque également que cette chanson est particulière, pensant qu'elle doit cacher quelque chose...

>  Le fichier est au format .raw, correspondant à des données brutes - on peut également avoir des fichiers sans extension. Ces fichiers peuvent être lus dans des logiciels comme GNU-Radio ou Audacity (ce dernier est plus simple d'utilisation).

*Auteur : `Racoon@8287` *

## Conception

C'est un challenge simple pour manipuler <ins>Audacity</ins>.
On a 2 fichiers audio : _flag.wav_ et _LeChanteur.mp3_. Le premier est une voix lisant le contenu du fichier text _flag_ (grâce au logiciel <ins>Balaboka</ins>), le second est la chanson _Le Chanteur_ de Daniel BALAVOINE.
Dans Audacity, j'ai appliqué deux effets sur _flag.wav_ :
- Un changement de vitesse ;
- Une inversion du sens de lecture.

Enfin, j'ai assemblé les deux pistes :
- **A droite.** La chanson de Daniel BALAVOINE;
- **A gauche.** Un morceau de la chanson, puis le flag, puis la fin de la chanson.

Le résultat final est accessible au format mp3 avec le fichier *flag_encode.wav* et le montage dans *Navi.aup3*.
> Les différentes ressources sont disponible dans le dossier Conception.

## Solution

On est face à un fichier comportant des données brutes. La solution la plus simple est de l'ouvrir dans _Audacity_ :
`Fichier > Importer > Données brutes (Raw) ...`
En laissant les paramètres inchangés, on entend la musique _Le Chanteur_. Au premier quart de la chanson, une voix sourde se fait entendre.
> Rq : Le volume baisse légèrement car une des deux pistes ne comporte plus la musique, mais une voix lisant le flag encodé. Un coup d'oeil sur le spectrogramme affirme cette observation.

En important de nouveau le fichier audio, mais cette fois ci en précisant le mode stéréo, on observe 2 pistes dont une anormale. En isolant cette partie, et accélérant la vitesse et en inversant le sens de lecture, on entend une voix récitant une suite de caractères. On obtient le flag en passant par exemple par [Cyberchef](https://gchq.github.io/CyberChef/).

`404CTF{1tr0_4Ux_R4d10-fR3qU3Nc35}`

@Racoon-r
