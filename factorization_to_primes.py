# Factorization algorithms

# 1. Simple trial, having list of enough primes to factorize certain integer
# Factorize by trial division over the list, we assume, that we have, a list of
# primes generated, for example from Sieve of Erasthotenes.

# Function factorize_trial

from Euler import is_prime, prime_sieve, segmented_sieve, modularexponenation, miller_rabin2, miller_rabin
from math import log, e
import time
import sympy



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


def primes_array(k, n, pr_array):
    if k % 2 == 0: # make k odd
        k += 1
    out = []
    """returns primes from k to n (trial algorithm)"""
    for i in range(k + 2, n + 1 , 2):
        if miller_rabin(i):
           out.append(i)
    return pr_array + out

pr = 200000000
primes = prime_sieve(pr)
pr_len = pr // log(pr, e)
print(pr_len, pr_len ** 2)
n = 5123441 * 997
print(len(primes), len((primes)) ** 2)
st = time.time()
for x in range(10000):
    factors = factorize_trial(n, primes)
end = time.time()
print(f'Time: {end - st:.2f}s\n')
print("factors", factors)

