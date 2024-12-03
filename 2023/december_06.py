with open("rices.txt", "r") as file:
    lines = file.readlines()

races = {}
for i in lines:
    my_key, my_value = i.strip().split(":")
    values = [int(x) for x in my_value.strip().split()]
    races[my_key] = values

result = 0
largest_distance = 0
ways_to_win = 0
# speed = 0

for race in range(len(races['Time'])):
    for i in range(1, races['Time'][race] + 1):
        current_distance = i * (races['Time'][race] - i)
    #     if current_distance > largest_distance:
    #         largest_distance = current_distance
        if current_distance > races['Distance'][race]:
            ways_to_win += 1
    # largest_distance = 0
    if result != 0:
       result *= ways_to_win
    else:
        result = ways_to_win
    ways_to_win = 0

print(result)