# algorithm for shuffling given subscriptable data structure
# from Knuth

import random


def swap(alist, i, j):
    """swaps input lists i, j elements"""
    alist[i], alist[j] = alist[j], alist[i]


def shuffle(data):
    """randomly shuffles element in the input data"""
    n = len(data)
    for token in range(n - 1):
        swap(data, token, random.randrange(token, n))

alist1 = [1, 3, 5, 6]
print(alist1)
shuffle(alist1)
print(alist1)
