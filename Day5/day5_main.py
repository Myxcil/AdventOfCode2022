# ---------------------------------------------------------------------------------------------------------------------
class Move:
    def __init__(self, inputline):
        elements = inputline.split()
        self.num_crates = int(elements[1])
        self.source = int(elements[3])
        self.target = int(elements[5])

    def __str__(self):
        return f"#{self.num_crates} [{self.source}]->[{self.target}]"

    def __repr__(self):
        return str(self)


# ---------------------------------------------------------------------------------------------------------------------
stacks = []
reading_stacks = True
moves = []
for line in open("input.txt", "r"):
    if reading_stacks:
        if line[1] == '1':
            reading_stacks = False
            continue
        for i in range(0, len(line), 4):
            stackIndex = i >> 2
            if stackIndex >= len(stacks):
                stack = []
                stacks.append(stack)
            else:
                stack = stacks[stackIndex]
            if line[i] == '[':
                stack.insert(0, line[i+1])
    elif len(line) > 1:
        moves.append(Move(line))

print(stacks)

for move in moves:
    source_stack = stacks[move.source - 1]
    target_stack = stacks[move.target - 1]
    insert_index = len(target_stack)
    for i in range(move.num_crates):
        # part one, act like a LIFO
        # target_stack.append(source_stack.pop())
        # part two, move in order
        target_stack.insert(insert_index, source_stack.pop())
    print(stacks)

result = ""
for stack in stacks:
    result += stack[-1];
print(result)
