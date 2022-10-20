import pygame as pg
#--------------------------

def flip():
    pg.display.flip()
    
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

box_1 = (660, 600, 1255, 660)
box_2 = (660, 725, 1255, 785)
box_3 = (660, 850, 1255, 910)

fullscreen = True
ekraan = pg.display.set_mode([1200, 800], pg.SCALED)
desktop_sizes = pg.display.get_desktop_sizes()
pg.display.set_caption("Scuffed Blackjack")
logo = pg.image.load("Python\Project\Scuffed Blackjack new\Blackjack logo.png")
pg.display.set_icon(logo)

ekraan_w = pg.display.Info().current_w
ekraan_h = pg.display.Info().current_h

Jack = Queen = King = 10
#♧ ♡ ♢ ♧
card_pack = ["2♤", "3♤", "4♤", "5♤", "6♤", "7♤", "8♤", "9♤", "10♤", "Jack♤", "Queen♤", "King♤", "Ace♤",
         "2♧", "3♧", "4♧", "5♧", "6♧", "7♧", "8♧", "9♧", "10♧", "Jack♧", "Queen♧", "King♧", "Ace♧",
         "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "Jack♢", "Queen♢", "King♢", "Ace♢",
         "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "Jack♡", "Queen♡", "King♡", "Ace♡"]