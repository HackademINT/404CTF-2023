# Container forensics

## 1ère partie

### Intitulé

Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.

Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.

La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.

Votre mission consiste à exploiter le fichier fourni pour y retrouver les traces du maître chanteur.

### Solution

Fournir le tar et voir https://kubernetes.io/blog/2023/03/10/forensic-container-analysis/ pour résoudre le challenge, le flag étant dans la mémoire d'un des processus ou dans le fichier de log.

`strings checkpoint/page* | grep 404`

## 2ème partie

### Intitulé

Après vos premières découvertes, vous faites votre rapport à la Comtesse de Ségur. Vous lui expliquez que quelqu'un a réussi à lui voler ses derniers livres grâce à une faille dans son application. La Comtesse de Ségur vous demande alors de trouver où ont été exfiltrées ses livres et de vous infiltrer sur ce serveur.

### Déploiement

Déployer le C2 avec les ports 1337 à 1339 et 31337 exposés

### Résolution

Reverse le binaire `agent` fourni dans le tar, comprendre le fonctionnement du C2 (port-knocking du port 1337 à 1339 dans l'ordre), puis se connecter au C2 pour récupérer le flag via nc sur le port 31337 (le flag est envoyé à la connexion si le port-knocking a été fait précédemment)
