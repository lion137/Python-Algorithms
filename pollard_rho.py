# pollard's rho algorithm to factorization https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
# https://lion137.blogspot.co.uk/2017/02/python-pollards-rho-algorithm.html


from random import randint



def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a == 0:
        return b
    while b != 0:
        a, b = b, a % b
    return a


def pollard_rho(n):
    s = set()
    i = 0
    xi = randint(0, n-1)
    y = xi
    k = 2
    while i < 2 * n:
        i += 1
        xi = ((xi^2) - 1)%n
        d = gcd(y - xi, n)
        if d != 1 and d != n:
            s.add(d)
        if i == k:
            y = xi
            k *= 2
    return sorted(s)


