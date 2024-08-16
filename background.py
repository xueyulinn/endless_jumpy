import settings


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
