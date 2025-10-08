import pygame.mask

from util import *
from config import *


class Animal:

    def __init__(self, window):
        #加载动画图片
        self.idle_images=load_sprites("image/dino/", "idle_", 10,153,153)#10张照片
        self.run_images = load_sprites("image/dino/", "run_", 8, 153, 153)
        self.jump_images = load_sprites("image/dino/", "jump_", 10, 153, 153)

        #获取图片大小
        self.rect=self.idle_images[0].get_rect()

        #设置显示的位置
        self.rect.bottom=GROUND_HEIGHT
        self.rect.left=500#横坐标

        #当前图片在站立图片集合中的索引
        self.idle_index=0
        # 当前图片在跑步图片集合中的索引
        self.run_index=0
        self.jump_index=0

        #默认让其处于站立状态
        self.idle=True
        self.run=False
        self.jump=False

        #上抛运动 计算位移方式
        self.t=0.5
        self.g=3
        self.jump_count=0
        self.jump_speed=ANIMAL_JUMP_SPEED

        self.window=window

        #记录animation方法执行的次数
        self.call_count=0


    def draw(self):
        #如果恐龙目前处于站立状态
        if self.idle:
            #绘制站立状态时的图片
            self.window.blit(self.idle_images[self.idle_index], self.rect)
        elif self.run:
            self.window.blit(self.run_images[self.run_index], self.rect)
        elif self.jump:
            self.window.blit(self.jump_images[self.jump_index], self.rect)


    def animation(self):
        #每执行一次animation方法计数器就增加一
        self.call_count+=1
        if self.idle and self.call_count%DINO_FPS==0: #每调用 3 次 animation()，才会切换恐龙的 idle 图片
            self.idle_index+=1
            #如果索引超出了图片列表的长度
            if self.idle_index>=10:
                self.idle_index=0

        elif self.run and self.call_count%DINO_FPS==0:
            self.run_index+=1
            if self.run_index>=8:
                self.run_index=0

        elif self.jump and self.call_count%DINO_FPS==0:
            self.jump_index += 1
            if self.jump_index >= 10:
                self.jump_index = 0

    def call_jump(self):
        if self.jump:
            #上抛运动
            v0=self.jump_speed
            s=v0*self.t-0.5*self.g*self.t**2
            self.jump_speed=v0-self.g*self.t
            #根据计算出的位移, 改变恐龙位置
            self.rect.top-=s
            #判断恐龙是否落地
            if self.rect.bottom>=GROUND_HEIGHT:
                self.rect.bottom=GROUND_HEIGHT
                #将状态切换成奔跑状态
                self.run=True
                self.jump=False
                #连跳次数归零重新计数
                self.jump_count=0

    def start_jump(self):
        if self.jump_count<2:
            self.run=False
            self.jump=True
            #重新设置初始速度
            self.jump_speed=40
            self.jump_index=len(self.jump_images)-1

    def check_collision(self, game_obj):
        """检查是否与其他游戏物体碰撞了"""
        if self.run:
            #获取奔跑时图片表面
            dino_mask=pygame.mask.from_surface(self.run_images[self.run_index])
        elif self.jump:
            dino_mask = pygame.mask.from_surface(self.jump_images[self.jump_index])
        else:
            dino_mask = pygame.mask.from_surface(self.idle_images[self.idle_index])

        #获取其他游戏物体表面或者当前表面的偏移量
        offset_0=(game_obj.rect.left-self.rect.left, game_obj.rect.top-self.rect.top)
        #rect.top上边缘的y坐标--offset_0 是一个元组 (x_offset, y_offset)，分别表示 game_obj 相对于 self 的水平和垂直偏移量

        #判断是否碰撞到了
        collide=dino_mask.overlap(pygame.mask.from_surface(game_obj.current_image),offset_0)

        return collide








