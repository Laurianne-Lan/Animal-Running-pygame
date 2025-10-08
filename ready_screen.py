from util import *
from config import *

class ReadyScreen:
    def __init__(self,window):
        #设置文本颜色
        self.color=(19,130,98)
        #设置是否显示准备面板
        self.show=True
        #初始化一下从主程序传过来的window对象方便画图
        self.window=window

    def draw(self):
        text_plane,text_rect=draw_text("Animal Run","font/monofonto.ttf",100,self.color, SCREEN_WIDTH/2, SCREEN_HEIGHT/4,"midtop")
        self.window.blit(text_plane, text_rect)

        text_plane_1, text_rect_1=draw_text("click space to start the game","font/monofonto.ttf",60,self.color, SCREEN_WIDTH/2, SCREEN_HEIGHT/3+50,"midtop")
        self.window.blit(text_plane_1, text_rect_1)