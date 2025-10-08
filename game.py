"""this file is the main code"""
import random
#引入pygame引擎
import pygame as pg
import os
from pygame import KEYDOWN, KEYUP

from Cactus import Cactus
from Lizard import Lizard
from Spider import Spider
from config import * #引入config文件中所有的属性配置
from background import *
from game_over_screen import GameOverScreen
from score import *
from ready_screen import *
from Animal import *
from star import Star

#设置游戏界面显示在屏幕中间
os.environ["SDL_VIDEO_CENTERED"]="1"

#初始化pygame模块
pg.init()
#创建游戏界面
window=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pg.display.set_caption(TITLE)

clock=pg.time.Clock()

#创建所有背景图层
all_backgrounds=AllBackgrounds(window)

#创建得分面板
score=Score(window)

#创建准备阶段面板
ready_screen=ReadyScreen(window)

#创建恐龙
dino=Animal(window)

#创建蜘蛛
spider=Spider(window)


#存放蜥蜴的列表
lizard_list=[]
#记录创建蜥蜴个数
liz_call_count=0

#创造蜥蜴函数
def make_lizard():
    global liz_call_count
    liz_call_count+=1
    #每执行100次该函数 创建一个蜥蜴
    if liz_call_count%100==0:
        liz= Lizard(window)
        lizard_list.append(liz)
#绘制蜥蜴的函数
def liz_draw():
    for l in lizard_list:
        l.draw()
#让蜥蜴移动的函数
def liz_move():
    for l in lizard_list:
        l.move()
        #切换图片形成动画
        l.animation()


#生成仙人掌的函数
def make_cactus():
    #存放所有仙人掌
    ca_list=[]
    for index in range(CACTUS_COUNT):
        cactus_type=random.randint(0,4)
        cactus=Cactus(window,cactus_type)
        #如果创建的是第一个仙人掌--列表里面之前没仙人掌
        if len(ca_list)==0:
            #将其位置设置到屏幕最后面
            cactus.rect.left=SCREEN_WIDTH
        else:
            #其他的:以前面一个仙人掌的位置作为参照物设置位置
            a=random.randint(330,900)
            cactus.rect.left=ca_list[index-1].rect.right+a
        ca_list.append(cactus)
    return ca_list

#创建所有仙人掌
cactus_list=make_cactus()

def cactus_draw():
    for c in cactus_list:
        c.draw()

#让所有的仙人掌都移动起来
def cactus_move():
    for c in cactus_list:
        c.move()

#存放星星列表
star_list=[]
#创建星星精灵组
star_group=pygame.sprite.Group()
#制作星星存入列表
def make_star():
    for i in range(STAR_COUNT):
        star=Star(window)
        if len(star_list)==0:
            star.rect.left=SCREEN_WIDTH
        else:
            #每个星星对于前面一颗星星的距离是200
            star.rect.left=star_list[i-1].rect.right+200

        star_list.append(star)
        #把星星加入到精灵组中
        star_group.add(star)

#调用制作星星函数
make_star()#相当于把星星存在了列表里

#让所有星星移动
def star_move():
    for s in star_list:
        s.move()
        s.move_down()


def star_draw():
    for star in star_list:
        star.draw()
        star.animation()

#判断游戏是否结束
game_over=False

#创建游戏结束画面
gameOver_screen=GameOverScreen(window)

#记录while循环次数
count=0

#记录摘得星星个数
get_star_num=0

#加载播放音乐
pg.mixer.music.load("sound/春来.mp3")
pg.mixer.music.play()

#加载音效
s_jump=pg.mixer.Sound("sound/jump.wav")
s_score=pg.mixer.Sound("sound/score.wav")


running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:  # 处理窗口关闭事件
            running = False

        #如果事件类型是键盘按下的事件
        if event.type==KEYDOWN:
            #如果按的是空格键
            if event.key==pygame.K_SPACE:
                if ready_screen.show:
                    #开始游戏, 准备界面消失
                    ready_screen.show=False
                    #恐龙站立状态取消
                    dino.idle=False
                    #恐龙奔跑状态打开
                    dino.run=True
            #如果按的是W键 或者是“上”键
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                #如果游戏开始(恐龙不处于站立状态时)
                if not dino.idle:
                    dino.start_jump()
                    s_jump.play()

        #如果当前按键类型-松开按键
        if event.type==KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                #如果恐龙处于跳跃状态
                if dino.jump:
                    #连跳次数加一, 防止无限连跳
                    dino.jump_count+=1



    #绘制背景图层
    all_backgrounds.draw()
    #如果游戏没结束
    if not game_over:
        # 如果恐龙不处于站立状态--说明游戏开始!了
        if not dino.idle:
            count+=1
            if count==5:
                #跑步距离增加1m
                score.high_score+=1
                #从新计算累计
                count=0
            # 让背景图层移动起来
            all_backgrounds.move()
            # 调用恐龙跳跃方法
            dino.call_jump()

            # 让仙人掌移动
            cactus_move()
            # 创建蜥蜴
            make_lizard()
            # 蜥蜴移动
            liz_move()
            # 蜘蛛移动
            spider.move()
            # 绘制星星
            star_draw()
            # 星星移动
            star_move()


    #绘制得分面板
    score.draw()

    #准备界面
    if ready_screen.show:
        ready_screen.draw()

    #绘制恐龙
    dino.draw()
    # 调用恐龙显示动画的方法
    dino.animation()

    #画仙人掌
    cactus_draw()

    #画蜥蜴
    liz_draw()

    # 绘制蜘蛛
    spider.draw()


    #判断是否撞到了蜘蛛
    sprite_hit=dino.check_collision(spider)
    if sprite_hit:
        game_over=True

    # 判断是否撞到了仙人掌
    #遍历所有的仙人掌
    for c in cactus_list:
        sprite_hit=dino.check_collision(c)
        if sprite_hit:
            game_over = True

    # 判断是否撞到了蜥蜴
    for l in lizard_list:
        sprite_hit = dino.check_collision(l)
        if sprite_hit:
            game_over = True

    star_hit=pygame.sprite.spritecollide(dino,star_group, True)
    for star in star_hit:
        star.is_get=True
        s_score.play()
        get_star_num+=1

    #所得分数计算--奔跑的距离*50+摘得的星星数量*100
    score.current_score=score.high_score*50+get_star_num*100

    # 如果游戏结束了--绘制游戏结束画面
    if game_over:
        gameOver_screen.draw(score.high_score, score.current_score)
        mouse_pos=pg.mouse.get_pos()
        if event.type==pg.MOUSEBUTTONDOWN and gameOver_screen.check_click(mouse_pos):
            game_over=False
            dino.rect.top=SCREEN_HEIGHT/2-50

            # 4. 重置分数和计数
            score.high_score = 0  # 奔跑距离重置为 0
            get_star_num = 0  # 摘星数量重置为 0
            count = 0  # 循环计数（控制奔跑距离）重置为 0

            # 6. 重置游戏结束画面的“点击标记”
            gameOver_screen.was_clicked = False



    #设置帧速率
    clock.tick(FPS)
    #每执行一次循环刷新一次
    pg.display.update()



pg.time.wait(5000)
pg.quit()



