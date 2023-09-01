from pathlib import Path
import re

with open(Path("input/day5.txt")) as file:
    crates_and_moves = file.read().splitlines()


crates = [item for item in crates_and_moves if 'move' not in item and item]
moves = [item for item in crates_and_moves if 'move' in item]
num_stacks = int(crates[-1][-2])

crates_simplified = []
for crate in crates:
    crate_simplified = []
    for i in range(num_stacks):
        crate_simplified += crate[i*4 + 1]
    crates_simplified += [crate_simplified]

crates_simplified = crates_simplified[::-1][1:]

stacks = [[] for x in range(num_stacks)]

for crate in crates_simplified:
    for i in range(num_stacks):
        if crate[i] != ' ':
            stacks[i].append(crate[i])

moves_simplified = [re.findall(r'\d+', move) for move in moves]

for move in moves_simplified:
    items_to_move = []
    for x in range(int(move[0])):
        item = stacks[int(move[1])-1].pop()
        items_to_move+=item
    stacks[int(move[2])-1]+=items_to_move[::-1]

res = ''
for stack in stacks:
    res+=stack.pop()

print(res)