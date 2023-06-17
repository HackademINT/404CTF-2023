#!/bin/bash

Caligula=Caius

listePersonnes="Cherea Caesonia Scipion Senectus Lepidus Caligula Caius Drusilla"

echo "Bonjour Caligula, ceci est un message de Hélicon. Je sais que les actionnaires de ton entreprise veulent se débarrasser de toi, je me suis donc dépêché de t'obtenir la lune, elle est juste là dans le fichier lune.txt !

En attendant j'ai aussi obtenu des informations sur Cherea, Caesonia, Scipion, Senectus, et Lepidus, de qui veux-tu que je te parle ?"
read personne
eval "grep -wie ^$personne informations.txt"

while true; do
    echo "
De qui d'autre tu veux que je te parle ?"
    read personne

    if [ -n $personne ] && [ $personne = "stop" ] ; then
    exit
    fi

    bob=$(grep -wie ^$personne informations.txt)
    
    if [ -z "$bob" ]; then
        echo "Je n'ai pas compris de qui tu parlais. Dis-moi stop si tu veux que je m'arrête, et envoie l'un des noms que j'ai cités si tu veux des informations."
    else
        echo $bob
    fi  

done


    