with open("almanac.txt", "r") as file:
    almanac_source = file.readlines()

almanac = {}
almanac_data = []
almanac_key = None

for inx, line in enumerate(almanac_source):
    if inx == 0:
        almanac_key, my_data = line.strip().split(':')
        almanac_data.append([int(x) if x.isdigit() else x for x in my_data.strip().split()])
    elif line[0].isalpha():
        if almanac_key is not None and almanac_data:
            almanac[almanac_key] = almanac_data
        almanac_key = line.replace(':', '').strip()
        almanac_data = []
    elif line[0].isdigit():
        almanac_data.append([int(x) if x.isdigit() else x for x in line.strip().split()])

# Zpracuj poslední klíč
if almanac_key is not None and almanac_data:
    almanac[almanac_key] = almanac_data

care_plan = {
    'seed': None,
    'soil': None,
    'fertilizer': None,
    'water': None,
    'light': None,
    'temperature': None,
    'humidity': None,
    'location': None,
}
almanac_keys = list(almanac.keys())
care_plan_keys = list(care_plan.keys())
seeds = []

for i in almanac["seeds"][0]:
    care_plan['seed'] = i
    seeds.append(care_plan.copy())

def shifter(mapping, source_value):
    for x in mapping:
        if source_value >= x[1] and source_value <= x[1] + x[2]:
            return x[0] + (source_value - x[1])
    return source_value

for seed in seeds:
    for key in range(len(almanac_keys) - 1):  # Iterace omezená na počet map
        source_key = care_plan_keys[key]
        target_key = care_plan_keys[key + 1]

        if key + 1 >= len(almanac_keys):
            print(f"Chybějící mapa pro {target_key}")
            continue

        seed[target_key] = shifter(almanac[almanac_keys[key + 1]], seed[source_key])

lowest_location = None

for i in seeds:
    if None == lowest_location:
        lowest_location = i['location']
    elif i['location'] < lowest_location:
        lowest_location = i['location']
print(lowest_location)


print(seeds)
