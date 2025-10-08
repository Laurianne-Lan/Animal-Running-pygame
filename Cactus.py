import random
from util import *
from config import *

class Cactus:
    def __init__(self,window,index):#index决定了仙人掌种类
        #初始化仙人掌图片以及矩形区域
        self.image, self.rect=load_image("image/cactus/cactus_"+str(index)+".png", 160, 160)
        #设置矩形区域位置
        self.rect.bottom=GROUND_HEIGHT-5
        #设置当前显示的图片
        self.current_image=self.image
        #仙人掌随着背景图移动
        self.speed=BG_SPEED
        self.window=window

    def draw(self):
        self.window.blit(self.image, self.rect)

    def move(self):
        self.rect.left-=self.speed#左边缘的 x 坐标-左移

