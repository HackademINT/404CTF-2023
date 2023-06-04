import nclib as nc

n = nc.Netcat('challenges.404ctf.fr',31420)

while 1:
    chall = n.recv_until(b'>')
    if b'tromper' in chall:
        print("houla")
        exit()
    if b'>' not in chall:
        break
    nb = chall.count(b')')
    n.sendline(str(nb).encode())
print(chall.decode('utf-8').split('é')[4].strip())
