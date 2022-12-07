# ---------------------------------------------------------------------------------------------------------------------
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size}"

    def __repr__(self):
        return str(self)


class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subdirectories = []
        self.files = []

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    def calc_size(self):
        total_size = 0
        for sub_dir in self.subdirectories:
            total_size += sub_dir.calc_size()
        for file in self.files:
            total_size += file.size
        return total_size

    def find_subdirectory(self, subdir_name):
        for sub_dir in self.subdirectories:
            if sub_dir.name == subdir_name:
                return sub_dir
        return None


# ---------------------------------------------------------------------------------------------------------------------
root = Directory(None, "/")
current_dir = root
all_dirs = [root]
for line in open("input.txt", "r"):
    parameters = line.split()
    if line[0] == '$':
        if parameters[1] == "cd":
            if parameters[2] == "..":
                current_dir = current_dir.parent
            elif parameters[2] == "/":
                current_dir = root
            else:
                current_dir = current_dir.find_subdirectory(parameters[2])
        elif parameters[1] == "ls":
            continue
    # directory
    elif line.startswith("dir"):
        new_dir = Directory(current_dir, parameters[1])
        current_dir.subdirectories.append(new_dir)
        all_dirs.append(new_dir)
    # file
    else:
        current_dir.files.append(File(parameters[1], int(parameters[0])))

# part one
total_size = 0
for directory in all_dirs:
    dir_size = directory.calc_size()
    if dir_size <= 100000:
        total_size += dir_size
print(f"part one size: {total_size}")

# part two
size_to_free = 30000000 - (70000000 - root.calc_size())
smallest_to_free = 70000000
for directory in all_dirs:
    dir_size = directory.calc_size()
    if size_to_free <= dir_size < smallest_to_free:
        smallest_to_free = dir_size
print(f"part two size: {smallest_to_free}")
