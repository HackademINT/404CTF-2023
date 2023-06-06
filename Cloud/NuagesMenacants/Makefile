user := proust

image: ubuntu.qcow2 cloud-config.img downloads/QEMU_EFI.fd keys/id_ecdsa setup-ssh.sh
	./start-ssh.sh > /dev/null & \
	until SSH_AUTH_SOCK="" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${user}@localhost -p 5555 -i keys/id_ecdsa < setup-ssh.sh;\
	do \
    	echo "Waiting for VM to be up...";\
        sleep 2;\
  	done; \
  	echo "Waiting for Qemu to exit...";\
  	wait

cloud-config.yaml: keys/id_ecdsa.pub
	./render-config.sh ${user}

keys/id_ecdsa keys/id_ecdsa.pub:
	ssh-keygen -C "404ctf@404ctf.fr" -f keys/id_ecdsa -t ecdsa -P ""

cloud-config.img: cloud-config.yaml
	cloud-localds --disk-format qcow2 cloud-config.img cloud-config.yaml

ubuntu.qcow2: downloads/ubuntu.img
	qemu-img convert -O qcow2 downloads/ubuntu.img ubuntu.qcow2
	qemu-img resize ubuntu.qcow2 3G

downloads/ubuntu.img:
	wget 'https://cloud-images.ubuntu.com/releases/18.04/release/ubuntu-18.04-server-cloudimg-arm64.img' -O downloads/ubuntu.img

downloads/QEMU_EFI.fd:
	wget 'https://releases.linaro.org/components/kernel/uefi-linaro/16.02/release/qemu64/QEMU_EFI.fd' -O downloads/QEMU_EFI.fd

clean-downloads:
	rm  downloads/QEMU_EFI.fd \
		downloads/ubuntu.img

clean:
	rm  keys/id_ecdsa \
		keys/id_ecdsa.pub \
		cloud-config.img \
		cloud-config.yaml \
		ubuntu.qcow2 \
		setup-ssh.sh

clean-all: clean clean-downloads