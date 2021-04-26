import pygame

class Player:

    def __init__(self, player, vel, movement_keys):
        self.score = 0
        self.player = player
        self.vel = vel
        self.movement_keys = movement_keys
    
    def movement(self, key_pressed, max_height):
        if key_pressed[self.movement_keys["Up"]] and self.player.y + self.vel > 0:
            self.player.y -= self.vel
        elif key_pressed[self.movement_keys["Down"]] and self.player.y + self.vel + self.player.height < max_height:
            self.player.y += self.vel
