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
background = Background(0, 0, bgImage, screen)

playerImage = pygame.image.load("./assets/jump.png").convert_alpha()
player = Player(settings.PLAYERX, settings.PLAYERY, playerImage)

platformImage = pygame.image.load("./assets/wood.png").convert_alpha()
platforms = pygame.sprite.Group()

# create platform
platform = Platform(settings.WINDOW_WIDTH//2-50,
                    settings.WINDOW_HEIGHT-50, platformImage, 100)
platforms.add(platform)

# game variables
bgScroll = 0
gameOver = False
score = 0
fontSmall = pygame.font.SysFont('Lucida Sans', 20)
fontBig = pygame.font.SysFont('Lucida Sans', 24)
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(settings.FPS)

    if not gameOver:
        scroll = player.move(platforms)

        bgScroll += scroll
        if bgScroll >= settings.WINDOW_HEIGHT:
            bgScroll = 0

        # draw elements
        background.draw(bgScroll)
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

        if player.rect.top > settings.WINDOW_HEIGHT:
            gameOver = True

    else:
        background.drawText('GAME OVER', fontBig,
                            settings.TEXT_COLOR, 130, 200)
        background.drawText('SCORE: ' + str(score), fontBig,
                            settings.TEXT_COLOR,  130, 250)
        background.drawText('PRESS SPACE TO START AGAIN',
                            fontBig, settings.TEXT_COLOR,  40, 280)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # reset variables
            gameOver = False
            scroll = 0
            score = 0
            player.rect.center = (settings.PLAYERX, settings.PLAYERY)

            # reset platforms
            platforms.empty()
            platform = Platform(settings.WINDOW_WIDTH//2-50,
                                settings.WINDOW_HEIGHT-50, platformImage, 100)
            platforms.add(platform)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# uninitialize all pygame modules
pygame.quit()
