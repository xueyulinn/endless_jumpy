import settings
import pygame


class Background:
    def __init__(self,  x, y, image, screen):
        self.image = image
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self, scroll):
        self.screen.blit(self.image, (self.x, scroll))
        self.screen.blit(self.image, (self.x, -settings.WINDOW_HEIGHT+scroll))

    def drawText(self, text, font, color, x, y):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def drawPanel(self, score, font, color):
        pygame.draw.rect(self.screen, settings.PANEL_COLOR,
                         (0, 0, settings.WINDOW_WIDTH, 30))
        pygame.draw.line(self.screen, (255,255,255), (0, 30),
                         (settings.WINDOW_WIDTH, 30), 2)
        self.drawText('SCORE: ' + str(score), font,
                      settings.TEXT_COLOR,  0, 0)
