from util import *


class Score:
    def __init__(self, window):
        #奖杯图片
        self.high_score_image, self.high_rect=load_image("image/score/high_score.png",35,35)
        #当前分数图片
        self.current_score_image, self.current_rect=load_image("image/score/current_score.png",35,35)

        #分别设置两图片位置
        self.high_rect.topleft=(15,20)
        self.current_rect.topleft=(15,65)

        #初始状态分数都为0
        self.high_score=0
        self.current_score=0

        self.window=window

    def draw(self):
        self.window.blit(self.high_score_image, self.high_rect)
        self.window.blit(self.current_score_image, self.current_rect)

        #绘制分数文本
        text_plane, text_rect=draw_text(str(self.high_score)+"m","font/monofonto.ttf", 28, (19,130,98),75, 20,"topleft")
        self.window.blit(text_plane,text_rect)

        text_plane_1, text_rect_1 = draw_text(str(self.current_score) , "font/monofonto.ttf", 28, (19, 130, 98), 75, 65,
                                          "topleft")
        self.window.blit(text_plane_1, text_rect_1)

