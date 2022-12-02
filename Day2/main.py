shape = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

scores = {
    "AX": 3,    # rock rock
    "AY": 6,    # rock paper
    "AZ": 0,    # rock scissor
    "BX": 0,    # paper rock
    "BY": 3,    # paper paper
    "BZ": 6,    # paper scissor
    "CX": 6,    # scissor rock
    "CY": 0,    # scissor paper
    "CZ": 3,    # scissor scissor
}

# part1
totalScore = 0
for line in open("input.txt", "r"):
    totalScore += shape[line[2]] + scores[line[0] + line[2]]
print(f"score is {totalScore}")


# part2
results = {
    "X": 0,
    "Y": 1,
    "Z": 2,
}
choose = ["A", "B", "C"]
totalScore = 0
for line in open("input.txt", "r"):
    outcome = results[line[2]]
    mine = choose[(shape[line[0]] + outcome + 1) % 3]
    totalScore += 3*outcome + shape[mine]
print(f"score is {totalScore}")
