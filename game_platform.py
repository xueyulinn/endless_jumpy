import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        self.rect.y += scroll
