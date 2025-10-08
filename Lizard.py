import random

from util import *
from config import *

class Lizard:
    def __init__(self, window):
        #加载蜥蜴移动的图片
        self.images=load_sprites("image/dino/","crawl_", 20, 118*0.7,75*0.7)
        #初始显示第一张图片作为当前显示的图片
        self.current_image=self.images[0]
        #设置位置
        self.rect=self.current_image.get_rect()
        self.rect.bottom=GROUND_HEIGHT-10
        self.window=window
        self.speed=random.randint(6,20)

        self.image_index=0

    def draw(self):
        self.window.blit(self.current_image, self.rect)

    def move(self):
        self.rect.right+=self.speed

    #蜥蜴移动的动画
    def animation(self):
        self.image_index+=1
        #当加到最后一张照片索引时, 这个时候就回到第一张, 0-19
        self.image_index=self.image_index%20
        #根据索引从图片列表中获取图片
        self.current_image=self.images[self.image_index]


