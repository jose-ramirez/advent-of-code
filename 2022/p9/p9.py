from point import Point
from cartesian import Cartesian
class Rope:
    # head is the last item, tail is the first one:
    def __init__(self, size) -> None:
        self.size = size
        self.knots = [Point(0, 0)] * self.size
        self.tail_steps = set([self.knots[0]])

    def update_knot_position(self, tail_index, head_index, direction):
        tail, head = self.knots[tail_index], self.knots[head_index]
        if not tail.is_next(head):
            if tail.in_line(head):
                self.knots[tail_index] = tail.move(direction)
            else:
                if head.is_ne(tail):
                    self.knots[tail_index] = Point(tail.x + 1, tail.y + 1)
                elif head.is_nw(tail):
                    self.knots[tail_index] = Point(tail.x - 1, tail.y + 1)
                elif head.is_se(tail):
                    self.knots[tail_index] = Point(tail.x + 1, tail.y - 1)
                else:
                    self.knots[tail_index] = Point(tail.x - 1, tail.y - 1)

    def step(self, direction):        
        self.knots[-1] = self.knots[-1].move(direction)
        for i in range(self.size - 1, 0, -1):
            self.update_knot_position(i - 1, i, direction)
        self.tail_steps.add(self.knots[0])

    def plot_rope(self, cartesian):
        l = len(self.knots) - 1
        for i in range(l):
            cartesian.plot_point(self.knots[i], f'{l - i}')
        cartesian.plot_point(self.knots[-1], 'H')
        cartesian.print_cartesian()

with open('input', 'r') as input:
    rope = Rope(10)
    for line in input.readlines():
        direction, times = line.strip().split(' ')
        print(f'=== {direction} {times} ===')
        for i in range(int(times)):
            rope.step(direction)
            rope.plot_rope(Cartesian(15, 15, 15, 15))
            print()
    print(len(rope.tail_steps))
