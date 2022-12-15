class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}, {self.size}'

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = None
        self.subfolders = None

    def __repr__(self) -> str:
        return f'{self.name}, {len(self.files)} files, {len(self.subfolders)} subfolders'

    def cd(self, name):
        if name == '..':
            return self.parent
        else:
            for d in self.subfolders:
                if d.name == name:
                    return d
            return None

    def size(self):
        if self.subfolders == None or len(self.subfolders) == 0:
            return sum([f.size for f in self.files])
        else:
            return sum([f.size for f in self.files]) + sum([d.size() for d in self.subfolders])
        
def bfs_size_total(node: Directory):
    total = 0
    visited = [node]
    queue = [node]

    while queue:
        d = queue.pop(0)

        s = d.size()
        if s < 100000:
            total += s

        for dir in d.subfolders:
            if dir not in visited:
                visited.append(dir)
                queue.append(dir)

    print(total)

def bfs_size_minimum(node: Directory, target_size):
    visited = [node]
    queue = [node]
    size_set = set()

    while queue:
        d = queue.pop(0)

        s = d.size()
        if s > target_size:
            size_set.add(s)

        for dir in d.subfolders:
            if dir not in visited:
                visited.append(dir)
                queue.append(dir)

    print(min(size_set))

root = None
current = None

with open('input', 'r') as input:
    for line in input.readlines():
        command = line.strip().replace('$ ', '')
        if command == 'cd /':
            root = Directory('/', None)
            current = root
        else:
            cmd_params = command.split(' ')
            if cmd_params[0] == 'cd':
                current = current.cd(cmd_params[1])
            elif cmd_params[0] == 'ls':
                if current.subfolders == None:
                    current.subfolders = []
                if current.files == None:
                    current.files = []
            elif cmd_params[0] == 'dir':
                current.subfolders.append(Directory(cmd_params[1], current))
            else:
                current.files.append(File(cmd_params[1], int(cmd_params[0])))

def p1(root):
    bfs_size_total(root)

def p2(root):
    minimum_space_needed = 30000000
    total_space = 70000000
    target_size = minimum_space_needed - (total_space - root.size()) # 6090134
    bfs_size_minimum(root, target_size)

p1(root)
p2(root)
