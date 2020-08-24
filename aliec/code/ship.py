'''创建飞船图像,这个文件存放飞船的相关设置'''
import pygame

class Ship():
    #初始化飞船位置
    def __init__(self,screen):
        self.screen =screen

        #self.ai_settings = ai_settings

        #加载飞船并获取其外形
        self.image = pygame.image.load('E:\\外星人\\images\\f.png')
        self.rect = self.image.get_rect()#获取飞船对象
        self.screen_rect = screen.get_rect()#屏幕矩形

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx#  x坐标
        self.rect.bottom =self.screen_rect.bottom#  y坐标

       # self.center = float(self.rect.centerx)

        #移动标记
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.rect.centerx += 1

        if  self.moving_left and self.rect.left>0:
            self.rect.centerx -= 1

       # self.rect.centerx = self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
