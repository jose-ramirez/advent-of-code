from itertools import groupby
from operator import itemgetter

def p4_1(a=271973, b=785961):
    total = 0
    for n in range(a, b):
        l = str(n)
        is_increasing = all(l[i] <= l[i+1] for i in range(5))
        has_two_equal_digits = any(l[i] == l[i+1] for i in range(5))
        if is_increasing and has_two_equal_digits:
            total += 1
    return total

def p4_2(a=271973, b=785961):
    total = 0
    for n in range(a, b):
        l = str(n)
        is_increasing = all(l[i] <= l[i+1] for i in range(5))
        has_two_equal_digits = any(l[i] == l[i+1] for i in range(5))
        has_at_least_one_pair = any(len(list(data)) == 2 for (key, data) in groupby(l, key=itemgetter(0)))
        if is_increasing and has_two_equal_digits and has_at_least_one_pair:
            total += 1
    return total

print(p4_1())
print(p4_2())
