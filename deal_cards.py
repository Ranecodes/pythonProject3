import create_deck
deck = create_deck.deck
def deal_cards(deck, number):
    hand_value = 0

    if number > len(deck):
        number = len(deck)

    for count in range(number):
        key, value = deck.popitem()
        print(key)
        hand_value += value

    print("The hand value is ", hand_value)


