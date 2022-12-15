import pygame as pg
import os
from lib.settings import *
import random
from collections import namedtuple
#--------------------------------

def choose_color(rect, mouse_pos, fill = False): # Changes color of an entity if the player is hovering on the box
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

def get_profiles(): # Gets all profiles from the profiles.txt file and sorts them into a list, ["name", "money_value"]
    with open(os.path.abspath("lib\profiles.txt"), "r") as file:
        profiles = list(map(lambda x: x.strip("\n").split(":"), file.readlines()))
    return profiles

def save_profile(name, money): # Saves a profile to the profiles.txt
    with open(os.path.abspath("lib\profiles.txt"), "a") as file:
        file.write(name + ":" + str(money) + "\n")
    file.close()

def create_card(card, cords): # Builds a card depening on the input puts it on cordinates 
    if card.value in range(1, 10):  # Argument must be namedtuple('card', ['value', 'suit'])
        card_name, value_text = "blank", card.value
    elif card.value == 10: 
        card_name, value_text = "Jack", "J"
    elif card.value == 11:
        card_name, value_text = "Queen", "Q"
    elif card.value == 12:
        card_name, value_text = "King", "K"
    elif card.value == 13:
        card_name, value_text = "blank", "A"

    card_image = pg.image.load(os.path.abspath("Assets\card_" + card_name + ".png"))
    card_suit = pg.transform.scale(pg.image.load(os.path.abspath("Assets\_" + card.suit + ".jpg")), (70, 70))
    text_card = text_font.render(str(value_text), 1, "black")

    card_image.blit(card_suit, (card_image.get_width()-card_suit.get_width()-10, 10)) #upper suit
    card_image.blit(card_suit, (10, card_image.get_height()-card_suit.get_height()-10)) #lower suit

    if isinstance(value_text, int):
        text_card = text_font.render(str(value_text+1), 1, "black")
        card_image.blit(text_card, (card_image.get_width()-card_suit.get_width()-text_card.get_width()-10, 10))
        card_image.blit(text_card, (text_card.get_height()+10, card_image.get_height()-card_suit.get_height()-10))
        text_card = pg.transform.scale(text_card, (130, 160))
        card_image.blit(text_card, (card_image.get_width()/2-text_card.get_width()/2, card_image.get_height()/2-text_card.get_height()/2))
    
    elif value_text == "A":
        card_suit = pg.transform.scale(pg.image.load(os.path.abspath("Assets\_" + card.suit + ".jpg")), (130, 130))
        pg.draw.circle(card_image, "black", (card_image.get_width()/2,card_image.get_height()/2), 100, 2)
        card_image.blit(card_suit, (card_image.get_width()/2-card_suit.get_width()/2, card_image.get_height()/2-card_suit.get_height()/2))
        card_image.blit(text_card, (card_image.get_width()-card_suit.get_width()-text_card.get_width()-10, 10))
        card_image.blit(text_card, (text_card.get_height()+10, card_image.get_height()-card_suit.get_height()-10))

    elif value_text in ["J", "Q", "K"]:
        card_image.blit(text_card, (card_image.get_width()-card_suit.get_width()-text_card.get_width()-10, 10))
        card_image.blit(text_card, (text_card.get_height()+10, card_image.get_height()-card_suit.get_height()-10))
    
    card_image = pg.transform.scale(card_image, (278/2.5, 437/2.5)) #scale card smaller
    ekraan.blit(card_image, [(cords[0] - card_image.get_width()/2, cords[1]), (100, 100)]) #put card on screen

def blit_all_player_cards(player_hand): # Displays all the cards in front of the player, dividing the space evenly
    vahemik_v, vahemik_p = 30, ekraan_w/4*3 - 30
    vahe = vahemik_p - vahemik_v
    i = 1 
    for card in player_hand:
        vahe_between_cards = vahe/(len(player_hand) + 1)
        create_card(card, (vahemik_v + vahe_between_cards * i, ekraan_h - 437/2.5 - 15))
        i += 1

def blit_all_dealer_cards(dealer_hand, revealed):
    ekraan.blit(text_font.render("Dealer's hand:", 1, "black"), (10,10))
    if not revealed:
        ekraan.blit(pg.transform.scale(pg.image.load(os.path.abspath("Assets\card_back.png")), (278/2.5, 437/2.5)), (20, 80))
        create_card(dealer_hand[1], (20 + 278/2.5 + 60, 80))
    if revealed:
        starting_pos = [80, 80]
        for card in dealer_hand:
            create_card(card, starting_pos)
            starting_pos[0] += 278/2.5

def update_player_balance(profile, amount): # Updates player balance in profiles.txt 
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

def generate_deck(): # Generates shuffled deck
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = namedtuple('card', ['value', 'suit'])
    deck = list(card(value, suit) for suit in suits for value in range(1,14))
    random.shuffle(deck)
    return deck  

def deal(amount, target, deck): # Adds cards to target hand, updates target total 
    x = []
    for i in range(1, amount + 1):
        y = deck[random.randint(1, len(deck) - 1)]
        if y.value in range(1, 10):
            target['total'] += y.value + 1
        elif y.value in range(10, 13):
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

def game_end_scene(result, displayit, current_profile_money): #endgame scene
    if displayit:
        pg.draw.rect(ekraan, "white", [(ekraan_w/2-300, ekraan_h/2-150), (600, 300)], 0)
        pg.draw.rect(ekraan, "black", [(ekraan_w/2-300, ekraan_h/2-150), (600, 300)], 4)
        game_end_balance = text_font.render("Current balance: " + str(current_profile_money) + "$", 1, "black")
        ekraan.blit(game_end_balance, (ekraan_w/2-game_end_balance.get_width()/2, ekraan_h/2-game_end_balance.get_height()/2-50))
        if result == "win":
            win_message = text_font.render("You win gg", 1, "black")
            ekraan.blit(win_message, [(ekraan_w/2-win_message.get_width()/2, ekraan_h/2-win_message.get_height()/2-100), (200, 75)])

        elif result == "lose":
            lose_message = text_font.render("You lose lmao", 1, "black")
            ekraan.blit(lose_message, [(ekraan_w/2-lose_message.get_width()/2, ekraan_h/2-lose_message.get_height()/2-100), (200, 75)])

        elif result == "tie":
            tie_message = text_font.render("Game is tied bruh", 1, "black")
            ekraan.blit(tie_message, [(ekraan_w/2-tie_message.get_width()/2, ekraan_h/2-tie_message.get_height()/2-100), (200, 75)])
        return "displayit"    
