# kasutajatega based, redpilled and scuffed blackjack
# by Karl Martin Puna and Karl Kustav Muldia
import profile
from random import randint
import time
import datetime
import pygame as pg
from lib.settings import *
from lib.functions import *
# ------------------------------------------------------------------------------

pg.init()

try: 
    open(os.path.abspath("lib\profiles.txt"), "x") # If profiles dont exist, creates one.
except:
    print("")

while Running:

    if reset:
        profiles = get_profiles()
        deck = generate_deck()
        player = {'total': 0, 'hand': []}
        dealer = {'total': 0, 'hand': []}
        dealer, deck = deal(2, dealer, deck)
        player, deck = deal(1, player, deck)
        show_dealer_hand = False
        reset = False
        user_text = ""
    
    ekraan.fill("white")
    events = pg.event.get()
        
    ekraan_w = pg.display.Info().current_w
    ekraan_h = pg.display.Info().current_h

    if game_running: 

        table_image = pg.image.load(os.path.abspath("Assets\Table.png"))
        dealer_image = pg.image.load(os.path.abspath("Assets\dealer.png"))

        ekraan.blit(dealer_image, [(320, 130), (100, 100)])
        ekraan.blit(table_image, [(100, 420), (100, 100)])

        if game_bet:
            if writing_kast_active:
                writing_kast_background = pg.draw.rect(ekraan, pg.Color('azure3'), [(ekraan_w- 250, ekraan_h - 150), (200, 60)])

            bet_writing_box = pg.draw.rect(ekraan, "black", [(ekraan_w- 250, ekraan_h - 150), (200, 60)], 3)
            bet_writing_txt= text_font.render(user_text, 1, bet_color)
            bet_txt = text_font.render("Bet", 1, "black")
            bet_box = pg.draw.rect(ekraan, button_colors["bet"], [(ekraan_w - 250, ekraan_h - 75), (200, 60)], 3)

            ekraan.blit(bet_writing_txt, [(ekraan_w - 150 - bet_writing_txt.get_width()/2, ekraan_h - 160),(200, 75)])
            ekraan.blit(bet_txt, [(ekraan_w - 150 - bet_txt.get_width()/2, ekraan_h - 50 - bet_txt.get_height()/2),(200, 75)])
    
        elif game_play:
            draw_txt = text_font.render("Draw", 1, "black")
            endturn_txt = text_font.render("End", 1, "black")

            draw_box = pg.draw.rect(ekraan, "black", [(ekraan_w - 250, ekraan_h - 150), (200, 60)], 3)
            end_box = pg.draw.rect(ekraan, "black", [(ekraan_w- 250, ekraan_h - 75), (200, 60)], 3)
            
            blit_all_player_cards(player['hand'])
            blit_all_dealer_cards(dealer["hand"], show_dealer_hand)
            ekraan.blit(draw_txt, [(ekraan_w - 150 - draw_txt.get_width()/2 , ekraan_h/3*2 + 110),(200, 75)]) 
            ekraan.blit(endturn_txt, [(ekraan_w - 150 - endturn_txt.get_width()/2, ekraan_h/3*2 + 185),(200, 75)])
            
        money_amount = text_font.render("$" + str(active_money), 1, "green")

        pg.draw.line(ekraan, "black", (ekraan_w/4*3, 0), (ekraan_w/4*3, ekraan_h), 4)  
        ekraan.blit(money_amount, [(ekraan_w - money_amount.get_width(), 0), (200, 75)])

    elif not game_running:

        if title_logo_boxes:

            if menu_box_booelans.get("box1"):
                kast1 = pg.draw.rect(ekraan, button_colors["button1"], [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)], 3) # Top clickable box
            if menu_box_booelans.get("box2"):
                kast2 = pg.draw.rect(ekraan, button_colors["button2"], [(ekraan_w/2 - 300, ekraan_h/3*2), (600, 75)], 3) # Middle clickable box
            if menu_box_booelans.get("box3"):
                kast3 = pg.draw.rect(ekraan, button_colors["button3"], [(ekraan_w/2 - 300, ekraan_h/3*2 + 125), (600, 75)], 3) # Bottom clickable box

            ekraan.blit(logo, [ekraan_w/2 - logo.get_width()/2, ekraan_h/5 - 25]) # Logo
            ekraan.blit(nimi, [ekraan_w/2 - nimi.get_width()/2, ekraan_h/25]) # Name

        if main_menu:

            select_profile_txt = text_font.render("Select profile", 1, "black")
            fullscreen_txt = text_font.render("Fullscreen", 1, "black")
            Quit_txt = text_font.render("Quit", 1, "black")

            ekraan.blit(select_profile_txt, [(ekraan_w/2 - select_profile_txt.get_width()/2, ekraan_h/3*2 - 125),(200, 75)]) # Select_profile
            ekraan.blit(fullscreen_txt, [(ekraan_w/2 - fullscreen_txt.get_width()/2, ekraan_h/3*2),(200, 75)])  # Fullscreen 
            ekraan.blit(Quit_txt, [(ekraan_w/2 - Quit_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])     # Quit

        elif profile_menu:

            new_profile_txt = text_font.render("New profile", 1, "black")
            load_profile_txt = text_font.render("Load profile", 1, "black")
            back_txt = text_font.render("Back", 1, "black")

            ekraan.blit(new_profile_txt, [(ekraan_w/2 - new_profile_txt.get_width()/2, ekraan_h/3*2 - 125),(200, 75)]) 
            ekraan.blit(load_profile_txt, [(ekraan_w/2 - load_profile_txt.get_width()/2, ekraan_h/3*2),(200, 75)])
            ekraan.blit(back_txt, [(ekraan_w/2 - back_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])
        
        elif new_profile_menu:

            input_txt = text_font.render(user_text, 1, "black")
            confirm_txt = text_font.render("Confirm", 1, "black")
            back_txt = text_font.render("Back", 1, "black")

            if writing_kast_active:
                writing_kast_background = pg.draw.rect(ekraan, pg.Color('azure3'), [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)])

            ekraan.blit(input_txt, [(ekraan_w/2 - input_txt.get_width()/2, ekraan_h/3*2 - 125),(200, 75)])
            writing_kast = pg.draw.rect(ekraan, "black", [(ekraan_w/2 - 300, ekraan_h/3*2 - 125), (600, 75)], 3)

            ekraan.blit(confirm_txt, [(ekraan_w/2 - confirm_txt.get_width()/2, ekraan_h/3*2),(200, 75)])
            ekraan.blit(back_txt, [(ekraan_w/2 - back_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])

        elif load_profile_menu:

            back_txt = text_font.render("Back", 1, "black")

            vasaknool = pg.draw.polygon(ekraan, "black", [(250, 570), (280, 600), (280, 540)], button_colors["nool1"])
            paremnool = pg.draw.polygon(ekraan, "black", [(950, 570), (920, 600), (920, 540)], button_colors["nool2"])

            if profile_number == -len(profiles) or profile_number == len(profiles):
                profile_number = 0
            try:
                displayed_profile_txt = text_font.render(profiles[profile_number][0], 1, "black")
            except IndexError:
                displayed_profile_txt = text_font.render("No profiles to load", 1, "black")

            ekraan.blit(displayed_profile_txt, [(ekraan_w/2 - displayed_profile_txt.get_width()/2, ekraan_h/3*2),(200, 75)])
            ekraan.blit(back_txt, [(ekraan_w/2 - back_txt.get_width()/2, ekraan_h/3*2 + 125),(200, 75)])

    for event in events:
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            if not game_running:
                if load_profile_menu:
                    button_colors["nool1"] = choose_color(vasaknool, mouse_pos, True)
                    button_colors["nool2"] = choose_color(paremnool, mouse_pos, True)
                button_colors["button1"] = choose_color(kast1, mouse_pos) # Changes the color of the square
                button_colors["button2"] = choose_color(kast2, mouse_pos)
                button_colors["button3"] = choose_color(kast3, mouse_pos)
            elif game_running:
                button_colors["bet"] = choose_color(bet_box, mouse_pos) 

        elif event.type == pg.MOUSEBUTTONUP:
            if game_running:
                if game_play:
                    if draw_box.collidepoint(mouse_pos) and canpress:
                        player, deck = deal(1, player, deck)
                        if player["total"] == 21 and dealer["total"] == 21:
                            displayit = True
                            show_dealer_hand = True
                            canpress = False
                            game_result = "tie"
                            active_money += int(user_text)
                            update_player_balance(active_profile, int(user_text)*2)
                            profiles = get_profiles()

                        elif player['total'] == 21:
                            displayit = True
                            show_dealer_hand = True
                            canpress = False
                            game_result = "win"
                            active_money += int(user_text)*2
                            update_player_balance(active_profile, int(user_text)*2)
                            profiles = get_profiles()

                        elif player['total'] > 21:
                            displayit = True
                            show_dealer_hand = True
                            canpress = False
                            game_result = "lose"
                            update_player_balance(active_profile, "-"+user_text)
                            profiles = get_profiles()

                    elif end_box.collidepoint(mouse_pos) and canpress:
                        displayit = True
                        show_dealer_hand = True
                        while dealer['total'] < 17:
                            dealer, deck = deal(1, dealer, deck)

                        if player['total'] == dealer['total']:
                            game_result = "tie"
                            active_money += int(user_text)
                            profiles = get_profiles()

                        elif dealer['total'] > 21:
                            game_result = "win"
                            active_money += int(user_text)*2
                            update_player_balance(active_profile, user_text)
                            profiles = get_profiles()

                        elif player['total'] > dealer['total']:
                            game_result = "win"
                            active_money += int(user_text)*2
                            update_player_balance(active_profile, int(user_text)*2)
                            profiles = get_profiles()

                        else:
                            game_result = "lose"
                            active_money -= int(user_text)
                            update_player_balance(active_profile, "-"+user_text)
                            profiles = get_profiles()
                        canpress = False

                    elif endkast.collidepoint(mouse_pos):
                        Running = False

                    elif againkast.collidepoint(mouse_pos):
                        reset = True
                        canpress = True
                        displayit = False
                        game_play = False
                        game_bet = True
                        user_text = ""

                elif game_bet:
                    if bet_writing_box.collidepoint(mouse_pos):
                        writing_kast_active = True
                        user_text = ""
                    elif bet_box.collidepoint(mouse_pos) and user_text != "" and int(user_text) > 0 and int(user_text) <= int(active_money):
                            game_play = True
                            game_bet = False
                            active_money -= int(user_text)
                            
            elif not game_running:
                if main_menu:
                    if kast1.collidepoint(mouse_pos):
                        profile_menu = True
                        main_menu = False
                    elif kast2.collidepoint(mouse_pos):  
                        pg.display.toggle_fullscreen()
                    elif kast3.collidepoint(mouse_pos):
                        Running = False

                elif profile_menu:
                    if kast1.collidepoint(mouse_pos):
                        new_profile_menu = True
                        menu_box_booelans["box1"] = False
                        profile_menu = False
                    elif kast2.collidepoint(mouse_pos):
                        menu_box_booelans["box1"] = False
                        load_profile_menu = True
                        profile_number = 0
                        profile_menu = False
                    elif kast3.collidepoint(mouse_pos):
                        main_menu = True
                        profile_menu  = False

                elif new_profile_menu:
                    if kast2.collidepoint(mouse_pos) and user_text != "":
                        game_running = True
                        active_profile = str(user_text)
                        active_money = 200
                        save_profile(user_text, active_money)
                        user_text = ""
                    elif writing_kast.collidepoint(mouse_pos):
                        writing_kast_active = True
                    elif kast3.collidepoint(mouse_pos):
                        profile_menu = True
                        menu_box_booelans["box1"] = True
                        new_profile_menu = False
                        writing_kast_active = False
                        user_text = ""

                elif load_profile_menu:
                    if vasaknool.collidepoint(mouse_pos):
                        profile_number -= 1
                    elif paremnool.collidepoint(mouse_pos):
                        profile_number += 1
                    elif kast2.collidepoint(mouse_pos):
                        try:
                            active_profile = profiles[profile_number][0]
                            active_money = int(profiles[profile_number][1])
                            noExistingProfiles = False
                            game_running = True
                        except IndexError:
                            noExistingProfiles = True
                    elif kast3.collidepoint(mouse_pos):
                        profile_menu = True
                        menu_box_booelans["box1"] = True
                        load_profile_menu = False

        elif event.type == pg.KEYDOWN:
            if new_profile_menu and writing_kast_active: # Input for creating a new profile
                if event.key == pg.K_RETURN:
                    writing_kast_active = False
                elif event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif input_txt.get_width() > 550:
                    user_text = user_text
                else:
                    user_text += event.unicode
            elif game_bet and writing_kast_active:
                if event.key == pg.K_RETURN:
                    writing_kast_active = False
                elif event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                    if user_text != "" and (int(user_text) <= 0 or int(user_text) > int(active_money)):
                        bet_color = "red"
                    elif user_text != "":
                        bet_color = "green"
                elif bet_writing_txt.get_width() > 175:
                    user_text = user_text
                elif event.unicode.isnumeric():
                    user_text += event.unicode
                    if int(user_text) <= 0 or int(user_text) > int(active_money):
                        bet_color = "red"
                    else:
                        bet_color = "green" 
        elif event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
                Running = False

    try:
        if game_end_scene(game_result, displayit, active_money) == "displayit":
            endkast = pg.draw.rect(ekraan, "black", [(ekraan_w/2+50, ekraan_h/2+50), (120, 70)], 4)
            againkast = pg.draw.rect(ekraan, "black", [(ekraan_w/2-150, ekraan_h/2+50), (120, 70)], 4)
            ekraan.blit(text_font.render("end?", 1, "black"), (ekraan_w/2+50, ekraan_h/2+50))
            ekraan.blit(text_font.render("again", 1, "black"), (ekraan_w/2-150, ekraan_h/2+50))

    except NameError:
        continue
    finally:
        pg.display.update()

pg.quit()
