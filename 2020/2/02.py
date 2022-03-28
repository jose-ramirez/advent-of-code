def check_constraint_number(constraint, number):
    limits, _ = constraint.split(' ')
    _min, _max = [int(s) for s in limits.split('-')]
    return _min <= number <= _max

def check_constraint_positions(constraint, pwd):
    limits, c = constraint.split(' ')
    _min, _max = [int(s) for s in limits.split('-')]
    return (pwd[_min - 1] == c) ^ (pwd[_max - 1] == c)

def validate_password(constraint, pwd):
    c = constraint[-1]
    char_total = len([s for s in pwd if s == c])
    return check_constraint_number(constraint, char_total)

def part_01():
    total = 0
    with open('input_02', 'r') as input:
        for line in input.readlines():
            constraint, password = line.strip().split(': ')
            if validate_password(constraint, password):
                total += 1
    return total

def part_02():
    total = 0
    with open('input_02', 'r') as input:
        for line in input.readlines():
            constraint, password = line.strip().split(': ')
            if check_constraint_positions(constraint, password):
                total += 1
    return total

print(part_01())
print(part_02())