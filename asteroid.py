from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self,dt):
        self.position += self.velocity *dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.kill()
        gen_angle = random.uniform(0, 360)
        vel1 = self.velocity.rotate(gen_angle)
        vel2 = self.velocity.rotate(gen_angle + 180) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2
        self.kill()

        