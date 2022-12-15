import pygame as pg
import os
#--------------------------
#-------------------------- Frontend settings
pg.font.init()
font_size = 50
font_type = "comicsansms"
text_font = pg.font.SysFont(font_type, font_size)
nimi_font = pg.font.SysFont(font_type, font_size*2)

bet_color = "green"

button_colors = {"button1": "white", "button2": "white", "button3": "white", "nool1": 4, "nool2": 4, "bet": "white"}
menu_box_booelans = {"box1": True, "box2": True, "box3": True}

ekraan_w = 1200
ekraan_h = 800

ekraan = pg.display.set_mode([ekraan_w, ekraan_h], pg.SCALED)

nimi = nimi_font.render("Scuffed Blackjack", 1, "black")
logo = pg.image.load(os.path.abspath("Assets\Blackjack logo.png"))
print(os.path.abspath(""))
pg.display.set_caption("Scuffed Blackjack")
pg.display.set_icon(logo)

#-------------------------- Backend defaults

profile_number = 0

Running = True
game_running = False
title_logo_boxes = True
main_menu = True
profile_menu = False
new_profile_menu = False
textbox_active = False
load_profile_menu = False
writing_kast_active = False
game_running = False
game_result = ""
game_bet = True
game_play = False
show_dealer_hand = False
user_text = ""
displayit = False


player = {'total': 0, 'hand': []}
dealer = {'total': 0, 'hand': []}
deck = []