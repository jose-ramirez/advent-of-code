def p1():
    results = {
        'A': {
            'X': 4, 
            'Y': 8,
            'Z': 3,
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C': {
            'X': 7,
            'Y': 2,
            'Z': 6
        }
    }

    with open('input', 'r') as input:
        total = 0
        for line in input.readlines():
            them, you = line.strip().split(' ')
            print(results[them][you])
            total += results[them][you]
        print(total)

def p2():
    results = {
        'A': {  
            'X': 3, 
            'Y': 4,
            'Z': 8,
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C': {
            'X': 2,
            'Y': 6,
            'Z': 7
        }
    }

    with open('input', 'r') as input:
        total = 0
        for line in input.readlines():
            them, you = line.strip().split(' ')
            print(results[them][you])
            total += results[them][you]
        print(total)

p2()