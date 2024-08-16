import pygame
import settings
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, moving):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moving = moving
        self.direction = random.choice([-1, 1])
        self.movaCount = random.randint(0, 50)
        self.speed = random.randint(1, 3)

    def update(self, scroll, score):

        self.rect.y += scroll
        # delete platforms below ground
        if self.rect.top > settings.WINDOW_HEIGHT:
            self.kill()

        if self.moving and score > 1000:
            self.rect.x += self.direction * self.speed

            if self.rect.right >= settings.WINDOW_WIDTH or self.rect.left <= 0:
                self.direction = self.direction * (-1)
