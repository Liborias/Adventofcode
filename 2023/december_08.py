import re

with open('l_r_map.txt', 'r') as file:
    instruction = list(file.readline().strip())
    file.readline()
    coord = file.readlines()

coordinates = {}
for line in coord:
    parts = [item.strip() for item in re.split(r'[;=,()\n]', line.strip()) if item.strip()]
    coordinates[parts[0]] = (parts[1], parts[2])

to_go = 'AAA'
target = 'ZZZ'
step = 0
instruction_len = len(instruction)

while to_go != target:
    direction = instruction[step % instruction_len] # cycle for repeting in instruction range
    go = 0 if direction == 'L' else 1
    to_go = coordinates[to_go][go]
    step += 1

print(step)