import pygame as pg
import os
from settings import *
#--------------------------------
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