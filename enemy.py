import pygame
import random
import settings


class Enemy(pygame.sprite.Sprite):
    def __init__(self, y, spriteSheet, scale):
        pygame.sprite.Sprite.__init__(self)
        self.direction = random.choice([-1, 1])
        self.updateTime = pygame.time.get_ticks()
        self.frameList = []
        self.frameIndex = 0
        self.frameTime = 50
        self.frameNumber = 8
        # collection all frames 
        for frame in range(self.frameNumber):
            image = spriteSheet.get_image(
                frame, 32, 32, scale, (0, 0, 0))
            image.set_colorkey((0, 0, 0))
            self.image = pygame.transform.flip(
                image, True if self.direction == 1 else False, False)
            self.frameList.append(self.image)

        self.rect = self.frameList[self.frameIndex].get_rect()
        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = settings.WINDOW_WIDTH

        self.rect.y = y
        self.speed = random.randint(1, 2)

    def update(self, scroll):
        self.rect.y += scroll
        self.rect.x += self.direction * self.speed

        # animation
        self.image = self.frameList[self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > self.frameTime:
            if self.frameIndex >= len(self.frameList)-1:
                self.frameIndex = 0
            else:
                self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()

        if self.rect.left > settings.WINDOW_WIDTH or self.rect.right < 0:
            self.kill()
