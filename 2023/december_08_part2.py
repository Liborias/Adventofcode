# import re
#
# with open('l_r_map.txt', 'r') as file:
#     instruction = list(file.readline().strip())
#     file.readline()
#     coord = file.readlines()
#
# coordinates = {}
# for line in coord:
#     parts = [item.strip() for item in re.split(r'[;=,()\n]', line.strip()) if item.strip()]
#     coordinates[parts[0]] = (parts[1], parts[2])
#
# all_keys = list(coordinates.keys())
# keys = [key for key in all_keys if key.endswith("A")]
# to_go = 'AAA'
# target = 'ZZZ'
# step = 0
# all_ends = [0] * len(keys)
# go_to = keys[:]
# instruction_len = len(instruction)
# keys_len = len(keys)
#
# # while to_go != target:
# #     direction = instruction[step % instruction_len] # cycle for repeting in instruction range
# #     go = 0 if direction == 'L' else 1
# #     to_go = coordinates[to_go][go]
# #     step += 1
# # print(step)
#
#
# def finder(key, key_index, side):
#     my_go = 0 if side == 'L' else 1
#     my_go_to = coordinates[key][my_go]
#     go_to[key_index] = my_go_to
#     all_ends[key_index] = 1 if my_go_to.endswith('Z') else 0
#     if my_go_to.endswith('Z'):
#         print(my_go_to)
#
#
# while sum(all_ends) != 6:
#     my_direction = instruction[step % instruction_len]  # cycle for repeting in instruction range
#     my_key = keys[step % keys_len]  # cycle for repeting in keys range
#     my_key_index = step % keys_len
#     finder(my_key, my_key_index, my_direction)
#     step += 1
#     # print(all_ends)
#     # print(step)
#     # print(go_to)


#
# import re
#
# # Načti instrukce a mapu
# with open('l_r_map.txt', 'r') as file:
#     instruction = file.readline().strip()
#     file.readline()  # Přeskočit prázdný řádek
#     coord = file.readlines()
#
# # Převést koordináty na slovník
# coordinates = {}
# for line in coord:
#     parts = [item.strip() for item in re.split(r'[;=,()\n]', line.strip()) if item.strip()]
#     coordinates[parts[0]] = (parts[1], parts[2])
#
# # Najdi všechny startovací uzly končící na "A"
# current_nodes = [key for key in coordinates if key.endswith("A")]
# steps = 0
# instruction_len = len(instruction)
#
#
# # Hlavní smyčka
# while not all(node.endswith("Z") for node in current_nodes):
#     next_nodes = []
#     direction = instruction[steps % instruction_len]  # Cyklování instrukcí
#     for node in current_nodes:
#         # Vyber další uzel na základě směru
#         if direction == "L":
#             next_nodes.append(coordinates[node][0])
#         elif direction == "R":
#             next_nodes.append(coordinates[node][1])
#     current_nodes = next_nodes  # Aktualizuj uzly
#     steps += 1
#
# print(steps)

import math

def get_steps(start):
    steps = 0
    pos = start
    while not pos.endswith("Z"):
        dir = directions[steps % len_dirs]
        pos = node_map[pos][dir]
        steps += 1
    return steps


with open('l_r_map.txt', "r") as f:
    directions_str, _, *nodes = (l.strip() for l in f.readlines())

directions = [int(c == "R") for c in directions_str]
len_dirs = len(directions)
node_map = {}
startings = []
for line in nodes:
    key, targets = line.split(" = ")
    if key.endswith("A"):
        startings.append(key)
    node_map[key] = targets.strip("()").split(", ")


part1 = get_steps("AAA")
print(f"Part 1: {part1}")

step_counts = [get_steps(start) for start in startings]
part2 = math.lcm(*step_counts)
print(f"Part 2: {part2}")
