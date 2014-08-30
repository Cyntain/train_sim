import pygame, sys
from pygame.locals import *
from World_File import *

class Game(object):
    def __init__(self, MAPWIDTH=48, MAPHEIGHT=48, TILESIZE=16):
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.TILESIZE = TILESIZE

        pygame.init()
        self.DISPLAY = pygame.display.set_mode((self.MAPWIDTH*self.TILESIZE, self.MAPHEIGHT*self.TILESIZE))
        pygame.display.set_caption("GAME")
        
if __name__ == "__main__":
    MAPWIDTH = 48
    MAPHEIGHT = 48
    TILESIZE = 16
    
    game = Game(MAPWIDTH, MAPHEIGHT, TILESIZE)
    world = World(MAPWIDTH, MAPHEIGHT, TILESIZE)
    world.populate_map()

    while True:
        for event in pygame.event.get():                                          
            if event.type == QUIT:                                                    
                pygame.quit()                                                           
                sys.exit()
    
        for cl in range(MAPWIDTH):
            for rw in range(MAPHEIGHT):
                game.DISPLAY.blit(world.textures[world.tilemap[cl][rw]], (rw*TILESIZE, cl*TILESIZE))
         
        pygame.display.update()
   
