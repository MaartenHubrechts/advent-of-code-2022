from pathlib import Path

with open(Path("input/day6.txt")) as file:
    signal = file.read()

res = -1
for i in range(len(signal)):
    if i >= 13:
        code = signal[(i-13):i+1]
        if 14 == len(set(code)):
            res = i
            break

print(res+1)