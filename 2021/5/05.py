BLANK = '.'
MAX = 1000

def convert_to_segment(line):
    str1, str2 = line.split(' -> ')
    p1 = list(map(int, str1.split(',')))
    p2 = list(map(int, str2.split(',')))
    return [p1, p2]

def is_straight(segment):
    return segment[0][0] == segment[1][0] or segment[0][1] == segment[1][1]

def parse_data():
    with open('input_05', 'r') as input:
        return [convert_to_segment(line.strip()) for line in input.readlines()]

def paint_segment(m, segment):

    p1, p2 = segment

    if p1[0] == p2[0]: # vertical
        for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            if m[i][p1[0]] == BLANK:
                m[i][p1[0]] = 1
            else:
                m[i][p1[0]] += 1

    if p1[1] == p2[1]: # horizontal
        for j in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            if m[p1[1]][j] == BLANK:
                m[p1[1]][j] = 1
            else:
                m[p1[1]][j] += 1

    if p1[0] > p2[0] and p1[1] > p2[1]: # NW direction
        for i in range(p1[0] - p2[0] + 1):
            if m[p1[1] - i][p1[0] - i] == BLANK:
                m[p1[1] - i][p1[0] - i] = 1
            else:
                m[p1[1] - i][p1[0] - i] += 1

    if p1[0] > p2[0] and p1[1] < p2[1]: # SW direction
        for i in range(p1[0] - p2[0] + 1):
            if m[p1[1] + i][p1[0] - i] == BLANK:
                m[p1[1] + i][p1[0] - i] = 1
            else:
                m[p1[1] + i][p1[0] - i] += 1    

    if p1[0] < p2[0] and p1[1] < p2[1]: # SE direction
        for i in range(p2[0] - p1[0] + 1):
            if m[p1[1] + i][p1[0] + i] == BLANK:
                m[p1[1] + i][p1[0] + i] = 1
            else:
                m[p1[1] + i][p1[0] + i] += 1

    if p1[0] < p2[0] and p1[1] > p2[1]: # NE direction
        for i in range(p2[0] - p1[0] + 1):
            if m[p1[1] - i][p1[0] + i] == BLANK:
                m[p1[1] - i][p1[0] + i] = 1
            else:
                m[p1[1] - i][p1[0] + i] += 1

def print_grid(m):
    for row in m:
        print(''.join(map(str, row)))
    print()

def part_01():
    full_data = parse_data()
    filtered_data = [segment for segment in full_data if is_straight(segment)]
    m = [[BLANK for j in range(MAX)] for i in range(MAX)]
    for segment in filtered_data:
        paint_segment(m, segment)
    total = 0
    for i in range(MAX):
        for j in range(MAX):
            if m[i][j] != BLANK and m[i][j] > 1:
                total += 1
    return total

def part_02():
    full_data = parse_data()
    m = [[BLANK for j in range(MAX)] for i in range(MAX)]
    for segment in full_data:
        paint_segment(m, segment)
    total = 0
    for i in range(MAX):
        for j in range(MAX):
            if m[i][j] != BLANK and m[i][j] > 1:
                total += 1
    return total

print(part_01())
print(part_02())