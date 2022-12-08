lines = open("input.txt", "r").readlines()
width = len(lines[0]) - 1
height = len(lines)
trees = [[0 for y in range(height)] for x in range(width)]
for y in range(height):
    line = lines[y]
    for x in range(width):
        trees[x][y] = line[x]


def is_visible(coord_x, coord_y):
    tree_height = trees[coord_x][coord_y]
    visible = 1 | 2 | 4 | 8
    # left
    for x in range(coord_x-1, -1, -1):
        if trees[x][coord_y] >= tree_height:
            visible = visible & ~1
            break
    # right
    for x in range(coord_x+1, width, 1):
        if trees[x][coord_y] >= tree_height:
            visible = visible & ~2
            break
    # up
    for y in range(coord_y-1, -1, -1):
        if trees[coord_x][y] >= tree_height:
            visible = visible & ~4
            break
    # down
    for y in range(coord_y+1, height, 1):
        if trees[coord_x][y] >= tree_height:
            visible = visible & ~8
            break
    return visible != 0


# Part one
num_visible = 2 * (width-1) + 2 * (height-1)
for y in range(1, height - 1):
    for x in range(1, width-1):
        if is_visible(x, y):
            num_visible += 1
print(f"num visible: {num_visible}")


def calc_viewing_distance(coord_x, coord_y):
    tree_height = trees[coord_x][coord_y]
    view_up = 0
    view_left = 0
    view_right = 0
    view_down = 0
    # up
    for y in range(coord_y - 1, -1, -1):
        view_up += 1
        if trees[coord_x][y] >= tree_height:
            break
    # left
    for x in range(coord_x - 1, -1, -1):
        view_left += 1
        if trees[x][coord_y] >= tree_height:
            break
    # right
    for x in range(coord_x + 1, width, 1):
        view_right += 1
        if trees[x][coord_y] >= tree_height:
            break
    # down
    for y in range(coord_y + 1, height, 1):
        view_down += 1
        if trees[coord_x][y] >= tree_height:
            break
    return view_up * view_left * view_right * view_down


# part two
max_viewing_distance = 0
for y in range(1, height-1):
    for x in range(1, width-1):
        max_viewing_distance = max(max_viewing_distance, calc_viewing_distance(x, y))
print(f"max viewing distance = {max_viewing_distance}")

