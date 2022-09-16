import pygame

class SpriteSheet():

    def __init__(self, image) -> None:
        self.sheet = image

    def get_image(self, frame, width, height, scale=1, color=(0,0,0)):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), (frame * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        
        return image