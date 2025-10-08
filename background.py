from util import load_image
from config import *

class Background:
    def __init__(self, window, image_path,speed):
        #图层图片
        self.image_0, self.rect_0=load_image(image_path, 1280, 720)
        self.image_1, self.rect_1=load_image(image_path, 1280, 720)

        self.rect_0.bottom=SCREEN_HEIGHT#强制背景图像在垂直方向 “锚定” 窗口底部
        self.rect_1.bottom = SCREEN_HEIGHT

        #设置第二张背景图层的左侧位置等于第一张背景图层右侧位置
        self.rect_1.left=self.rect_0.right

        self.window=window

        #设置背景涂层移动速度
        self.speed=speed

    def draw(self):
        self.window.blit(self.image_0, self.rect_0)
        self.window.blit(self.image_1, self.rect_1)


    def move(self):
        """背景图层移动的方法"""
        self.rect_0.left-=self.speed
        self.rect_1.left -= self.speed
        #如果第一张图向左溢出了屏幕
        if self.rect_0.right<0:
            #让第一张图重新拼接到第二张图的右侧
            self.rect_0.left=self.rect_1.right
        if self.rect_1.right<0:
            self.rect_1.left=self.rect_0.right


class AllBackgrounds:

    def __init__(self, window):
        #分别创建四个背景图层
        self.bg_0=Background(window,"image/background/bg_0.png",BG_SPEED)
        self.bg_1 = Background(window, "image/background/bg_1.png",BG_SPEED-10)
        self.bg_2 = Background(window, "image/background/bg_2.png",BG_SPEED-12)
        self.bg_3 = Background(window, "image/background/bg_3.png",BG_SPEED-14)

    def draw(self):
        #绘图时,先画的会画在底部
        self.bg_3.draw()
        self.bg_2.draw()
        self.bg_1.draw()
        self.bg_0.draw()

    def move(self):
        self.bg_0.move()
        self.bg_1.move()
        self.bg_2.move()
        self.bg_3.move()


