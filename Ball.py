import pygame

class Ball:

    def __init__(self, vel, ball):
        self.vel = vel
        self.xDirection = 1;
        self.yDirection = 1;
        self.ball = ball


    def movement(self, max_height, max_width):
        
        if self.ball.x <= 0 or self.ball.x >= max_width:
            self.xDirection = -self.xDirection
        
        if self.ball.y <= 0 or self.ball.y >= max_height:
            self.yDirection = -self.yDirection

        self.ball.x += self.vel * self.xDirection
        self.ball.y += self.vel * self.yDirection