import re

all_cards = []
won_cards = {}
with open('inputs/scratchcards.txt') as sc:
    for line in sc:  # Put the entire card collection in an array.
        card = re.split(': | \\| ', line)  # Split the cards by [card id, winning number, numbers you have]

        all_cards.append(card)

for card in all_cards:  # Fill the dictionary of won cards with the initial hand
    print(card[0].split()[-1])  # Dict won_cards = {card_id: number_won}
    won_cards[int(card[0].split()[-1])] = 1
          
for card_number in range(1, len(all_cards) + 1):  # For each card_id
    card = all_cards[card_number - 1]  # Get te card and get all win and have numbers.
    win = card[1].split()
    have = card[2].split()
    cards_won = 0
    for number in win:  # For each number in win
        if number in have:  # If we have that on our card, add a won card.
            cards_won += 1
    multiply = won_cards.get(card_number)  # Get the amount of cards we have for the current card ID.

    for next_card in range(1, cards_won + 1):  # Add the multiply value to the next amount of cards won.
        current_cards = won_cards.get(card_number + next_card)
        print('multiply, current_cards', multiply, current_cards, (current_cards + multiply))
        won_cards[card_number + next_card] = current_cards + multiply

total = 0  
for key, value in won_cards.items():  # Count all cards
    total += value

print(total)