from time import sleep

import RPi.GPIO as GPIO
import pygame

from ..config.camera_config import CameraConfig
from ..config.gpio_config import GpioConfig
from ..config.screen_config import ScreenConfig


class Screen:
    """
    Method handling a screen display in the SelfPyBox
    """
    @classmethod
    def display_image(cls, file):
        """
        Display a new image in the PyGame Screen
        :param file:
        :return:
        """
        img = pygame.image.load(file)
        img = pygame.transform.smoothscale(img, (CameraConfig.SCALE_WIDTH, ScreenConfig.SCREEN_HEIGHT))
        ScreenConfig.screen.blit(img, ((ScreenConfig.SCREEN_WIDTH - CameraConfig.SCALE_WIDTH) / 2, 0))
        pygame.display.flip()

    @classmethod
    def start_countdown(cls, countdown: int = 4):
        """
        Launch the countdown before taking the picture
        :param countdown: how long we need to wait ! be careful to have a corresponding screen in assets/countdown !
        """
        for i in reversed(range(countdown)):
            GPIO.output(GpioConfig.LED_PIN, GPIO.HIGH)
            cls.display_image(ScreenConfig.COUNTDOWN_TIMER[i])
            if i == 0:
                # when the countdown reaches 0, we take the picture directly we do not wait one extra seconds
                return
            sleep(0.5)
            GPIO.output(GpioConfig.LED_PIN, GPIO.LOW)
            sleep(0.5)
