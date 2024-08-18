import pygame
import settings


class Player:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (45, 45))
        self.width = 25
        self.height = 40
        # initialize a rect object at top-left corner of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # repositions the rect to the x and y coordinates
        self.rect.center = (x, y)
        self.velY = 0
        self.flip = False

    def move(self, platforms):
        scroll = 0
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        # process keypresses
        if key[pygame.K_a]:
            dx = -8
            self.flip = True

        if key[pygame.K_d]:
            dx = 8
            self.flip = False

        self.velY += settings.GRAVITY
        dy += self.velY

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        elif self.rect.right + dx > settings.WINDOW_WIDTH:
            dx = settings.WINDOW_WIDTH - self.rect.right

        # check collision with platforms
        for platform in platforms:
            # collision in y direction
            # created a temporary rect object to check collision
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy,
                                         self.width, self.height):
                # check if player is above platform
                if self.rect.bottom < platform.rect.centery:
                    # if player is falling
                    if self.velY > 0:
                        # avoid the player overlapping with platforms
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.velY = -20

          # Prevent player from jumping higher than the top of the screen
        if self.rect.top + dy < 0:
            self.rect.top = 0
            dy = 0
            self.velY = 0  # Stop upward movement

        if self.rect.top <= settings.SCROLL_THRESH:
            if self.velY < 0:
                scroll = -dy

        self.rect.left += dx
        self.rect.bottom += dy

        return scroll

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),
                    (self.rect.x-12, self.rect.y-5))
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
