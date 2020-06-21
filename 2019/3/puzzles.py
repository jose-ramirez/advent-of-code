from functools import reduce

def try_intersect(h, v):
    intersecting = min(v[0][1], v[1][1]) < h[0][1] < max(v[0][1], v[1][1]) and min(h[0][0], h[1][0]) < v[0][0] < max(h[0][0], h[1][0])
    if intersecting:
        return (v[0][0], h[0][1])
    else:
        return None

def get_intersects(h_segments, v_segments):
    intersection_set = set()
    for h in h_segments:
        for v in v_segments:
            p = try_intersect(h, v)
            if p:
                intersection_set.add(p)
    return intersection_set

def is_horizontal(segment):
    return segment[0][1] == segment[1][1]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def add_segment(segment_dict, direction):
    val = int(direction[1:])
    start_point = segment_dict['start']
    new_segment = None

    if direction.startswith('D'):
        new_segment = [start_point, [start_point[0], start_point[1] - val]]
    elif direction.startswith('U'):
        new_segment = [start_point, [start_point[0], start_point[1] + val]]
    elif direction.startswith('L'):
        new_segment = [start_point, [start_point[0]- val, start_point[1]]]
    else:
        new_segment = [start_point, [start_point[0] + val, start_point[1]]]

    if is_horizontal(new_segment):
        segment_dict['segments']['horizontal'].append(new_segment)
    else:
        segment_dict['segments']['vertical'].append(new_segment)
    segment_dict['start'] = new_segment[1]
    return segment_dict

def p3():
    with open('input.txt', 'r') as input_file:
        segment_sets = []
        for wire in input_file.readlines():
            directions = wire.strip().split(',')
            some_dict = {
                'start': [0, 0],
                'segments': {
                    'horizontal': [],
                    'vertical': []
                }
            }
            directions.insert(0, some_dict)
            segment_sets.append(reduce(add_segment, directions))
        i_set1 = get_intersects(segment_sets[0]['segments']['horizontal'], segment_sets[1]['segments']['vertical'])
        i_set2 = get_intersects(segment_sets[1]['segments']['horizontal'], segment_sets[0]['segments']['vertical'])
        all_intersects =i_set1.union(i_set2)
        return min(map(lambda p: manhattan_distance((0, 0), p), all_intersects))

print(p3())