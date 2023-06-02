#!/bin/bash

sed "s#%SSH_KEY%#$(cat keys/id_ecdsa.pub)#" cloud-config.yaml.tpl > cloud-config.yaml
sed "s#%USER%#$1#" -i cloud-config.yaml