
# Sous son trépas victorieux

Logiciels abordés :

- GQRX
- QSSTV _(ou autre logiciel du même type)_

## Énoncé

Comme à votre habitude, lors du mois de quatorzembre, vous vous levez à l'aurore. Lors de cette belle et douce matinée, un souvenir vous revient, datant de vos dernières courses dans votre supermarché préféré.
Au fin fond de l'allée pour les produits frais, vous aperceviez votre amie Simone DE BEAUVOIR. Celle ci, un panier presque vide à la main, vous attend un grand sourire au visage. La connaissant bien, vous saviez qu'elle attendait quelque chose de vous. Et de fait, elle vous tend une clé USB en vous suppliant de l'aider à récupérer la photo à l'intérieur.

_"C'est au sujet de mon ami Alexandre ! Il a disparu et j'ai besoin de le retrouver, aide moi !"_ clame - t - elle.

Pressé de partir, vous l'entendez murmurer en sortant du magasin :

_"Sous son trépas victorieux, il est honoré au Panthéon..."_

De plus en plus étrange...
En scrutant attentivement ce support de stockage amovible inventé dans les années 2000, vous remarquez qu'il contient un dossier nommé **H4SGEL_S1**.

Pris au dépourvu, vous vous mettez à chercher ce que votre très chere compagne souhaitait.

_Auteur: `Racoon@8487`_

## Conception

Le principe est celui de la transmission satellite : l'image est décomposé en pixels, chacun d'entre eux est ensuite associé à une fréquence. Pour recevoir ce signal, on utilise un logiciel SSTV (tel _QSSTV_)
Couplé à ce dispositif, il y a une <ins>modulation fréquentielle</ins> (WBFM) et un <ins> décalage fréquentiel</ins> (Frequency Shift)
- **WBFM** _(Wideband Frequency Modulation)_. Cela permet une modulation en fréquence. La différence avec le NBFM réside dans le filtre passe-bas nécessaire pour la modulation. Dans _GNU Radio_, c'est le bloc _WBFM Transmit_.
- **Frequency Shift.** Cela permet de décaler la fréquence du signal. Dans _GNU Radio_, c'est le bloc _Frequency Shift_.
Un bloc SigMF permet d'obtenir deux fichiers : les données brutes, et un fichier texte contenant les caractéristiques du signal.

> Les différents éléments tel que le graphe _GNU Radio_ ou bien la police et la photo sont disponibles dans le dossier Conception

## Solution

Pour effectuer les tests, j'ai utilisé GQRX et QSSTV.

- On commence par ouvrir le fichier dans GQRX, en précisant la fréquence d'échantillonnage. Pour ceci, on va dans "Configure I/O devices", et dans le champ "Device string" on renseigne les informations.
- Dans "Receiver Options", on choisit le mode "WFM Mono", et on décale le curseur rouge de 40 kHz pour obtenir le signal satellite.
- Sous "Audio", le bouton "Rec" permet d'enregistrer le signal dans un fichier audio.
- Pour finir, avec le logiciel QSSTV (Linux), on peut lire le fichier et obtenir le flag.

@Racoon
