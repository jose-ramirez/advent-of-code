from operator import mul
from functools import reduce

map = []
with open('input_03') as input:
    map = [list(line.strip()) for line in input.readlines()]

def find_steps_total(right, down, map):
    rows = len(map)
    cols = len(map[0])
    total = 0
    for m in range(1, rows):
        i, j = (down * m), ((right * m) % cols)
        if i >= rows:
            break
        else:
            if map[i][j] == '#':
                total += 1
    return total

def part_01():
    return find_steps_total(3, 1, map)

def part_02():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    return reduce(mul, [find_steps_total(a, b, map) for a, b in slopes], 1)


print(part_01())
print(part_02())
