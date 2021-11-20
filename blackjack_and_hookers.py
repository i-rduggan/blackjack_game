import random

class Player:
    def __init__(self, cards = [], score = 0, chips = 200):
        self.cards = cards
        self.score = score
        self.chips = chips

card_suit = ["diamond", "club", "heart", "spade"]
card_val = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_deck = {}
for suit in card_suit:
    card_deck[suit] = card_val

print("Welcome to blackjack and hookers!")
num_of_players = int(input("How many people are playing today? "))

players = []
for i in range(1, num_of_players + 1):
    players.append(i)

cards = []

for i in range(1,52*6+1):
    cards.append(i)

round_counter = 0

def card_calc(card):
    if card >= 1 and card <= 52:
        return card
    elif card <= 52 * 2:
        return card - 52
    elif card <= 52 * 3:
        return card - 52 * 2
    elif card <= 52 * 4:
        return card - 52 * 3
    elif card <= 52 * 5:
        return card - 52 * 4
    else:
        return card - 52 * 5

def initial_deal():
    players_cards = []
    for player in players:
        player_cards = []
        card1 = cards.pop(random.randint(0,len(cards)-1))
        card_calc1 = card_calc(card1)
        player_cards.append(card_calc1)
        card2 = cards.pop(random.randint(0,len(cards)-1))
        card_calc2 = card_calc(card2)
        player_cards.append(card_calc2)
        players_cards.append(player_cards)
    return players_cards

players_cards = initial_deal()
def get_cards(players_cards):
    temp_hands = []
    for hand in players_cards:
        temp_hand = []
        for card in hand:
            val = 0
            # 1 - 9
            if card >= 1 and card <= 9:
                temp_hand.append(card)
            # 10 - 13
            elif card > 9 and card <=13:
                val = 10
                temp_hand.append(val)
            # 13 - 22
            elif card <= 13 * 2 - 4:
                val = card - 13
                temp_hand.append(val)
            # 23 - 26
            elif card > 13 * 2 - 4 and card <= 13 * 2:
                val = 10
                temp_hand.append(val)   
            # 27 - 35
            elif card <= 13 * 3 - 4:
                val = card - (13 * 2)
                temp_hand.append(val)
            # 36 - 39
            elif card > 13 * 3 - 4 and card <= 13 * 3:
                val = 10
                temp_hand.append(val)
            # 40 - 48
            elif card <= 13 * 4 - 4:
                val = card - 13 * 3
                temp_hand.append(val)
            # 49 - 52
            elif card > 13 * 4 - 4:
                val = 10
                temp_hand.append(val)
        temp_hands.append(temp_hand)
    return temp_hands
test_hand = [[1,2,3,4,5,6,7,8,9,13],[14,15,16,17,18,19,20,21,22,26],[27,28,29,30,31,32,33,34,35,39],[40,41,42,43,44,45,46,47,48,52]] 
#print(test_hand)
print(get_cards(players_cards))
