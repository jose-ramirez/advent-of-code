
def part_01():
    with open('input_01', 'r') as input:
        data = [int(s.strip()) for s in input.readlines()]
        for i in range(len(data)):
            for j in range(i, len(data)):
                if data[i] + data[j] == 2020:
                    return data[i] * data[j]

def part_02():
    with open('input_01', 'r') as input:
        data = [int(s.strip()) for s in input.readlines()]
        for i in range(len(data)):
            for j in range(len(data)):
                for k in range(len(data)):
                    if data[i] + data[j] + data[k] == 2020:
                        return data[i] * data[j] * data[k]

print(part_01())
print(part_02())