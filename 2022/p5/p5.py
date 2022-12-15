# Initial state:
# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    '1': ['T', 'V', 'J', 'W', 'N', 'R', 'M', 'S'],
    '2': ['V', 'C', 'P', 'Q', 'J', 'D', 'W', 'B'],
    '3': ['P', 'R', 'D', 'H', 'F', 'J', 'B'],
    '4': ['D', 'N', 'M', 'B', 'P', 'R', 'F'],
    '5': ['B', 'T', 'P', 'R', 'V', 'H'],
    '6': ['T', 'P', 'B', 'C'],
    '7': ['L', 'P', 'R', 'J', 'B'],
    '8': ['W', 'B', 'Z', 'T', 'L', 'S', 'C', 'N'],
    '9': ['G', 'S', 'L']
}

def move_9000(n, from_stack, to_stack, stacks):
    f = stacks[from_stack]
    t = stacks[to_stack]
    for i in range(n):
        t.insert(0, f.pop(0))

def move_9001(n, from_stack, to_stack, stacks):
    f = stacks[from_stack]
    t = stacks[to_stack]
    stacks[to_stack] = f[:n] + t
    del f[:n]
    
def p1():
    with open('input', 'r') as input:
        for line in input.readlines():
            data = line.strip().split(' ')
            n_of_crates = int(data[1])
            from_stack = data[3]
            to_stack = data[5]
            move_9000(n_of_crates, from_stack, to_stack, stacks)
        print(''.join([v[0] for (_, v) in stacks.items()]))

def p2():
    with open('input', 'r') as input:
        for line in input.readlines():
            data = line.strip().split(' ')
            n_of_crates = int(data[1])
            from_stack = data[3]
            to_stack = data[5]
            move_9001(n_of_crates, from_stack, to_stack, stacks)
        print(''.join([v[0] for (_, v) in stacks.items()]))

# remember to not run these at the same time!
# p1()
p2()