import random

card_suit = ["diamond", "club", "heart", "spade"]
card_val = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_deck = {}
for suit in card_suit:
    card_deck[suit] = card_val

print(card_deck)