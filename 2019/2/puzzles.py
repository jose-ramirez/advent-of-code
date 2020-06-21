def add(start_index, program):
    program[program[start_index + 3]] = program[program[start_index + 1]] + program[program[start_index + 2]]

def mult(start_index, program):
    program[program[start_index + 3]] = program[program[start_index + 1]] * program[program[start_index + 2]]

def p2(a, b):
    with open('input.txt', 'r') as input_file:
        program = list(map(int, input_file.readlines()[0].strip().split(',')))
        program[1] = a
        program[2] = b
        steps = len(program) // 4
        for i in range(steps):
            if program[4 * i] == 1:
                add(4 * i, program)
            elif program[4 * i] == 2:
                mult(4 * i, program)
            elif program[4 * i] == 99:
                break
        return program[0]

def noun_verb():
    for i in range(100):
        for j in range(100):
            if p2(i, j) == 19690720:
                return i, j

print(p2(12, 2))
print(noun_verb())