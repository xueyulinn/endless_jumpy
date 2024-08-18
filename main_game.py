import pygame
import settings
from player import Player
from background import Background
from game_platform import Platform
import random
import os
from sprite_sheet import SpriteSheet
from enemy import Enemy

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
platform = Platform(settings.WINDOW_WIDTH//2-50,
                    settings.WINDOW_HEIGHT-50, platformImage, 100, False)
platforms.add(platform)

enemyImage = pygame.image.load("./assets/bird.png").convert_alpha()
birdSheet = SpriteSheet(enemyImage)
enemies = pygame.sprite.Group()

# game variables
bgScroll = 0
gameOver = False
score = 0
fontSmall = pygame.font.SysFont('Lucida Sans', 20)
fontBig = pygame.font.SysFont('Lucida Sans', 24)
fadeCount = 0

if os.path.exists('high_score.txt'):
    with open('high_score.txt', 'r') as f:
        highScore = int(f.read())
else:
    highScore = 0


clock = pygame.time.Clock()


running = True
while running:
    clock.tick(settings.FPS)

    if not gameOver:
        scroll = player.move(platforms)

        bgScroll += scroll
        if bgScroll >= settings.WINDOW_HEIGHT:
            bgScroll = 0

        # generate platforms randomly
        if len(platforms) < settings.MAX_PLATFORMS:
            pW = random.randint(40, 60)
            pX = random.randint(0, settings.WINDOW_WIDTH-pW)
            pY = platform.rect.top - random.randint(80, 120)
            pM = random.randint(0, 1)
            platform = Platform(pX,
                                pY, platformImage, pW, True if pM == 1 else False)
            platforms.add(platform)

        platforms.update(scroll, score)

        if len(enemies) == 0:
            enemy = Enemy(100, birdSheet, 1.5)
            enemies.add(enemy)

         # draw sprites
        background.draw(bgScroll)
        player.draw(screen)
        platforms.draw(screen)
        enemies.draw(screen)

        enemies.update(scroll)

        if scroll > 0:
            score += scroll

        background.drawPanel(score, fontSmall, settings.PANEL_COLOR)

        # draw the high score
        pygame.draw.line(screen, settings.TEXT_COLOR, (0, score -
                         highScore+settings.SCROLL_THRESH),
                         (settings.WINDOW_WIDTH, score -
                         highScore+settings.SCROLL_THRESH),
                         3
                         )
        background.drawText('Highest Score', fontSmall, settings.TEXT_COLOR, settings.WINDOW_WIDTH-130, score -
                            highScore+settings.SCROLL_THRESH+2)

        # game over judgement
        if player.rect.top > settings.WINDOW_HEIGHT:
            gameOver = True

    else:
        # game over
        if fadeCount < settings.WINDOW_HEIGHT:
            fadeCount += 5
            for y in range(0, 6, 2):
                # expand from left to right
                pygame.draw.rect(screen, settings.GAMEOVER_COLOR,
                                 (0, y*100, fadeCount, 100))
                # expand from right to left
                pygame.draw.rect(screen, settings.GAMEOVER_COLOR,
                                 (settings.WINDOW_WIDTH - fadeCount, (y+1)*100, settings.WINDOW_WIDTH, 100))
        else:
            background.drawText('GAME OVER', fontBig,
                                settings.TEXT_COLOR, 130, 200)
            background.drawText('SCORE: ' + str(score), fontBig,
                                settings.TEXT_COLOR,  130, 250)
            background.drawText('PRESS SPACE TO START AGAIN',
                                fontBig, settings.TEXT_COLOR,  40, 280)

        # update highScore
        highScore = max(score, highScore)
        with open('high_score.txt', 'w') as f:
            f.write(str(highScore))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # reset variables
            gameOver = False
            scroll = 0
            score = 0
            player.rect.center = (settings.PLAYERX, settings.PLAYERY)
            fadeCount = 0
            enemies.empty()
                        
            # reset platforms
            platforms.empty()
            platform = Platform(settings.WINDOW_WIDTH//2-50,
                                settings.WINDOW_HEIGHT-50, platformImage, 100, False)
            platforms.add(platform)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# uninitialize all pygame modules
pygame.quit()
