import pygame as pg
import os
from lib.settings import *
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
    with open(os.path.abspath("lib\profiles.txt"), "r") as file:
        profiles = list(map(lambda x: x.strip("\n").split(":"), file.readlines()))
    return profiles

def save_profile(name, money): #saves a profile to the profiles.txt
    with open(os.path.abspath("lib\profiles.txt"), "a") as file:
        file.write("\n" + name + ":" + str(money))
    file.close()

def create_card(card, cords): #builds a card depening on the input and puts it on the 
    if card.value in range(1, 10):  #argument must be namedtuple('card', ['value', 'suit'])
        card_name, value_text = "blank", card.value
    elif card.value == 11: 
        card_name, value_text = "Jack", "J"
    elif card.value == 12:
        card_name, value_text = "Queen", "Q"
    elif card.value == 13:
        card_name, value_text = "King", "K"
    elif card.value == 14:
        card_name, value_text = "blank", "A"

    card_image = pg.image.load(os.path.abspath("Assets\card_" + card_name + ".png"))
    text_card = text_font.render(str(value_text), 1, "black")
    card_suit = pg.transform.scale(pg.image.load(os.path.abspath("Assets\_" + card.suit + ".jpg")), (70, 70))
    
    card_image.blit(card_suit, (card_image.get_width()-card_suit.get_width()-10, 10))
    card_image.blit(card_suit, (10, card_image.get_height()-card_suit.get_height()-10))
    card_image.blit(text_card, (card_image.get_width()-card_suit.get_width()-text_card.get_width()-10, 10))
    card_image.blit(text_card, (text_card.get_height()+10, card_image.get_height()-card_suit.get_height()-10))

    if isinstance(value_text, int):
        text_card = pg.transform.scale(text_card, (130, 160))
        card_image.blit(text_card, (card_image.get_width()/2-text_card.get_width()/2, card_image.get_height()/2-text_card.get_height()/2))
    elif value_text == "A":
        card_suit = pg.transform.scale(pg.image.load(os.path.abspath("\Assets\_" + card.suit + ".jpg")), (130, 130))
        pg.draw.circle(card_image, "black", (card_image.get_width()/2,card_image.get_height()/2), 100, 2)
        card_image.blit(card_suit, (card_image.get_width()/2-card_suit.get_width()/2, card_image.get_height()/2-card_suit.get_height()/2))
    card_image = pg.transform.scale(card_image, (278/2.5, 437/2.5))
    ekraan.blit(card_image, [(cords[0] - card_image.get_width()/2, cords[1]), (100, 100)])

def blit_all_player_cards(player_hand): #puts all the cards in front of the player, dividing the space evenly
    vahemik_v, vahemik_p = 30, ekraan_w/4*3 - 30
    vahe = vahemik_p - vahemik_v
    i = 1 
    for card in player_hand:
        vahe_between_cards = vahe/(len(player_hand) + 1)
        create_card(card, (vahemik_v + vahe_between_cards * i, ekraan_h - 437/2.5 - 15))
        i += 1

def update_player_balance(profile, amount):
    with open(os.path.abspath("lib\profiles.txt"), "r") as file:
        profiles = list(map(lambda x: x.strip("\n").split(":"), file.readlines()))
        for i in profiles:
            if i[0] == profile:
                i[1] = str(int(i[1]) + int(amount))
        text = ""
        for i in profiles:
            text += "%s:%s\n" %(i[0], i[1])
    file.close()
    with open(os.path.abspath("lib\profiles.txt"), "w") as file:
        file.write(text)

def generate_deck():  # Generates shuffled deck and creates player and dealer hand lists
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = namedtuple('card', ['value', 'suit'])
    deck = list(card(value, suit) for suit in suits for value in range(1,14))
    random.shuffle(deck)
    return deck

def deal(amount, target, deck):    # Chooses <amount> card(s) from deck at random, adds them to target and removes them from deck
    x = []
    for i in range(1, amount + 1):
        y = deck[random.randint(1, len(deck) - 1)]
        if y.value in range(2, 11):
            target['total'] += 1
        elif y.value in range(11, 14):
            target['total'] += 10
        else:
            if target['total'] + 11 > 21:
                target['total'] += 1
            else:
                target['total'] += 11
        x.append(y)
        deck.remove(y)
    target['hand'].extend(x)
    return [target, deck]