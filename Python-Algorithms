# program to generate the all 2^n subsets of n length binary sequence
# ex.: 2 bits -> (00), (01), (10), (11)
# also generating any m length sequences of k objects - both of them as
# iterators, and recursively and iteratively (slow) generating  gray code:
# https://en.wikipedia.org/wiki/Gray_code


def bin_pow_set(n):
    """returns power set of the all bit sequences of
    length n as an iterator"""
    def append_zeroes(x, n):
        """helper function to append zeroes"""
        x = bin(x)
        x = x[2:]
        return '0' * (n - len(x)) + x
    i = 0
    k = 0
    while k < 2 ** n - 1:
        k += 1
        i = append_zeroes(k, n)
        yield i


def dec_to_any(n,base):
    conv_string = "0123456789ABCDEF"
    if n < base:
       return conv_string[n]
    else:
        return dec_to_any(n // base, base) + conv_string[n % base]

def any_pow_set(n, m):
    """returns the all length n sequences of
    m elements, as an iterator"""
    def append_zeroes(x, n, base):
        """helper function to append zeroes"""
        x = dec_to_any(x, base)
        return '0' * (n - len(x)) + x
    i = 0
    k = 0
    while k < m ** n - 1:
        k += 1
        i = append_zeroes(k, n, m)
        yield i


def gray(n, xs=[""]):
    """recursively computes a list of gray codes of
    length n"""
    def zero_pref(xs):
        if not xs:
            return ["0"]
        return ["0" + x for x in xs]

    def one_pref_rev(xs):
        if not xs:
            return ["1"]
        else:
            return ["1" + x for x in [y[::-1] for y in xs]]
    if n == 0:
        return ""
    else:
        return zero_pref(gray(n - 1, xs)) + one_pref_rev(gray(n - 1, xs))

def gray_iter(n):
    """iteratively computes a list of gray codes of
        length n"""
    def zero_pref(xs):
        if not xs:
            return ["0"]
        return ["0" + x for x in xs]

    def one_pref_rev(xs):
        if not xs:
            return ["1"]
        else:
            return ["1" + x for x in [y[::-1] for y in xs]]
    xs= [""]
    k = 0
    while k < n:
        xs = zero_pref(xs) + one_pref_rev(xs)
        k += 1
    return xs






