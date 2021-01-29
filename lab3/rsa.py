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


def make_key_pair(length):
    n_min = 1 << (length - 1)
    n_max = (1 << length) - 1

    start = 1 << (length // 2 - 1)
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start, stop)

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise ValueError(f"cannot find 'p' and 'q' for a key of length={length}")

    stop = (p - 1) * (q - 1)
    for e in range(3, stop, 2):
        if are_relatively_prime(e, stop):
            break
    else:
        raise ValueError(f"cannot find 'e' with p={p} and q={q}")

    for d in range(3, stop, 2):
        if d * e % stop == 1:
            break
    else:
        raise ValueError(f"cannot find 'd' with p={p}, q={q} and e={e}")

    return PublicKey(e, p * q), PrivateKey(d, p * q)


class PublicKey:
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def encrypt(self, text):
        return bytes([pow(ord(letter), self.e, self.n) for letter in text])


class PrivateKey:
    def __init__(self, d, n):
        self.d = d
        self.n = n

    def decrypt(self, text):
        return ''.join([chr(pow(letter, self.d, self.n)) for letter in text])
