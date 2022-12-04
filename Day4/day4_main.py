# part one
fully_contained = 0
for line in open("input.txt", "r").read().splitlines():
    first, second = line.split(',')
    start1, end1 = first.split('-')
    start2, end2 = second.split('-')
    if (int(start1) <= int(start2) and int(end2) <= int(end1)) or (int(start2) <= int(start1) and int(end1) <= int(end2)):
        fully_contained += 1
print(f"fully contained = {fully_contained}")

# part two
num_overlaps = 0
for line in open("input.txt", "r").read().splitlines():
    first, second = line.split(',')
    start1, end1 = first.split('-')
    start2, end2 = second.split('-')
    if not (int(end2) < int(start1) or int(start2) > int(end1)):
        num_overlaps += 1
print(f"overlaps = {num_overlaps}")
