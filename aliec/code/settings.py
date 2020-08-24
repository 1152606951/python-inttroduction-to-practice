'''将屏幕设置存放文件'''

class Settings():

    def __init__(self):
        #1200*800
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230) #屏幕颜色

        #self.ship_speed_factor = 1.5  ？？？根据书上的代码设置1.5飞船无法移动，所以跳过

        #子弹设置
        #设置一个宽三像素、高15像素深灰色子弹、子单的速度比飞船慢
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60



