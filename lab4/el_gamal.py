import bisect
import random


def get_primes(start, stop):
    if start >= stop:
        return []

    primes = [2]

    for n in range(3, stop + 1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)

    i = bisect.bisect_left(primes, start)
    return primes[i:]


def are_relatively_prime(a, b):
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def get_relatively_prime(n):
    while True:
        res = random.randint(2, n - 1)
        if are_relatively_prime(res, n):
            return res


def generate_private_key(length):
    key_min = 1 << (length - 1)
    key_max = (1 << length) - 1
    primes = get_primes(key_min, key_max)
    p = random.choice(primes)
    return PrivateKey(p)


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g


class PrivateKey:
    def __init__(self, p):
        self.p = p
        self.g = primitive_root(self.p)
        self.x = get_relatively_prime(self.p - 1)
        self.y = (self.g ** self.x) % self.p

    def get_session_key(self):
        return SessionKey(self.p, self.g, self.y)

    def decrypt(self, text_and_key):
        a, b = text_and_key
        return ''.join([chr((letter * (a ** (self.p - 1 - self.x))) % self.p) for letter in b])


class SessionKey:
    def __init__(self, p, g, y):
        self.p = p
        self.g = g
        self.y = y
        self.k = get_relatively_prime(self.p - 1)
        self.a = (self.g ** self.k) % self.p

    def encrypt(self, text):
        return self.a, bytes([(self.y ** self.k * ord(letter)) % self.p for letter in text])
