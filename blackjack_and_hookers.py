##############################################
#                                            #
# Blackjack and Hookers                      #
#                                            #
##############################################

import random
import time

print("Welcome to blackjack and hookers!")
num_of_players = int(input("How many people are playing today? "))

players = {}
for i in range(1, num_of_players + 1):
    players[f"player {i}"] = []

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
    for player in players.keys():
        card1 = card_calc(cards.pop(random.randint(0,len(cards)-1)))
        card2 = card_calc(cards.pop(random.randint(0,len(cards)-1)))
        players[player].append(card1)
        players[player].append(card2)

print("Please wait while I deal the cards.")
initial_deal()
time.sleep(0.5)

def find_suits(card):
    if card >= 1 and card <= 13:
        return "diamonds"
    elif card > 13 and card <= 26:
        return "clubs"
    elif card > 26 and card <= 39:
        return "hearts"
    elif card > 39 and card <= 52:
        return "spades"

def convert_for_is_face(card):
    if card >= 1 and card <= 13:
        return card
    elif card > 13 and card <= 26:
        return card - 13
    elif card > 26 and card <= 39:
        return card - 13 * 2
    elif card > 39 and card <= 52:
        return card - 13 * 3
    else:
        return card

def is_face(card):
    new_card = convert_for_is_face(card)
    if new_card > 9 and new_card <= 13:
        if new_card == 10:
            return "jack"
        elif new_card == 11:
            return "queen"
        elif new_card == 12:
            return "king"
        elif new_card == 13:
            return "ace"
    else:
        return new_card

def get_cards(players_cards):
    temp_hands = []
    for hand, card in players_cards.items():
        temp_hand = []
        for card in players_cards[hand]:
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

player_cards = get_cards(players)

string = "You currently have "

for card in players['player 1']:
    string += str(is_face(card)) + " of " +  str(find_suits(card)) + " and "

print(string)
# test_hand = [[1,2,3,4,5,6,7,8,9,13],[14,15,16,17,18,19,20,21,22,26],[27,28,29,30,31,32,33,34,35,39],[40,41,42,43,44,45,46,47,48,52]] 
# print(test_hand)
# print(get_cards(players_cards))
