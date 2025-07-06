from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot 

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 180
		self.shot_timer = 0.0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		points = self.triangle()
		pygame.draw.polygon(screen, "white", points, 2)

	def turn(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt 

	def update(self, dt):
		self.shot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.turn(-dt)
		if keys[pygame.K_d]:
			self.turn(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			return self.shoot()
	
	def shoot(self):
		if self.shot_timer > 0:
			return
		self.shot_timer = PLAYER_SHOOT_COOLDOWN
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = forward * PLAYER_SHOOT_SPEED

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt  
		