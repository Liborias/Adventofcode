import re
with open('mul_operations.txt', 'r') as file:
    row_operators = file.readlines()

string_operators =''
for line in row_operators:
    for i in line:
        string_operators += i

operators = re.findall(r'mul\(\d+,\d+\)', string_operators)
switched_operators = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", string_operators)
mul_operators = []

# part 1
for i in operators:
    changed_i = i.replace('(', ':(')
    new_key, new_value = [part.strip() for part in changed_i.split(':')]
    new_value = tuple(map(int, new_value.strip('()').split(',')))
    one_operator = {new_key: new_value}
    mul_operators.append(one_operator)

part1_result = 0
for i in mul_operators:
    mul = i['mul'][0] * i['mul'][1]
    part1_result += mul

# part 2
mul_operators2 = []
validator = False
for i in switched_operators:
    if i == 'don\'t()':
        validator = False
    elif i == 'do()':
        validator = True
    else:
        if validator:
            changed_i = i.replace('(', ':(')
            new_key, new_value = [part.strip() for part in changed_i.split(':')]
            new_value = tuple(map(int, new_value.strip('()').split(',')))
            one_operator = {new_key: new_value}
            mul_operators2.append(one_operator)

part2_result = 0
for i in mul_operators2:
    mul = i['mul'][0] * i['mul'][1]
    part2_result += mul

# print(mul_operators2)
# print(switched_operators)
# print(string_operators)
print(part1_result)
print(part2_result)

