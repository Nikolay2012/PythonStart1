import pygame
import modules.settings as settings

pygame.init()
#
list_settings_table = [
    420, # width, height
]
#
list_cross = []
#
list_zero = []
#
list_win = [0,0,0,0,0,0,0,0,0]
list_win_cor = []
#
end_game = False
#
class Sprite(settings.Settings):
    def __init__(self, object = None, **kwargs):
        super().__init__(**kwargs)
        self.SHOW = False
        self.OBJECT = object

    def show(self, window, index):
        if self.SHOW:
            self.blit_sprite(window)
            if self.OBJECT == "CROSS":
                list_win[index] = 1
            elif self.OBJECT == "ZERO":
                list_win[index] = 2
    
def victory(index1, index2, index3, value):
    global end_game
    if list_win[index1] == value and list_win[index2] == value and list_win[index3] == value:
        if value == 1:
            print("Победили крестики!")
        elif value == 2:
            print("Победили нолики!")
        end_game = True
        
        list_win_cor.extend([list_cross[index1], list_cross[index3]])
        # print(a[0].X)
        # return a
        # 
# def draw_line():

table = Sprite(
    x = settings.list_settings_window[0] // 2 - list_settings_table[0] // 2,
    y = settings.list_settings_window[1] // 2 - list_settings_table[0] // 2,
    width = list_settings_table[0],
    height = list_settings_table[0],
    name = 'images/1.png'
)
#
def create(name_list, name_img, object):
    x = 20
    y = 20 
    for num in range(3):
        for num1 in range(3):
            cross = Sprite(
                object= object,
                x = x,
                y = y, 
                width = 100,
                height = 100,
                name = name_img
            )
            name_list.append(cross)
            x += cross.WIDTH + 40
        x = 20
        y += list_cross[0].HEIGHT + 40
#
create(list_cross,  "images/cross.png", "CROSS")
create(list_zero,  "images/apple.png", "ZERO")



