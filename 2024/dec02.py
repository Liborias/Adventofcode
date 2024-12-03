with open('nuclear_set.txt', 'r') as file:
    row_data = file.readlines()
    data = [[int(i) for i in line.split()] for line in row_data]

def try_without(sample):
    my_data = []
    for my_index in range(len(sample)):
        new_sample = []
        for ix, value in enumerate(sample):
            if ix != my_index:
                new_sample.append(value)
        my_data.append(new_sample)
    return my_data

def check_tresholds(packet, treshold1, treshold2):
    result = True
    for i in range(1, len(packet)):
        if abs(packet[i] - packet[i - 1]) > treshold1:
            if abs(packet[i] - packet[i - 1]) < treshold2:
                result = True
            else:
                return False
        else:
            return False
    return result
semi_part2_result = 0
part1_result = 0
part2_result = 0

for this_packet in data:
    #part1
    if sorted(this_packet) == this_packet or sorted(this_packet, reverse=True) == this_packet:
        if check_tresholds(this_packet, 0, 4):
            part1_result += 1
    # part2
    new_packets = try_without(this_packet)
    for my_packet in new_packets:
        if sorted(my_packet) == my_packet or sorted(my_packet, reverse=True) == my_packet:
            if check_tresholds(my_packet, 0, 4):
                semi_part2_result += 1
    if semi_part2_result > 0:

        part2_result += 1
    semi_part2_result = 0

print(part1_result)
print(part2_result)
