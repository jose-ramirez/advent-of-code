from collections import defaultdict

def get_point(line):
    x, y = line.strip().split(', ')
    return (int(x), int(y))

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def get_data():
    with open('input_06', 'r') as input:
        return [get_point(l) for l in input.readlines()]

def closest(p, points):
    current_state = (0, -1, 720) # max possible distance is 713 in the given input
    for i in range(len(points)):
        d = manhattan_distance(p, points[i])
        if d < current_state[2]:
            current_state = (1, i, d)
        elif d == current_state[2]:
            min_count, min_index, current_min_d = current_state
            current_state = (min_count + 1, min_index, current_min_d)
    if current_state[0] > 1:
        return -1
    else:
        return current_state[1]

def is_border(x, y, max_x, max_y):
    return x in [0, max_x] or y in [0, max_y]

def distance_sum(p, points):
    return sum([manhattan_distance(p, point) for point in points])


points = get_data()
xs, ys = zip(*points)
max_x, max_y = max(xs), max(ys)

def part_01():
    closest_map = defaultdict(lambda: [False, 0])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            index = closest((x, y), points)
            if index != -1:
                i_b, count = closest_map[index]
                new_i_b = True if (i_b or is_border(x, y, max_x, max_y)) else i_b
                closest_map[index] = [new_i_b, count + 1]

    closest_finite_map = { k: v for k, v in closest_map.items() if not v[0] }
    max_finite_area = max([v[1] for v in closest_finite_map.values()])

    return max_finite_area

def part_02():
    total_area = 0
    MAX_DISTANCE_SUM = 10000
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if distance_sum((x, y), points) < MAX_DISTANCE_SUM:
                total_area += 1
    return total_area

print(part_01())
print(part_02())