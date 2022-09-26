deck = input().split()
shuffle_count = int(input())

middle_deck = []

for shuffle in range(shuffle_count):
    final_deck = []
    middle_deck = len(deck) // 2

    left_side = middle_deck[0:middle_deck]
    right_side = middle_deck[middle_deck:]

    for index in range(left_side):
        final_deck.append(left_side[index])
        final_deck.append(right_side[index])

    deck = final_deck

print(deck)