import settings


class Background:
    def __init__(self,  x, y, image):
        self.image = image
        self.x = x
        self.y = y

    def draw(self, screen, scroll):
        screen.blit(self.image, (self.x, scroll))
        screen.blit(self.image, (self.x, -settings.WINDOW_HEIGHT+scroll))
