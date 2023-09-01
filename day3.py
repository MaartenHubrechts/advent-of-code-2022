from pathlib import Path

with open(Path("input/day3.txt")) as file:
    sacks = file.read().splitlines()

items = []
for i in range(0, len(sacks), 3):
    # items += list(set([c for c in first_compartement if c in second_compartement]))
    sack1 = sacks[i]
    sack2 = sacks[i+1]
    sack3 = sacks[i+2]

    items += list(set([c for c in sack1 if c in sack2 and c in sack3]))

counts = [ord(c) - 96 if c.islower() else ord(c) - 38 for c in items]
print(sum(counts))