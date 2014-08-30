import Game_File
from Game_File import *

class Player(Game_File):
    def __init__(self, MAPWIDTH=48, MAPHEIGHT=48, TILESIZE=16):
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.TILESIZE = TILESIZE
        self.player_pos = [0,0]
        self.player_score = 0
        
    def player_movement(self, direction="up", amount=1):
        if direction.lower() == "up" and self.player_pos[1] >0:
            self.player_pos[1] -= amount
        elif direction.lower() == "down" and self.player_pos[1] < self.MAPHEIGHT - 1:
            self.player_pos[1] += amount
        elif direction.lower() == "right" and self.player_pos[0] > 0:
            self.player_pos += amount
        elif direction.lower() == "left" and self.player_pos < self.MAPWIDTH - 1:
            self.player_pos[0] -= amount
        else:
            return "Unable to caculate move"

    def player_scoring(self, add_or_take="add", amount=10):
        if add_or_take.lower() == "add":
            self.player_score += amount
        else:
            self.player_score -= amount
        return self.player_score



    
