import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.points = 0
        self.lives = PLAYER_LIVES

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shoot(dt)
        if keys[pygame.K_ESCAPE]:
            print("Thanks for playing!")
            print(f"Your score was: {self.points}")
            pygame.quit()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def get_lives(self):
        return PLAYER_LIFE_INDICATOR * self.lives
    
    def life_color(self):
        if self.lives == 1:
            return (255, 0, 0)
        else:
            return (255, 255, 255)
        
    def set_window_title(self):
        pygame.display.set_caption(f"ASSteroids -- Score: {self.points} -- Lives remaining: {self.lives}")