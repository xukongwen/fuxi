# coding=utf-8

import sys
import pygame
from pygame.locals import *

pygame.init()

mline_text="The Scroobious Pip went out one day\nWhen the grass was green, and the sky was grey.\nThen all the beasts in the world came round\nWhen the Scroobious Pip sat down on the ground.\n"

WIDTH = 600
HEIGHT= 500
WHITE = 255,255,255
BLUE  = 0,0,200



def read_text(file):
    inputFile = open(file, 'rb')
    #print(inputFile)
    print(inputFile.read())

read_text('data/text/yjj.txt')

while (True):
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()