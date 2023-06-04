from fastecdsa.curve import P521
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
from os import urandom


flag = b"404CTF{N_0ub1ie_j4m415_C3lu1_qu1_cr017_5@v0ir_n'4ppr3nd_plu5.}"


class Curve:

    def __init__(self, a, b, d, sk, seed):
        self.C = P521
        self.G = P521.G
        self.q = P521.q
        self.a = a
        self.b = b
        self.d = d
        self.sk = sk
        self.k = seed
        self.pk = sk * self.G

    def get_next_a(self):
        self.a = (self.a + self.d) % self.q

    def get_next_nonce(self):
        self.get_next_a()
        self.k = (self.a * self.k + self.b) % self.q

    def sign(self, m):
        self.get_next_nonce()
        assert self.q > m > 0
        P = self.k * self.G
        r = P.x
        assert r > 0
        s = (pow(self.k, -1, self.q) * (m + self.sk * r)) % self.q
        assert s > 0
        return r, s

    def encrypt_flag(self, flag):
        iv = urandom(16)
        key = sha256(str(self.sk).encode()).digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv=iv)
        ciphertext = aes.encrypt(pad(flag, 16))
        return ciphertext.hex(), iv.hex()


q = P521.q
C = Curve(randint(0, q), randint(0, q), randint(0, q), randint(0, q), randint(0, q))
f = open("data.txt", "w")
messages = [pow(C.d, i, q) for i in range(1, 5)]
signatures = [C.sign(m) for m in messages]
for i in range(4):
    f.write(f"{messages[i]} : {signatures[i]}\n")
cipher, iv = C.encrypt_flag(flag)
f.write(iv+"\n")
f.write(cipher)




