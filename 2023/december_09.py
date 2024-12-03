# with open('oasis_data.txt', 'r') as file:
#     oasis_row_data = file.readlines()
# oasis_data = [[int(i) for i in list(line.strip().split())] for line in oasis_row_data]
#
# def value_calc(one_line):
#     data_list = [one_line]
#     next_line = []
#     i_round = 0
#     last_digit= None
#     while last_digit != 0:
#         for i in range(len(data_list[i_round]) - 1):
#             last_digit = data_list[i_round][i + 1] - data_list[i_round][i]
#             next_line.append(last_digit)
#         data_list.append(next_line)
#         next_line=[]
#         i_round += 1
#     while i_round != 0:
#         data_list[i_round-1].append(data_list[i_round][-1] + data_list[i_round-1][-1])
#         i_round -= 1
#     # print(data_list)
#     return data_list[0][-1]
#
# result = 0
#
# for data in oasis_data:
#     result += value_calc(data)
#
# print(result)

# print(*oasis_data, sep='\n')

with open('oasis_data.txt', 'r') as file:
    oasis_row_data = file.readlines()
oasis_data = [[int(i) for i in list(line.strip().split())] for line in oasis_row_data]

def value_calc(one_line):
    data_list = [one_line]
    next_line = []
    i_round = 0
    last_digit= None
    while last_digit != 0:
        for i in range(len(data_list[i_round]) - 1):
            last_digit = data_list[i_round][i + 1] - data_list[i_round][i]
            next_line.append(last_digit)
        data_list.append(next_line)
        next_line=[]
        i_round += 1
    while i_round != 0:
        data_list[i_round - 1].insert(0, data_list[i_round - 1][0] - data_list[i_round][0])
        data_list[i_round-1].append(data_list[i_round][-1] + data_list[i_round-1][-1])
        i_round -= 1
    # print(data_list)
    return [data_list[0][0], data_list[0][-1]]

start_result = 0
end_result = 0

for data in oasis_data:
    result = value_calc(data)
    start_result += result[0]
    end_result += result[1]

print(start_result)
print(end_result)
