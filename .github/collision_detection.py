# PyGame Collision Practice, Aidan Hendricks, 1/04/22, 11:44 AM, v0.2

import pygame, sys, random
import pygame.locals import *

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock() 

# Setup PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')
