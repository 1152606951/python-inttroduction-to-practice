import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏、并创建一个屏幕对象
    pygame.init()
    '''创建一个1200*800的屏幕  screen窗口对象'''
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #设置一个颜色变量
    bg_color = (ai_settings.bg_color)
    # 创建一艘飞船
    ship = Ship(screen)
    #开始游戏的主循环
    while True:
        gf.check_events(ship)

        ship.update()
        #每次循环时都重绘屏幕
        gf.update_screen(ai_settings,screen,ship)



run_game()
