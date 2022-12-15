from point import Point

class Cartesian:
    def __init__(self, xh, xl, yh, yl):
        self.m = [['.' for j in range(xl + xh + 1)] for i in range(yl + yh + 1)] 
        self.oi = xl
        self.oj = yh
        self.m[yh][xl] = 's'

    def print_cartesian(self):
        for row in self.m:
            print(''.join(row))

    def plot_point(self, p, char = '#'):
        self.m[self.oi - p.y][self.oj + p.x] = char
