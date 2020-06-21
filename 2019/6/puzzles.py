from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()

    def add(self, child):
        self.children.add(child)

    def __repr__(self):
        return self.value

    def is_leaf(self):
        return len(self.children) == 0

def get_paths(tree):
    final_paths = []
    if tree.is_leaf():
        return [[tree.value]]
    else:
        for child in tree.children:
            paths = get_paths(child)
            for path in paths:
                path.insert(0, tree.value)
                final_paths.append(path)
    return final_paths

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def create_graph(input_file_name):
    graph_dict = defaultdict(lambda: None)

    with open(input_file_name, 'r') as input_file_name:
        for line in input_file_name.readlines():
            a, b = line.strip().split(')')

            if graph_dict[a] == None:
                graph_dict[a] = set([b])
            else:
                graph_dict[a].add(b)

            if graph_dict[b] == None:
                graph_dict[b] = set([a])
            else:
                graph_dict[b].add(a)
    
    return graph_dict

def p6(graph):
    nodes_to_visit = set(bfs(graph, 'COM')) - set(['COM'])
    paths = [list(bfs_paths(graph, 'COM', node))[0] for node in nodes_to_visit]
    path_lengths = [len(path) - 1 for path in paths]
    return sum(path_lengths)


print(p6(create_graph('input.txt')))