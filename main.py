import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from astroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for thing in updatable:
            thing.update(dt)            

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.check_collision(player):
                print("Game over!")
                pygame.quit()

        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        #limits framerate to tick value
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()