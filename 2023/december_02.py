with open ("games.txt", "r") as file:
    games = file.readlines()
# je potřeba převést na seznam rozdělením pomocí dvojtečky
# z jednotlivých sad oddělených středníkem je třeba udělat samostatné seznamy
all_games = {}
for i in games:
    game, dices = i.split(": ")
    dices_list = dices.split("; ")
    final_dices = []
    for i in dices_list:
        set = {}
        set_list = i.split(", ")
        for item in set_list:
            set_value, set_key = item.strip().split(" ")
            set_value = int(set_value)
            set[set_key] = set_value
        final_dices.append(set)
    all_games[game] = final_dices

# množství kostek ve vaku
inicial_red = 12
inicial_green = 13
inicial_blue = 14
rounds_id = 0
count_id = 0
posible_games = 0
#Porovnání jednotlivých her,
for i in all_games:
    sets = len(i)
    enoug_colors = True
    for item in all_games[i]:
        if "blue" in item:
            if item["blue"] > inicial_blue:
                print(f"Na hru {i} je málo modrých kostek")
                enoug_colors = False
        if "red" in item:
            if item["red"] > inicial_red:
                print(f"Na hru {i} je málo rudých kostek")
                enoug_colors = False
        if "green" in item:
            if item["green"] > inicial_green:
                print(f"Na hru {i} je málo rudých kostek")
                enoug_colors = False
    rounds_id += 1
    if enoug_colors:
        posible_games += 1
        count_id += rounds_id

print(count_id)

