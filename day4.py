from pathlib import Path

with open(Path("input/day4.txt")) as file:
    sections = file.read().splitlines()
count = 0
for section in sections:
    first_section = section.split(',')[0]
    second_section = section.split(',')[1]

    first_section_start = int(first_section.split('-')[0])
    first_section_end = int(first_section.split('-')[1])
    second_section_start = int(second_section.split('-')[0])
    second_section_end = int(second_section.split('-')[1])
    
    if (first_section_start <= second_section_start and first_section_end >= second_section_start) or (second_section_start <= first_section_start and second_section_end >= first_section_start):
        count += 1
    elif (first_section_start <= second_section_end and first_section_end >= second_section_end) or (second_section_start <= first_section_end and second_section_end >= first_section_end):
        count += 1
    elif (first_section_start <= second_section_start and first_section_end >= second_section_end) or (second_section_start <= first_section_start and second_section_end >= first_section_end):
        count += 1

print(count)
