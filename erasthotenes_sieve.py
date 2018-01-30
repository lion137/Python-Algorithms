# Erasthotenes Sieve algorithm
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from math import sqrt
from Euler import prime_sieve

def simple_sieve(n):
    arr = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if arr[i] is True:
            j = i*i
            k = 1
            while j < n:
                arr[j] = False
                j = i * i + k * i
                k += 1
    output = []
    for i in range(2, len(arr)):
        if arr[i] is True:
            output.append(i)
    return output



def segmented_sieve(n):
    delta = n // int(sqrt(n))
    def calculate_smallest_mult(a, p):
        left = a - delta + 1
        left_mul = (left) // p
        tmp = p * left_mul
        if tmp < left:
            return tmp + p
        else:
            return tmp
    ms = [] # initialize array of top of segments
    primes = []  # initialize primes array
    i = 2 * delta # used to create first delta primes
    ind = delta

    while i <= n:
        ms.append(i)
        i += delta
    primes = prime_sieve(delta)

    k = 1 # index of numbers in ms
    for num in ms: # num is another starting from the 2*delta topmost value of segments
        arr = [True] * delta
        ind = 0
        p = primes[ind]
        while p <= int(sqrt(num)):
            start = calculate_smallest_mult(num, p)
            while start <= num:
                # print(arr)
                arr[start - delta * k - 1] = False
                start += p
            ind += 1
            p = primes[ind]
        for x in range(len(arr)):
            if arr[x] is True:
                primes.append(x + delta * k + 1)
        k += 1
    return primes








