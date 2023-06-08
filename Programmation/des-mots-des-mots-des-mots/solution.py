import subprocess
from nclib import Netcat
import parse

nc = Netcat(("challenges.404ctf.fr", 30980))

command = "./des-mots-des-mots-des-mots-solution/main"

p = parse.compile("Entrée : {{{input}}}\n")

cosetteIter = ["cosette", "ettesoc", "ttsoc", "ottsc", "PPtt!15QRUWcos"]

step = 0

while step < 6:
    rec_msg = nc.recv_until("\n").decode("utf-8")
    print("Reçu: " + rec_msg)

    r = p.parse(rec_msg)
    if r and "input" in r:
        print("Entrée : " + r["input"])
        send_msg = ""
        if step < 5:
            send_msg = cosetteIter[step]
        else:
            send_msg = subprocess.getoutput(command + " " + r["input"])

        print("Envoi : " + send_msg)
        nc.sendline(send_msg)
        step += 1

rec_msg = nc.recv_until("\n").decode("utf-8")
print("Reçu: " + rec_msg)

rec_msg = nc.recv_until("\n").decode("utf-8")
print("Reçu: " + rec_msg)
