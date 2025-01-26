import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    me = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        me.update(dt)
        screen.fill("black")
        me.draw(screen)

        pygame.display.flip()

        #limits framerate to tick value
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()