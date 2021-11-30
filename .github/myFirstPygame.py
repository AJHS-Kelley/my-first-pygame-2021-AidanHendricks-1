# My First PyGame, Aidan Hendricks, 11/30/21, 1:31PM, v0.5

import pygame, sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# Setup the Window to draw on.
windowSurface = pygame.display.setmode((500, 400), 0, 32)
pygame.display.set_caption('My First PyGame')

# Setup color values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
DARKPURPLE (150, 0, 150)

# Setup the fonts.
basicFont = pygame.font.SysFont(None, 48)

# Setup the text.
text = basicFont.render('Hello, world', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill in window background color.
windowSurface.fill(DARKPURPLE)