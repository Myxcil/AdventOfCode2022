def get_priority(item):
    priority = ord(item)
    if 65 <= priority <= 90:
        return priority - 65 + 27
    else:
        return priority - 97 + 1


# Part one
totalPriority = 0
for line in open("input.txt", "r"):
    middle = len(line) >> 1
    duplicate = list(set([c for c in line[:middle] if c in line[middle:]]))
    totalPriority += get_priority(duplicate[0])
print(f"totalPriority = {totalPriority}")

# Part two
totalPriority = 0
lines = open("input.txt", "r").read().splitlines()
for index in range(0, len(lines), 3):
    duplicate = list(set([c for c in lines[index] if c in lines[index+1] and c in lines[index+2]]))
    totalPriority += get_priority(duplicate[0])
print(f"totalPriority = {totalPriority}")
