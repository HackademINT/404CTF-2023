from sys import argv
from Crypto.Cipher import AES
from pyshark import FileCapture
from base64 import b32decode
from math import ceil
from sys import stdout, stderr


def eprint(text):
    stderr.write(text + '\n')
    stderr.flush()


def b32decode_nopad(b32str):
    pad_length = ceil(len(b32str) / 8) * 8 - len(b32str)
    return b32decode(b32str + "=" * pad_length)


IV = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
KEY = bytes.fromhex(
    "6c bb f2 a3 9f c7 a2 a6 4e 92 17 c8 72 48 5e 41 51 ec fe f9 e3 48 e2 07 07 ec 1b d3 65 b1 12 2d"
    .replace(' ', "")
)

# We are making the bet that thing came in order, but sometimes duplicated
seen = set()

capture = FileCapture(argv[1], display_filter="dns")
for packet in capture:
    dns = packet["DNS"]
    name = dns.qry_name
    if not name.endswith(".7.cxu5zdk80j3rtqqm1xk5nikxitq2ub.xyz"):
        continue
    if 'txt' in dir(dns):
        continue
    if name in seen:
        eprint("Ignoring duplicate name")
        continue
    seen.add(name)
    data = name.split('.')[0]
    data = b32decode_nopad(data)
    cipher = AES.new(KEY, AES.MODE_CBC, iv=IV)
    data = cipher.decrypt(data)
    size = data[0]
    data = data[9: size + 1]
    stdout.buffer.write(data)
    stdout.flush()
