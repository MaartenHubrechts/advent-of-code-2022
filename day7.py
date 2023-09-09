from pathlib import Path

with open(Path("input/day7.txt")) as file:
    commands = file.read().splitlines()

grouped_commands = []
current_command = []

# group commands together (command + output)
for command in commands:
    if command[0] == '$':
        grouped_commands.append(current_command)
        current_command = [command]
    else:
        current_command += [command]
grouped_commands.append(current_command)

grouped_commands = grouped_commands[1:]  # remove first empty list


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
        self.files = []

    def get_size(self):
        return self.size + sum([child.get_size() for child in self.children])


ROOT_DIR = Directory(name='/', parent=None)
CURRENT_DIR = ROOT_DIR


def process_command(command, output):
    if 'cd' in command:
        process_cd(command.split(' ')[1])
    elif 'ls' in command:
        process_ls(output)
    else:
        raise ValueError('Unknown command given.')


def process_cd(dir):
    global CURRENT_DIR
    if dir == '/':
        CURRENT_DIR = ROOT_DIR
    elif dir == '..':
        CURRENT_DIR = CURRENT_DIR.parent
    else:
        CURRENT_DIR = [d for d in CURRENT_DIR.children if d.name == dir][0]


def process_ls(output):
    global CURRENT_DIR
    for file_or_dir in output:
        res = file_or_dir.split(' ')
        if res[0] == 'dir':
            new_dir = Directory(name=res[1], parent=CURRENT_DIR)
            CURRENT_DIR.children.append(new_dir)
        else:
            CURRENT_DIR.size += int(res[0])


# process individual grouped commands
for grouped_command in grouped_commands:
    command = grouped_command[0][2:]
    output = grouped_command[1:]
    process_command(command, output)

result = 0

def count(directory):
    global result
    if directory.get_size() <= 100000:
        result += directory.get_size()
    for child in directory.children:
        count(child)

required = ROOT_DIR.get_size() - 40000000
smallest = ROOT_DIR.get_size()

def find_smallest(directory):
    global required, smallest
    if directory.get_size() >= required and directory.get_size() < smallest:
        smallest = directory.get_size()
    for child in directory.children:
        find_smallest(child)


count(ROOT_DIR)
find_smallest(ROOT_DIR)
print(result)
print(smallest)
