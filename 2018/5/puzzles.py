from functools import reduce

def opposite(u1, u2):
    return u1 != u2 and (u1 == u2.lower() or u2 == u1.lower())

def react(polymer, unit):
    if len(polymer) == 0:
        return [unit]
    else:
        if opposite(polymer[-1], unit):
            return polymer[:-1]
        else:
            polymer.append(unit)
            return polymer

def prepare_polymer_arr(polymer_str):
    polymer_arr = [ch for ch in polymer_str]
    polymer_arr.insert(0, [])
    return polymer_arr

def p1():
    with open('input.txt', 'r') as file:
        polymer = file.readlines()[0].strip()
        res = reduce(react, prepare_polymer_arr(polymer))
        return len(res)

print(p1())

def p2():
    with open('input.txt', 'r') as file:
        polymer = file.readlines()[0].strip()
        min_len = 100000
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            test_polymer = polymer.replace(ch, '').replace(ch.lower(), '')
            res = reduce(react, prepare_polymer_arr(test_polymer))
            if len(res) < min_len:
                min_len = len(res)
        return min_len

print(p2())