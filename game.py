import pygame, sys, random
from pygame.locals import *

BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

MAPWIDTH = 50
MAPHEIGHT = 30 
TILESIZE = 30
MAPSIZEY = MAPHEIGHT + TILESIZE + 50
# Tiles
GRASS = 0
GRASS_BOT_RIGHT = 1
GRASS_BOT_LEFT = 2
GRASS_TOP_RIGHT = 3
GRASS_TOP_LEFT = 4
WATER = 5

score = 0
print("The height of the map from mapheight times tilesize plus 50 is: ", MAPSIZEY)

def main():
    
    def updateScore(add, amount):
        """ Add or take amount from the players score, need to add different check to update the score
            add = True then add amount or add = Flase take amount
        """
        global score
        if add == True:
            score += amount
        elif add == False:
            if score <= amount:
                score = 0
            else:
                score -= amount
        else:
            return score
        return score

    def showScore():
        print(score)
    
    pygame.init()
    # Set the size of the screen
    DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))   # Set the size of the screen according to the mapwidth and height times by tile size then add 50 to add the blackstrip at the bottom
    pygame.display.set_caption("TRAINS :P")                                                                             # Label the gui 
    PLAYER= pygame.image.load("char.png")                                                                           # Load the character image
    CURSOR = pygame.image.load("cursor.png")                                               # Load the mouse cursor image
    FONT = pygame.font.Font(None, 18)                                                                                    # init the font for the screen 

    playerPos = [0,0]                                                                                                               # List of the player coord x, y
    cursorPos = [0, 0]
    mousex = 0                                                                                                                      # x coord of the mouse
    mousey = 0                                                                                                                      # y coord of the mouse
    mouseClicked = None                                                                                                     # var to check state of the mouse button
    
    # Images for the tile map
    textures = {
                            GRASS : pygame.image.load("grass.png"),
                            GRASS_BOT_RIGHT : pygame.image.load("grass_bot_right.png"),
                            GRASS_BOT_LEFT : pygame.image.load("grass_bot_left.png"),
                            GRASS_TOP_RIGHT : pygame.image.load("grass_top_right.png"),
                            GRASS_TOP_LEFT : pygame.image.load("grass_top_left.png"),
                            WATER : pygame.image.load("water.png")
                            }
    # List of all resources that can be generated
    resources = [GRASS, GRASS_BOT_RIGHT, GRASS_BOT_LEFT, GRASS_TOP_RIGHT, GRASS_TOP_LEFT, WATER]
    tilemap = [[GRASS for w in range(MAPWIDTH + 1)] for h in range(MAPHEIGHT + 1)] # Create the tile map with just GRASS in it
                               
    for rw in range(MAPHEIGHT): # Check through the y axis
        for cl in range(MAPWIDTH): # Check through the x axis
            ranNum = random.randint(0,15) # generate a random number
            if ranNum <= 10:
                tile = GRASS
            else:
                tile = WATER
                tilemap[rw][cl] = tile # add that tile to the tilemap at y, x

    while True:
        for event in pygame.event.get():   # get all user inputs
            if event.type == QUIT: # check if the input is exit 
                pygame.quit() # close the game engine
                sys.exit() # close the window
                
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
                    
            # Mouse position 
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if mousex >0 and mousex <= MAPWIDTH*TILESIZE:
                    cursorPos[0] = int((mousex / TILESIZE)*10)
                else:
                    cursorPos[0] = 0
                if mousey > 0 and mousey <= MAPHEIGHT*TILESIZE:
                    cursorPos[1] = int((mousey / TILESIZE)*10)
                    print(cursorPos[0], " ", cursorPos[1])
                else:
                    cursorPos[1] = 0
                
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if mousex >0 and mousex <= MAPWIDTH*TILESIZE:
                    cursorPos[0] = (mousex % TILESIZE)*10
                    print("mouse x : ",mousex)
                else:
                    cursorPos[0] = 0
                if mousey > 0 and mousey <= MAPHEIGHT*TILESIZE:
                    cursorPos[1] = (mousey % TILESIZE)
                    print("mouse y: ", mousey)
                else:
                    cursorPos[1] = 0
                    
                mouseClicked = True
            
        # Places tiles on to the screen   
        for row in range(MAPHEIGHT ):
            for column in range(MAPWIDTH):
                DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
                
          # Draws the player on to the screen  
        DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
        DISPLAY.blit(CURSOR, (cursorPos[0]*TILESIZE, cursorPos[1]*TILESIZE))
        
        # Draws text on to the screen
        textobj = FONT.render("SCORE: " + str(score), True, WHITE, BLACK)
        DISPLAY.blit(textobj, (5, MAPHEIGHT*TILESIZE + 20))

        pygame.display.update() # update the screen for all the drawings
        
if __name__ == '__main__':
    main()
                
