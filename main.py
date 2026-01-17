import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
            
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        player.update(dt)

print("Starting Asteroids")
print(f"Screen width {SCREEN_WIDTH}")
print(f"Screen height {SCREEN_HEIGHT}")
    


if __name__ == "__main__":
    main()
