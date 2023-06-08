

# Encore des portes. Un trauma ?

Logiciels abordés :

- GNU Radio

## Énoncé

Nous y voilà. Le temps s'écoule comme à son habitude, et l'après-midi montre son museau, à l'image d'un renard dans une plaine voyant une petite poule égarée perdu dans la vaste étendue du monde.
A votre table, de manière surprenante et inatendue, vous voyez vos nombreuses tasses tapissé d'une légère marc de café. A votre droite, Alexandre DUMAS est plongé dans une profonde relecture d'une de ses oeuvres : le fameux _Comte de Monte-Cristo_. A votre gauche, Simone DE BEAUVOIR, frottant le papier de sa fine plume aiguisée. Un rapide coup d'oeil vous permet de voir un titre, _Le Deuxième Sexe_, et une phrase qui restera dans votre mémoire : "On ne naît pas femme, on le devient".

Derrière vous, un courrant d'air se fait ressentir : une *porte* s'ouvre, laissant entrer deux hommes élancés. Devant vous, les *portes* menant à la cuisine. Une vague d'angoisse surgit : des _portes_, tout autour de vous. Fort heureusement, Simone dispose d'un cerveau à l'image de Chtulhu : aucun mot ne peut décrire l'indéscriptible surhumain. Vous voyant avec des perles de sueur sur le visage, elle commence à vous rassurer. Vous avez encore cette vision terrifiante de quelqu'un, au sourire plein de fourberie, vous parlant de ses "_amies les portes_".

Une main se pose sur la vôtre. Un sourire appaisant sur le visage de Simone. Elle sort une antenne et clâme :

" J'ai développé cette technologie époustouflante. Regarde. Là, une antenne en émission. Sur ton ordinateur, tu as cette antenne tant utilisé pour nous aider. Je suis sûre que tu vas réussir à récupérer mon signal, c'est une magnifique vidéo. Elle va te détendre. " Sur ce dernier mot, il vous semble percevoir un léger rictus.

"Oh, j'allais oublier, 10.7622 MSps. Ce sera suffisant. Tu vois la télévision sur le comptoir ? C'est le même procédé, mais américain."

Votre angoisse commence à s'apaiser. Vous vous plongez dans cette quête.
Vous entendez quelque part au fin fond de vous : "n'est pas mort ce qui à jamais dort".
Qu'allez vous trouvez au milieu de ces ondes perfides ?

_Auteur: `Racoon@8487`_

## Conception

Nous étudions ici la transmission TV par le protocole ATSC.
Une sombre folie nous a emparé, on a donc filmé des portes. Puis j'ai monté sous Premiere Pro et After Effect pour obtenir un .mp4. Avec le logiciel mp42ts, on convertit pour avoir un fichier de flux vidéo .ts.
Ensuite, le graphe dans le dossier Conception permet de moduler notre signal.

> Dans le dossier Conception se trouve le fichier de transmission tx, reception rx, et les deux fichiers vidéos en .mp4 et .ts.

## Solution

On parle d'une vidéo, et d'une fréquence d'environ 10 MHz, ainsi qu'un procédé américain de diffusion tv. On se penche sur la piste d'une transmission ATSC. Un graphe sous GNU Radio relativement simple permet de récupérer notre signal. Attention, il faut bien récupérer un fichier .ts et non .mp4.

@Racoon
