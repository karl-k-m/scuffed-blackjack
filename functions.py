import pygame as pg
import os
from settings import *
import random
from collections import namedtuple
#--------------------------------

def choose_color(rect, mouse_pos, fill = False): #changes color of an entity if the player is hovering on the box
    if fill:
        if rect.collidepoint(mouse_pos):
            button_color = 0
        else:
            button_color = 4
    else:
        if rect.collidepoint(mouse_pos):
           button_color = "black"
        else:
            button_color = "white"
    return button_color

def get_profiles(): #gets all profiles from the profiles.txt file and sorts them into a list, ["name", "money_value"]
    with open(os.path.abspath("scuffed-blackjack\profiles.txt"), "r") as file:
        profiles = list(map(lambda x: x.strip("\n").split(":"), file.readlines()))
    return profiles

def save_profile(name, money): #saves a profile to the profiles.txt
    with open(os.path.abspath("scuffed-blackjack\profiles.txt"), "a") as file:
        file.write("\n" + name + ":" + str(money))
    file.close()

def create_card(card): #builds a card depening on the input and puts it on the screen
    if card.value in range(1, 10):  #argument must be namedtuple('card', ['value', 'suit'])
        card_name, value_text = "blank", card.value + 1
    elif card.value == 10: 
        card_name, value_text = "Jack", "J"
    elif card.value == 11:
        card_name, value_text = "Queen", "Q"
    elif card.value == 12:
        card_name, value_text = "King", "K"
    elif card.value == 13:
        card_name, value_text = "blank", "A"

    card_image = pg.image.load(os.path.abspath("scuffed-blackjack\Assets\card_" + card_name + ".png"))
    text_card = text_font.render(str(value_text), 1, "black")
    card_suit = pg.transform.scale(pg.image.load(os.path.abspath("scuffed-blackjack\Assets\_" + card.suit + ".jpg")), (70, 70))
    
    card_image.blit(card_suit, (card_image.get_width()-card_suit.get_width()-10, 10))
    card_image.blit(card_suit, (10, card_image.get_height()-card_suit.get_height()-10))
    card_image.blit(text_card, (card_image.get_width()-card_suit.get_width()-text_card.get_width()-10, 10))
    card_image.blit(text_card, (text_card.get_height()+10, card_image.get_height()-card_suit.get_height()-10))

    if isinstance(value_text, int):
        text_card = pg.transform.scale(text_card, (130, 160))
        card_image.blit(text_card, (card_image.get_width()/2-text_card.get_width()/2, card_image.get_height()/2-text_card.get_height()/2))
    elif value_text == "A":
        card_suit = pg.transform.scale(pg.image.load(os.path.abspath("scuffed-blackjack\assets\_" + card.suit + ".jpg")), (130, 130))
        pg.draw.circle(card_image, "black", (card_image.get_width()/2,card_image.get_height()/2), 100, 2)
        card_image.blit(card_suit, (card_image.get_width()/2-card_suit.get_width()/2, card_image.get_height()/2-card_suit.get_height()/2))

    ekraan.blit(card_image, [(100, 100), (100, 100)])

def blit_all_player_cards(player_hand): #puts all the cards in front of the player, dividing the space evenly
    print("bruh")
'''
def generate_hands_deck():  # Generates shuffled deck and creates player and dealer hand lists
    global deck, player, player_total, dealer, dealer_total
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = namedtuple('card', ['value', 'suit'])
    deck = list(card(value, suit) for suit in suits for value in range(1,14))
    random.shuffle(deck)
    return deck

def deal(amount):    # Chooses <amount> card(s) from deck at random, adds them to target and removes them from deck
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
    return x
'''

def slider(startingpos, endpos, current, max, min=0):
    Slider = pg.draw.line(ekraan, "black", (startingpos, endpos), 5)
    pg.draw.circle(Slider, "black", (startingpos, endpos), 5, 0)



