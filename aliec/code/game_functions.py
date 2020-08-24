import sys
import pygame

def check_keydown_events(event,ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:  # 判断是不是向右的按键
        # 是就向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 判断是不是向左键
        ship.moving_left = True

def check_keyuo_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''响应按键和鼠标事件,事件都是通过方法pygame.event.get()获取的
    每次按键事件都被注册成一个KEYDOWN事件
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #如果检测到事件是按向右箭头，就要增大rect.centerx的值
        elif event.type == pygame.KEYDOWN:#判断是不是按键事件
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyuo_events(event, ship)

def update_screen(ai_setings,screen,ship):
    #设置背景颜色
    screen.fill(ai_setings.bg_color)
    ship.blitme()  # 绘制飞船
    # 让最新屏幕可见、
    pygame.display.flip()