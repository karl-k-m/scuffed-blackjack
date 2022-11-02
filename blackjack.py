from collections import namedtuple
import random
from settings import *

def generate_hands_deck():  # Generates shuffled deck and creates player and dealer hand lists
    global deck, player, player_total, dealer, dealer_total
    player = []
    player_total = 0
    dealer = []
    dealer_total = 0
    deck = []
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = namedtuple('card', ['value', 'suit'])
    deck = list(card(value, suit) for suit in suits for value in range(1,14))
    random.shuffle(deck)

def deal(target, amount):    # Chooses <amount> card(s) from deck at random, adds them to target and removes them from deck
    global deck, player, player_total, dealer, dealer_total
    x = []
    for i in range(1, amount + 1):
        y = deck[random.randint(1, len(deck) - 1)]
        if y.value in range(2, 11):
            player_total += y.value
        elif y.value in range(11, 14):
            player_total += 10
        else:
            if player_total + 11 > 21:
                player_total += 1
            else:
                player_total += 11
        x.append(y)
        deck.remove(y)
    target.extend(x)