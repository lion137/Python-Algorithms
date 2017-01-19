from itertools import product


def variations_with_repetitions(data, count):
    """returns an iterator with variations with repetitions
    of data elements from a set with count number of elems"""
    for x in product(data, repeat=count):
        w = ''.join(x)
        yield (w)

cnt = 0
for i in variations_with_repetitions(['A', 'B', 'C', 'D'], 2):
    print(i)
    cnt += 1
print("liczba = ", cnt)
