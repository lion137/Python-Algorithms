# binary search


# recursive with slices


def bin_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return bin_search(alist[:midpoint], item)
            else:
                return bin_search(alist[midpoint + 1:], item)


# iterative version

def bin_search_iter(alist, item):
    L = 0
    R = len(alist) - 1
    test = False
    while L <= R and not test:
        m = (L + R) // 2
        if alist[m] < item:  # m1 = 1, m2 = 2
            L = m + 1
            test = True
        if alist[m] > item:
            R = m - 1
            test = True
        if not test:
            return True
        test = False
    return False


print(bin_search_iter([1, 2, 3], 743787874875857) == bin_search([1, 2, 3], -743787874875857) == False)

# output: -> True
