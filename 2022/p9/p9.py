from rope import Rope

def simulate(input, num_knots):
    rope = Rope(num_knots)
    for line in input.readlines():
        direction, times = line.strip().split(' ')
        for i in range(int(times)):
            rope.step(direction)
    print(len(rope.tail_steps))

def p1():
    with open('input', 'r') as input:
        simulate(input, 2)

def p2():
    with open('input', 'r') as input:
        simulate(input, 10)

p1()
p2()