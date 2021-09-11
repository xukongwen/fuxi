# coding=utf-8

# 黑客帝国-圆觉经
# 练习写入，读取json
# 中文和英文的分词

import pygame
from random import choice, randrange
import json

pygame.init()

WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

FONT_SIZE = 35
alpha_value = randrange(30, 40, 5)

test_data = {
    'a' : "sdfsf",
    'b' : "sdfsdf"
}

# 写入json
def write_json():

    with open('data/json/test_data.json','w') as test_file:
        json.dump(test_data, test_file)

# 读取json
def load_json(file):
    # 如是json里面有中文的话，就要写一个‘rb’
    with open(file, 'rb') as test_file:
        data = json.load(test_file)
    
    return data



# 拆解英文句子到字
def word_split(text):
     x = text.split()
     return x


# 拆解一句中文到字
def word_split_cn(text):
    list_of_word = list(text)
    return list_of_word
    

def read_jing():
    jing = []
    yuanjuejing = load_json('data/json/yuanjuejing.json')
    for i in yuanjuejing:
        jing.append(yuanjuejing[i])

    return jing
    


jing = read_jing()
jing_c =[]
for i in jing:
    #print(i)
    jing_c.append(word_split_cn(i))

jing_d = []
for i in jing_c:
    for j in i:
        jing_d.append(j)
#print(jing_d)


font = pygame.font.Font('data/font/KKong3.ttf', FONT_SIZE)
font_2 = pygame.font.Font('data/font/KKong3.ttf', FONT_SIZE - FONT_SIZE // 6)
font_3 = pygame.font.Font('data/font/KKong3.ttf', FONT_SIZE - FONT_SIZE // 3)

green_chars = [font.render(char, True, (randrange(0, 100), 255, randrange(0, 100))) for char in jing_d]
green_chars_2 = [font_2.render(char, True, (40, randrange(100, 175), 40)) for char in jing_d]
green_chars_3 = [font_3.render(char, True, (40, randrange(50, 100), 40)) for char in jing_d]

screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(alpha_value)

clock = pygame.time.Clock()

print(green_chars)

class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 50
        #choice是在list里选一个
        self.value = choice(green_chars)

    def draw(self):
        # 從文章的list里選擇一個字
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))

    def draw_2(self):
        self.value_2 = choice(green_chars_2)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_2, (self.x, self.y))

    def draw_3(self):
        self.value_3 = choice(green_chars_3)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_3, (self.x, self.y))


symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 3)]
symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 3)]

run = True
while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw() for symbol in symbols]
    [symbol_2.draw_2() for symbol_2 in symbols_2]
    [symbol_3.draw_3() for symbol_3 in symbols_3]

    # 這里實際上是下落的速度
    pygame.time.delay(70)

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
