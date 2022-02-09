def binary_str_to_int(code):
    if len(code) == 1:
        return int(code)
    else:
        return 2 * binary_str_to_int(code[:-1]) + int(code[-1])

def get_seat_id(code):
    bin_code = code.strip().replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    a, b = binary_str_to_int(bin_code[:7]), binary_str_to_int(bin_code[7:])
    return 8 * a + b

def get_data():
    with open('input_05', 'r') as file:
        return [get_seat_id(s) for s in file.readlines()]


seat_ids = get_data()

def part_01():
    return max(seat_ids)

def part_02():
    seat_id_set = set(seat_ids)
    for i in range(911):
        if ((i - 1) in seat_id_set) and ((i + 1) in seat_id_set) and (i not in seat_id_set):
            return i

print(part_01())
print(part_02())