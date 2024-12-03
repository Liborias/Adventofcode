with open('camel_game.txt', 'r') as file:
    lines = file.readlines()
    camel_game = [line.strip().split() for line in lines]

card_values = {
    '2': 'a',
    '3': 'b',
    '4': 'c',
    '5': 'd',
    '6': 'e',
    '7': 'f',
    '8': 'g',
    '9': 'h',
    'T': 'i',
    'J': 'j',
    'Q': 'k',
    'K': 'l',
    'A': 'm'
}

# changing hands in list to easily sortable system
maped_camel_game = []
mapovani = str.maketrans(card_values)
for game in camel_game:
    remaped_game = []
    remaped_hand = game[0].translate(mapovani)
    remaped_game.append(remaped_hand)
    remaped_game.append(game[1])
    maped_camel_game.append(remaped_game)

hand_values = {
    'high_card': [],
    'one_pair': [],
    'two_pair': [],
    'three_of_a_kind': [],
    'full_house': [],
    'four_of_a_kind': [],
    'five_of_a_kind': [],
}


def sorter(hand, item):
    if len(set(hand)) == 5:
        hand_values['high_card'].append(item)
    elif len(set(hand)) == 4:
        hand_values['one_pair'].append(item)
    elif len(set(hand)) == 3:
        this_hand = any(hand.count(char) == 3 for char in set(hand))
        if this_hand:
            hand_values['three_of_a_kind'].append(item)
        else:
            hand_values['two_pair'].append(item)
    elif len(set(hand)) == 2:
        this_hand = any(hand.count(char) == 4 for char in set(hand))
        if this_hand:
            hand_values['four_of_a_kind'].append(item)
        else:
           hand_values['full_house'].append(item)
    elif len(set(hand)) == 1:
        hand_values['five_of_a_kind'].append(item)

for i in maped_camel_game:
    sorter(i[0], i)

# evaluating the game
evaluated_games = []
result = 0
hand_values_keys = list(hand_values.keys())
for item in hand_values_keys:
    for game in sorted(hand_values[item]):
        evaluated_games.append(int(game[1]))

# final count
for  inx, item in enumerate(evaluated_games):
    actual_win = item * (inx + 1)
    result += actual_win
print(result)
