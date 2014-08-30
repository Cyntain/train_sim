import random, Game_File
from Game_File import *

class World(object):
    def __init__(self, MAPWIDTH=48, MAPHEIGHT=48, TILESIZE=16):
        
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.TILESIZE = TILESIZE

        self.GRASS = 0
        self.WATER = 1
        self.STATION = 2

        self.textures = {
                            self.GRASS : pygame.image.load("grass.png"),
                            self.WATER : pygame.image.load("water.png")
                            #self.station : pygame.image.load("station.png")
            }
        self.resources = [self.GRASS, self.WATER, self.STATION]
        self.resources_name = ["Grass",  "Water", "Station"]

        self.tilemap = [[self.GRASS for w in range(self.MAPWIDTH + 1)] for h in range(self.MAPHEIGHT + 1)]

    def populate_map(self):
        x = 15
        for cl in range(self.MAPWIDTH):
            for rw in range(self.MAPHEIGHT):
                ran_num = random.randint(0, x)
                if ran_num <= 10:
                    tile = self.GRASS
                    x = 11
                else:
                    tile = self.WATER
                    x = 50
                self.tilemap[cl][rw] = tile

    def replace_tile(self, tile_x, tile_y, tile_replace_to):
        self.tilemap[tile_x][tile_y] = tile_replace_to

    def get_tile_name(self, tile_x, tile_y):
        tile = self.tilemap[tile_x][tile_y]
        if tile in self.resources:
            return self.resources_name[tile]
        else:
            return None
