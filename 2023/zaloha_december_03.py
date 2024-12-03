from subprocess import check_call

with open ("engin.txt", "r") as file:
    engin = file.readlines()

# first all lines to separated lists and all those lists to complete engin list
engin_list = []
line_list = []

checked_symbols = ""

for line in engin:
    for index in line:
        line_list.append(index)
    engin_list.append(line_list)
    # print(line_list)
    line_list = []

def valid_digit_check(data, row, col):
    engin_rows, engin_cols = len(data), len(data[0])
    checked_directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for dr, dc in checked_directions:
        r, c = row + dr, col + dc
        if 0 <= r < engin_rows and 0 <= c < engin_cols:
            if data[r][c] != ".":
                return True
    return False

current_row = 0
current_col = 0
stored_digit = "" # odkládací proměnná
ok_digit = False # odkládací proměnná
parts_list = []

for line in engin_list:
    for symbol in line:
        if symbol.isdigit():
            stored_digit += str(symbol)
            if valid_digit_check(engin_list, current_row, current_col):
                ok_digit = True
            current_col += 1
        elif symbol.isdigit() == False and stored_digit !="":
                if ok_digit == True:
                    parts_list.append(int(stored_digit))
                ok_digit = False
                stored_digit = ""
                current_col += 1
    current_row +=1
    current_col = 0

result = sum(parts_list)
#
# for item in checked_symbols.split(","):
#     if item.isdigit():
#         result += int(item)
#         parts_list.append(int(item))
#
print(result)
print(parts_list)

