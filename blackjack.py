from collections import namedtuple
import random

def generate_hands_deck():
    global deck
    global player
    global dealer
    player = []
    dealer = []
    deck = []
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = namedtuple('card', ['value', 'suit'])
    deck = list(card(value, suit) for suit in suits for value in range(1,14))
    random.shuffle(deck)

def deal(amount, recipient):
    x = []
    for i in range(1, amount + 1):
        y = deck[random.randint(1, len(deck) - 1)]
        x.append(y)
        deck.remove(y)
    recipient.append(x)

generate_hands_deck()