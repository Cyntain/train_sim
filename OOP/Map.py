# Train simulator
# Map module:
# Creates the map,replaces tiles from the map, states tile names, compares tiles of the map

import pygame, random, Game
from pygame.locals import *

class Map(object):
    
    def __init__(self, MAPHEIGHT, MAPWIDTH):
        self.MAPHEIGHT = MAPHEIGHT
        self.MAPWIDTH = MAPWIDTH
        
        self.GRASS = 0
        self.WATER = 1
        self.STATION = 2
        
        self.textures = {
                                self.GRASS : pygame.image.load("grass.png"),
                                self.WATER : pygame.image.load("water.png"),
                                self.STATION : pygame.image.load("station.png")
                                }
        
        self.resources = [self.GRASS, self.WATER, self.STATION]
        self.resourceName = ["Grass", "Water", "Station"]
        
        self.tilemap = [[self.GRASS for w in range(self.MAPWIDTH + 1)] for h in range(self.MAPHEIGHT + 1)]
 
    def populateMap(self):       
        for rw in range(self.MAPHEIGHT):
            for cl in range(self.MAPWIDTH):
                ranNum = random.randint(0,15)
                if ranNum <= 10:
                    tile = self.GRASS
                else:
                    tile = self.WATER
                self.tilemap[rw][cl] = tile
                
    def replaceTile(self, tileCoordX, tileCoordY, tileType):
        self.tilemap[tileCoordY][tileCoordX] = tileType

    def stateTileName(self, tileCoordX,tileCoordY):
        tile = self.tilemap[tileCoordY][tileCoordX]
        if tile in self.resources:
            return self.resourceName[tile]
        else:
            return None
        

if __name__ == '__main__':
    print("Module was run directly and not imported into a main class")
    landscape = Map(40, 30)
    landscape.populateMap()

    
