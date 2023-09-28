# Le Cracken

## Énoncé

Au milieu du café trône une table depuis laquelle un homme scrute ses semblables en engloutissant un breuvage étrange. Vous l'observez du coin de l'œil depuis plusieurs minutes déjà quand la porte du café s'ouvre avec fracas. Un homme surgit alors, criant comme si le café était tout à lui.

« Capitaine ! »

Vous comprenez immédiatement qu'il s'adresse à votre homme, qui aborde par ailleurs la plus belle casquette de marin qu'il vous ait été donné d'observer.

« Du respect matelot ! rétorque-t-il. Ne troublez pas ainsi mes hôtes !

— Mes excuses capitaine, ainsi qu'à ces messieurs et dames, mais je me dois de vous informer des évènements qui viennent de frapper le nautilus. Notre nouveau mousse a voulu profiter de notre rare escale pour utiliser internet, et je lui ai ouvert une session sur le système, mais cet inconscient s'est laissé attraper par un courriel agicheur et j'ai bien peur que le nautilus ait été compromis par un pirate !

— Comment ! s'exclame alors le capitaine Némo, dont la barbe finement taillée contient à peine la colère qui rougit ses joues. Vous ne pouvez donc vous tenir cinq minutes ! Je suppose que vous avez pris les mesures adéquates ?

— Bien sûr capitaine, j'ai pris soin de faire un dump de la machine affectée et ait entrepris de capturer le réseau passant par le routeur, nous devrions pouvoir investiguer l'affaire. Connaissez-vous quelqu'un qui pourrait mener l'analyse ? Commandez et j'irai à sa rencontre. »

Vous même féru d'analyse forensique lors de vos temps perdus, vous marmonnez alors :

« Je pourrais bien m'en charger, moi. »

Némo vous entends, et ni une, ni deux, son regard vous fusille.

« Attention, on ne parle pas en vain ici, vous allez vous y coller ! »

Le matelot vous remet alors une clé USB...


Analysez les données remises par le matelot et retrouvez précisément le document exfiltré par le Malware à son C2.

> Attention, ce challenge contient du code à visée malveillante. Bien que le concepteur ait fait de son mieux pour qu'ils soient inoffensifs, il vous appartient de prendre les précautions nécessaires à l'analyse des fichiers proposés.

> [Cracken.7z](https://github.com/HackademINT/404CTF-2023/releases/download/cracken/Cracken.7z) sha256: `28356457d3263a074dcc90846d766f07`

Auteur: `Smyler#7078`

## Sources et dépôt

- `Malware/Agent/` code source C++ du malware à examiner dans le challenge
- `Malware/C2/` code source Python du serveur de command & control du malware
- `Vagrantfile` décrit l'infrastructure virtualisée Active Directory dans lequel le scénario du challenge a été exécuté
- `Scripts/` contient des scripts utilisés lors de l'installation de infrastructure
- `Flag/` contient le PDF du flag ainsi que ses fichier sources (image générée avec Midjourney)
- `Network.png` schéma de l'infrastructure
- `solve.py` script python de déchirement de l'échange entre le malware et le C2 utilisé pour testé le challenge

Les fichiers binaires distribues lors du CTF sont trouvable dans [les Releases GitHub](https://github.com/HackademINT/404CTF-2023/releases/tag/cracken).

## Writeups

Il y avait plusieurs manières de résoudre le challenge, et plusieurs participants ont pris le temps d'écrire de formidable writeups assez complémentaires :
- [Narthorn](https://github.com/Narthorn/ctf/tree/master/2023-05-10_404CTF-2023/01.%20forensics/Le%20Cracken) (*la partie hardmode vaut le détour*)
- [TaylorDeDordogne](https://nudistbeaaach.github.io/write-ups/cracken/)
- [TechieNeurons](https://github.com/TechieNeurons/404CTF_2023_write_ups/tree/main/forensics/le_cracken)

