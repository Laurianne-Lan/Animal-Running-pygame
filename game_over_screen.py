from util import *
from config import *

class GameOverScreen:
    def __init__(self, window):
        self.replay_image, self.rect=load_image("image/game_over/replay_0.png",200,60)
        self.rect.center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+30)
        self.window=window
        self.was_clicked=False

    def draw(self, m, score):
        text_plane, text_rect=draw_text("GAME OVER","font/northcliff_stencil.otf", 80, (255,0,0),SCREEN_WIDTH/2,SCREEN_HEIGHT/5,"midtop")
        self.window.blit(text_plane, text_rect)
        text_plane, text_rect = draw_text("YOU HAVE RUN FOR "+str(m)+" METERS, SCORING "+str(score)+" IN TOTAL!", "font/hxbsbt.otf", 55, (255, 0, 0), SCREEN_WIDTH / 2,
                                          SCREEN_HEIGHT / 3, "midtop")
        self.window.blit(text_plane, text_rect)
        self.window.blit(self.replay_image, self.rect)
        self.was_clicked = False

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.was_clicked=True
            return True
        return False


