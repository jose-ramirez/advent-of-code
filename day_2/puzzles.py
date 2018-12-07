from collections import defaultdict

def groups(_id):
    group_dict = defaultdict(lambda: None)
    for character in _id:
        if not group_dict[character]:
            group_dict[character] = 1
        else:
            group_dict[character] += 1
    return group_dict

def count_differences(id1, id2):
    total = 0
    for i in range(len(id1)):
        total += (id2[i] != id1[i])
    return total

def p1():
    with open('input.txt', 'r') as file:
        two_counts = 0
        three_counts = 0
        for id_string in file.readlines():
            char_counts = set(groups(id_string).values())
            if 2 in char_counts:
                two_counts += 1
            if 3 in char_counts:
                three_counts += 1
        return two_counts * three_counts

# print(p1())

def p2():
    with open('input.txt', 'r') as file:
        ids = [l.strip() for l in file.readlines()]
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                if count_differences(ids[i], ids[j]) == 1:
                    for k in range(len(ids[i])):
                        if ids[i][k] != ids[j][k]:
                            return ids[i][:k] + ids[i][(k + 1):]


# print(p2())