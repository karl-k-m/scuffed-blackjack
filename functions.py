import pygame as pg
import os
from settings import *
import random
from collections import namedtuple

#--------------------------------
def flip():
    pg.display.flip()
    
class Kast():
    def __init__(self, ekraan, color, x, y, w, h):
        
        self.color = color
        self.cords = (x, y)
        self.size = (w, h)
        
        def change_color(self, color_new):
            self.color = color_new
            
        self.rect = pg.draw.rect(ekraan, self.color, [self.cords, self.size], 3)

def choose_color(rect, mouse_pos, fill = False):
    if fill:
        if rect.collidepoint(mouse_pos):
            button_color = 0
        else:
            button_color = 4
    else:
        if rect.collidepoint(mouse_pos):
           button_color = black
        else:
            button_color = white
    return button_color

def click_in_box(rect, mouse_pos):
    if rect.collidepoint(mouse_pos):
        return True

def get_profiles():
    with open(os.path.join(os.getcwd(),"profiles.txt"), "r") as file:
        profiles = list(map(lambda x: x.strip("\n").split(" "), file.readlines()))
    return profiles

def save_profile(name, money):
    with open("profiles.txt", "a+") as file:
        file.write("\n" + name + " " + str(money))
    file.close()

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