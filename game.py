import pygame, sys, random
from pygame.locals import *

BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

MAPWIDTH = 50
MAPHEIGHT = 30 
TILESIZE = 30

# Tiles
GRASS = 0
GRASS_BOT_RIGHT = 1
GRASS_BOT_LEFT = 2
GRASS_TOP_RIGHT = 3
GRASS_TOP_LEFT = 4
WATER = 5

score = 0


def main():
    
    def updateScore(positive):
        """ Add or take 100 from the players score, need to add different check to update the score
            positive = True then add 100 or positive = Flase take 100
        """
        global score
        if positive == True:
            score += 100
        elif positive == False:
            if score <= 100:
                score = 0
            else:
                score -= 100
        else:
            return score
        return score

    
    pygame.init()
    #FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))
    pygame.display.set_caption("TRAINS :P")
    PLAYER= pygame.image.load("char.png")
    FONT = pygame.font.Font(None, 18)

    playerPos = [0,0]

    textures = {
                            GRASS : pygame.image.load("grass.png"),
                            GRASS_BOT_RIGHT : pygame.image.load("grass_bot_right.png"),
                            GRASS_BOT_LEFT : pygame.image.load("grass_bot_left.png"),
                            GRASS_TOP_RIGHT : pygame.image.load("grass_top_right.png"),
                            GRASS_TOP_LEFT : pygame.image.load("grass_top_left.png"),
                            WATER : pygame.image.load("water.png")
                            }

    resources = [GRASS, GRASS_BOT_RIGHT, GRASS_BOT_LEFT, GRASS_TOP_RIGHT, GRASS_TOP_LEFT, WATER]
    tilemap = [[GRASS for w in range(MAPWIDTH + 1)] for h in range(MAPHEIGHT + 1)]
                               
    for rw in range(MAPHEIGHT):
        for cl in range(MAPWIDTH):
            ranNum = random.randint(0,15)
            if ranNum <= 10:
                tile = GRASS             
##                if tilemap[rw - 1][cl] == WATER and tilemap[rw][cl + 1] == WATER and (tilemap[rw +1][cl] != WATER and tilemap[rw][cl-1] != WATER):
##                    print("G, bt, right")
##                    tile = GRASS_BOT_RIGHT
##                elif  tilemap[rw + 1][cl] == WATER and tilemap[rw][cl + 1] == WATER and (tilemap[rw -1][cl] != WATER and tilemap[rw][cl-1] != WATER):
##                    print("G, bt, left")
##                    tile = GRASS_BOT_LEFT
##                elif  tilemap[rw - 1][cl] == WATER and tilemap[rw][cl - 1] == WATER and (tilemap[rw +1][cl] != WATER and tilemap[rw][cl+1] != WATER):
##                    print("top right")
##                    tile = GRASS_TOP_RIGHT
##                elif tilemap[rw + 1][cl] == WATER and tilemap[rw][cl - 1] == WATER and (tilemap[rw -1][cl] != WATER and tilemap[rw][cl+1] != WATER):
##                    print("top left")
##                    tile = GRASS_TOP_LEFT
            else:
                tile = WATER
                
                tilemap[rw][cl] = tile

    while True:
        for event in pygame.event.get():   
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Player movement
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                    playerPos[0] += 1
                if event.key == K_LEFT and playerPos[0] > 0:
                    playerPos[0] -= 1
                if event.key == K_UP and playerPos[1] > 0:
                    playerPos[1] -= 1
                if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:
                    playerPos[1] += 1

        # Places tiles on to the screen   
        for row in range(MAPHEIGHT ):
            for column in range(MAPWIDTH):
                DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
                
          # Draws the player on to the screen  
        DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
        
        # Draws text on to the screen
        textobj = FONT.render("SCORE: " + str(score), True, WHITE, BLACK)
        DISPLAY.blit(textobj, (5, MAPHEIGHT*TILESIZE + 20))

        pygame.display.update()
        
if __name__ == '__main__':
    main()
                
