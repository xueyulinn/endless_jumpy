import pygame
import settings
from player import Player
from background import Background

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

clock = pygame.time.Clock()

running = True

while running:
    
    clock.tick(settings.FPS)
    player.move()
    
    # draw elements
    background.draw(screen)
    player.draw(screen)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# uninitialize all pygame modules
pygame.quit()
