from sage.all import EllipticCurve, GF
import hashlib
from Crypto.Cipher import AES
from secret import FLAG
from os import urandom

p = 231933770389389338159753408142515592951889415487365399671635245679612352781
a = ?
b = ?

determinant = 4 * a**3 + 27 * b**2
assert determinant != 0

E = EllipticCurve(GF(p), [a,b])
G = E.random_point()
H = E.random_point()

print(G.xy()[0], G.xy()[1])
print(H.xy()[0], H.xy()[1])
print(p)

iv = urandom(16)
key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
cipher = aes.encrypt(FLAG)
print(cipher.hex())
print(iv.hex())



