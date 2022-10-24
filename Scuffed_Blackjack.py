# kasutajatega based, redpilled and scuffed blackjack
# by Karl Martin Puna and Karl Kustav Muldia
import profile
from random import randint
import time
import datetime
import pygame as pg
from pygame_widgets.textbox import TextBox
from settings import *
from functions import *
# ------------------------------------------------------------------------------

pg.init() 
pg.mixer.init()

pg.display.set_icon(logo)

text_font = pg.font.SysFont(font_type, font_size)
nimi_font = pg.font.SysFont(font_type, font_size*2)

profiles = get_profiles()

clock = pg.time.Clock()

try:
    open(os.path.join(os.getcwd(), "profiles.txt"), "x") #if profiles dont exist, creates one.
except:
    print("")

while Running:
    
    ekraan.fill(white)
    events = pg.event.get()
        
    ekraan_w = pg.display.Info().current_w
    ekraan_h = pg.display.Info().current_h

    if title_logo_boxes:

        if menu_box_booelans.get("box1"):
            kast1 = pg.draw.rect(ekraan, button_color1, [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)], 3) #new profile
        if menu_box_booelans.get("box2"):
             kast2 = pg.draw.rect(ekraan, button_color2, [(ekraan_w/2 - 300, ekraan_h/3*2), (600, 75)], 3) #Load_profile
        if menu_box_booelans.get("box3"):
            kast3 = pg.draw.rect(ekraan, button_color3, [(ekraan_w/2 - 300, ekraan_h/3*2 + 125), (600, 75)], 3) #back

        ekraan.blit(logo, [ekraan_w/2 - logo.get_width()/2, ekraan_h/5 - 25]) #logo
        ekraan.blit(nimi, [ekraan_w/2 - nimi.get_width()/2, ekraan_h/25]) #nimi

    if main_menu:

        select_profile_txt = text_font.render("Select profile", 1, black)
        fullscreen_txt = text_font.render("Fullscreen", 1, black)
        Quit_txt = text_font.render("Quit", 1, black)

        ekraan.blit(select_profile_txt, [(ekraan_w/2 - select_profile_txt.get_width()/2, ekraan_h/3*2 - 125),(200, 75)]) #select_profile
        ekraan.blit(fullscreen_txt, [(ekraan_w/2 - fullscreen_txt.get_width()/2, ekraan_h/3*2),(200, 75)])  #fullscreen 
        ekraan.blit(Quit_txt, [(ekraan_w/2 - Quit_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])     #quit

    elif profile_menu:

        new_profile_txt = text_font.render("New profile", 1, black)
        load_profile_txt = text_font.render("Load profile", 1, black)
        back_txt = text_font.render("Back", 1, black)

        ekraan.blit(new_profile_txt, [(ekraan_w/2 - new_profile_txt.get_width()/2, ekraan_h/3*2 - 125),(200, 75)]) 
        ekraan.blit(load_profile_txt, [(ekraan_w/2 - load_profile_txt.get_width()/2, ekraan_h/3*2),(200, 75)])
        ekraan.blit(back_txt, [(ekraan_w/2 - back_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])

    elif load_profile_menu:

        back = text_font.render("Back", 1, black)

        vasaknool = pg.draw.polygon(ekraan, black, [(250, 570), (280, 600), (280, 540)], nool_color1)
        paremnool = pg.draw.polygon(ekraan, black, [(950, 570), (920, 600), (920, 540)], nool_color2)

        try:
            displayed_profile_txt = text_font.render(profiles[profile_number][0], 1, black)
        except:
            profile_number = -1
        
        ekraan.blit(displayed_profile_txt, [(ekraan_w/2 - displayed_profile_txt.get_width()/2, ekraan_h/3*2),(200, 75)])
        ekraan.blit(back, [(ekraan_w/2 - back.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])

    for event in events:
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            if load_profile_menu:
                nool_color1 = choose_color(vasaknool, mouse_pos, True)
                nool_color2 = choose_color(paremnool, mouse_pos, True)
            button_color1 = choose_color(kast1, mouse_pos) #changes the color of the square
            button_color2 = choose_color(kast2, mouse_pos)
            button_color3 = choose_color(kast3, mouse_pos)
        elif event.type == pg.MOUSEBUTTONUP:

            if main_menu:
                if click_in_box(kast1, mouse_pos):
                    profile_menu = True
                    main_menu = False
                elif click_in_box(kast2, mouse_pos):  
                    pg.display.toggle_fullscreen()
                elif click_in_box(kast3, mouse_pos):
                    Running = False

            elif profile_menu:
                if click_in_box(kast1, mouse_pos):
                    new_profile_menu = True
                    load_profile_menu = False
                elif click_in_box(kast2, mouse_pos):
                    menu_box_booelans["box1"] = False
                    load_profile_menu = True
                    profile_menu = False
                elif click_in_box(kast3, mouse_pos):
                    main_menu = True
                    profile_menu  = False

            elif new_profile_menu:
                if click_in_box(kast3, mouse_pos):
                    continue

            elif load_profile_menu:
                if click_in_box(vasaknool, mouse_pos):
                    profile_number -= 1
                elif click_in_box(paremnool, mouse_pos):
                    profile_number += 1
                elif click_in_box(kast2, mouse_pos):
                    continue #alusta mänguga
                elif click_in_box(kast3, mouse_pos):
                    profile_menu = True
                    menu_box_booelans["box2"] = True
                    load_profile_menu = False

        elif event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
            Running = False

    flip()

pg.quit()
