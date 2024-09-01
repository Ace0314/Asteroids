import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
      pygame.init()
      screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

      clock = pygame.time.Clock()
      dt = 0

      updateable = pygame.sprite.Group()
      drawable = pygame.sprite.Group()
      asteroids = pygame.sprite.Group()
      shots = pygame.sprite.Group()

      Asteroid.containers = (asteroids, updateable, drawable)
      Shot.containers = (shots, updateable, drawable)
      AsteroidField.containers = (updateable)
      asteroid_field = AsteroidField()
      
      Player.containers = (updateable, drawable)

      player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        return

            for object in updateable:
                  object.update(dt)

            for asteroid in asteroids:
                  if asteroid.collision(player):
                        print("Game Over!")
                        sys.exit()
                  for shot in shots:
                        if asteroid.collision(shot):
                              asteroid.split()
                              shot.kill()

            screen.fill("black")
            
            for object in drawable:
                  object.draw(screen)

            pygame.display.flip()
            dt = clock.tick(60) / 1000
            

if __name__ == "__main__":
    main()