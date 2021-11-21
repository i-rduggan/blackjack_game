##############################################
#                                            #
# Blackjack and Hookers                      #
#                                            #
##############################################

import random
import time

print("Welcome to blackjack and hookers!")
num_of_players = int(input("How many people are playing today? "))

#instantiate the players
players = {}
for i in range(1, num_of_players + 1):
    players[f"player {i}"] = []

#instantiate the cards (6 decks, input can change later)
cards = []
for i in range(1,52*6+1):
    cards.append(i)

round_counter = 0

#make sure all cards used are actually between 1 and 52
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

# make it so that it goes round twice instead of both cards at once maybe counter = 0 with while loop
def initial_deal():
    for i in range(1,3):
        for player in players.keys():
            card1 = card_calc(cards.pop(random.randint(0,len(cards)-1)))
            players[player].append(card1)

print("Please wait while I deal the cards.")
initial_deal()
time.sleep(0.5)

# this section deals with identifying cards for the player (who is always player 1)
def find_suits(card):
    if card >= 1 and card <= 13:
        return "diamonds"
    elif card > 13 and card <= 26:
        return "clubs"
    elif card > 26 and card <= 39:
        return "hearts"
    elif card > 39 and card <= 52:
        return "spades"

def convert_to_only_suit(card):
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
    new_card = convert_to_only_suit(card)
    if new_card == 1:
        return "ace"
    elif new_card > 10 and new_card <= 13:
        if new_card == 11:
            return "jack"
        elif new_card == 12:
            return "queen"
        elif new_card == 13:
            return "king"
    else:
        return new_card

#bit of a misnomer here, it's actually getting card values because all face cards are worth 10
def get_cards(players_cards):
    temp_hands = []
    for hand, card in players_cards.items():
        temp_hand = []
        for card in players_cards[hand]:
            converted_card = convert_to_only_suit(card)
            if converted_card == 1:
                temp_hand.append(11)
            # 2 - 9
            elif converted_card >= 2 and converted_card <= 9:
                temp_hand.append(converted_card)
            # 10 - 13
            elif converted_card > 9 and converted_card <=13:
                temp_hand.append(10)
        temp_hands.append(temp_hand)
    return temp_hands

#this is used to get the cards actual value to determine winner
player_cards = get_cards(players)
print(player_cards)

def card_string(card_list):
    card_string = "You currently have the "
    if len(card_list) == 1:
        card_string += str(is_face(card_list)) + " of " + str(find_suits(card_list)) + "."
    elif len(card_list) == 2:
        card_string += str(is_face(card_list[0])).capitalize() + " of " + str(find_suits(card_list[0])).capitalize() + " and " + str(is_face(card_list[1])).capitalize() + " of " + str(find_suits(card_list[1])).capitalize() + "."
    elif len(card_list) > 2:
        for i in range(0, len(card_list)):
            card_face = str(is_face(card_string[i])).capitalize()
            card_suit = str(find_suits(card_string[i])).capitalize()
            card_string += card_face + " of " + card_suit + " and, "
        card_string += str(is_face(card_string[-1])).capitalize() + " of " + str(find_suits(card_list[-1])) +  "."
    return card_string

print(card_string(players['player 1']))

def hit(player):
    add_card = card_calc(cards.pop(random.randint(0,len(cards)-1)))
    players[player].append(add_card)

def find_winner(player_cards):
    print(player_cards)
    player_sums = []
    for hand in player_cards:
        player_sums.append(sum(hand))
    return player_sums

decision = input("Would you like to hit or stand? ").lower()
print(decision)

if decision == "hit":
    hit('player 1')
    winner = find_winner(get_cards(players))
    print(card_string(players['player 1']))
    print("Other players stand.")
    again = input("Would you like to hit again?").lower()
    if again == "yes":
        hit('player 1')
        winner = find_winner(get_cards(players))
    if winner[0] > 21:
        print("BUST! Try again.")
    highest_hand = 0
    winning_player = ""
    for i in range(len(winner)):
        if winner[i] > highest_hand:
            highest_hand = winner[i]
            winning_player = f"player {i}"
    print(f"{winning_player} wins with {highest_hand}!")
else:
    print(find_winner(player_cards))

# find end result and display winner 
# to-do
# add ablility to hit, pass, double-down (computer is stuck with what it has, maybe some small AI like if total is less than 13 hit)
# find end result and display winner 
