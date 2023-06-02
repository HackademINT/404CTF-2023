# Harpagon Et Le Magot

## Intitulé

![Gravure de l'Avare](https://upload.wikimedia.org/wikipedia/commons/0/07/Harpagon_Pouget.jpg)
<br>

<h3 style="text-align: center">La Flèche.</h3>
<div style="text-align: center; font-style: italic">Brisant le quatrième mur</div>

Hé quoi ! Ce coquin d'Harpagon ne se lassera donc jamais d’importuner les jeunes gens !
Voilà donc maintenant qu'il va jusqu'à louer des serveurs pour mettre ses écus à l’abri,
alors même qu'il refuse à ses propres enfants la moindre dot.
Son fils mon maître est désespéré de ne pouvoir prétendre à sa bien-aimée Mariane, que son père tente de lui ravir.
Sa fille Élise n'est pas mieux traitée, la voilà promise à un ancêtre. Ha non vraiment,
je ne puis me résoudre à les abandonner !
Sachez que j'ai donc mené mon enquête, et je pense avoir trouvé de quoi déstabiliser le coquin.
Je ne crois pas qu'il ait jamais réussi à faire marcher sa machine comme il le souhaitait,
mais elle contient néanmoins sûrement toutes sortes de choses qui pourraient faire avancer notre affaire.
Accepteriez-vous de m'apporter votre que concours pour dévoiler les secrets du vieil avare afin que nos chers amis
puissent plus aisément le raisonner ?

<br>

Mot de passe : `T8h2UKEstg`
Auteur: `Smyler#7078`

## Solution :

On peut regarder `.bash_history` pour avoir une idée de ce qui s'est passé :

```
harpagon@jardin:~$ cat .bash_history 
.bash_history              .profile
.bash_logout               .ssh/
.bashrc                    .sudo_as_admin_successful
.cache/                    values.yaml
.gnupg/                    vaultwarden/
.kube/                     
harpagon@jardin:~$ cat .bash_history 
curl -sfL https://get.k3s.io | sh -
echo 'export KUBECONFIG=.kube/config' > .bashrc
mkdir ~/.kube
sudo k3s kubectl config view --raw > .kube/config
chmod 600 .kube/config
. .bashrc
kubectl cluster-info
sudo curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
kubectl create namespace cassette
kubectl config set-context --current --namespace cassette
sudo apt install git
git clone https://github.com/guerzon/vaultwarden
cp vaultwarden/values.yaml values.yaml
vim values.yaml
helm install cassette vaultwarden --values values.yaml --set ingress.enabled=true
vim values.yaml
helm install cassette vaultwarden --values values.yaml --set ingress.enabled=true
helm upgrade cassette vaultwarden --values values.yaml --set ingress.enabled=true
```

Donc un bitwarden a été déployé avec Helm, puis redéployé après que les valeurs ont été une valeur a été changée.
En regardant le fichier des valeurs, une ligne a un commentaire :

```
adminToken: "Yh6UxUhujjl4UqBrIJFtsWM8xTbvvT" # Bas les pattes, voleur, mon secret ne se trouve plus ici !
```

On peut retrouver l'ancienne valeur via l'historique des release helm :

```
harpagon@jardin:~$ kubectl get secrets
NAME                             TYPE                 DATA   AGE
cassette-vaultwarden             Opaque               3      109m
sh.helm.release.v1.cassette.v1   helm.sh/release.v1   1      109m
sh.helm.release.v1.cassette.v2   helm.sh/release.v1   1      107m
```

On peut récupérer le yaml de la première release avec `kubectl get secret sh.helm.release.v1.cassette.v1 -o yaml,
qui contient un gros bloque de base64 avec toutes les données de la précédente release.

En passant ce bloc deux fois dans un décodeur de base 64 puis en le décompressant avec GZIP, on obtient du texte lisible.
Le flag s'y trouve, il apparaît à plusieurs endroits.
Il est inversé pour éviter que `sudo grep -a 404CTF /dev/vda` donne le flag.
