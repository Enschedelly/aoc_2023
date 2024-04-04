import re

all_cards = []
won_cards = []
with open('inputs/scratchcards.txt') as sc:
    for line in sc:
        card = re.split(': | \\| ', line)

        all_cards.append(card)

won_cards = all_cards
i = 0            
cards_left = True
while cards_left:
    try:
        card = won_cards[i]
        card_number = card[0].split()[-1]
        win = card[1].split()
        have = card[2].split()
        next_idx = int(card_number) 
        for number in win:
            if number in have:
                won_cards.append(all_cards[next_idx])
                next_idx += 1
                if next_idx >= len(all_cards):
                    break
        i += 1
    except IndexError:
        cards_left = False

print(len(won_cards))
