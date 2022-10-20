# kasutajatega based and redpilled scuffed blackjack
# by Karl Martin Puna and
import profile
from random import randint
import time
import datetime
import pygame as pg
from settings import *
from functions import *
# ------------------------------------------------------------------------------

pg.init()
pg.mixer.init()

pg.display.set_icon(logo)

text_font = pg.font.SysFont(font_type, font_size)
nimi_font = pg.font.SysFont(font_type, font_size*2)
    
Running = True
menu_on = True
profile_on = False

clock = pg.time.Clock()

while Running:
    
    ekraan.fill(white)
    events = pg.event.get()
        
    ekraan_w = pg.display.Info().current_w
    ekraan_h = pg.display.Info().current_h
    
    if menu_on:

        nimi = nimi_font.render("Scuffed Blackjack", 1, black)
        select_profile = text_font.render("Select profile", 1, black)
        fullscreen = text_font.render("Fullscreen", 1, black)
        Quit = text_font.render("Quit", 1, black)
        
        kast1 = pg.draw.rect(ekraan, button_color1, [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)], 3) #profile
        kast2 = pg.draw.rect(ekraan, button_color2, [(ekraan_w/2 - 300, ekraan_h/3*2), (600, 75)], 3) #fullscreen
        kast3 = pg.draw.rect(ekraan, button_color3, [(ekraan_w/2 - 300, ekraan_h/3*2 + 125), (600, 75)], 3) #quit

        ekraan.blit(logo, [ekraan_w/2 - 115, ekraan_h/5 - 25]) #logo
        ekraan.blit(nimi, [ekraan_w/8 + 25, ekraan_h/25]) #nimi
        ekraan.blit(select_profile, [(ekraan_w/2 - 145, ekraan_h/3*2 - 125),(200, 75)]) #select_profile
        ekraan.blit(fullscreen, [(ekraan_w/2 - 105, ekraan_h/3*2),(200, 75)])  #fullscreen 
        ekraan.blit(Quit, [(ekraan_w/2 - 45, ekraan_h/3*2 + 125),(200, 75)])     #quit

    elif profile_on:

        new_profile = text_font.render("New profile", 1, black)
        load_profile = text_font.render("Load profile", 1, black)
        back = text_font.render("Back", 1, black)

        kast1 = pg.draw.rect(ekraan, button_color1, [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)], 3) #new profile
        kast2 = pg.draw.rect(ekraan, button_color2, [(ekraan_w/2 - 300, ekraan_h/3*2), (600, 75)], 3) #Load_profile
        kast3 = pg.draw.rect(ekraan, button_color3, [(ekraan_w/2 - 300, ekraan_h/3*2 + 125), (600, 75)], 3) #back

        ekraan.blit(logo, [ekraan_w/2 - 115, ekraan_h/5 - 25])
        ekraan.blit(nimi, [ekraan_w/8 + 25, ekraan_h/25])
        ekraan.blit(new_profile, [(ekraan_w/2 - 110, ekraan_h/3*2 - 125),(200, 75)]) 
        ekraan.blit(load_profile, [(ekraan_w/2 - 115, ekraan_h/3*2),(200, 75)])
        ekraan.blit(back, [(ekraan_w/2 - 55, ekraan_h/3*2 + 125),(200, 75)])

    for event in events:
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            button_color1 = choose_color(kast1, mouse_pos) #changes the color of the square
            button_color2 = choose_color(kast2, mouse_pos)
            button_color3 = choose_color(kast3, mouse_pos)
        elif event.type == pg.MOUSEBUTTONUP:
            if menu_on:
                if click_in_box(kast1, mouse_pos):
                    profile_on = True
                    menu_on = False
                elif click_in_box(kast2, mouse_pos):  
                    pg.display.toggle_fullscreen()
                elif click_in_box(kast3, mouse_pos):
                    Running = False
            if profile_on:
                if click_in_box(kast3, mouse_pos):
                    menu_on = True
                    profile_on  = False
        elif event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
            Running = False

    flip()
print(get_profiles())
pg.quit()