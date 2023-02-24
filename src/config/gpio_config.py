import logging

import RPi.GPIO as GPIO


class GpioConfig:
    """
    Gpio configuration for the SelfyBox
    """
    BUTTON_PIN = 26
    LED_PIN = 13
    SHUTDOWN_PIN = 6

    @classmethod
    def set_up(cls):
        """
        Create an inital configuration for the selfpiboy
        """
        logging.info('Begin GPIO configuration')
        # Setup GPIO (Input/Output of the Raspberry PI)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(cls.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(cls.LED_PIN, GPIO.OUT, initial=GPIO.LOW)
        logging.info('GPIO configured')

