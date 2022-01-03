from functools import reduce

def compare_accumulate(vals, num):
    return (vals[0] + (vals[1] < num), num)

def process(l):
    initial = (0, l.pop(0))
    result = reduce(compare_accumulate, l, initial)
    return result[0]

def part_1():
    with open('input_01', 'r') as input:
        l = list(map(lambda s: int(s.strip()), input.readlines()))
        return process(l)

def part_2():
    with open('input_01', 'r') as input:
        l = list(map(lambda s: int(s.strip()), input.readlines()))
        m = [sum(l[i : i + 3]) for i in range(len(l) - 3)]
        return process(m)

print(part_1())
print(part_2())