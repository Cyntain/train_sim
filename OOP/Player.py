# Train Simulator
# Player module:
# Manages player pos and movement, Player score, adds or takes from score
import pygame
from pygame.locals import *

class Player(object):
    def __init__(self, MAPHEIGHT, MAPWIDTH):
        self.MAPHEIGHT = MAPHEIGHT
        self.MAPWIDTH = MAPWIDTH
        self.PLAYER = pygame.image.load("char.png") # Needs to be changed to look in a new dir
        self.playerPos = [0,0]
        self.playerScore = 0

    def plPosition(self):
        print(self.playerPos)
        return self.playerPos
    
    def playerMovement(self, direction, amount=1):
        if direction.lower() == "up" and self.playerPos[1] > 0:
            self.playerPos[1] -= amount
        if direction.lower() == "down" and self.playerPos[1] < self.MAPHEIGHT - 1:
            self.playerPos[1] += amount
        if direction.lower() == "right" and self.playerPos[0] > 0:
            self.playerPos[0] += amount
        if direction.lower() == "left" and self.playerPos[0] > self.MAPHEIGHT - 1:
            self.playerPos[0] -= amount

    def plScore(self):
        print(self.playerScore)
        return self.playerScore

    def addToScore(self, amount):
        self.playerScore += amount
        return self.playerScore
    
    def takeFromScore(self, amount):
        if self.playerScore  <= amount:
            self.playerScore = 0
        else:
            self.playerScore -= amount
        return self.playerScore

    
if __name__ == '__main__':
    player = Player(30, 20)
    player.plPosition()
    player.plScore()


