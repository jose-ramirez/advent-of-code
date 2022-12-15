def is_visible(h, line):
    return all([h > t for t in line])

def max_visibility(h, line):
    vis = 0
    for i in range(len(line)):
        if h > line[i]:
            vis += 1
        else:
            return vis + 1
    return vis

def p1():
    with open('input', 'r') as input:
        grid = []
        for line in input.readlines():
            grid.append([int(c) for c in line.strip()])

        total = 0
        rows, columns = len(grid), len(grid[0])
        trees_on_edges = 4 * (len(grid) - 1)
        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                height = grid[i][j]
                left = is_visible(height, grid[i][:j])
                right = is_visible(height, grid[i][j + 1:])
                column = [grid[k][j] for k in range(len(grid))]
                top = is_visible(height, column[:i])
                bottom = is_visible(height, column[i + 1:])
                if any([left, right, top, bottom]):
                    total += 1
        print(total + trees_on_edges)

def p2():
    with open('input', 'r') as input:
        grid = []
        for line in input.readlines():
            grid.append([int(c) for c in line.strip()])

        max_scenic_score = 0
        current_scenic_score = -1
        rows, columns = len(grid), len(grid[0])    
        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                height = grid[i][j]
                max_vis_left = max_visibility(height, grid[i][:j][::-1])
                max_vis_right = max_visibility(height, grid[i][j + 1:])
                column = [grid[k][j] for k in range(len(grid))]
                max_vis_top = max_visibility(height, column[:i][::-1])
                max_vis_bottom = max_visibility(height, column[i + 1:])
                current_scenic_score = max_vis_left * max_vis_right * max_vis_top * max_vis_bottom
                if current_scenic_score > max_scenic_score:
                    max_scenic_score = current_scenic_score
        print(max_scenic_score)

p1()
p2()