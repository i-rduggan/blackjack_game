import random

class Player:
    def __init__(self, cards, score = 0, chips = 200):
        self.cards = cards
        self.score = score
        self.chips = chips


card_suit = ["diamond", "club", "heart", "spade"]
card_val = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_deck = {}
for suit in card_suit:
    card_deck[suit] = card_val

cards = []

for i in range(1,53):
    cards.append(i)

player1 = Player([1,2])

print(cards)