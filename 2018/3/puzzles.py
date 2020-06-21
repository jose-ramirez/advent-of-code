def overlap(rect1, rect2):
    p11, p12 = rect1[1], rect1[2]
    p21, p22 = rect2[1], rect2[2]
    if p12[0] <= p21[0] or p11[0] >= p22[0]:
        return False
    if p12[1] <= p21[1] or p11[1] >= p22[1]:
        return False
    return True

def get_rect_data(definition_string):
    values = [v for v in definition_string.split(' ') if v != '@']
    _id = values[0]
    d1 = list(map(int, values[1].replace(':', '').split(',')))
    d2 = list(map(int, values[2].split('x')))
    return _id, d1, [d1[0] + d2[0], d1[1] + d2[1]]

def update_fabric(fabric, rect):
    p1, p2 = rect[1], rect[2]
    for i in range(p1[1], p2[1]):
        for j in range(p1[0], p2[0]):
            fabric[i][j] += 1
    return fabric

def p1():
    fabric = [[0] * 1000 for i in range(1000)]
    with open('input.txt', 'r') as file:
        coordinates = [get_rect_data(line.strip()) for line in file.readlines()]
        for rect in coordinates:
            fabric = update_fabric(fabric, rect)
        count = 0
        for row in fabric:
            count += len([x for x in row if x > 1])
        return count

print(p1())

def p2():
    with open('input.txt', 'r') as file:
        r = [get_rect_data(line.strip()) for line in file.readlines()]
        for i in range(len(r)):
            overlaps = False
            for j in range(len(r)):
                if i != j:
                    overlaps = overlaps or overlap(r[i], r[j])
            if not overlaps:
                return r[i][0][1:]

print(p2())