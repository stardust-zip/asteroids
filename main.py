import sys

import pygame

import asteroid
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0  # Delta time

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        for d in drawable:
            d.draw(screen)
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Convert from miliseconds to seconds


if __name__ == "__main__":
    main()
