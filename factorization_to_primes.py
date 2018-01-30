# Factorization algorithms

# 1. Simple trial, having list of enough primes to factorize certain integer
# Factorize by trial division over the list, we assume, that we have, a list of
# primes generated, for example from Sieve of Erasthotenes.

# Function factorize_trial

from Euler import miller_rabin


def factorize_trial(n, primes):
    """Factorizing n"""
    if miller_rabin(n):
        return n
    result = []
    for p in primes:
        while n % p == 0:
            result.append(p)
            n //= p
        if miller_rabin(n):
            result.append(n)
            break
    return result



