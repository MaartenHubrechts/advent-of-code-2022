from pathlib import Path

with open(Path("input/day9.txt")) as file:
    moves = file.read().splitlines()

head_position = (0, 0)
tails_positions = [(0, 0) for _ in range(9)]

visited = set()
visited.add(tails_positions[-1])

def is_adjacent(head_position, tail_position):
    return (
        (abs(head_position[0] - tail_position[0]) <= 1)
        and (abs(head_position[1] - tail_position[1]) <= 1)
    )

def move_tail_position_coordinate(head_position, tail_position, coordinate):
    if head_position[coordinate] - tail_position[coordinate] > 1:
        return head_position[coordinate] - 1
    elif head_position[coordinate] - tail_position[coordinate] < -1:
        return head_position[coordinate] + 1
    else:
        return head_position[coordinate]

def move_tail_position(head_position, tail_position):
    tail_position_x = move_tail_position_coordinate(head_position, tail_position, 0)
    tail_position_y = move_tail_position_coordinate(head_position, tail_position, 1)
    return (tail_position_x, tail_position_y)

for move in moves:
    direction, steps = move.split(' ')
    if direction == 'U':
        move_head_position = (lambda x: (x[0], x[1] + 1))
    elif direction == 'D':
        move_head_position = (lambda x: (x[0], x[1] - 1))
    elif direction == 'R':
        move_head_position = (lambda x: (x[0] + 1, x[1]))
    else:
        move_head_position = (lambda x: (x[0] - 1, x[1]))
    
    for _ in range(int(steps)):
        head_position = move_head_position(head_position)
        for idx, tail_position in enumerate(tails_positions):
            if idx == 0:
                current_head_position = head_position
            else:
                current_head_position = tails_positions[idx - 1]
            if not is_adjacent(current_head_position, tail_position):
                tails_positions[idx] = move_tail_position(current_head_position, tail_position)
            if idx == len(tails_positions) - 1:
                visited.add(tails_positions[idx])

print(len(visited))