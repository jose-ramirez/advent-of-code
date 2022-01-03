from copy import deepcopy


def create_board(rows):
    return [[[int(x), False] for x in filter(lambda s: s != '', row.strip().split(' '))] for row in rows]

def parse_data():
    with open('input_04', 'r') as input:
        lines = input.readlines()
        numbers = map(int, lines[0].strip().split(','))
        boards = [create_board(lines[i:(i + 5)]) for i in range(2, len(lines), 6)]
        return list(numbers), boards

def mark_number(board, number):
    for i in range(5):
        for j in range(5):
            v, m = board[i][j]
            if v == number and not m:
                board[i][j][1] = True

def is_row_bingo(board, row_index):
    return all([item[1] for item in board[row_index]])

def is_column_bingo(board, col_index):
    return all([item[1] for item in [board[i][col_index] for i in range(5)]])

def is_board_bingo(board):
    return any([is_row_bingo(board, i) for i in range(5)]) \
        or any([is_column_bingo(board, i) for i in range(5)])

def calculate_score(board, number_index):
    total = 0
    for row in board:
        d = list(map(lambda e: e[0], filter(lambda e: not e[1], row)))
        total += sum(d)
    return numbers[number_index] * total

def print_board(board):
    for row in board:
        print(row)
    print()

numbers, boards = parse_data()

def part_01():
    for i in range(len(numbers)):
        # check all boards:
        [mark_number(board, numbers[i]) for board in boards]
        # see which one becomes a bingo first:
        for j in range(len(boards)):
            if is_board_bingo(boards[j]):
                return calculate_score(boards[j], i)

def part_02():
    bingoes = []
    for i in range(len(numbers)):
        # check all boards:
        [mark_number(board, numbers[i]) for board in boards]
        # see which one becomes a bingo first:
        for j in range(len(boards)):
            if is_board_bingo(boards[j]) and j not in map(lambda e: e[0], bingoes):
                bingoes.append((j, i, deepcopy(boards[j])))
    _, number_index, board = bingoes.pop()
    return calculate_score(board, number_index)

print(part_01())
print(part_02())
