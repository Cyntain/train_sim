import pygame, sys
from pygame.locals import *
from World_File import *
from Player_File import *

class Game(object):
    def __init__(self, MAPWIDTH=48, MAPHEIGHT=48, TILESIZE=16):
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.TILESIZE = TILESIZE

        pygame.init()
        self.DISPLAY = pygame.display.set_mode((self.TILESIZE * 9, self.TILESIZE * 5 + 25))
        pygame.display.set_caption("GAME")

# could move to own file or to the Player_File
class WolfSprite(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("char.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        
if __name__ == "__main__":

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (126, 234, 115)
    
    MAPWIDTH = 48
    MAPHEIGHT = 48
    TILESIZE = 128
    
    camera_pos = [ 0, 0 ]
    
    clock = pygame.time.Clock()
    game = Game(MAPWIDTH, MAPHEIGHT, TILESIZE)
    world = World(MAPWIDTH, MAPHEIGHT, TILESIZE)
    player = Player(MAPWIDTH, MAPHEIGHT, TILESIZE)
    
    screen_y = camera_pos[0] + 10
    screen_x = camera_pos[1] + 10
    
    wolf = WolfSprite([TILESIZE, TILESIZE])
    enitity_list = pygame.sprite.Group()
    enitity_list.add(wolf)
    
    FONT = pygame.font.Font(None, 18)

    world.populate_map()
    
## MAIN GAME LOOP
    while True:
## Game controls
        for event in pygame.event.get():
            if event.type == QUIT:                                                    
                pygame.quit()                                                           
                sys.exit()
                
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                if event.key == K_RIGHT and camera_pos[1] < MAPWIDTH - 1:
                    camera_pos[1] += 1
                    player.player_pos[0] += 1
                if event.key == K_LEFT and camera_pos[1] > 0:
                    camera_pos[1] -= 1
                    player.player_pos[0] -= 1
                if event.key == K_UP and camera_pos[0] > 0:                                          
                    camera_pos[0] -= 1
                    player.player_pos[1] -= 1
                if event.key == K_DOWN and camera_pos[0] < MAPHEIGHT - 1:             
                    camera_pos[0] += 1
                    player.player_pos[1] += 1
                    
## Drawning to the screen
        game.DISPLAY.fill(BLACK) # Fill black to reset the screen 
        for cl in range(screen_x):
            for rw in range(screen_y):
                try:
                    #if camera_pos[0] <= MAPHEIGHT - 5 and camera_pos[1] <= MAPWIDTH -9:
                     game.DISPLAY.blit(world.textures[world.tilemap[cl + camera_pos[0]][rw + camera_pos[1]]], (rw*TILESIZE, cl*TILESIZE + 25))
                except IndexError:
                    pass

        game.DISPLAY.blit(wolf.image, (TILESIZE * 4, TILESIZE * 2.5))
        
        txt_score = FONT.render("Player Score: " + str(player.player_score), True, WHITE)
        txt_camera_pos = FONT.render("Camera Pos: " + str(camera_pos), True, WHITE)
        txt_player_pos = FONT.render("player Pos: " + str(player.player_pos), True, WHITE)
        game.DISPLAY.blit(txt_score, (5,  5))
        game.DISPLAY.blit(txt_player_pos, ( 150, 5))
        game.DISPLAY.blit(txt_camera_pos, ( 300, 5))
        pygame.display.update()
