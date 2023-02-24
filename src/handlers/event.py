import logging
import time

import RPi.GPIO as GPIO

from ..config.gpio_config import GpioConfig


class Event:
    """
    Class containing all the major event for the app
    """
    @classmethod
    def shutdown(cls):
        """
        Call this method for shutting down the SelfPiBox in a clean way
        """
        GPIO.cleanup()
        logging.debug('SelfPiBox stopped')
        exit()

    @classmethod
    def wait_for_event(cls):
        """
        This is the method that "wait" for the user input before taking a picture (it actually blocks the code). it will check every seconds if the button is pressed. If the button is pressed, it will stop "waiting"
        :return:
        """
        GPIO.wait_for_edge(GpioConfig.BUTTON_PIN, GPIO.FALLING)