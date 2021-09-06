# coding=utf-8

# 实验用pygame来画出先天八卦的衍生动画

import pygame
pygame.init()

# 一些常数设定

# 屏幕宽高
SCR_WIDTH = 1280
SCR_HIGH = 480

# 各种空隙

# 卦之间空隙
GAP_OUT = 30
# 卦内部空隙
GAP_IN =10

# 各种颜色
color = (0,255,255) 
WHITE = (255,255,255)
BLACK = (0,0,0)

# 一个阳卦的长度
GUA_WIDTH = 70
#一个阴卦的长度（一半的长度）
YIN_WIDTH = 30
# 卦本身的高度（线条的厚度）
LINE_WIDTH =16

# 字体
FONT = pygame.font.Font("KKong3.ttf", 50)

# 临时的八卦
list_test = [1,-1,1,1,-1]

# 创建屏幕
scr = pygame.display.set_mode((SCR_WIDTH,SCR_HIGH))

# 背景白色
scr.fill(WHITE)

# 在座标上显示一行中文
def text (text,x,y):
    font = pygame.font.Font("KKong3.ttf", 50)
    text_render = font.render(text, True, (255,255,255))
    scr.blit(text_render,(x,y))

# 如古人般，竖着写字
def display_text_animation(string):
    text = ''
    for i in range(len(string)):
        text = string[i]
        text_surface = FONT.render(text, True, BLACK)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        text_rect = text_surface.get_rect()
        text_rect.center = (800 , 100 + text_height*i)
        scr.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)


# 在座标画一个阳
def yang (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+GUA_WIDTH,y),LINE_WIDTH)

# 在座标画一个阴
def yin (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+YIN_WIDTH,y),LINE_WIDTH)
    pygame.draw.line(scr, BLACK, (x+YIN_WIDTH+GAP_IN, y), (x+YIN_WIDTH+GAP_IN+YIN_WIDTH,y),LINE_WIDTH)


total = 1
for i in list_test:
    if i == 1:
        yang(SCR_WIDTH/2,SCR_HIGH/2 - GAP_OUT*total)
        total += 1
    if i == -1:
        yin(SCR_WIDTH/2,SCR_HIGH/2 - GAP_OUT*total)
        total += 1
    
    # 每画一次就暂停一下，这样有动画的效果
    pygame.display.update()
    pygame.time.wait(100)

display_text_animation('你好世界!')


# 显示图像
pygame.display.flip() 



# 游戏的loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False