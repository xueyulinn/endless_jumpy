import pygame
import settings
from player import Player
from background import Background
from game_platform import Platform
import random


# initialize all imported pygame modules
pygame.init()

# create game window
screen = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

pygame.display.set_caption("Jumpy")

# load images
bgImage = pygame.image.load("./assets/bg.png").convert_alpha()
background = Background(0, 0, bgImage)

playerImage = pygame.image.load("./assets/jump.png").convert_alpha()
player = Player(settings.PLAYERX, settings.PLAYERY, playerImage)

platformImage = pygame.image.load("./assets/wood.png").convert_alpha()
platforms = pygame.sprite.Group()

# create platform
platform = Platform(settings.WINDOW_WIDTH//2-50,
                    settings.WINDOW_HEIGHT-50, platformImage, 100)

platforms.add(platform)


bgScroll = 0
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(settings.FPS)
    scroll = player.move(platforms)

    bgScroll += scroll
    if bgScroll >= settings.WINDOW_HEIGHT:
        bgScroll = 0

    # draw elements
    background.draw(screen, bgScroll)
    player.draw(screen)
    platforms.draw(screen)

    if len(platforms) < settings.MAX_PLATFORMS:
        pW = random.randint(40, 60)
        pX = random.randint(0, settings.WINDOW_WIDTH-pW)
        pY = platform.rect.top - random.randint(80, 120)
        platform = Platform(pX,
                            pY, platformImage, pW)
        platforms.add(platform)

    platforms.update(scroll)

    pygame.draw.line(screen, (255, 255, 255), (0, settings.SCROLL_THRESH),
                     (settings.WINDOW_WIDTH, settings.SCROLL_THRESH))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# uninitialize all pygame modules
pygame.quit()
