from pathlib import Path

with open(Path("input/day1.txt")) as file:
    food_inputs = file.read().splitlines()

food = []
food_group = []
for food_input in food_inputs:
    if food_input:
        food_group.append(int(food_input))
    else:
        food.append(food_group)
        food_group = []
if food_group:
    food.append(food_group)

calorie_counts = [sum(food_group) for food_group in food]
calorie_counts.sort(reverse=True)
print(sum(calorie_counts[:3]))
