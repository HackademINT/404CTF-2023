#!/bin/sh

echo "Installing K3s"
curl -sfL https://get.k3s.io | sh -
echo 'export KUBECONFIG=.kube/config' > .bashrc
. .bashrc
mkdir ~/.kube 2> /dev/null
sudo k3s kubectl config view --raw > "$KUBECONFIG"
chmod 600 "$KUBECONFIG"

echo "Installing Helm..."
# Install Helm
sudo curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

echo "Setting up challenge dependencies..."
sudo apt install git
git clone https://github.com/guerzon/vaultwarden
cp vaultwarden/values.yaml values.yaml

echo "Setting up initial value.yaml..."
sed -i 's/class: "default"/class: "local-path"/' values.yaml
sed -i 's/size: "15Gi"/size: "30Mi"/' values.yaml
sed -i 's#domain: ""#domain: http://cassette.local/#' values.yaml
sed -i 's/hostname: "warden.contoso.com"/hostname: cassette.local/' values.yaml
sed -i 's/host: ""/host: cassette.local/' values.yaml
sed -i 's/from: ""/from: bitwarden@cassette.local/' values.yaml
sed -i 's/adminToken: "R@ndomToken$tring"/adminToken: "##FLAG##"/' values.yaml

# Wait for K3s installation to be over
while kubectl get jobs --all-namespaces | grep -v '1/1' | grep -q 'kube-system'
do
  echo "Waiting for all Kubernetes jobs to have completed..."
  sleep 5
done
echo "Jobs:"
kubectl get jobs --all-namespaces
echo "Pods:"
kubectl get pods --all-namespaces

echo "Installing release..."
kubectl create namespace cassette
kubectl config set-context --current --namespace cassette
helm install cassette vaultwarden --values values.yaml --set ingress.enabled=true
echo "Sleeping for about a minute so the history is at least somewhat believable..."
sleep 63
echo "Done sleeping"

echo "Editing values.yaml..."
sed -i 's/adminToken: "##FLAG##"/adminToken: "Yh6UxUhujjl4UqBrIJFtsWM8xTbvvT" # Bas les pattes, voleur, mon secret ne se trouve plus ici !/' values.yaml

echo "Upgrading release..."
helm upgrade cassette vaultwarden --values values.yaml --set ingress.enabled=true

# Speed-up boot time
sudo apt purge -y snapd plymouth ufw lxd
sudo apt autoremove -y
sudo touch /etc/cloud/cloud-init.disabled
sudo systemctl disable sshd

while kubectl get pods | grep -v 'Running' | grep -q 'cassette'
do
  echo "Waiting for all challenge pods to be running..."
  sleep 5
done

kubectl get pods

echo "Faking bash history..."
cat > .bash_history << EOF
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
EOF
history -c

echo "All done !"

# Shutdown
(sleep 3 && sudo shutdown now) &
exit