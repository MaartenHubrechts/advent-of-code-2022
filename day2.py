from pathlib import Path

ROCK = 'A'
PAPER = 'B'
SICCORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

with open(Path("input/day2.txt")) as file:
    games = file.read().splitlines()


total_score = 0
for game in games:
    p1 = game[0]
    p2 = game[-1]
    score = 0

    if p2 == WIN:
        score += 6
    if p2 == DRAW:
        score += 3

    if p1 == ROCK and p2 == WIN:
        p2 = PAPER
    elif p1 == ROCK and p2 == DRAW:
        p2 = ROCK
    elif p1 ==  ROCK and p2 == LOSE:
        p2 = SICCORS
    
    if p1 == PAPER and p2 == WIN:
        p2 = SICCORS
    elif p1 == PAPER and p2 == DRAW:
        p2 = PAPER
    elif p1 == PAPER and p2 == LOSE:
        p2 = ROCK

    if p1 == SICCORS and p2 == WIN:
        p2 = ROCK
    elif p1 == SICCORS and p2 == DRAW:
        p2 = SICCORS
    elif p1 == SICCORS and p2 == LOSE:
        p2 = PAPER

    # score for shape
    if p2 == ROCK:
        score += 1
    if p2 == PAPER:
        score += 2
    if p2 == SICCORS:
        score += 3

    total_score += score

print(total_score)
    
