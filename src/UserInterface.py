import pygame

from .Configuration import Configuration


class UserInterface():
    @classmethod
    def display_image(cls, file):
        img = pygame.image.load(file)
        img = pygame.transform.smoothscale(img, (Configuration.SCALE_WIDTH, Configuration.SCREEN_HEIGHT))
        Configuration.screen.blit(img, ((Configuration.SCREEN_WIDTH - Configuration.SCALE_WIDTH) / 2, 0))
        pygame.display.flip()
