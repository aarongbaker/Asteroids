import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				sys.exit("Game Over!")
			for shot in shots:
				if asteroid.check_collision(shot):
					asteroid.split()
					shot.kill()
		screen.fill("black")
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) /1000

if __name__ == "__main__":
	main()
