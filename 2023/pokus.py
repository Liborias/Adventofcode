with open("engin.txt", "r") as file:
    engin = file.readlines()

# Převod vstupních dat do seznamu seznamů
engin_list = [list(line.strip()) for line in engin]

stored_nr = ""
right_check = 0
current_row = 0
current_col = 0
parts = []

directions = [
]

def valid_digit_check(data, row, col, direction):
    engin_rows, engin_cols = len(data), len(data[0])
    for dr, dc in direction:
        r, c = row + dr, col + dc
        if 0 <= r < engin_rows and 0 <= c < engin_cols:
            if data[r][c] != ".":
                return True
    return False

for indx, line in enumerate(engin_list):
    for idx, symbol in enumerate(line):
        if symbol.isdigit() and line[idx - 1].isdigit() != True:
            stored_nr += symbol
            if indx != 0:
                directions.append((-1, 0))
            if indx != len(engin_list) + 1:
                directions.append((1, 0))
            right_check += 1
            # druhé číslo
            if idx + 1 < len(line) and line[idx + 1].isdigit():
                stored_nr += line[idx + 1]
                if indx != 0:
                    directions.append((-1, 1))
                if indx != len(engin_list) + 1:
                    directions.append((1, 1))
                right_check += 1
                # třetí číslo
                if idx + 2 < len(line) and line[idx + 2].isdigit():
                    stored_nr += line[idx + 2]
                    if indx != 0:
                        directions.append((-1, 2))
                    if indx != len(engin_list) + 1:
                        directions.append((1, 2))
                    right_check += 1
                    # čtvrté číslo, kdyby bylo
                    if idx + 3 < len(line) and line[idx + 3].isdigit():
                        stored_nr += line[idx + 3]
                        if indx != 0:
                            directions.append((-1, 3))
                        if indx != len(engin_list) + 1:
                            directions.append((1, 3))
                        right_check += 1

            if idx != 0:
                directions.append((0, -1))
                if indx != 0:
                    directions.append((-1, -1))
                if indx != len(engin_list):
                    directions.append((1, -1))
            if idx + right_check != len(line):
                directions.append((0, right_check))
                if indx != 0:
                    directions.append((-1, right_check))
                if indx != len(engin_list):
                    directions.append((1, right_check))
            if valid_digit_check(engin_list, current_row, current_col, directions):
                parts.append(int(stored_nr))

            stored_nr = ""
            directions = []
            right_check = 0

        else:
            stored_nr = ""
            directions = []
            right_check = 0
            pass

        current_col += 1
    stored_nr = ""
    directions =[]
    right_check = 0
    current_row += 1
    current_col = 0

print(sum(parts))