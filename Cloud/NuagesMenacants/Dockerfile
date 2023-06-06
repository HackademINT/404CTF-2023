FROM debian:bullseye-20230320-slim

RUN apt update && apt install -y openssh-server qemu-system-arm && apt clean

COPY sshd_config ssh_banner /etc/ssh/
RUN ssh-keygen -A

RUN useradd -U -m 404ctf && \
    echo '404ctf:4GqWrNkNuN' | chpasswd && \
    mkdir /run/sshd

COPY ubuntu.qcow2 downloads/QEMU_EFI.fd ssh-entrypoint.sh /home/404ctf/
RUN chmod +x /home/404ctf/ssh-entrypoint.sh

CMD /usr/sbin/sshd -De