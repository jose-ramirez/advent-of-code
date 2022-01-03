from functools import reduce

state_lambdas = {
    'up': lambda state, n: (state[0], max(state[1] - n, 0)),
    'down': lambda state, n: (state[0], state[1] + n),
    'forward': lambda state, n: (state[0] + n, state[1])
}

state_lambdas_aim = {
    'up': lambda state, n: (state[0], state[1], state[2] - n),
    'down': lambda state, n: (state[0], state[1], state[2] + n),
    'forward': lambda state, n: (state[0] + n, state[1] + (n * state[2]), state[2])
}

def process_direction(current_state, direction, lambdas):
    s1, s2 = direction.split(" ")
    return lambdas[s1](current_state, int(s2))

def pd_part1(current_state, direction):
    return process_direction(current_state, direction, state_lambdas)

def pd_part2(current_state, direction):
    return process_direction(current_state, direction, state_lambdas_aim)

def part_01():
    current_state = (0, 0)
    with open('input_02', 'r') as input:
        l = list(map(lambda s: s.strip(), input.readlines()))
        final_x, final_y = reduce(pd_part1, l, current_state)
        return final_x * final_y

def part_02():
    current_state = (0, 0, 0)
    with open('input_02', 'r') as input:
        l = list(map(lambda s: s.strip(), input.readlines()))
        final_x, final_y, final_aim = reduce(pd_part2, l, current_state)
        return final_x * final_y

print(part_01())
print(part_02())