with open ("scratchcards.txt", "r") as file:
    cards = file.readlines()
    scratchcards = {}

for i in cards:
    card_name, to_check = i.strip().split(": ")
    card_part, control_part = to_check.strip().split("| ")
    scratchcards[card_name] = {
        "card_numbers": list(card_part.strip().split()),
        "control_numbers":  list(control_part.strip().split())
    }

subtotal = 0
totalsum = 0

for value in scratchcards.values():
    for nr in value['card_numbers']:
        if subtotal == 0 and nr in value['control_numbers']:
            subtotal += 1
        elif nr in value['control_numbers']:
            subtotal *= 2
    totalsum += subtotal
    subtotal = 0

print(totalsum)


