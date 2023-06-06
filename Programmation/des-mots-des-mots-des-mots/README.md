# Des mots, des mots, des mots

## Énoncé

Prenant du bon temps à votre table en lisant un livre, vous buvez une gorgée de café. En baissant votre tasse, vous remarquez à travers la fenêtre une petite silhouette, elle semble chercher quelque chose ou quelqu'un.

Cette intrigante situation à aller à sa rencontre. La silhouette est en réalité une jeune fille rousse. Vos regards se croisent, elle a l'air perdue. Vous la rejoignez, et lui demandez :

« Bonjour, puis-je t'aider ?</br>
— Oui. Je cherche à traduire un texte selon des règles étranges mot à mot. Il s'agit d'un livre nommé _Les Misérables_. Peut-tu m'aider ? Au fait, moi c'est Cosette !</br>
— Je vois, aucun problème. Je peux justement te faire **un script qui va transformer chaque mot de ton texte**. Quelles sont ces règles ?</br>
— Je vais tout t'expliquer, allons nous installer à l'intérieur.»

Elle vous suit à votre table et vous vous mettez au travail.

> _**Indication** : les voyelles sont {a, e, i, o, u, y}. L'indiçage commence à 0._

<div class="author">Occalepsus#9283</div>

## Flag

404CTF{:T]cdeikm_)W_doprsu_nt_;adei}

## Conception

Le challenge se déroule en 2 phases :

- D'abord l'utilisateur va découvrir le principe et les règles, règle après règle il doit entrer la traduction du mot cosette par cette règle.
- Ensuite une fois les 4 règles validés pour le mot cosette, l'utilisateur se voit donner une suite de mots séparés par des espaces, dont les caractères sont des lettres minuscules non accentuées (ASCII 97 = a à 122 = z). L'utilisateur a 5 secondes pour retourner la liste de ces mots traduits dans ce langage, séparés par un espace.

Les 4 règles sont énoncées dans le fichier [règles.md](règles.md)

## Déploiement

Sur un docker avec un port TCP en lecture/écriture pour les utilisateurs.

_Génération de la solution :_

> Le fichier textSlicer.py sert à transformer des chapitres trouvés sur [ce site](http://www.groupugo.univ-paris-diderot.fr/Miserables/Default.htm) en suite de mots de plus de 5 à 15 caractères sans caractères spéciaux, accents, ou majuscules, séparés par des espaces.
Pour trouver la solution à ces fichiers, utiliser la solution en passant 2 paramètres désignant respectivement les chemins du dossier contenant les fichiers entrée et du dossier qui va contenir les fichiers sortie.

## Solution

Dans le sous dossier ./des-mots-des-mots-des-mots-solution, entrer la commande make pour compiler la solution.

Ensuite lancer le script python solution.py. _Il faudra au préalable installer les bibliothèques python `parse` et `nclib`._

@Occalepsus
