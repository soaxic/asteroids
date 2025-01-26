import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from astroidfield import *
from shot import *

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    game_over = False

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

    player.set_window_title()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Your score was: {player.points}")
                pygame.quit()

        for thing in updatable:
            thing.update(dt)            

        screen.fill("black")

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
                    player.points += 1
                    player.set_window_title()
            if player.lives > 0:
                if asteroid.check_collision(player):
                    player.lives -= 1
                    player.set_window_title()
                    if player.lives == 0:
                        print("Game over!")
                        print(f"Your score was: {player.points}")
                        player.kill()
                        game_over = True
                        game_over_text = big_font.render(f"GAME OVER", True, (255, 255, 255))
                        game_over_subtext = font.render(f"Press ESC to quit", True, (150, 150, 150))
                    else:
                        asteroid.kill()
        
        for thing in drawable:
            thing.draw(screen)

        score_text = font.render(f"Score: {player.points}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        remaining_lives_text = font.render(f"Lives remaining: {player.get_lives()}", True, player.life_color())
        screen.blit(remaining_lives_text, (10, 50))

        if game_over:
            screen.blit(game_over_text, (500, 500))
            screen.blit(game_over_subtext, (550, 600))

        pygame.display.flip()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            print("Thanks for playing!")
            print(f"Your score was: {self.points}")
            pygame.quit()

        #limits framerate to tick value
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()