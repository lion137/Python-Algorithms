# string edit distance algorithm description:
# https://lion137.blogspot.co.uk/2017/01/algorithms-in-python.html


st1 = "sunday euheu jodjodjsjdkeuamd"
st2 = "saturdaydkwdwmmdwodqwrdhrtdkl"


def edit_dist_dp(str1, str2, m, n):
    store = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                store[i][j] = j

            elif j == 0:
                store[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                store[i][j] = store[i - 1][j - 1]

            else:
                store[i][j] = 1 + min(store[i][j - 1], store[i - 1][j],
                                      store[i - 1][j - 1])

    return store[m][n]


print(edit_dist_dp(st1, st2, len(st1), len(st2)))
# output: -> 22
