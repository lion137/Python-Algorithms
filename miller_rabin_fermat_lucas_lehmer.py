# Primality Tests
#
# Copyleft 2018 lion137
#
# 1. Fermat Test


from random import randint


def modularexponenation(base, exponent, modulus):
    """modular exponentiation"""
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


# Fast Exp
def exp(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        a = exp(x * x, n // 2)
        return a
    elif not n % 2 == 0:
        b = x * exp(x * x, (n - 1) // 2)
        return b


def fermat_test_single(n):
    """performs single Fermat test"""
    def test(a):
        return modularexponenation(a, n, n) == a
    return test(randint(1, n - 1))


def fermat_extended(n, cnt):
    """performing fermat tests in a loop,
    for #cnt of numbers (0, n) """
    for i in range(cnt):
        if not fermat_test_single(n):
            return False
    return True

# 2. Miler - Rabin


def miller_rabin(n, s):
    """Miler Rabin Test"""

    # procedure nontrivial_root, which looking for a non trivial square root of one mod n
    def nontrivial_root(a, n):
        """checking Fermat Theorem, and non trivial square root"""

        # find t and u, such that u odd, t >= 1 and n - 1 = 2^tu:
        t, u = 0, n - 1
        while u % 2 == 0:
            t += 1
            u //= 2

        x0 = modularexponenation(a, u, n)
        for i in range(1, t + 1):
            x1 = x0 ** 2 % n
            if x1 == 1 and x0 != 1 and x0 != n - 1:
                return True
        if x1 != 1:
            return True
        return False

    # Return True if n = 2
    if n == 2:
        return True
    # Return False if even
    if n % 2 == 0:
        return False

    for i in range(s):
        a = randint(1, n - 1)
        if nontrivial_root(a, n):
            return False
    return True


# 3. Lucas - Lehmer Test, check primality only Mersenne Primes:
# https://en.wikipedia.org/wiki/Mersenne_prime

# Procedure Lucas-Lehmer, tests if Mp is prime, p > 2:

def lucas_lehmer(p):
    s = 4
    m = exp(2, p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % m
    return True if s == 0 else False

if __name__ == '__main__':
    # print(miller_rabin(2  ** 44497 - 1, 40)) # -> True in... stop after 2008 secs:)
    print(lucas_lehmer(44497)) # -> True in 79.08 sec
