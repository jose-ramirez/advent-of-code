# Number of k-digit integers, ending in m, whose digits are increasing and have at least two equal digits.
# Still need to validate it though, might be wrong
def f(k, m):
    _m = [[0] * (m + 1) for i in range(k + 1)]
    _m[1] = [i for i in range(m + 1)]
    for r in range(2, k + 1):
        _m[r][1] = 1
        for s in range(2, m + 1):
            _m[r][s] = sum([_m[r - 1][j] * (10 - j) for j in range(1, s + 1)])
    return _m

def p4():
    for l in f(3, 9):
        print(l)