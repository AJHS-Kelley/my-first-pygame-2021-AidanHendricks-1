# Simple Animation with PyGame, Aidan Hendricks, 12/10/21, 1:14pm, v0.5

from PyGamePractice import GREEN
import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup direction variable
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT ='upright'

MOVESPEED = 4

# Setup color values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup box data
b1 = {'rect':pygame.rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.rect(200, 200, 20, 20), 'color':BLUE, 'dir':UPLEFT}
b3 = {'rect':pygame.rect(100, 150, 60, 60), 'color':GREEN, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop
while True: 
    # Check for QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()