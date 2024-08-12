class Background:
    def __init__(self,  x, y, image):
        self.image = image
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))