import random

from config import *
from util import *

class Spider:
    def __init__(self, window):
        self.image, self.rect=load_image("image/zhangaiwu/zai_0.png")
        self.rect.bottom=0
        self.rect.left=random.randint(self.image.get_width(), SCREEN_WIDTH-self.image.get_width())
        self.dir=0 #蜘蛛移动的方向 0:向下移动 1:向上移动
        self.speed=5
        self.current_image=self.image
        self.window=window

    def draw(self):
        self.window.blit(self.image, self.rect)

    #蜘蛛移动的函数
    #向下落, 落到最低点就上升, 反之亦然
    def move(self):
        #判断运动方向
        if self.dir==0:
            self.rect.bottom+=self.speed
            #如果移动到图片完全展现出来
            if self.rect.bottom>=self.image.get_height():
                self.dir=1
        else:
            self.rect.bottom -= self.speed
            # 如果移动到图片完全展现出来
            if self.rect.bottom <=0:
                #重新随机蜘蛛的横坐标
                self.rect.left = random.randint(self.image.get_width(), SCREEN_WIDTH - self.image.get_width())
                self.dir=0
