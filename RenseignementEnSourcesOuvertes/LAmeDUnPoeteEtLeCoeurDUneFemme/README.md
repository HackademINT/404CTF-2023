# L'âme d'un poète et le cœur d'une femme


# 1/ L'âme d'un poète et le cœur d'une femme [1/4]

## Énoncé : 
Une jeune femme s'approche de votre table : « Bonjour, j'ai cru comprendre que vous aviez fait vos preuves lors de précédentes enquêtes. J'aurais besoin de votre aide. Connaissez vous une certaine 'Louise Colet' ? J'ai appris qu'elle commencait à utiliser les réseaux sociaux. Pouvez vous m'aider à trouver plus d'informations sur elle ? »

> Trouvez un flag au format 404CTF{..}

## Solution :
Sur le compte Facebook de Louise Colet on trouve le flag suivant.

Il es situé dans ses infos, à la ligne citations préférées :
404CTF{4_mon_ch3r_4mi_v1ctor}


# 2/L'âme d'un poète et le cœur d'une femme [2/4]

## Énoncé :
« Vous avez réussi à trouver toutes ces informations ? Félicitations ! Mais avez vous entendu parler de l'évènement organisé par Mme Colet ? »

Trouvez la date de l'évènement ainsi que le nom du compte qui le mentionne.

> **Format** : 404CTF{12_decembre_HackademINT}

## Solution :
Sur le compte Instagram Colet_louise il y a une seule publication : une invitation pour ses amis et connaissances à son salon littéraire. 

Sur la photo on peut lire que l'évènement a lieu le 25 mai 2023.

Le flag est donc : 404CTF{25_mai_colet_louise}


# 3/ L'âme d'un poète et le cœur d'une femme [3/4]

## Énoncé :
« C'est exactement ça ! 'Le salon littéraire de Louise Colet'. Pensez vous pouvoir me trouver une invitation ? »
 
Trouvez une invitation pour rejoindre le salon


## Solution :
En cherchant louise Colet sur Github, c'est le 1er résultat :
https://github.com/LouiseRevoil/Salon-litteraire-de-Louise-Colet

On trouve sur le README une invitation pour un serveur discord ainsi que le flag.

404CTF{B13nv3nue_d4ns_le_s4lon_l1tter4ir3_de_lou1se_C0l3t}

# 4/ L'âme d'un poète et le cœur d'une femme [4/4]

## Énoncé :
« Je vous remercie pour l'invitation ! Avez-vous pu vous en procurer une ? J'ai entendu dire que Mme Colet tenait ce salon pour permettre à des personnes talentueuse de se rencontrer. Je suis sûre qu'elle sera ravie de faire votre connaissance, vos talents ne sont plus à démontrer. Peut-être qu'en répondant à ses questions, vous pourrez obtenir un cadeau de sa part ? »
 

Obtenir un cadeau de la part de Louise Colet

## Solution : 
On effectue une escalade de privilèges sur le serveur discord : En répondant correctement aux questions de Louise on obtient l'accès à de nouveaux salons jusqu'à obtenir le flag.


###  1) le_petit_salon
Savez-vous en quelle année un promeneur inoccupé qui, sortant du jardin des Tuileries, se serait dirigé sous les arcades de la rue de Rivoli, aurait pu apercevoir sous la porte cochère d'un des plus beaux hôtels du quartier, un grand vieillard à la chevelure et à la moustache blanches ?

*Format* : 2002

> flag : 1853

C'est une phrase tirée du livre *Un drame dans la rue de Rivoli*

### 2) le_boudoir
Complétez la suite du poème :
Il faut laisser à l'homme la gloire,
Les triomphes, le bruit,

*Format* : tout sur une ligne, majuscule au début des vers, laisser les espaces et la ponctuation


> flag : Pour nous, aimer et croire Au bonheur nous conduit.

Extrait du poème *La voix d'une mère*


### 3) le_fumoir
Où et quand ai-je rendu visite à Mon ami Victor Hugo pour la première fois ?

*Format* : Paris_2002

> flag : Guernesey_1857

On peut trouver cette information dans un recueil de correspondances de Louise Colet :

https://gallica.bnf.fr/ark:/12148/bpt6k8572147/f7.item.zoom (p203 - dans les toutes premières pages consultables)


## la bibliothèque
Flag final dans le salon :  404CTF{j3_su1s_ravie_d_av0ir_fait_v0tre_connaiss4nce}
