def p1():
    with open('input.txt', 'r') as file:
        total = 0
        for line in file.readlines():
            total += int(line.strip())
        return total

# print(p1())

def p2():
    with open('input.txt', 'r') as file:
        past_frequencies = set()
        current_frequency = 0
        i = 0
        shifts = list(map(lambda e: int(e.strip()), file.readlines()))
        while current_frequency not in past_frequencies:
            past_frequencies.add(current_frequency)
            index = i % len(shifts)
            current_frequency += shifts[index]
            i += 1
        return current_frequency

# print(p2())