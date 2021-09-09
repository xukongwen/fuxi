# coding=utf-8




# 实验用pygame来画出先天八卦的衍生动画
from itertools import chain
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
# 方块卦的边缘像素
GAP_BOX = 2
# 方块卦之间的空隙
GAP_BOX_OUT = 10

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

list_two_gua = [1,-1]
list_four_gua = [[1,1],[1,-1],[-1,1],[-1,-1]]
list_bagua = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]

# 创建屏幕
scr = pygame.display.set_mode((SCR_WIDTH,SCR_HIGH))

# 背景白色
scr.fill(WHITE)

# 在座标上显示一行中文
def text_draw (text,x,y):
    font = pygame.font.Font("KKong3.ttf", 50)
    text_render = font.render(text, True, (0,0,0))
    scr.blit(text_render,(x,y))

# 如古人般，竖着写字
def draw_text_v (string,x,y,time):
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
        
def wrapline(text, font, gap,maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:] 
    total = 1
    for i in wrapped:
        draw_text_v(i, (1200-gap*total),50,50)        
        total += 1                        
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
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
    
# 画阴（方块）
def yin_box(x,y,w):
    rect = pygame.Rect(x,y, w, w)
    pygame.draw.rect(scr, BLACK, rect)

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
def draw_all_gua(list,width):
    total_all = 1
    for i in list:
        total = 1
        for j in i:
            if j ==1:
                yang_box((50+ 40*total_all),400 - (width+width*0.2)*total,width)
                total += 1
            if j == -1:
                yin_box((50 + 40*total_all),400 - (width+width*0.2)*total,width)
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


#draw_gua_cn()
#draw_gua(50)

# 畫整體的掛
draw_all_gua(calc_gua(6),30)


# 竖排古文实验运行
wrapline("sdf士大夫實得分數地方",FONT,55,400)

# 自动换行实验
#wrapline("实验一下特别特别长的句子实验一下特别特别长的句子实验一下特别特别长的句子", FONT, 520)

# 显示图像
pygame.display.flip() 



# 游戏的loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False