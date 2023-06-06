#!/bin/bash

qemu-system-aarch64 \
    -smp 4 \
    -m 1024 \
    -M virt \
    -cpu cortex-a57 \
    -bios downloads/QEMU_EFI.fd \
    -nographic \
    -device virtio-blk-device,drive=ubuntu \
    -drive if=none,id=ubuntu,file=ubuntu.qcow2 \
    -device virtio-blk-device,drive=cloud \
    -drive if=none,id=cloud,file=cloud-config.img \
    -device e1000,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::5555-:22 \
    -monitor unix:/tmp/qemu.sock,server,nowait
