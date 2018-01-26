# Primality Tests
#
# Copyleft 2018 lion137
#
# 1. Fermat Test

#from Euler import modularexponenation
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


def miller_rabin(n, s):
    """Miler Rabin Test"""

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


