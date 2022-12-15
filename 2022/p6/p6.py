def get_data():
    with open('input', 'r') as input:
        return input.readline().strip()

def p1(line, marker_size):
    for i in range(len(line) - marker_size):
        if len(set(line[i:i + marker_size])) == len(line[i:i + marker_size]):
            return i + marker_size

data = get_data()
print(p1(data, 4))
print(p1(data, 14))