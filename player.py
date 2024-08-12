import pygame


class Player:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
