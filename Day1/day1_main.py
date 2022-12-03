elves = []
calories = 0
maxCalories = 0
for line in open("input.txt", "r"):
    if len(line) == 1:
        maxCalories = max(maxCalories,calories)
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)
print(f"max calories : {maxCalories}")

elves.sort(reverse=True)
maxCalories = 0
for i in range(3):
    maxCalories += elves[i]
print(f"max calories top three: {maxCalories}")
