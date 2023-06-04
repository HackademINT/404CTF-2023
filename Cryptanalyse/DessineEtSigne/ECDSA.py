from random import randint
from hashlib import sha256


def bytes_to_long(b):
    return int(b.hex(),16)


def long_to_bytes(n):
    return n.to_bytes(32, byteorder='big')


def bxor(b1, b2):
    b1, b2 = b1[:min(len(b1), len(b2))], b2[:min(len(b1), len(b2))]
    return bytes([a ^ b for (a, b) in zip(b1, b2)])


def inverse(a, n):
    return pow(a, n-2, n)


class Point:

    def __init__(self, x, y, neutral=False):
        self.x = x
        self.y = y
        self.neutral = neutral

    def __eq__(self, Q):
        if isinstance(Q, Point):
            return self.x == Q.x and self.y == Q.y
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def is_neutral(self):
        return self.neutral


class Curve:

    def is_on_curve(self, P):
        return P.y**2 % self.p == (P.x**3 + self.a * P.x + self.b) % self.p

    def __init__(self, a, b, p, n, G):
        assert 4*a**3 + 27*b**2 != 0
        self.a = a
        self.b = b
        self.p = p
        self.n = n
        assert self.is_on_curve(G)
        assert self.double_and_add(n, G) == Point(0, 1)
        self.G = G
        self.d1 = randint(1, p - 1)
        self.d2 = randint(1, p - 1)
        self.PK = self.double_and_add(self.d1, G)

    def add_points(self, P, Q):
        if P.is_neutral():
            return Q
        if Q.is_neutral():
            return P
        assert self.is_on_curve(P) and self.is_on_curve(Q)
        if P.x == Q.x and P.y != Q.y:
            return Point(0, 1)
        if P != Q:
            l = (Q.y - P.y) * inverse(Q.x - P.x, self.p)
        else:
            l = (3 * P.x ** 2 + self.a) * inverse(2 * P.y, self.p)
        x = (l ** 2 - P.x - Q.x) % self.p
        y = (l * (P.x - x) - P.y) % self.p
        return Point(x,y)

    def double_and_add(self, k, P):
        b = bin(k)[2:][::-1]
        res = Point(0, 0, neutral=True)
        tmp = P
        for bit in b:
            if bit == '1':
                res = self.add_points(res, tmp)
            else:
                _ = self.add_points(res, tmp)
                # Learnt this trick to avoid Side-Channel Attack!
            tmp = self.add_points(tmp, tmp)
        return res

    def compute_nonce(self, m):
        tmp_nonce = sha256(m + long_to_bytes(self.d1)).digest()
        nonce = tmp_nonce[:-6]
        add_on = b""
        for i in range(6, 0, -1):
            add_on += bytes(tmp_nonce[tmp_nonce[-i] % len(tmp_nonce)])
        nonce += bxor(add_on, long_to_bytes(self.d2)[-6:])
        return nonce

    def sign(self, m):
        nonce = bytes_to_long(self.compute_nonce(m))
        h = bytes_to_long(sha256(m).digest())
        P = self.double_and_add(nonce, self.G)
        r = P.x % self.n
        assert r != 0
        s = inverse(nonce, self.n) * (h + r * self.d1) % self.n
        assert s != 0
        return r, s

    def verify(self, sign, m):
        r, s = sign
        e = bytes_to_long(sha256(m).digest())
        u1, u2 = e * inverse(s, self.n) % self.n, r * inverse(s, self.n) % self.n
        P = self.add_points(self.double_and_add(u1, self.G), self.double_and_add(u2, self.PK))
        return r % self.n == P.x % self.n











