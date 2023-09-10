from pathlib import Path

with open(Path("input/day8.txt")) as file:
    trees = file.read().splitlines()

map = [[False]*len(trees[0]) for _ in range(len(trees))]


def process_trees_left(trees):
    for idx_y in range(len(trees)):
        prev = -1
        for idx_x in range(len(trees[0])):
            if int(trees[idx_y][idx_x]) > prev:
                prev = int(trees[idx_y][idx_x])
                map[idx_y][idx_x] = True

def process_trees_right(trees):
    for idx_y in range(len(trees)):
        prev = -1
        for idx_x in range(len(trees[0])-1, -1, -1):
            if int(trees[idx_y][idx_x]) > prev:
                prev = int(trees[idx_y][idx_x])
                map[idx_y][idx_x] = True

def process_trees_top(trees):
    for idx_x in range(len(trees[0])):
        prev = -1
        for idx_y in range(len(trees)):
            if int(trees[idx_y][idx_x]) > prev:
                prev = int(trees[idx_y][idx_x])
                map[idx_y][idx_x] = True

def process_trees_bottom(trees):
    for idx_x in range(len(trees[0])):
        prev = -1
        for idx_y in range(len(trees)-1, -1, -1):
            if int(trees[idx_y][idx_x]) > prev:
                prev = int(trees[idx_y][idx_x])
                map[idx_y][idx_x] = True

def increase_count_if_less(trees, idx_x, idx_y, x_range, y_range):
    count = 0
    for x in x_range:
        for y in y_range:
            if int(trees[y][x]) < int(trees[idx_y][idx_x]):
                count += 1
            else:
                return count + 1
    return count

def calculate_scenic_score(trees, idx_x, idx_y):
    return(
        increase_count_if_less(trees, idx_x, idx_y, range(idx_x - 1, -1, -1), [idx_y])
        * increase_count_if_less(trees, idx_x, idx_y, range(idx_x + 1, len(trees[0])), [idx_y])
        * increase_count_if_less(trees, idx_x, idx_y, [idx_x], range(idx_y - 1, -1, -1))
        * increase_count_if_less(trees, idx_x, idx_y, [idx_x], range(idx_y + 1, len(trees)))
    )

# part one
process_trees_left(trees)
process_trees_right(trees)
process_trees_top(trees)
process_trees_bottom(trees)
print(sum([1 for tree_row in map for visible in tree_row if visible]))

# part two
scenic_map = [calculate_scenic_score(trees, idx_x, idx_y) for idx_x in range(len(trees[0])) for idx_y in range(len(trees))]
print(max(scenic_map))


