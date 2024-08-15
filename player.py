import pygame
import settings


class Player:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.velY = 0
        self.flip = False

    def move(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        # process keypresses
        if key[pygame.K_a]:
            dx = -10
            self.flip = True

        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        self.velY += settings.GRAVITY
        dy += self.velY

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        elif self.rect.right + dx > settings.WINDOW_WIDTH:
            dx = settings.WINDOW_WIDTH - self.rect.right

        if self.rect.bottom + dy > settings.WINDOW_HEIGHT:
            dy = 0
            self.velY = -20

        self.rect.left += dx
        self.rect.bottom += dy

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),
                    (self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
