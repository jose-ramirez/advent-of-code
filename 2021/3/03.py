from statistics import mode, multimode


def oxygen_bit(bit_list):
    d = multimode(bit_list)
    if len(d) == 2:
        return '1'
    else:
        return d[0]

def CO2_bit(bit_list):
    d = multimode(bit_list)
    if len(d) == 2:
        return '0'
    else:
        return str(1 - int(d[0]))

def b_to_i(bit_str):
    return int(bit_str, 2)

def oxygen_p(current_state):
    bit_pos, readings = current_state[0], current_state[1]
    bits = list(zip(*map(lambda s: list(s.strip()), readings)))[bit_pos]
    b = oxygen_bit(bits)
    filtered_readings = list(filter(lambda s: s[bit_pos] == b, readings))
    if len(filtered_readings) == 1:
        return filtered_readings[0]
    else:
        return oxygen_p((bit_pos + 1, filtered_readings))

def CO2_p(current_state):
    bit_pos, readings = current_state[0], current_state[1]
    bits = list(zip(*map(lambda s: list(s.strip()), readings)))[bit_pos]
    b = CO2_bit(bits)
    filtered_readings = list(filter(lambda s: s[bit_pos] == b, readings))
    if len(filtered_readings) == 1:
        return filtered_readings[0]
    else:
        return CO2_p((bit_pos + 1, filtered_readings))

def part_01():
    with(open('input_03', 'r')) as input:
        gamma_bits = [mode(l) for l in zip(*map(lambda s: list(s.strip()), input.readlines()))]
        epsilon_bits = [str(1 - int(b)) for b in gamma_bits]
        gamma, epsilon = int(''.join(gamma_bits), 2), int(''.join(epsilon_bits), 2)
        return gamma * epsilon

def part_02():
    with(open('input_03', 'r')) as input:
        readings = list(map(lambda s: s.strip(), input.readlines()))
        oxygen_reading = oxygen_p((0, readings))
        CO2_reading = CO2_p((0, readings))
        return b_to_i(oxygen_reading) * b_to_i(CO2_reading)

print(part_01())
print(part_02())

# print(oxygen_p((0, ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'])))
# print(CO2_p((0, ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'])))
