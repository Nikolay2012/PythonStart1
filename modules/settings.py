import pygame 
import os 
import random

pygame.init()

#
list_settings_window = [420,420]
#
def finding_path(name_file):
    path_file = os.path.abspath(__file__ + '/..').split('\\')
    del path_file[-1]
    path_file = os.path.join('\\'.join(path_file), name_file)
    return path_file

class Settings:
    def __init__(self, x= None, y= None, width= None, height= None, name= None, color= None):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME = name
        self.COLOR = color
        self.IMAGE = None
        if self.NAME:
            self.load_image()
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
    
    def load_image(self):
        path_img = finding_path(self.NAME)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))

    def blit_sprite(self, window):
        window.blit(self.IMAGE, (self.X, self.Y))