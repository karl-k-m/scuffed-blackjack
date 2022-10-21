import pygame as pg
import os
#--------------------------
white = [255, 255, 255]
black = [0, 0, 0]

pg.font.init()
font_size = 50
font_type = "comicsansms"
text_font = pg.font.SysFont(font_type, font_size)
nimi_font = pg.font.SysFont(font_type, font_size*2)

button_color1 = white
button_color2 = white
button_color3 = white
nool_color1 = 4
nool_color2 = 4


box_1 = (660, 600, 1255, 660)
box_2 = (660, 725, 1255, 785)
box_3 = (660, 850, 1255, 910)

menu_box_booelans = {"box1": True, "box2": True, "box3": True}

profile_number = 0

fullscreen = True
Running = True
title_logo_boxes = True
menu_on = True
profile_on = False
load_profiles = False

ekraan_w = 1200
ekraan_h = 800

ekraan = pg.display.set_mode([ekraan_w, ekraan_h], pg.SCALED)

nimi = nimi_font.render("Scuffed Blackjack", 1, black)
logo = pg.image.load(os.path.join(os.getcwd(), 'Blackjack logo.png'))
pg.display.set_caption("Scuffed Blackjack")
pg.display.set_icon(logo)

Jack = Queen = King = 10
#♧ ♡ ♢ ♧
card_pack = ["2♤", "3♤", "4♤", "5♤", "6♤", "7♤", "8♤", "9♤", "10♤", "Jack♤", "Queen♤", "King♤", "Ace♤",
         "2♧", "3♧", "4♧", "5♧", "6♧", "7♧", "8♧", "9♧", "10♧", "Jack♧", "Queen♧", "King♧", "Ace♧",
         "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "Jack♢", "Queen♢", "King♢", "Ace♢",
         "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "Jack♡", "Queen♡", "King♡", "Ace♡"]