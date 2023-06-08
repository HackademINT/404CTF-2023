# FROM bitnami/minideb <- libc trop ancienne
FROM debian:bookworm-slim

RUN apt update && apt install -y ncat && apt clean

COPY vm shellcode_my_vm.vmr Eont3ih4 /
RUN chmod +x /vm

USER 65534:65534
EXPOSE 31337

ENTRYPOINT ncat -lkvp 31337 -e '/vm shellcode_my_vm.vmr'