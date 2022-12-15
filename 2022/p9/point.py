class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_next(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def in_line(self, other):
        return self.x == other.x or self.y == other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def is_ne(self, other):
        return self.x > other.x and self.y > other.y

    def is_nw(self, other):
        return self.x < other.x and self.y > other.y

    def is_se(self, other):
        return self.x > other.x and self.y < other.y

    def is_sw(self, other):
        return self.x < other.x and self.y < other.y

    def translate(self, x_, y_):
        self.x += x_
        self.y += y_
        return self

    def move(self, direction):
        if direction == 'L':
            return Point(self.x - 1, self.y)
        elif direction == 'R':
            return Point(self.x + 1, self.y)
        elif direction == 'U':
            return Point(self.x, self.y + 1)
        else:
            return Point(self.x, self.y - 1)