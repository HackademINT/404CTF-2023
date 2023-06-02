#cloud-config

preserve_hostname: false
hostname: jardin
fqdn: 404ctf.local
manage_etc_hosts: true

users:
  - name: %USER%
    ssh_authorized_keys:
      - %SSH_KEY%
    sudo: 'ALL=(ALL) NOPASSWD:ALL'
    groups: sudo
    shell: /bin/bash

bootcmd:
  - sed -i "s/-o '-p -- \\\\\\\\u'/-a %USER%/" /lib/systemd/system/serial-getty@.service
  - chmod -x /etc/update-motd.d/*
  - chmod +x /etc/update-motd.d/00-header

write_files:
  - path: /etc/update-motd.d/01-cloud
    permissions: '0o755'
    content: |
      #! /bin/bash

      # 404 CTF cloud motd

      echo ""
      echo "Ceci est votre instance personnelle d'informatique nuagique publique."
      echo ""
      echo "Elle vous offre un environment Kubernetes prêt à l'emploie pour répondre à tout vos besoins."
      echo ""
      echo "Documentation :"
      echo -e '    * Ubuntu :        https://help.ubuntu.com/18.04'
      echo -e '    * Kubernetes :    https://kubernetes.io/docs/home/'
      echo -e '    * K3s :           https://docs.k3s.io/'
      echo -e '    * Kubectl :       https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands'
      echo -e '    * Helm :          https://helm.sh/docs/'
      echo ""
      echo "Pour quitter votre instance, éteignez le système."
      echo ""
  - path: /etc/systemd/network/10-eth0.netdev
    permissions: '0o644'
    content: |
      [NetDev]
      Name=eth0
      Kind=dummy
  - path: /etc/systemd/network/20-eth0.network
    permissions: '0o644'
    content: |
      [Match]
      Name=eth0

      [Network]
      Address=10.0.0.2/24
      Gateway=10.0.0.1