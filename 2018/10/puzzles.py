import math

def parse(line):
    # position=<-31763, -21177> velocity=<3, 2> => [[-31763, -21177], [3, 2]]
    p = list(map(int, line.split('> ')[0][10:].split(', ')))
    v = list(map(int, line.split('> ')[1][10:-1].split(', ')))
    return p, v

def update(points, velocities):
    l = []
    for i in range(len(points)):
        l.append([points[i][0] + velocities[i][0], points[i][1] + velocities[i][1]])
    return l

def update_matrix(points):
    hspan, vspan = span(points)
    m = [['.'] * hspan for i in range(vspan)]
    for p in points:
        m[p[1]][p[0]] = '#'
    for r in m:
        print(''.join(r))
    print()

def translate(points):
    x_min, y_min = min([p[0] for p in points]), min([p[1] for p in points])
    return [[p[0] - x_min, p[1] - y_min] for p in points]

def span(points):
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    return max(xs) - min(xs) + 1, max(ys) - min(ys) + 1

def p():
    with open('input.txt', 'r') as file:
        pvs = [parse(line.strip()) for line in file.readlines()]
        points, velocities = [p[0] for p in pvs], [p[1] for p in pvs]
        points = translate(points)
        hspan, vspan = span(points)
        min_span = hspan * vspan
        not_min = True
        t = 0
        while not_min:
            points = update(points, velocities)
            s = span(points)[0] * span(points)[1]
            t += 1
            if s == 620:
                min_span = s
                not_min = False
        return t, points

t, points = p()

# message:
points = translate(points)
update_matrix(points)

# time:
print(t)
