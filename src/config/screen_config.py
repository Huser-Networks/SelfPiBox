import logging

import pygame


class ScreenConfig:
    """
    Screen configuration for the SelfyBox
    """
    COUNTDOWN_TIMER = [
        '/opt/SelfPiBox/assets/countdown/0.png',
        '/opt/SelfPiBox/assets/countdown/1.png',
        '/opt/SelfPiBox/assets/countdown/2.png',
        '/opt/SelfPiBox/assets/countdown/3.png'
    ]

    # Screen spec
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    screen = None

    @classmethod
    def set_up(cls):
        """
        Create an inital configuration for the selfpiboy
        """
        logging.info('Begin Screen configuration')
        pygame.init()
        cls.screen = pygame.display.set_mode((cls.SCREEN_WIDTH, cls.SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.mouse.set_visible(0)
        logging.info('pygame configured')
