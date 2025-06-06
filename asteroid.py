import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroid_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = 1.2 * self.velocity.rotate(random_angle)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = 1.2 * self.velocity.rotate(-random_angle)     

        asteroid_group.add(asteroid1)
        asteroid_group.add(asteroid2)  