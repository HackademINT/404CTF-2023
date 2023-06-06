#!/bin/sh

echo "Installing K3s"
curl -sfL https://get.k3s.io | sh -
echo 'export KUBECONFIG=.kube/config' > .bashrc
. .bashrc
mkdir ~/.kube 2> /dev/null
sudo k3s kubectl config view --raw > "$KUBECONFIG"
chmod 600 "$KUBECONFIG"

until kubectl get nodes | grep -w "Ready"
do
  echo "Waiting for k3s to boot"
  kubectl get nodes
  sleep 5
done

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

echo "Installing dependencies..."
kubectl create ns 404ctf
kubectl apply -f /tmp/config-k8s/service-account-logs.yaml
kubectl apply -f /tmp/config-k8s/service-account-secrets.yaml
kubectl apply -f /tmp/config-k8s/secrets.yaml
kubectl apply -f /tmp/config-k8s/my-app.yaml

echo "Sleeping for about a minute so the history is at least somewhat believable..."
sleep 63
echo "Done sleeping"

echo "Speed-up boot time"
sudo apt purge -y snapd plymouth ufw lxd
sudo apt autoremove -y
sudo touch /etc/cloud/cloud-init.disabled
sudo systemctl disable sshd

while kubectl get pods -n 404ctf | grep -v 'Running' | grep -q 'my-app'
do
  echo "Waiting for all challenge pods to be running..."
  sleep 5
done

kubectl get pods

OLDSHELL=$(cat /etc/passwd | grep proust)
NEWSHELL=$(echo $OLDSHELL | sed "s#/bin/bash#/opt/shell.sh#")

sudo sed "s#$OLDSHELL#$NEWSHELL#" -i /etc/passwd

echo "Faking bash history..."
cat > .bash_history << EOF
EOF
history -c

echo "All done !"

# Shutdown
(sleep 3 && sudo shutdown now) &
exit