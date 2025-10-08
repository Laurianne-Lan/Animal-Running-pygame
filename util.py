"""tools"""
import pygame


def load_image(path,size_x=0, size_y=0):#size_x 和 size_y 的默认值被设为 0
    #加载图片冰并转化成像素
    image=pygame.image.load(path).convert_alpha()
    #重新设置图片大小
    if size_x>0 and size_y>0:
        #缩放
        image=pygame.transform.scale(image,(size_x, size_y))
    return image, image.get_rect()

def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
    images=[]
    for i in range(0, number_of_image):
        path=image_path+image_name_prefix+str(i)+".png"
        image, image_rect=load_image(path, size_x, size_y)
        images.append(image)
    return images



def draw_text(text, font_name, size,text_color, position_x, position_y, position):
    font=pygame.font.Font(font_name, size)
    text_plane=font.render(text,True,text_color)#render()：是 Font 类的方法，作用是把文本转换成 Pygame 能直接绘制的图像
    text_rect=text_plane.get_rect()

    #设置字体布局
    if position=="midtop":
        text_rect.midtop=(position_x, position_y)
    elif position=="topleft":
        text_rect.topleft=(position_x, position_y)

    return text_plane, text_rect
