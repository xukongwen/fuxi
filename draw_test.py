# coding=utf-8




# 实验用pygame来画出先天八卦的衍生动画
from typing import Union
from itertools import chain
import pygame
import pygame_gui
pygame.init()

# 一些常数设定

clock = pygame.time.Clock()

# 屏幕宽高
SCR_WIDTH = 1280
SCR_HIGH = 1280

# 各种空隙

# 卦之间空隙
GAP_OUT = 30
# 卦内部空隙
GAP_IN =10
# 方块卦的边缘像素
GAP_BOX = 2
# 方块卦之间的空隙
GAP_BOX_OUT = 10

# 各种颜色
color = (0,255,255) 
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
Alpha = 2

# 一个阳卦的长度
GUA_WIDTH = 70
#一个阴卦的长度（一半的长度）
YIN_WIDTH = 30
# 卦本身的高度（线条的厚度）
LINE_WIDTH =16

# math

PI = 3.141592653589

# 字体
FONT = pygame.font.Font("data/font/KKong3.ttf", 50)

# 所有单体方块的组

ALL_BOX = []

# 创建屏幕
scr = pygame.display.set_mode((SCR_WIDTH,SCR_HIGH))

# 背景白色
scr.fill(WHITE)

# 在座标上显示一行中文
def text_draw (text,x,y):
    font = pygame.font.Font("data/font/KKong3.ttf", 50)
    text_render = font.render(text, True, (0,0,0))
    scr.blit(text_render,(x,y))

def text_optic_animate (text,x,y,a):
    font = pygame.font.Font("data/font/KKong3.ttf", 50)
    text_render = font.render(text, True, (0,0,0))
    text_render.set_alpha(a)
    x += 1
    scr.blit(text_render,(x,y))
    clock.tick(60)
    pygame.display.update()


# 如古人般，竖着写字
def draw_text_v (string,x,y,a,time):
    text = ''
    for i in range(len(string)):
        text = string[i]
        text_surface = FONT.render(text, True, BLACK)
        # 获得每个字的宽与高
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        text_rect = text_surface.get_rect()
        # 竖着写
        text_rect.center = (x , y + text_height*i)
        text_surface.set_alpha(a)
        a += 10
        scr.blit(text_surface, text_rect)
        #一个字一个字的写
        pygame.display.update()
        pygame.time.wait(time)

# 长句子自动换行（横版）
def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             

# 画出竖着的中文，单行        
def wrapline(text, font, gap,maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:] 
    total = 1
    for i in wrapped:
        draw_text_v(i, (1200-gap*total),50,1,50)        
        total += 1                        
    return wrapped
# 画出竖着的中文，多行
def wrap_multi_line(text, font, maxwidth):
    
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

# 在座标画一个阳
def yang (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+GUA_WIDTH,y),LINE_WIDTH)

# 在座标画一个阴
def yin (x,y):
    pygame.draw.line(scr, BLACK, (x, y), (x+YIN_WIDTH,y),LINE_WIDTH)
    pygame.draw.line(scr, BLACK, (x+YIN_WIDTH+GAP_IN, y), (x+YIN_WIDTH+GAP_IN+YIN_WIDTH,y),LINE_WIDTH)

# 画阳（方块）
def yang_box(x,y,w):
    rect = pygame.Rect(x,y, (w-GAP_BOX), (w-GAP_BOX))
    pygame.draw.rect(scr, BLACK, rect, GAP_BOX)
    ALL_BOX.append(rect)
    
# 画阴（方块）
def yin_box(x,y,w):
    rect = pygame.Rect(x,y, w, w)
    pygame.draw.rect(scr, BLACK, rect)
    ALL_BOX.append(rect)

# 画具体的卦
def draw_gua_cn():
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

# 画图形的卦
def draw_gua(width):
    total = 1
    for i in list_test:
        if i == 1:
            yang_box(500,400 - (width+width*0.2)*total,width) # 这里用width来控制大小，其间隙的大小是width的20%
            total += 1
        if i == -1:
            yin_box(500,400 - (width+width*0.2)*total,width)
            total += 1
    
    # 每画一次就暂停一下，这样有动画的效果
        pygame.display.update()
        pygame.time.wait(100)

# 画横向的图形八卦
def draw_all_gua(list,width,x,y):
    total_all = 1
    for i in list:
        total = 1
        for j in i:
            if j == 1:
                yang_box((x+ (width+width*0.2)*total_all),y - (width+width*0.2)*total,width)
                total += 1
                
            if j == -1:
                yin_box((x + (width+width*0.2)*total_all),y - (width+width*0.2)*total,width)
                total += 1
               
        total_all += 1
        
# 计算八卦第一个版本
def calc_gua(num):
    if num == 0:
        return [0] # 道
    elif num == 1:
        return [[1], [-1]]
    else:
        pre_gua = calc_gua(num - 1)
        new_gua = []
        for gua in pre_gua:
            new_gua.extend([[1] + gua, [-1] + gua])
        return new_gua

img1_sur = pygame.image.load('data/img/none-logo-black.png')
#draw_gua_cn()
#draw_gua(50)

# 实验block
#text_optic_animate('sdfsfdsdf',50,50,Alpha)

# 畫整體的掛
#draw_all_gua(calc_gua(6),30,100,300)


# 竖排古文实验运行
#wrapline("sdf士大夫實得分數地方",FONT,55,400)

# 自动换行实验
#wrapline("实验一下特别特别长的句子实验一下特别特别长的句子实验一下特别特别长的句子", FONT, 520)

# 显示图像
#pygame.display.flip() 

x1 = 50
y1 = 300
x2 = 50
w = 1

IN_BOX = None
gua = 0

#pygame.draw.circle(scr, BLACK,(500,200),50,2)


def draw_circle_gua(max_num,j,gap,width):
    x, y = SCR_WIDTH/2 -j, SCR_HIGH/2 - j
    space_radian = PI / 2 / 20
    #print("-----------------------------> start")
    for num in range(1, max_num + 1):
        gua = calc_gua(num)
        # print("------>", num, gua)
        max_gua_size = len(gua)
        circle_gua_indexes = list(chain(range(0, max_gua_size // 2), range(max_gua_size - 1, max_gua_size // 2, -1)))
        single_gua_radian = 2 * PI / (2 ** num)
        single_gua_half_radian  = single_gua_radian / 2
        for layer in range(num - 1, -1, -1):
            #print("------------>>", num, layer)
            j += gap
            y -= gap / 2
            x -= gap / 2
            count = 0
            start_radian = PI / 2 - single_gua_half_radian + space_radian
            end_radian = start_radian + single_gua_radian - space_radian * 2
            for idx in circle_gua_indexes:
                if start_radian > 2 * PI:
                    start_radian = abs(start_radian - 2 * PI)
                if end_radian > 2 * PI:
                    end_radian = abs(end_radian - 2 * PI)

                gua_value = gua[idx][layer]
                #print("------>", num, layer, y, idx, gua_value)
                if gua_value == 1:
                    #print([x, y, j, j], start_radian, end_radian)
                    pygame.draw.arc(scr, RED, [x, y, j, j], start_radian, end_radian, width)
                else:
                    pygame.draw.arc(scr, BLACK, [x, y, j, j], start_radian, end_radian, width)
                
                
                start_radian += single_gua_radian
                end_radian += single_gua_radian


def draw_a(x,y,j):
    pygame.draw.rect(scr, BLACK,[x,y,j,j],2)

    pygame.draw.arc(scr, BLACK, [x, y, j, j], 0, PI / 2, 2)
    pygame.draw.arc(scr, GREEN, [x, y, j, j], PI / 2, PI, 2)
    pygame.draw.arc(scr, BLUE, [x, y, j, j], PI, 3 * PI / 2, 2)
    pygame.draw.arc(scr, RED, [x, y, j, j], 3 * PI / 2, 2 * PI, 2)


# 游戏的loop
running = True
while running:
    scr.fill(WHITE)
    # 归零各种参数，哈哈复归是必须的
    ALL_BOX = []
    CHANGE = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]: 
        x1 += -10
    if keys[pygame.K_RIGHT]:
        x1 += 10

    # 增加一个次方
    if keys[pygame.K_UP]:
        CHANGE = True
        gua += 1

    # 减少一个次方
    if keys[pygame.K_DOWN]:
        CHANGE = True
        gua += -1
    # 如果改变了才再次计算
    if CHANGE:
        all_gua = calc_gua(6 + gua)
        CHANGE = False
    
    # 可以拖拽缩放整个卦相，但是觉得画的方法有问题，应该是第一次和有变动的时候才画，现在是每一帧都画
    #draw_all_gua(all_gua,w,x1,y1)
    draw_circle_gua(1+ w,100,20,5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x1 += -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for box in ALL_BOX:
                if box.collidepoint(event.pos):
                    IN_BOX = box
            if event.button == 4:# 向上滚放大
                w += 1

            elif event.button == 5:# 向下滚缩小
                w += -1
                
        elif event.type == pygame.MOUSEBUTTONUP:
            IN_BOX = None  
        elif event.type == pygame.MOUSEMOTION:
            if IN_BOX is not None:
                x1 += event.rel[0]
                y1 += event.rel[1]

                
        if event.type == pygame.KEYUP:
            pass
            
    
    pygame.display.update()
    clock.tick(60)