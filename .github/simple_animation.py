# Simple Animation with PyGame, Aidan Hendricks, 12/10/21, 11:53am, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
