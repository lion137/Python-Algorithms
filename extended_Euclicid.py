# Extended Euclicid https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

# Extended Euclicid Algorithm, returns gcd, and x, y in d = gcd(a, b) = ax + by
# complexity: O(lg(b))
#
# , and O(beta^3) bit operations (call it on 2 beta bits numbers) assuming that
# mult and division is O(beta^2)

def extended_euclicid(a, b):
    """ Extended Euclicid Algorithm, returns gcd, and x, y in d = gcd(a, b) = ax + by
        complexity: O(lg(b))"""
    if b == 0:
        return [a, 1, 0]
    else:
        [dn, xn, yn] = extendedeuclicid(b, a % b)
        [d, x, y] = [dn, yn, xn - (a // b) * yn]
        return [d, x, y]
