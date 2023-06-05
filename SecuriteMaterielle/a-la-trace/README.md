# Trace me in

## Enoncé

Votre regard s'attarde sur un coin reculé du bar. Vous voyez un homme qui a l'air nerveux. Vous vous dirigez alors vers lui pour vous enquérir de la situation.

 - "Bonjour, je n'ai pas le plaisir de vous connaître, puis-je vous demander qui vous êtes ?"
L'homme se retourne et rétorque : 
 - "Et bien, bonjour... Je me prénome Camus, Albert Camus."
 - "Pardonnez moi mais, vous me semblez nerveux."
 - "Excusez, moi. J'ai peut être semblé impoli. La verité c'est que j'attend mon café depuis 4h maintenant."
 - "Mais que se passe-t-il ?"
 - "On m'a dit que cet étrange énergumène de Jean Paul SAT était parti avec la machine à café ! Dites, vous voulez pas vous rendre utile ?"
Vous acceptez.
 - "Rendez vous à cette addresse, et tentez de rentrer chez lui. Je suis certain qu'elle est là bas. Cependant je n'ai jamais réussi à ouvrir sa serrure éléctronique."
Il vous tend un petit papier
 - "J'avais récupéré ça dans son portefeuille, je suis certain qu'il s'agit du mot de passe chiffré. Bonne chance."
 Voici les données du papier : `49 b7 71 9f 90 cc 74 9f ca a4 64 b9 83 7a 9e 5e`

Vous vous dirigez alors vers la maison de Jean-Paul SAT. En effet une drôle de serrure protège la porte.
Vous décidez d'utiliser vos compétences en sécurité materielle à profit.
Tout d'abord, vous entrez un mot de passe érroné, `I_want_my_coffee`. Vous en profitez pour récupérer les traces des signaux éléctriques internes.
Vous êtes convaincu que cela devrait pouvoir suffir à determiner l'algorithme interne de la serurre, et ainsi déchiffrer le mot de passe.

Format du flag: 404CTF{*mot de passe*}
Auteurs: `Astate#3107 et Redhpm#8108`

## Flag

`404CTF{I'm_n0t_4Dd1ct^^}`

## Fichiers

`ChallTrace.py` : Le système en myHDL.

`system.vcd` : Les traces du système.

`Trace_Me_In.py` : Le système avec les variables offusquées.

`Trace_Me_In.vcd` : Les traces offusquées, fichier fourni aux participants.

`solve.py` : Fichier python qui déchiffre le flag.

## Fonctionnement et solution

On peut ouvrir le fichier `.vcd` avec un logiciel tel que GTKwave.
En analysant les composants petit à petit on comprend l'algorithme.

Chaque caractère est xoré avec le précédent, puis on ajoute le précédent.

Pour retrouver le flag, on applique l'algorithme dans le sens inverse.
Le premier caractère est inchangé (xor puis add avec 0).
Pour retrouver le 2ème, on soustrait d'abord le caractère 1 (donc 73), puis on xor avec 73. On trouve 39.
Puis (0x71 - 39) ^ 39 = 109.
Puis (0x9f - 109) ^ 109 = 95

etc...

L'algorithme de déchiffrement est dans `solve.py`
