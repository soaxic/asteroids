import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            pos_random_angle = self.velocity.rotate(random_angle)
            neg_random_angle = self.velocity.rotate(-1 * random_angle)
            new_astroid_radius = self.radius - ASTEROID_MIN_RADIUS
            pos_asteroid = Asteroid(self.position.x, self.position.y, new_astroid_radius)
            neg_asteroid = Asteroid(self.position.x, self.position.y, new_astroid_radius)
            pos_asteroid.velocity = pos_random_angle * 1.2
            neg_asteroid.velocity = neg_random_angle * 1.2