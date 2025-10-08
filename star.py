import random
from tty import ISPEED

import pygame

from config import *
from util import load_sprites

class Star(pygame.sprite.Sprite):

    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        #加载星星旋转的动画图片
        self.images=load_sprites("image/score/","xx_",8,57*0.7,62*0.7)
        self.current_image=self.images[0]
        self.rect=self.current_image.get_rect()
        #星星图片高度范围
        self.rect.bottom=random.randint(150,400)
        self.image_index=0
        self.speed=BG_SPEED
        self.call_count=0
        #星星旋转频率
        self.xz_FPS=random.randint(3,8)
        #星星是否存活
        self.active=True
        #是否摘到星星
        self.is_get=False
        self.window=window

    def draw(self):
        if self.active:
            self.window.blit(self.current_image, self.rect)

    def animation(self):
        self.call_count+=2
        if self.call_count%self.xz_FPS==0:
            #每次调用这个函数, 就让图片下标向后移动, 移动到其他图片上
            self.image_index=self.image_index+1

            if self.image_index>=8:
                self.image_index=0
            #根据下标选取图片
            self.current_image=self.images[self.image_index]

    #星星移动的函数
    def move(self):
        self.rect.left-=self.speed


    def move_down(self):
        if self.is_get:
            self.rect.bottom+=self.speed
            if self.rect.bottom>=GROUND_HEIGHT:
                self.active=False


