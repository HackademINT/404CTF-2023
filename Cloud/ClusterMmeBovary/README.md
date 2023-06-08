# Le Cluster de Madame de Bovary

# Intitulé

Un individu dans un coin vous interpelle et vous invite à sa table. Une fois assis, il vous explique qu'il veut que vous infiltriez le cluster Kubernetes de Madame Bovary. Madame Bovary est une femme riche et influente qui a investi dans la technologie Kubernetes pour gérer les applications de son entreprise de production de médicaments. Vous vous doutez qu'il s'agit sans doute d'un concurrent industriel mais il vous offre une belle récompense si vous réalisez sa demande.

Votre mission consiste à prendre le contrôle du cluster Kubernetes de Madame Bovary et à accéder à ses applications critiques. Vous devrez exploiter toutes les vulnérabilités possibles pour atteindre votre objectif.

Le fichier fourni est une machine virtuelle à charger dans Virtualbox. Cette machine virtuelle contient le cluster Kubernetes du challenge.

    Utilisateur : ctf

    Mot de passe : 404ctf2023


# Solution

Une image Virtualbox avec un k3s installé et l'agent déployé est fourni.

Le but est de déployer the-container et web-server pour récupérer tout le flag.
