#!/bin/bash

DISK="/tmp/$$.qcow2"

cleanup() {
  rm -f "$DISK"
  exit 0
}

trap cleanup SIGHUP SIGINT
stty intr ^]

cp ubuntu.qcow2 "$DISK"

/usr/bin/qemu-system-aarch64 \
    -smp 4 \
    -m 2048 \
    -M virt \
    -cpu cortex-a57 \
    -bios /home/404ctf/QEMU_EFI.fd \
    -nographic \
    -monitor none \
    -device virtio-blk-device,drive=image \
    -drive if=none,id=image,file="$DISK" \
    -nic none \
    -loadvm speed_up_start

cleanup
