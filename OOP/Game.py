# Train simulator
# Game module:
# Creates the screen, updates the screen, inits Fonts and player controlled images
import pygame, Map
from pygame.locals import *


class Game(object):

    def __init__(self, MAPWIDTH, MAPHEIGHT, TILESIZE):
        pygame.init()
        
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.TILESIZE = TILESIZE
        
        self.DISPLAY = pygame.display.set_mode((self.MAPWIDTH*self.TILESIZE, self.MAPHEIGHT*self.TILESIZE + 50))
        pygame.display.set_caption("TRAINS")
        
        self.CURSOR = pygame.image.load("cursor.png") # Needs to be changed to look in a new dir
        self.FONT = pygame.font.Font(None, 18)
        
    def updateScreen(self):
        """ Updates the screen for drawing """
        pygame.display.update()

if __name__ == '__main__':
    print("Module was run directly and not imported into a main class")
    game = Game(40, 30, 30)
    
    
