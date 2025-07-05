from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_speed = PLAYER_SHOOT_SPEED
        self.shot_radius = SHOT_RADIUS
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.shot_radius)

    def update(self,dt):
        self.position += self.velocity *dt