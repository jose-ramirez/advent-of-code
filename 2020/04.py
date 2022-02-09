import re

def list_to_map(data):
    return dict([d.split(':') for d in data])

def fields_exist(p_map):
    fields = p_map.keys()
    return all([f in fields for f in ['byr', 'iyr', 'pid', 'ecl', 'hgt', 'hcl', 'eyr']])

def is_value_in_range(y, a, b):
    return a <= y <= b

def is_byr_valid(data):
    byr = data.get('byr', None)
    return byr is not None and is_value_in_range(int(byr), 1920, 2002)

def is_iyr_valid(data):
    iyr = data.get('iyr', None)
    return iyr is not None and is_value_in_range(int(iyr), 2010, 2020)

def is_eyr_valid(data):
    eyr = data.get('eyr', None)
    return eyr is not None and is_value_in_range(int(eyr), 2020, 2030)

def is_pid_valid(data):
    pid = data.get('pid', None)
    return pid is not None and sum([c.isdigit() for c in list(pid)]) == 9 and len(pid) == 9

def is_ecl_valid(data):
    ecl = data.get('ecl', None)
    return ecl is not None and ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_hgt_valid(data):
    hgt = data.get('hgt', None)
    if hgt is not None and (hgt.endswith('cm') or hgt.endswith('in')):
        number, dim = int(hgt[:-2]), hgt[-2:]
        if dim == 'in':
            return is_value_in_range(number, 59, 76)
        else:
            return is_value_in_range(number, 150, 193)
    else:
        return False

def is_hcl_valid(data):
    color = data.get('hcl', None)
    if color is not None:
        color_pattern = re.compile(r'^#[0-9a-f]{6}')
        return color_pattern.match(color) is not None and len(color) == 7
    else:
        return False

def is_passport_valid(passport):
    return is_ecl_valid(passport) \
        and is_hgt_valid(passport) \
        and is_pid_valid(passport) \
        and is_eyr_valid(passport) \
        and is_byr_valid(passport) \
        and is_iyr_valid(passport) \
        and is_hcl_valid(passport)

def get_passports():
    with open('input_04', 'r') as input:
        passports = []
        data = []
        for line in input.readlines():
            if len(line.strip()) > 0:
                data += line.strip().split(' ')
            else:
                passports.append(data)
                data = []
        passports.append(data)
        data = []
    return passports


passports = get_passports()

def part_01():
    total = 0
    for p in passports:
        is_p_ok = fields_exist(list_to_map(p))
        if is_p_ok:
            total +=1
    return total

def part_02():
    total = 0
    for p in passports:
        is_p_ok = is_passport_valid(list_to_map(p))
        if is_p_ok:
            total +=1
    return total

print(part_01())
print(part_02())