import time

import pygame

from .Configuration import Configuration
from .Camera import Camera


class UserInterface():
    screen = Configuration.screen

    @classmethod
    def display_image(cls, file):
        img = pygame.image.load(file)
        img = pygame.transform.smoothscale(img, (Configuration.SCALE_WIDTH, Configuration.SCREEN_HEIGHT))
        cls.screen.blit(img, ((Configuration.SCREEN_WIDTH - Configuration.SCALE_WIDTH) / 2, 0))
        pygame.display.flip()

    @classmethod
    def run_self_pi_box(cls):
        while True:
            Camera.wait_for_event()
            UserInterface.display_image(file=Configuration.EVENT_IMAGE)
            time.sleep(0.2)
            Camera.take_picture()