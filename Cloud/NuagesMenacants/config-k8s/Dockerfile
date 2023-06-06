FROM ubuntu:22.04

RUN useradd -U -m proust && \
    echo 'proust:les_nuages' | chpasswd

RUN apt-get update && apt-get install -y findutils openssh-server && ssh-keygen -A && mkdir -p /run/sshd

RUN chmod +s $(which find)

RUN touch /flag.txt && chmod 400 /flag.txt

EXPOSE 22

CMD /usr/sbin/sshd -De