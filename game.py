import pygame, sys, random
from pygame.locals import *

BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

MAPWIDTH = 50
MAPHEIGHT = 30 
TILESIZE = 30

# Tiles
GRASS = 0
WATER = 1
STATION = 2

score = 0
ranY = random.randint(0,MAPHEIGHT)
ranX = random.randint(0,MAPWIDTH)

def main():
    def updateScore(action, amount):
        """
           - Add or take amount from the players score, need to add different check to update the score
           - action = True then add amount or action = Flase take amount
           - action True means good False means bad
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
    
    def tileSelector(currentTile):
        """
            - Takes the argument of currentTile and checks what that tile is and preforms an action according to that tile
        """
        if currentTile == STATION:
            print("THIS IS THE STATION")
        elif currentTile == GRASS:
            print("THIS IS GRASS")
        elif currentTile == WATER:
            print("THIS IS WATER")
        else:
            print("Unknown Tile! ERROR: ", currentTile)

    def selectTile(counter):
        """ If the counter is even then it means the tile is selected else is is unselected
        """
        mouseClicked = counter % 2
        if mouseClicked == 0:
            return True
        else:
            return False
            
    pygame.init()
    # Set the size of the screen
    DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))   # Set the size of the screen according to the mapwidth and height times by tile size then add 50 to add the blackstrip at the bottom
    pygame.display.set_caption("TRAINS :P")                                                                             # Label the gui 
    PLAYER= pygame.image.load("char.png")                                                                            # Load the character image
    CURSOR = pygame.image.load("cursor.png")                                                                       # Load the mouse cursor image
    FONT = pygame.font.Font(None, 18)                                                                                    # init the font for the screen 

    playerPos = [0,0]                                                                                                               # List of the player coord x, y
    cursorPos = [0, 0]                                                                                                              # List of the cursor coord x, y
    mousex = 0                                                                                                                      # x coord of the mouse
    mousey = 0                                                                                                                      # y coord of the mouse
    mouseClicked = 1
    
    # Images for the game
    textures = {
                            GRASS : pygame.image.load("grass.png"),
                            WATER : pygame.image.load("water.png"),
                            STATION : pygame.image.load("station.png")
                            }
    
    resources = [GRASS, WATER, STATION]                                                                 # List of all resources that can be generated
    resourceName = ["Grass", "Water", "Station"]                                                            # Lists all of the resources names
    tilemap = [[GRASS for w in range(MAPWIDTH + 1)] for h in range(MAPHEIGHT + 1)]    # Create the tile map with just GRASS in it
                               
    for rw in range(MAPHEIGHT):                                              # Check through the y axis
        for cl in range(MAPWIDTH):                                            # Check through the x axis
            ranNum = random.randint(0,15)                                   # generate a random number
            if ranNum <= 10:                                                        # There is a 10 in 15 chance that the tile generated will be grass
                tile = GRASS
            else:
                tile = WATER
            tilemap[rw][cl] = tile                                                       # add that tile to the tilemap at y, x
    tilemap[ranY][ranX] = STATION                                               # create one station in the map

    while True:
        for event in pygame.event.get():                                            # get all user inputs
            if event.type == QUIT:                                                     # check if the input is exit 
                pygame.quit()                                                             # close the game engine
                sys.exit()                                                                   # close the window
                
            ## Player movement
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:                # Binds the player within the game screen
                    playerPos[0] += 1                                                                           # Moves the player by one tile
                if event.key == K_LEFT and playerPos[0] > 0:                                       # Binds the player within the game screen
                    playerPos[0] -= 1                                                                            # Moves the player by one tile
                if event.key == K_UP and playerPos[1] > 0:                                          # Binds the player within the game screen
                    playerPos[1] -= 1                                                                            # Moves the player by one tile
                if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:              # Binds the player within the game screen
                    playerPos[1] += 1                                                                           # Moves the player by one tile
                    
             ## Mouse buttons
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos                                                                   # Sets the mouse pos into mousex and mousey
                mousex = int(mousex/TILESIZE)                                                               # converts the mousex into tile size
                mousey = int(mousey/TILESIZE)                                                               # converts the mousey into tile size
                currentTile = tilemap[cursorPos[1]][cursorPos[0]]                                       # Saves the tile that is clicked into this var
                if mousex > 0 and mousex <= MAPWIDTH:                                   # checks if the mouse pos is within the screen on the x axis
                    cursorPos[0] = mousex                                                                          # sets the mouse x into the list of cursorPos
                else:
                    cursorPos[0] = 0                                                                                    # if the mouse pos if out side of the boundaries then set the cursor pos to 0
                if mousey > 0 and mousey <= (MAPHEIGHT - 1):                             # checks if the mouse pos is within the screen on the y axis
                    cursorPos[1] = mousey                                                                           # sets the mouse y into the list of cursorPos
                else:
                    cursorPos[1] = 0                                                                                    # if the mouse is out side of the boundaries then set the cursor pos to 0
                mouseClicked += 1
                tileSelector(currentTile)                                                                               # Checks what the tile is and preforms an action according to that tile

                
                
            ## Mouse control
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos                                                               # Saves the Pos of the mouse in mousex and mousey
                mousex = int(mousex/TILESIZE)                                                           # converts the mousex into tile size
                mousey = int(mousey/TILESIZE)                                                           # converts the mousey into tile size
                tileChosen = selectTile(mouseClicked)
                
                if tileChosen == False:
                    if mousex > 0 and mousex <= MAPWIDTH :                             # checks if the mouse pos is within the screen on the x axis
                        cursorPos[0] = mousex                                                                    # sets the mouse x into the list of cursorPos
                    else:
                        cursorPos[0] = 0                                                                                # if the mouse pos if out side of the boundaries then set the cursor pos to 0
                    if mousey > 0 and mousey <= (MAPHEIGHT - 1) :                             # checks if the mouse pos is within the screen on the y axis
                        cursorPos[1] = mousey                                                                      # sets the mouse y into the list of cursorPos
                    else:
                        cursorPos[1] = 0                                                                                # if the mouse is out side of the boundaries then set the cursor pos to 0
                    


        ## Places tiles on to the screen   
        for row in range(MAPHEIGHT ):                                                                                     # tiles on the y axis
            for column in range(MAPWIDTH):                                                                              # tiles on the x axis
                DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))      # draw all of the possible tiles onto the screen
                
          
        DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))                          # Draws the player on to the screen  
        DISPLAY.blit(CURSOR, (cursorPos[0]*TILESIZE, cursorPos[1]*TILESIZE))                        # Draws the cursor on to the screen
        
        # Draws text on to the screen
        textScore = FONT.render("SCORE: " + str(score), True, WHITE, BLACK)                      # Creates a textScore to be prep'ed to drawn onto the screen
        DISPLAY.blit(textScore, (5, MAPHEIGHT*TILESIZE + 20))                                           # draws the textScore onto the screen

        pygame.display.update()                                                                                         # update the screen for all the drawings
        
if __name__ == '__main__':                                                                                               # Lanches the main funtion
    main()
                
