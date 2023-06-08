
# Gestionnaire de perruche de Sparrman

Logiciel abordé :

- GNSS SDR

Figures littéraires :

- Alexandre DUMAS
- Simone DE BEAUVOIR

## Énoncé

Avec l'approche du rude Été, une grande soif vous gagne. Heureusement, vos synapses au sein de votre gigantesque cerveau sont très réactive : vous allez donc au café littéraire, dans l'espoir de croiser votre amie Simone. L'histoire n'aurait évidemment pas lieu si elle n'y était pas, c'est pour cela qu'à votre plus grande joie, vous voilà face à face avec Madame DE BEAUVOIR.
Hélàs, celle ci semble inquiète. Vous le savez si  bien dorénavant, celle-ci partage un amour poignant avec le grand Jean-Paul SAT, et ce dernier semble impliqué dans une certaine association.
L'idée est simple, et de par sa simplicité, elle devient difficile. Alexandre DUMAS, de par sa taille, son charisme, et son génie, viendra donc pour mettre au point la finalité d'un plan afin de voler des données confidentielles.
Pour l'heure, Simone a pu trouver une perruche, mais pas n'importe laquelle ! Une perruche de Sparrman. La particularité de ce _Cyanoramphus novaezelandiae_ est qu'il est particulièrement familier, il est donc parfait pour suivre cet incorruptible corrupteur qu'est Jean-Paul SAT.

Pendant cette harangue, le sommeil vous gagne. A votre réveil, vous entendez les dernières paroles :
"... seulement 8 millions d'échantillonnage par seconde ! Du génie n'est ce pas ? Pas la peine de m'applaudir, vous allez me faire rougir ! Bon par contre du fait de la taille de l'animal, du pelage innexistant, de son plumage, du ramage qui s'en rapporte, le signal sera sûrement de mauvaise qualité. Mais vous avez des talents, j'en suis certaine. Oh, et voila Alexandre qui arrive bientôt. Dernière précision : c'est du 8 bits, en complexe. Bonne chance !"

Elle se lève pour étreindre son honneur décoré _Chevalier de la Légion d'honneur_, qui n'est autre que ce très cher Alexandre DUMAS.

Vous voilà fort dépourvu. Une mission de taille, très technique, et aucune information car vous avez le sommeil facile. Vous prenez votre décaième café, et sortant votre ordinateur personnel dont le poids et la taille permettent un transport facile notamment en extérieur, vous vous lancez dans ce laborieux travail en quête d'un lieu où se trouverait le terminus de long et perilleux voyage de notre perruche de Sparrman.


> Format: 404CTF{hotel_d_orsay}

*Auteur : `Racoon@8487`*

## Conception

Challenge intéressant à mettre en place. Une première étape fut de détecter les satellites GPS et Galileo avec le HackRF. Peu concluant. Finalement, le site de la NASA met à disposition les éphémérides quotidien. Ces fichiers permettent d'avoir la position des satellites à partir d'une station d'acquisition.
Le logiciel [_gps-sdr-sim_](https://github.com/osqzss/gps-sdr-sim) permet de simuler les données brutes reçut par l'antenne en une position (x,y,z), dont la position évolue avec le temps (pour une durée maximum de 300s).
Pour obtenir une tracé, le logiciel [_ECEF Path Generator_](https://github.com/fpdf-easytable/ECEF_path_generator) permet d'obtenir un déplacement suivant (x,y,z,t). On obtient ainsi le trajet de notre perruche.
Enfin, pour vérifier le bon fonctionnement, l'utilisation du logiciel [_GNSS SDR_](https://gnss-sdr.org/) permet d'obtenir le résultat final, à savoir le déplacement de la perruche.

Difficultés rencontrées :

- Certaines éphémerides ne donnent aucune données brutes. La raison est que le satellite GPS L1 C/A permettant d'obtenir une position GPS à une date précise, au position (x,y,z), n'est pas détecté par la station d'acquisition ;
- Pour ces mêmes coordonnées, on peut avoir de nombreux satellites disponibles. Le fichier de configuration proposé pour [_My first position fix_](https://gnss-sdr.org/my-first-fix/) permet de trouver directement la position. Moins intéressant.
- D'autres éphémérides donnent seulement 2 ou 3 satellites. C'est insuffisant, vu mon niveau il est trop compliqué de bien configurer le fichier .conf.
- **Solution retenue :** Garder une acquisition permettant d'être résolu avec le fichier de configuration de _My first position fix_, mais en ajoutant du bruit. Pour ce faire, une fois le fichier de données brutes formé, on le passe sous _GNU Radio_ où on ajoute du bruit gaussien. Le résultat est ainsi satisfaisant : le fichier de configuration détecte quelque chose mais ne parvient pas à trouver la position, il faut ainsi fouiller la documentation du site et trouver le bon filtre pour éliminer le bruit.

> Le dossier Conception comporte les différentes resources, à savoir :
>
> - Les éphémérides utilisé (brdc1210.23n)
> - Le fichier de configuration gnss_gps.conf
> - Le résultat de GNSS-SDR pvt.datxxx.gpx
> - Le fichier ECEF Record.csv
> - Le graphe GNU Radio pour ajouter du bruit gaussien AddNoise.grc et AddNoise.py

## Solution

On veut une position, celle de la perruche. L'initial du challenge est GPS. On peut donc se tourner vers un logiciel tel que GNSS-SDR. Le site propose une sorte de _Hello World_ avec _My first position fix_ (voir le paragraphe Conception). On a ainsi une fichier de configuration a tester.
Les informations à disposition sont la fréquence d'échantillonnage (8 MSps), le type de données (8 bits, I/Q), et le fait que le signal est de mauvaise qualité. Avec les deux premières informations, on peut configurer le fichier et presque avoir des résultats. Le dernier points apporte la précision de la mauvaise qualité, laissant penser à du bruit. Le filtre [Notch Filter Lite](https://gnss-sdr.org/docs/sp-blocks/input-filter/#implementation-notch_filter_lite) permet de résoudre ce problème. On trouve ainsi l'évolution (x,y,z,t) de notre très chère perruche de Sparrman. Attention à bien lire le chemin dans le bon sens.

> Rq: On peut utiliser GNSS-SDR Monitor pour avoir un rendu direct. Pour ce faire, il suffit de récupérer le dépot officiel [ici](https://github.com/acebrianjuan/gnss-sdr-monitor), puis de modifier le fichier de configuration afin d'ajouter les ports de connexions (le README est complet à ce sujet).

Flag : `404CTF{ecole_de_kouaoua}`

@Racoon
