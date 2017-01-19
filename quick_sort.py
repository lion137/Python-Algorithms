# quicksort (not randomized)

import random
import time


def exchange(t, l, k):
    tmp = t[l]
    t[l] = t[k]
    t[k] = tmp


def partition(a, p, r):
    s = p
    x = a[s]
    i = p - 1
    j = p
    while j <= r - 1:
        if a[j] <= x:
            i += 1
            exchange(a, i, j)
        j += 1
    exchange(a, i + 1, r)
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


A = [7, 2, 8, 0, 1, 3, 4, 6, 5]
B = []
for cnt in range(100):
    B.append(random.randint(1, random.randint(2, 100000)))
start_time = time.time()
B.sort()
print(B[:20])
print("time of running in secs: ", time.time() - start_time)


'''
output ->
[138, 173, 236, 422, 778, 850, 996, 1050, 1510, 1804, 1916, 2015, 2249, 2861, 2936, 3006, 3186, 3204, 3280, 3579]
time of running in secs:  4.172325134277344e-05 <-
'''
