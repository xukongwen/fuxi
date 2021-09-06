# 实验用pygame来画出先天八卦的衍生动画

# coding=utf-8


import pygame
pygame.init()

# 一些常数设定
color = (0,255,255) 
WHITE = (255,255,255)
BLACK = (0,0,0)
# 一个阳卦的长度
GUA_WIDTH = 70

#一个阴卦的长度（一半的长度）
YIN_WIDTH = 30

# 卦本身的高度（线条的厚度）
LINE_WIDTH =16

# 临时的八卦
list_test = [1,-1,1]

# 创建屏幕
scr = pygame.display.set_mode((1280,480))

# 背景白色
scr.fill(WHITE)

# 在座标上显示一行中文
def text (text,x,y):
    font = pygame.font.Font("KKong3.ttf", 50)
    text_render = font.render(text, True, (255,255,255))
    scr.blit(text_render,(x,y))



# 在座标画一个阳
def yang (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+GUA_WIDTH,y),LINE_WIDTH)

# 在座标画一个阴
def yin (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+YIN_WIDTH,y),LINE_WIDTH)
    pygame.draw.line(scr, BLACK, (x+YIN_WIDTH+10, y), (x+YIN_WIDTH+10+YIN_WIDTH,y),LINE_WIDTH)

# 画一个方形
#pygame.draw.rect(scr, color, pygame.Rect(60, 60, 100, 100)) 

yang(30,30)
yin(30, 10)
#text('你好')
pygame.display.flip() 



# 游戏的loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False