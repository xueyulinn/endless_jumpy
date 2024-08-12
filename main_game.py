import pygame
import settings

# inialize the game
pygame.init()

# create game window
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

pygame.display.set_caption("Jumpy")

bgImage =  pygame.image.load("./assets/bg.png").convert_alpha()

running = True

while running:

    # draw background
    screen.blit(bgImage, (0, 0))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    
# means the game is over, so we need to quit pygame
pygame.quit()