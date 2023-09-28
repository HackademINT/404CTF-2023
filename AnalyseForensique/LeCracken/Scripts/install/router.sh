## Arguments :
##  - $1 : DHCP server

echo "############################"
echo "#  Package  installations  #"
echo "############################"

export DEBIAN_FRONTEND=noninteractive
apt update
apt install -y \
  tcpdump \
  firewalld \
  vim \
  isc-dhcp-relay \
  bind9 \
  python3 python3-pip \
  screen

echo "############################"
echo "#   Kernel configuration   #"
echo "############################"

# Routing
{
  echo "net.ipv4.ip_forward=1"
  echo "net.ipv6.conf.all.forward=1"
  echo "net.ipv4.conf.all.accept_redirects=1"
  echo "net.ipv6.conf.all.accept_redirects=1"
  echo "net.ipv4.conf.all.send_redirects=1"
  echo "net.ipv6.conf.all.send_redirects=1"
  echo "net.ipv4.conf.all.accept_source_route=1"
  echo "net.ipv6.conf.all.accept_source_route=1"
} > /etc/sysctl.d/00-router.conf

# Reload kernel settings
sysctl --system

echo "############################"
echo "#  Firewall configuration  #"
echo "############################"

# Create zones
firewall-cmd --permanent --new-zone=management
firewall-cmd --permanent --new-zone=users

# Assign zones to interfaces
firewall-cmd --permanent --zone=external --change-interface=eth0
firewall-cmd --permanent --zone=management --change-interface=eth1
firewall-cmd --permanent --zone=users --change-interface=eth2

# Accept all traffic on internal interfaces
firewall-cmd --permanent --zone=users --set-target=ACCEPT
firewall-cmd --permanent --zone=management --set-target=ACCEPT

# Apply rules
firewall-cmd --reload

echo "############################"
echo "# DHCP relay configuration #"
echo "############################"

{
  echo "SERVERS=\"$1\""
  echo 'INTERFACES="eth1 eth2"'
} > /etc/default/isc-dhcp-relay

# Restart server
systemctl restart isc-dhcp-relay

echo "##############################"
echo "#  DNS server configuration  #"
echo "##############################"
cp /vagrant/configs/bind9.conf /etc/bind/named.conf.options
cp -r /vagrant/Malware/C2 /opt/c2
python3 -m pip install -r /opt/c2/requirements.txt
mkdir -p /var/log/named
chown bind:bind /var/log/named/
systemctl restart bind9
