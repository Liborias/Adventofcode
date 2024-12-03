with open("data.txt", "r") as data:
    new_data = data.readlines()

def calc_code(my_data):
    values = []
    result = 0
    for index in new_data:
        first_digit = None
        second_digit = None
        for i in index:
            if int(i.isdigit()):
                if first_digit == None:
                    first_digit = i
                second_digit = i
        values.append(int(str(first_digit) + str(second_digit)))
    for digit in values:
        result += digit
    return result

print(calc_code(new_data))



