def includes(l1, h1, l2, h2):
    return (l1 <= l2 and h2 <= h1) or (l2 <= l1 and h1 <= h2)

def disjoint(l1, h1, l2, h2):
    return h1 < l2 or h2 < l1

def overlaps(l1, h1, l2, h2):
    return includes(l1, h1, l2, h2) or not disjoint(l1, h1, l2, h2)

def p1():
    with open('input', 'r') as input:
        total = 0
        for line in input.readlines():
            i1, i2 = line.strip().split(',')
            l1, h1 = map(int, i1.split('-'))
            l2, h2 = map(int, i2.split('-'))
            if includes(l1, h1, l2, h2):
                total += 1
        print(total)

def p2():
    with open('input', 'r') as input:
        total = 0
        for line in input.readlines():
            i1, i2 = line.strip().split(',')
            l1, h1 = map(int, i1.split('-'))
            l2, h2 = map(int, i2.split('-'))
            if overlaps(l1, h1, l2, h2):
                total += 1
        print(total)

p1()
p2()
