with open('2024/places.txt', 'r') as file:
    all_coordinates = file.readlines()
    coordinates =  [list(line.split()) for line in all_coordinates]
    coo1, coo2 = [int(line[0]) for line in coordinates], [int(line[1]) for line in coordinates]

result1 = 0
result2 = 0

def find_match(nr):
    matches = 0
    for i in coo2:
        if nr == i:
            matches += 1
    return matches * nr    

for i in range(len(coo1)):
    result1 +=  abs(sorted(coo2)[i] - sorted(coo1)[i])
    result2 += find_match(coo1[i])

print(result1)
print(result2)