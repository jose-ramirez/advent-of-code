def f(n):
    return n // 3 - 2

def f_rec(n):
    a = f(n)
    if a <= 0:
        return 0
    return a + f_rec(a)

def p1():
    with open('input.txt', 'r') as input_file:
        _sum = 0
        for line in input_file.readlines():
            _sum += f(int(line.strip()))
        return _sum

def p1_recursive():
    with open('input.txt', 'r') as input_file:
        _sum = 0
        for line in input_file.readlines():
            _sum += f_rec(int(line.strip()))
        return _sum

print(p1())
print(p1_recursive())