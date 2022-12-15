def p1():
    with open('input', 'r') as input:
        max_so_far = -1
        current_total = 0
        for line in input.readlines():
            n = line.strip()
            if len(n) > 0:
                current_total += int(n)
            else:
                if current_total > max_so_far:
                    max_so_far = current_total
                current_total = 0

        print(max_so_far)

def p2():
    with open('input', 'r') as input:
        calorie_counts = []
        current_total = 0
        for line in input.readlines():
            n = line.strip()
            if len(n) > 0:
                current_total += int(n)
            else:
                calorie_counts.append(current_total)
                current_total = 0

        calorie_counts.sort(reverse=True)
        print(sum(calorie_counts[:3]))

p2()